#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:52:14 2023

"""


from anndata import AnnData
from featuremap.quasildr.structdr import Scms
import numpy as np
import time
import matplotlib.pyplot as plt
import scanpy as sc
import pandas as pd

def plot_density(
        adata: AnnData
            ):
    data = adata.obsm['X_featmap'].copy()  # Exclude one leiden cluster;
    # data = adata[index_remove_outlier].obsm['X_featmap']  # Exclude one leiden cluster;
    # rotational_matrix = adata.uns['emb_umap']._densmap_kwds['VH_embedding']
    # rotational_matrix = adata.obsm['VH_embedding_original'].copy()
    # rotational_matrix = adata.obsm['VH_embedding'].copy()
    
    
    # r_emb = adata.obsm['rad_emb_no_log'].copy()
    
    s = Scms(data, 0.5, min_radius=5)
    min_x = min(data[:, 0])
    max_x = max(data[:, 0])
    min_y = min(data[:, 1])
    max_y = max(data[:, 1])
    # part = 200
    if data.shape[0] < 5000:
        num_grid_point = data.shape[0] * 0.5
    else:
        num_grid_point = 2000
    x_range = max_x - min_x
    y_range = max_y - min_y
    # x_range = 1 - 0.618
    # y_range = 0.618
    part_y = np.sqrt(num_grid_point / x_range * y_range)
    part_x = x_range / y_range * part_y
    # part_y = 60
    # part_x = 60
    # Assign num of grid points mort to vertical direction ??
    xv, yv = np.meshgrid(np.linspace(min_x, max_x, round(part_x)), np.linspace(min_y, max_y, round(part_y)),
                         sparse=False, indexing='ij')
    # xv, yv = np.meshgrid(np.linspace(-10, 10, part), np.linspace(-10, 15, part),
    #                       sparse=False, indexing='ij')
    grid_contour = np.column_stack([np.concatenate(xv), np.concatenate(yv)])
    T1 = time.time()
    # p1, g1, h1, msu,_ = s._kernel_density_estimate_anisotropic(grid_contour, rotational_matrix, r_emb)
    p1, g1, h1, msu = s._kernel_density_estimate(grid_contour, output_onlylogp=False, )
    T2 = time.time()
    print('Finish kernel_density_estimate_anisotropic in ' + str(T2-T1))
    # ifilter_1 = np.where(p1 >= (np.max(p1)*0.05))[0]  # sampling
    # fig, ax = plt.subplots(figsize=(15, 15))
    plt.contourf(xv, yv, p1.reshape(round(part_x), round(part_y)),
                 levels=20, cmap='Blues')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.clf()


def core_transition_state(
        adata:AnnData,
        cluster_key='clusters',
        top_percent = 0.2
        
        ):
    
    # adata.obs['clusters'] = adata.obs['clusters_fine']

    partition_label = adata.obs[cluster_key].copy()
    partition_label.value_counts()
    data = adata.obsm['X_featmap'].copy()
    # data = embedding.embedding_[data_index_0_2]
    # rotational_matrix = adata.obsm['VH_embedding'].copy()
    # rotational_matrix = adata.obsm['VH_embedding_original']
    
    # r_emb = adata.obsm['rad_emb_no_log'].copy()
    # from quasildr.structdr import Scms
    s = Scms(data, 0.8, min_radius=5)
    # p, _, _, _, _ = s._kernel_density_estimate_anisotropic( data, rotational_matrix, r_emb)
    p, _, _, _= s._kernel_density_estimate(data)
    adata.obs['density'] = p
    
    # Density in each cluster
    adata.obs['density_seperate_cluster'] = np.nan
    leiden_clusters = adata.obs[cluster_key].copy()
    leiden_clusters.value_counts()
    
    for cluster in leiden_clusters.cat.categories.values:
        cluster_in_cluster_label = (leiden_clusters == cluster)
        data_cluster = data[cluster_in_cluster_label, :]
        # rotational_matrix_cluster = rotational_matrix[cluster_in_cluster_label, :]
        # r_emb_cluster = r_emb[cluster_in_cluster_label, :]
    
        s = Scms(data_cluster, 0.8, min_radius=5)
        # p_1, _, _, _, _= s._kernel_density_estimate_anisotropic( data_cluster, rotational_matrix_cluster, r_emb_cluster)
        p_1, _, _, _= s._kernel_density_estimate( data_cluster)
        adata.obs['density_seperate_cluster'][cluster_in_cluster_label] = p_1
        density = adata.obs['density_seperate_cluster'][cluster_in_cluster_label]
    
    # Select top ratio(%) in each cluster as core state
    leiden_clusters = adata.obs[cluster_key].copy()
    
    adata.obs['corestates'] = np.nan
    adata.obs['corestates_largest'] = np.nan
    for cluster in leiden_clusters.cat.categories.values:
        cluster_in_cluster_label = (leiden_clusters == cluster)
        density = adata.obs['density_seperate_cluster'][cluster_in_cluster_label].copy()
        # density = adata.obs['density'][cluster_in_cluster_label]
        cluster_index = leiden_clusters.index[leiden_clusters == cluster]
        density_sort = density[cluster_index].sort_values(ascending=False)
        if int(len(cluster_index) * top_percent) > 50:
            density_sort_top20per_index = density_sort.index[:50]
        else:
            density_sort_top20per_index = density_sort.index[:int(len(cluster_index) * top_percent)]
        # density_sort_top20per_index = density_sort.index[:int(len(cluster_index) * 0.2)]
        # density_sort_top20per_index = density_sort.index[:200]
        adata.obs['corestates'][density_sort_top20per_index] = cluster
        # non-corestate
        # density_sort_rest_index = density_sort.index[int(len(cluster_index) * 0.2):]
        # adata.obs['corestates'][density_sort_rest_index] = f'{cluster} Rest'
        
        density_sort_largest_index = density_sort.index[:1]
        adata.obs['corestates_largest'][density_sort_largest_index] = cluster
    
    adata.obs['corestates'] = pd.Series(
        adata.obs['corestates'].copy(), dtype='category').values
    
    
    # Expand the core state by NNs
    from featuremap.featuremap_ import nearest_neighbors
    n_neighbors = 30
    knn_indices, knn_dists, _ = nearest_neighbors(adata.obsm['X_featmap'].copy(), n_neighbors=n_neighbors,
                                                  metric="euclidean", metric_kwds={}, angular=False, random_state=42)

    # corestates_nn_points coresponding to clusters
    adata.obs['corestates_nn_points'] = np.nan
    for cluster in leiden_clusters.cat.categories.values:
        corestates_points = np.where(adata.obs['corestates'] == cluster)[0]
        corestates_nn_points = np.unique(knn_indices[corestates_points].reshape(-1))
        # corestates_nn_points_binary = np.isin(np.array(range(adata.shape[0])), corestates_nn_points) * 1
        adata.obs['corestates_nn_points'][corestates_nn_points] = cluster
    sc.pl.embedding(adata, 'featmap', color=['corestates_nn_points'],)
 
    # corestates_nn_points: binary
    adata.obs['corestates_nn_points'] = np.nan
    corestates_points = np.where(adata.obs['corestates'].isna() == False)[0]
    
    corestates_nn_points = np.unique(knn_indices[corestates_points].reshape(-1))
    corestates_nn_points_binary = np.isin(np.array(range(adata.shape[0])), corestates_nn_points) * 1
    adata.obs['corestates_nn_points'] = corestates_nn_points_binary
    
    adata.obs['core_trans_states'] = '0'
    corestate_points = np.where(adata.obs['corestates_nn_points']==1)[0]
    # adata.obs['path_core_points'][trajectory_points] = '0'
    adata.obs['core_trans_states'][corestate_points] = '1'
    
    # from pandas.api.types import CategoricalDtype
    # cat_type = CategoricalDtype(categories=['Transition', 'Core'], ordered=True)
    # adata.obs['core_trans_states'] = adata.obs['core_trans_states'].astype(cat_type)
    
    sc.pl.embedding(adata, 'featmap', color=['core_trans_states'])

    

########################################################
# Collect trasition state and core state given clusters
##############################################################
from featuremap.plot.ridge_pseudotime import mst_subgraph

def nodes_of_transition_states(adata, start_state, end_state, clusters):

    node_name_start = adata.obs['corestates_largest'][adata.obs['corestates_largest'] == (start_state)].index[0]
    start = np.where(adata.obs_names == node_name_start)[0][0]
    
    node_name_end = adata.obs['corestates_largest'][adata.obs['corestates_largest'] == (end_state)].index[0]
    end = np.where(adata.obs_names == node_name_end)[0][0]
    
    # Spanning tree on embedding space
    ridge_points = np.where(np.array(adata.obs['trajectory_points'])==1)[0]
    corestate_points = np.where(pd.isna((adata.obs['corestates_largest'])) == False)[0]
    # Points for tree
    tree_points = np.union1d(ridge_points, corestate_points)
    mst_subg = mst_subgraph(adata, tree_points, emb='X_featmap')
    mst_subg.clusters().summary()

    start_id = mst_subg.vs.find(name=start).index
    end_id = mst_subg.vs.find(name=end).index
    
    path_given_start_end = mst_subg.get_shortest_paths(v=start_id, to=end_id)
    path_nodes_name = np.array([mst_subg.vs[i]['name'] for i in path_given_start_end])
    
    # Extend the path to both ends in trajectory
    nodes_start_state = np.where(np.array(adata.obs['clusters'] == str(start_state)) == True)[0]
    nodes_start_ridge = ridge_points[np.where(np.in1d(ridge_points, nodes_start_state))[0]]
    
    nodes_end_state = np.where(np.array(adata.obs['clusters'] == str(end_state)) == True)[0]
    nodes_end_ridge = ridge_points[np.where(np.in1d(ridge_points, nodes_end_state))[0]]
    
    node_corestate_start = adata.obs['corestates'][adata.obs['corestates_largest'] == start_state].index
    corestate_start = np.where(np.in1d(adata.obs_names, node_corestate_start))[0]
    
    node_corestate_end = adata.obs['corestates'][adata.obs['corestates_largest'] == end_state].index
    corestate_end = np.where(np.in1d(adata.obs_names, node_corestate_end))[0]
    
    from functools import reduce
    path_nodes = reduce(np.union1d, (path_nodes_name, corestate_start, corestate_end, nodes_start_ridge, nodes_end_ridge))
    
    path_binary = np.isin(np.array(range(adata.shape[0])), path_nodes)
    adata.obs['path_binary'] = (path_binary * 1).astype(int)

    sc.pl.embedding(adata, 'featmap', legend_loc='on data', s=10, color=['path_binary'],cmap='bwr')
    # sc.pl.embedding(adata_var, 'umap_v', legend_loc='on data', s=10, color=['path_binary'])
    
    from featuremap.featuremap_ import nearest_neighbors
    knn_indices, knn_dists, _ = nearest_neighbors(adata.obsm['X_featmap'].copy(), n_neighbors=60,
                                                  metric="euclidean", metric_kwds={}, angular=False, random_state=42)
    path_nodes_nn = np.unique(knn_indices[path_nodes].reshape(-1))
    
    core_nodes = np.array([]).astype(int)
    for cluster in clusters:
        core_nodes = np.append(core_nodes, np.where(adata.obs['corestates'] == str(cluster))[0])
    
    knn_indices, knn_dists, _ = nearest_neighbors(adata.obsm['X_featmap'].copy(), n_neighbors=60,
                                                  metric="euclidean", metric_kwds={}, angular=False, random_state=42)
    core_points = np.unique(knn_indices[core_nodes].reshape(-1))

    path_points_nn = np.union1d(path_nodes_nn, core_points)

    path_points_binary = np.isin(np.array(range(adata.shape[0])), path_points_nn) * 1
    adata.obs['path_points_nn'] = path_points_binary
    sc.pl.embedding(adata, 'featmap', legend_loc='on data', s=10, color=['path_points_nn'],cmap='bwr')    

    end_bridge_nodes = reduce(np.union1d, (path_nodes_name, corestate_start, corestate_end))
    end_bridge_nodes = np.unique(knn_indices[end_bridge_nodes].reshape(-1))
    transition_points = end_bridge_nodes

    end_bridge_points = np.union1d(end_bridge_nodes, core_points)
    # end_bridge_points_binary = np.isin(np.array(range(adata.shape[0])), end_bridge_points) * 1
    # adata.obs['end_bridge_points'] = end_bridge_points_binary
    # sc.pl.embedding(adata, 'featmap', legend_loc='on data', s=10, color=['end_bridge_points'],cmap=cmp('bwr'))    
    
    adata.obs['core_trans_temp'] = np.nan
    adata.obs['core_trans_temp'][end_bridge_points] = '0'
    adata.obs['core_trans_temp'][core_points] = '1'
    sc.pl.embedding(adata, 'featmap', color=['core_trans_temp'])

    
    return path_nodes, path_points_nn, end_bridge_points, core_points, transition_points


    
   