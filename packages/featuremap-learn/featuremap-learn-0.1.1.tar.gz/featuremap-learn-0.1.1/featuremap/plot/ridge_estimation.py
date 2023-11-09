#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:00:05 2023

"""



from anndata import AnnData
from featuremap.quasildr.structdr import Scms
import numpy as np
import matplotlib.pyplot as plt
# import scanpy as sc
# import pandas as pd

# from scipy.sparse import csr_matrix

# from scipy.sparse.csgraph import dijkstra





# # Given node i and j, Extract shortest path predecessors
# def track_shortest_path(node_i, node_j, predecessors):
#     """

#     Parameters
#     ----------
#     node_i : integer
#         Starting node of shortest path
#     node_j : integer
#         End node of shortest path
#     predecessors : array of shape(n, n)
#         predecessors matrix by dijkstra

#     Returns
#     -------
#     shortest_path_list:
#         list of node indices along the shortest path between i and j

#     """
#     shortest_path_list = []
#     i = node_i
#     j = node_j
#     shortest_path_list.append(j)
#     while i != j:
#         j = predecessors[i, j]
#         shortest_path_list.append(j)

#     return shortest_path_list[::-1]



# #######################################################
# # DFS traverse the spanning tree
# # Collect nodes between any intervals of the tree
# #########################################################3
# # mst_subg.is_tree()
# def dfs_1(adata, mst_subg, predecessors, plot='featmap',):

#     # DFS
#     # start = farthest_points[start_point]
#     rand_time = 0
#     trajectory_points = np.array([])
#     dfs_trace_collection = np.array([])
#     while rand_time < 50:
#         rand_time += 1
#         start = np.random.randint(mst_subg.vcount())
#         # print(f'start_{start}')
        
#         # Cut the DFS list into sub branches
#         dfs_branch = []
#         dfs_parent = np.array(mst_subg.dfs(start)[1])
#         dfs_parent_id = np.array([mst_subg.vs[i]['name'] for i in dfs_parent])
           
#         unique, counts = np.unique(np.array(dfs_parent_id), return_counts=True)
#         split_nodes = unique[np.where(counts>1)[0]]
        
#         split_idx = np.where( np.isin(np.array(dfs_parent_id), split_nodes ))[0]
        
#         for i in range(split_idx.shape[0]-1):
#             dfs_branch.append(dfs_parent_id[split_idx[i]:split_idx[i+1]].tolist())
        
#         # Collect the data points between the interval of two nodes, given a path. 
#         dfs_trace=[]
#         for i in range(len(dfs_branch)):
#             dfs_temp = np.array([],dtype=int)
#             for j in range(len(dfs_branch[i])-1):
#                 start = dfs_branch[i][j]
#                 end = dfs_branch[i][j+1]
#                 shortest_p_list = track_shortest_path(start, end, predecessors)
#                 # print(f'shortest_p_list_{shortest_p_list}')
#                 dfs_temp = np.append(dfs_temp,shortest_p_list)
             
#             dfs_trace.append(dfs_temp)
            
#         dfs_trace_collection = np.append(dfs_trace_collection, dfs_trace)
#         trajectory_points = np.append(trajectory_points, np.unique(np.concatenate(dfs_trace, axis=0)))


#     trajectory_points_update = np.isin(np.array(range(adata.shape[0])), np.unique(trajectory_points))
#     adata.obs['trajectory_points_update'] = (trajectory_points_update * 1).astype(int)            
#     # sc.pl.embedding(adata, plot, legend_loc='on data', color=['trajectory_points_update'], cmap='Greys')
#     sc.pl.embedding(adata, plot, legend_loc='on data', color=['trajectory_points_update'], cmap='Greys')
#     return dfs_trace_collection



