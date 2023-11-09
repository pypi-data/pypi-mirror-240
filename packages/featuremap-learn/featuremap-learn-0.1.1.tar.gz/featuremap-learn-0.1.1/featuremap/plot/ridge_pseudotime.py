#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:41:17 2023

"""


from scipy.special import expit
from sklearn.preprocessing import scale

from featmap.featmap_ import nearest_neighbors
from scipy.sparse.csgraph import shortest_path

# from anndata import AnnData
# from featuremap.quasildr.structdr import Scms
import numpy as np
import scanpy as sc
from scipy.sparse import csr_matrix
import pandas as pd



# from scipy.sparse.csgraph import shortest_path, dijkstra
def mst_subgraph(adata, tree_points, emb='X_featmap'):
    """

    Parameters
    ----------
    adata
    tree_points : np.array
        Points included in the induced subgraph

    Returns
    -------
    mst_subg : igraph
        minimum spanning_tree over tree_points (anchors).

    """
    # # M = adata.obsp['emb_dists'].copy().toarray() 
    # M = adata_var.obsm['knn_dists'].copy().toarray()

    # graph = csr_matrix(M) # knn graph
    # dist_matrix, predecessors = dijkstra(
    #     csgraph=graph, directed=False, return_predecessors=True)

    # dist_mat = dist_matrix
    # g = sc._utils.get_igraph_from_adjacency(dist_mat) # Complete graph from pairwise distance
    # g.vs["name"] = range(M.shape[0])  # 'name' to store original point id
    
    # g_induced_subg = g.induced_subgraph(tree_points)
    # mst_subg = g_induced_subg.spanning_tree(weights=g_induced_subg.es["weight"])
    
    n_neighbors = 60
    knn_indices, knn_dists, _ = nearest_neighbors(adata.obsm[emb][tree_points].copy(), n_neighbors=n_neighbors,
                                                  metric="euclidean", metric_kwds={}, angular=False, random_state=42)

    # Pairwise distance by knn indices and knn distances
    dist_mat = np.zeros([tree_points.shape[0], tree_points.shape[0]])
    for i in range(tree_points.shape[0]):
        for j in range(n_neighbors):
            dist_mat[i, knn_indices[i,j]] += knn_dists[i,j]

    # knn graph by iGraph
    g = sc._utils.get_igraph_from_adjacency(dist_mat) # Complete graph from pairwise distance
    g.vs["name"] = tree_points  # 'name' to store original point id
    # g_induced_subg = g.induced_subgraph(tree_points)
    mst_subg = g.spanning_tree(weights=g.es["weight"])
    return mst_subg


def ridge_pseudotime(adata, root, plot='featmap'):
    
    # Construct mst subgraph
    ridge_points = np.where(np.array(adata.obs['trajectory_points'])==1)[0]
    corestate_points = np.where(pd.isna((adata.obs['corestates_largest'])) == False)[0]
    tree_points = np.union1d(ridge_points, corestate_points)

    mst_subg = mst_subgraph(adata, tree_points, emb='X_featmap')

    farthest_points = mst_subg.farthest_points() # (34, 174, 140)
    farthest_points = np.array(farthest_points[:2])
    farthest_path = mst_subg.get_shortest_paths(v=farthest_points[0], to=farthest_points[1])
    farthest_path_name = np.array([mst_subg.vs[i]['name'] for i in farthest_path])
    farthest_path_binary = np.isin(np.array(range(adata.shape[0])), farthest_path_name)
    adata.obs['farthest_path'] = (farthest_path_binary * 1).astype(int)
    sc.pl.embedding(adata, plot, legend_loc='on data', s=100, color=['farthest_path','trajectory_points'])
    # sc.pl.embedding(adata, 'featmap', color=['leiden','corestates','farthest_path','trajectory_points'])
    
    # Set the starting point
    if root is None:
        start = farthest_points[0]
    else:
        # root_index = adata.obs['corestates_largest'][adata.obs['corestates_largest'] == root].index[0]
        # root_id = np.where(adata.obs_names == root_index)[0][0]
        start = np.where(mst_subg.vs['name'] == root)[0][0]
    # start = start
    dist_from_start = mst_subg.shortest_paths(start, weights="weight")
    nodes_in_tree = np.array([mst_subg.vs[i]['name'] for i in range(mst_subg.vcount())])
    dist_from_start_dict = dict(zip(nodes_in_tree, dist_from_start[0]))
    

    # Pairwise shortest path of origninal knn graph
    # M = adata.obsp['emb_dists'].toarray()
    # M = adata.obsp['knn_dists'].toarray()
    
    from umap.umap_ import fuzzy_simplicial_set
    _, _, _, knn_dists = fuzzy_simplicial_set(
        adata.obsm['X_featmap'] ,
        n_neighbors=60,
        random_state=42,
        metric="euclidean",
        metric_kwds={},
        # knn_indices,
        # knn_dists,
        verbose=True,
        return_dists=True)
    
    M = knn_dists.toarray()


    graph = csr_matrix(M)
    
    dist_matrix, predecessors = shortest_path(
        csgraph=graph, directed=False, indices=tree_points,return_predecessors=True)
    # For each node, find its nearest node in the tree
    dist_matrix = dist_matrix.T
    
    nearest_in_tree = np.argmin(dist_matrix, axis=1)
    nearest_in_tree_dist = np.min(dist_matrix, axis=1)
    data_dist = {'node_in_tree': tree_points[nearest_in_tree],
                 'dist': nearest_in_tree_dist}
    nearest_node_in_tree = pd.DataFrame.from_dict(data_dist,orient='columns')
    
    # For each node, compute the dist to start by first identifying its nearest node in the tree, then to start point
    emb_pseudotime = np.array([nearest_node_in_tree.at[i,'dist'] + 
              dist_from_start_dict[nearest_node_in_tree.at[i,'node_in_tree']]
              for i in range(dist_matrix.shape[0])
              ])
    
    emb_pseudotime[np.where(emb_pseudotime == np.inf)[0]] = 20
    
    adata.obs['ridge_pseudotime'] = expit(scale(emb_pseudotime))
    # adata.obs['emb_pseudotime'] = emb_pseudotime
    
    # root_idx = mst_s1ubg.vs[start]['name']
    # adata.uns["iroot"] = root_idx
    # sc.tl.dpt(adata)
    # adata.obs['dpt_pseudotime'] = expit(scale(adata.obs['dpt_pseudotime'])+1)
    # expit(scale(emb_pseudotime))
    sc.pl.embedding(adata, plot, legend_loc='on data', color=['ridge_pseudotime',])
    # sc.pl.embedding(adata, 'umap', legend_loc='on data', color=['emb_pseudotime',])