def ridge_estimation(
        adata:AnnData
        ):
    
    data = adata.obsm['X_featmap'].copy()  # Exclude one leiden cluster;
    # data = adata_var.obsm['X_umap_v']
    pos_collection = []
    # for sample_time in range(20):
    s = Scms(data, 0.5, min_radius=5)
    # p, _, h, msu,_ = s._kernel_density_estimate_anisotropic(data, rotational_matrix, r_emb)
    p, _, h, msu = s._kernel_density_estimate(data)
    ifilter_2 =  np.where(p >= (np.max(p)*0.05))[0] # sampling
    # shifted = np.append(grid_contour[ifilter_1, :],data[ifilter_2, :], axis=0)
    shifted = data[ifilter_2,:]
    inverse_sample_index = s.inverse_density_sampling(shifted, n_samples=200, n_jobs=1, batch_size=16)
    # ifilter_3 = np.random.randint(adata.shape[0], size=100)
    # shifted = np.append(shifted[inverse_sample_index], data[ifilter_3,:],axis=0)
    # inverse_sample_index = np.unique(np.array(inverse_sample_index).reshape(-1))
    shifted = shifted[inverse_sample_index]
    
    n_iterations = 500
    allshiftedx_grid = np.zeros((shifted.shape[0],n_iterations))
    allshiftedy_grid = np.zeros((shifted.shape[0],n_iterations))
    for j in range(n_iterations):
        allshiftedx_grid[:,j] = shifted[:,0]
        allshiftedy_grid[:,j] = shifted[:,1]
        shifted += 1*s.scms_update(shifted,method='GradientLogP',stepsize=0.02, relaxation=0.5)[0]
    pos = np.column_stack([allshiftedx_grid[:,-1], allshiftedy_grid[:,-1]])
    pos_collection.append(pos)
    pos = np.array(pos_collection).reshape(-1,2)
    p_pos, _, _, _ = s._kernel_density_estimate(pos)
    pos_filter_idx =  np.where(p_pos >= (np.max(p_pos)*0.1))[0] # sampling
    pos_filter = pos[pos_filter_idx]
    
    # Plot the ridge
    s = Scms(data, 0.5, min_radius=5)
    min_x = min(data[:, 0])
    max_x = max(data[:, 0])
    min_y = min(data[:, 1])
    max_y = max(data[:, 1])
    # part = 200
    num_grid_point = data.shape[0] * 0.5
    x_range = max_x - min_x
    y_range = max_y - min_y
    # x_range = 1 - 0.618
    # y_range = 0.618
    part_y = np.sqrt(num_grid_point / x_range * y_range)
    part_x = x_range / y_range * part_y
    # Assign num of grid points mort to vertical direction ??
    xv, yv = np.meshgrid(np.linspace(min_x, max_x, round(part_x)), np.linspace(min_y, max_y, round(part_y)),
                         sparse=False, indexing='ij')
    grid_contour = np.column_stack([np.concatenate(xv), np.concatenate(yv)])
    p1, g1, h1, msu = s._kernel_density_estimate(grid_contour, output_onlylogp=False, )
    
    plt.contourf(xv, yv, p1.reshape(
        round(part_x), round(part_y)), levels=20, cmap='Blues')
    plt.scatter(data[:,0],data[:,1], s=1, c='darkgrey', alpha=0.1)
    plt.scatter(pos_filter[:,0],pos_filter[:,1],c="red", s=1)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    plt.clf()
    
    
    # Relate the ridge points under the embedding graph
    trajectory_points = pos_filter
    trajectory_nn_points = np.array([], dtype=int)
    
    from sklearn.neighbors import NearestNeighbors
    nbrs = NearestNeighbors().fit(adata.obsm['X_featmap'].copy())
    _, indices = nbrs.kneighbors(trajectory_points)
    trajectory_nn_points = np.append(trajectory_nn_points, indices[:, 0])
    # trajectory_nn_points = np.append(trajectory_nn_points, indices[:,1])
    trajectory_nn_points = np.unique(trajectory_nn_points)
    # data_trajectory_nn_points = adata.obsm['X_featmap'][trajectory_nn_points]
    # plt.contourf(xv, yv, p1.reshape(
    #     round(part_x), round(part_y)), levels=20, cmap='Blues')
    
    # # label = np.array(adata.obs['leiden'].values).astype(int)
    # # label = np.array(adata.obs['corestates'].values).astype(int)
    # # label[label<0] = 4
    # # plt.scatter(data[:, 0], data[:, 1], cmap='fire', c=[sns.color_palette(n_colors=200)[x] for x in label],
    # #             s=0.5, alpha=0.1)
    # plt.scatter(data_trajectory_nn_points[:, 0], data_trajectory_nn_points[:,
    #             1], color='red', s=0.5)  # 1-dim density ridge
    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
    # plt.clf()
    
    trajectory = np.isin(np.array(range(adata.shape[0])), trajectory_nn_points)
    adata.obs['trajectory_points'] = (trajectory * 1).astype(int)
    
    # ##########################
    # # Connect the trajectory points
    # ############################
    # from umap.umap_ import fuzzy_simplicial_set
    # _, _, _, knn_dists = fuzzy_simplicial_set(
    #     adata.obsm['X_featmap'] ,
    #     n_neighbors=60,
    #     random_state=42,
    #     metric="euclidean",
    #     metric_kwds={},
    #     # knn_indices,
    #     # knn_dists,
    #     verbose=True,
    #     return_dists=True)

    # # M = adata.obsp['emb_dists'].copy().toarray()
    # M = knn_dists.toarray()

    # # Pairwise shortest path
    # graph = csr_matrix(M)
    # # dist_matrix, predecessors = shortest_path(
    # #     csgraph=graph, directed=False, method='D', return_predecessors=True)
    # dist_matrix, predecessors = dijkstra(
    #     csgraph=graph, directed=False, return_predecessors=True)

    # # Set the points in the tree
    # ridge_points = np.where(np.array(adata.obs['trajectory_points'])==1)[0]

    # # corestae_points: largest density in expression plot
    # corestate_points = np.where(pd.isna((adata.obs['corestates_largest'])) == False)[0]
    # # corestate_points = np.where(pd.isna((adata.obs['corestates'])) == False)[0]

    # # Add largest and smallest pseudotime points to compute the induced subgraph
    # # Points for tree
    # tree_points = np.union1d(ridge_points, corestate_points)
    # # tree_points = ridge_points

    # mst_subg = mst_subgraph(adata, tree_points,)
    # mst_subg.clusters().summary()

    # # import igraph as ig
    # # layout = mst_subg.layout("kamada_kawai")
    # # ig.plot(mst_subg, layout=layout)
    # dfs_trace_collection = dfs_1(adata, mst_subg, predecessors)



    # plt.contourf(xv, yv, p1.reshape(
    #     round(part_x), round(part_y)), levels=20, cmap='Blues')
    # data = adata.obsm['X_featmap'].copy()
    # plt.scatter(data[:,0],data[:,1], s=1, c='darkgrey', alpha=0.1)
    # # plt.scatter(data[trajectory_points,0],data[trajectory_points,1], s=1, c='red')

    # emb= adata.obsm['X_featmap']
    # for i in range(dfs_trace_collection.shape[0]):
    #     # i = 1
    #     for j in range(dfs_trace_collection[i].shape[0]-1):
    #         # j = 0
    #         cur_idx = np.array([dfs_trace_collection[i][j], dfs_trace_collection[i][j+1]])
    #         plt.plot(emb[cur_idx,0], emb[cur_idx,1], 'ro-', linewidth=2, markersize=0.1)

    # plt.xticks([])
    # plt.yticks([])
    # plt.show()
    # plt.clf()

