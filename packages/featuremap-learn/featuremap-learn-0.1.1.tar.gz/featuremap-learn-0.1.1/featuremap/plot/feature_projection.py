#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:06:30 2022

"""

# Adapts source code from: 
# https://github.com/scverse/scanpy
#

from anndata import AnnData
import anndata as ad
import time
# import numba

import numpy as np
import matplotlib.pyplot as plt

from featuremap.quasildr.structdr import Scms


import scanpy as sc
import scipy

from scipy.stats import norm as normal
from sklearn.neighbors import NearestNeighbors

def quiver_autoscale(X_emb, V_emb):
    import matplotlib.pyplot as pl

    scale_factor = np.abs(X_emb).max()  # just so that it handles very large values
    fig, ax = pl.subplots()
    Q = ax.quiver(
        X_emb[:, 0] / scale_factor,
        X_emb[:, 1] / scale_factor,
        V_emb[:, 0],
        V_emb[:, 1],
        angles="xy",
        scale_units="xy",
        scale=None,
    )
    Q._init()
    fig.clf()
    pl.close(fig)
    return Q.scale / scale_factor



def plot_gauge(
        adata:AnnData,
        embedding='X_featmap',
        vkey='X_gauge_v1',
        density=1,
        smooth=0.5,
        n_neighbors=None,
        min_mass=1,
        autoscale=True,
        ):
    # Set grid as the support
    X_emb=adata.obsm[embedding]  # Exclude one leiden cluster;
    # rotational_matrix = adata.uns['emb_umap']._densmap_kwds['VH_embedding']
    # rotational_matrix = adata.obsm['VH_embedding']
    # r_emb = adata.obsm['rad_emb_no_log']
    s = Scms(X_emb, 0.5, min_radius=5)

    # X_emb=adata.obsm[embedding]
    V_emb=adata.obsm[vkey] 
    idx_valid = np.isfinite(X_emb.sum(1) + V_emb.sum(1))
    X_emb = X_emb[idx_valid]
    V_emb = V_emb[idx_valid]

    # prepare grid
    n_obs, n_dim = X_emb.shape
    density = 1 if density is None else density
    smooth = 0.5 if smooth is None else smooth

    grs = []
    for dim_i in range(n_dim):
        m, M = np.min(X_emb[:, dim_i]), np.max(X_emb[:, dim_i])
        m = m - 0.01 * np.abs(M - m)
        M = M + 0.01 * np.abs(M - m)
        gr = np.linspace(m, M, int(50 * density))
        grs.append(gr)

    meshes_tuple = np.meshgrid(*grs)
    X_grid = np.vstack([i.flat for i in meshes_tuple]).T
    
    # p1, _, _, _, C = s._kernel_density_estimate_anisotropic(
    #   X_grid, rotational_matrix, r_emb)
    
    p1, _, _, _ = s._kernel_density_estimate(
      X_grid)
     
    # estimate grid velocities
    if n_neighbors is None:
        n_neighbors = int(n_obs / 50)
    nn = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=-1)
    nn.fit(X_emb)
    dists, neighs = nn.kneighbors(X_grid)

    scale = np.mean([(g[1] - g[0]) for g in grs]) * smooth
    weight = normal.pdf(x=dists, scale=scale)
    p_mass = weight.sum(1)
    
    # p_mass = p1
    V_grid = (V_emb[neighs] * weight[:, :, None]).sum(1)
    # V_grid = V_emb[neighs] 
    V_grid /= np.maximum(1, p_mass)[:, None]
    if min_mass is None:
        min_mass = 1    
    

    min_mass *= np.percentile(p_mass, 99) / 100
    # min_mass = 0.01
    X_grid, V_grid = X_grid[p_mass > min_mass], V_grid[p_mass > min_mass]
    
    if autoscale:
          V_grid /= 3 * quiver_autoscale(X_grid, V_grid)
    
    plt.contourf(meshes_tuple[0], meshes_tuple[1], p1.reshape(int(50 * density),int(50 * density)),
                  levels=20, cmap='Blues')
    emb = adata.obsm[embedding]
    # color = np.array(adata.obs['leiden']).astype(int)
    # plt.scatter(emb[:,0],emb[:,1], s=1, c=color, cmap='Set2', alpha=0.1)
    plt.scatter(emb[:,0],emb[:,1], s=1, alpha=0.1)
    plt.title('Eigengene')
    plt.xticks([])
    plt.yticks([])
    plt.quiver(X_grid[:,0], X_grid[:,1],V_grid[:,0],V_grid[:,1],color='black',alpha=1,scale=3)
    plt.show()
    plt.clf()
    
    
def matrix_multiply(X, Y):
   # X shape: (11951, 60, 100)
   # Y shape: (100, 14577)
   # The goal is to multiply each 60x100 matrix in X with Y, resulting in 11951 matrices of size 60x14577

   # Reshape X to a 2D array for matrix multiplication
   X_reshaped = X.reshape(-1, Y.shape[0])  # Shape becomes (11951*60, 100)
   
   # Perform matrix multiplication
   result = np.dot(X_reshaped, Y)  # Resulting shape is (11951*60, 14577)
   
   # Reshape the result back to 3D
   result_reshaped = result.reshape(X.shape[0], X.shape[1], Y.shape[1])  # Shape becomes (11951, 60, 14577)

   return result_reshaped


from multiprocessing import Pool
# import itertools
def compute_norm_chunk(array, start, end):
    # Slice the actual array
    chunk = array[start:end]
    return np.linalg.norm(chunk, axis=1)

def compute_norm_parallel(array, chunk_size):
    # Split the first dimension into chunks
    ranges = [(i, min(i + chunk_size, array.shape[0])) for i in range(0, array.shape[0], chunk_size)]

    with Pool() as pool:
        # Map the compute_norm_chunk function to each chunk
        results = pool.starmap(compute_norm_chunk, [(array, r[0], r[1]) for r in ranges])
    # Concatenate the results
    return np.concatenate(results)

# @numba.njit()
def feature_loading(
        adata: AnnData,
        parallel=False
            ):
    """
    Compute the feature variation and feature loadings based on local SVD.
    
    Parameters
    ----------
    adata : AnnData
        An annotated data matrix.
    """
    import numpy as np
    gauge_vh = adata.obsm['gauge_vh'].copy()
    # gauge_vh_original = adata.obsm['gauge_vh_original'].copy()
    # gauge_vh = gauge_vh_original
    
    # gauge_u = adata.obsm['gauge_u'].copy()
    singular_values_collection = adata.obsm['gauge_singular_value'].copy()
    pca_vh = adata.varm['pca_vh'].copy().T
    
    T1 = time.time()
    # Compute intrinsic dimensionality locally
    def pc_accumulation(arr, threshold):
        arr_sum = np.sum(np.square(arr))
        temp_sum = 0
        for i in range(arr.shape[0]):
            temp_sum += arr[i] * arr[i]
            if temp_sum > arr_sum * threshold:
                return i
    
    threshold = 0.9
    
    intrinsic_dim = np.zeros(adata.shape[0]).astype(int)
    
    for i in range(adata.shape[0]):            
        intrinsic_dim[i] = pc_accumulation(singular_values_collection[i], threshold)
    plt.hist(intrinsic_dim)
    plt.title('Local_intrinsic_dim')
    plt.show()
    plt.clf()
    
    adata.obs['instrinsic_dim'] = intrinsic_dim
    T2 = time.time()
    print(f'Local intrinsic dim time is {T2-T1}')
    
    # sc.pl.embedding(adata,'featmap',color=['instrinsic_dim'],cmap='plasma')
    # sc.pl.embedding(adata,'umap',color=['instrinsic_dim'],cmap='plasma')
    
    # Compute the gene norm in top k PCs (norm of the arrow in biplot)
    k = int(np.median(intrinsic_dim))
    
    print("Start matrix multiplication")
    T1 = time.time()
    pcVals_project_back = np.matmul(gauge_vh, pca_vh[np.newaxis, :])
    # pcVals_project_back =  matrix_multiply(gauge_vh, pca_vh)
    T2 = time.time()
    print(f'Finish matrix multiplication in {T2-T1}')
    
    T1 = time.time()
    
    # if parallel:
    # gene_val_norm = compute_norm_parallel(pcVals_project_back[:, :k, :], 500)
    # else:
    # gene_val_norm = np.linalg.norm(pcVals_project_back[:, :k, :], axis=1)
    gene_val_norm = np.sum((pcVals_project_back[:, :k, :])**2, axis=1) # square norm


    # velocity = gene_val_norm
    # adata.obsm['pc_loadings'] = pcVals_project_back[:, :k, :]
    adata.layers['variation_feature'] = gene_val_norm
    T2 = time.time()
    print(f'Finish norm calculation in {T2-T1}')
    
    T1 = time.time()        
    gene_norm_first_two = np.linalg.norm(pcVals_project_back[:, :2, :], axis=1)
    pc_loadings_scale = pcVals_project_back[:, :2, :] /\
        gene_norm_first_two[:,np.newaxis,:] *\
            gene_val_norm[:,np.newaxis,:]
    
    # pc_loadings_scale = pcVals_project_back[:, :2, :] /\
    #     np.linalg.norm(pcVals_project_back[:, :2, :], axis=1)[:,np.newaxis,:] 
    
    adata.obsm['feature_loading_scale'] = pc_loadings_scale
    T2 = time.time()
    print(f'Finish feature loading in {T2-T1}')
    
    # Feature loadings on each local gauge
    gauge_vh_emb = adata.obsm['VH_embedding']
    feature_loading_emb = adata.obsm['feature_loading_scale'] 
    feature_loadings_embedding = np.matmul(feature_loading_emb.transpose(0,2,1), gauge_vh_emb.transpose(0,2,1)) # Project to gauge_embedding
    adata.obsm['feature_loading_embedding'] = feature_loadings_embedding.transpose(0,2,1)
    
    
# @numba.njit()
# def local_svd(
#         data,
#         weight,
#         k
#         ):
#     gene_val_norm = np.empty((data.shape[0], data.shape[1]), dtype=np.float32)
#     pc_loadings_scale = np.empty((data.shape[0],2, data.shape[1]), dtype=np.float32)
    
#     for row_i in range(data.shape[0]):
        
#         # row_i = 0
#         row_weight = weight[row_i]
        
#         # if len(row_weight) < n_neighbors_in_guage:
#         #     raise ValueError(
#         #         "Some rows contain fewer than n_neighbors distances!"
#         #     )
#         #  val = np.exp(-((knn_dists[i, j] - rhos[i]) / (sigmas[i])))
#         data_around_i_index = np.argsort(-row_weight)[1: 61]
#         # print('data_around_i_index, ' + str(data_around_i_index))
#         data_around_i = data[data_around_i_index] - data[row_i]
        
#         weight_around_i = np.zeros(60, dtype=np.float32)
#         for neighbor_j in range(60):
#             neighbor_j_index = data_around_i_index[neighbor_j]
#             weight_around_i[neighbor_j] = weight[row_i][neighbor_j_index]
#             # idx = np.intersect1d(np.where(head==row_i)[0], np.where(tail==neighbor_j_index)[0])[0]
#             # weight_around_i[neighbor_j] = weight[idx]
            
#         # weighted SVD around i
#         # store first n_components rows of VH
#         weight_around_i = np.diag(weight_around_i) / np.sum(weight_around_i)
#         weight_around_i = np.sqrt(weight_around_i)
#         _, _, vh = np.linalg.svd(np.dot(weight_around_i, data_around_i), full_matrices=False)
        
#         # gene_val_norm[row_i, :] = np.linalg.norm(vh[:k,:], axis=0)
#         gene_val_norm[row_i, :] = np.sum(vh[:k,:]**2, axis=0)

#         # pc_loadings_scale[row_i, :, :] = vh[:2,:]/\
#         #     np.linalg.norm(vh[:2,:], axis=0) *\
#         #         gene_val_norm[row_i, :]
        
#         pc_loadings_scale[row_i, :, :] = vh[:2,:]/\
#             np.sum(vh[:2,:]**2, axis=0) *\
#                 gene_val_norm[row_i, :]
        
#     return gene_val_norm, pc_loadings_scale 


# def feature_loading(
#         adata: AnnData
#             ):
#     """
#     Compute the feature variation and feature loadings based on local SVD.
    
#     Parameters
#     ----------
#     adata : AnnData
#         An annotated data matrix.
#     """
#     import numpy as np
#     # gauge_vh = adata.obsm['gauge_vh'].copy()
#     # gauge_vh_original = adata.obsm['gauge_vh_original'].copy()
#     # gauge_vh = gauge_vh_original
    
#     # gauge_u = adata.obsm['gauge_u'].copy()
#     singular_values_collection = adata.obsm['gauge_singular_value'].copy()
#     # pca_vh = adata.varm['pca_vh'].copy().T
    
#     T1 = time.time()
#     # Compute intrinsic dimensionality locally
#     def pc_accumulation(arr, threshold):
#         arr_sum = np.sum(np.square(arr))
#         temp_sum = 0
#         for i in range(arr.shape[0]):
#             temp_sum += arr[i] * arr[i]
#             if temp_sum > arr_sum * threshold:
#                 return i
    
#     threshold = 0.9
    
#     intrinsic_dim = np.zeros(adata.shape[0]).astype(int)
    
#     for i in range(adata.shape[0]):            
#         intrinsic_dim[i] = pc_accumulation(singular_values_collection[i], threshold)
#     plt.hist(intrinsic_dim)
#     plt.title('Local_intrinsic_dim')
#     plt.show()
#     plt.clf()
    
#     adata.obs['instrinsic_dim'] = intrinsic_dim
#     T2 = time.time()
#     print(f'Local intrinsic dim time is {T2-T1}')
    
     
#     # Compute the gene norm in top k PCs (norm of the arrow in biplot)
#     k = int(np.median(intrinsic_dim))
    
#     weight = adata.obsm['weight_graph'].toarray()
#     # knn_index = adata.obsm['knn_indices'] 
#     data = adata.X.astype(np.float32)
    
#     # gene_val_norm = np.empty((data.shape[0], data.shape[1]), dtype=np.float32)
#     # pc_loadings_scale = np.empty((data.shape[0],2, data.shape[1]), dtype=np.float32)

#     T1 = time.time()
    
#     # for row_i in range(data.shape[0]):
        
#     #     # row_i = 0
#     #     row_weight = weight[row_i]
        
#     #     # if len(row_weight) < n_neighbors_in_guage:
#     #     #     raise ValueError(
#     #     #         "Some rows contain fewer than n_neighbors distances!"
#     #     #     )
#     #     #  val = np.exp(-((knn_dists[i, j] - rhos[i]) / (sigmas[i])))
#     #     data_around_i_index = np.argsort(-row_weight)[1: 61]
#     #     # print('data_around_i_index, ' + str(data_around_i_index))
#     #     data_around_i = data[data_around_i_index] - data[row_i]
        
#     #     weight_around_i = np.zeros(60, dtype=np.float32)
#     #     for neighbor_j in range(60):
#     #         neighbor_j_index = data_around_i_index[neighbor_j]
#     #         weight_around_i[neighbor_j] = weight[row_i][neighbor_j_index]
#     #         # idx = np.intersect1d(np.where(head==row_i)[0], np.where(tail==neighbor_j_index)[0])[0]
#     #         # weight_around_i[neighbor_j] = weight[idx]
            
#     #     # weighted SVD around i
#     #     # store first n_components rows of VH
#     #     weight_around_i = np.diag(weight_around_i) / np.sum(weight_around_i)
#     #     weight_around_i = np.sqrt(weight_around_i)
#     #     _, _, vh = np.linalg.svd(np.dot(weight_around_i, data_around_i), full_matrices=False)
        
#     #     # gene_val_norm[row_i, :] = np.linalg.norm(vh[:k,:], axis=0)
#     #     gene_val_norm[row_i, :] = np.sum(vh[:k,:]**2, axis=0)

#     #     # pc_loadings_scale[row_i, :, :] = vh[:2,:]/\
#     #     #     np.linalg.norm(vh[:2,:], axis=0) *\
#     #     #         gene_val_norm[row_i, :]
        
#     #     pc_loadings_scale[row_i, :, :] = vh[:2,:]/\
#     #         np.sum(vh[:2,:]**2, axis=0) *\
#     #             gene_val_norm[row_i, :]
    
    
#     gene_val_norm, pc_loadings_scale = local_svd(data, weight, k)
#     T2 = time.time()
#     print(f'Finish norm calculation in {T2-T1}')

       
    
#     # print("Start matrix multiplication")
#     # T1 = time.time()
#     # pcVals_project_back = np.matmul(gauge_vh, pca_vh[np.newaxis, :])
#     # # pcVals_project_back =  matrix_multiply(gauge_vh, pca_vh)
#     # T2 = time.time()
#     # print(f'Finish matrix multiplication in {T2-T1}')
    
#     # T1 = time.time()
#     # gene_val_norm = np.linalg.norm(pcVals_project_back[:, :k, :], axis=1)


#     # velocity = gene_val_norm
#     # adata.obsm['pc_loadings'] = pcVals_project_back[:, :k, :]
#     adata.layers['variation_feature'] = gene_val_norm
#     # T2 = time.time()
#     # print(f'Finish norm calculation in {T2-T1}')
    
    
#     # # pc_loadings_scale = pcVals_project_back[:, :2, :] /\
#     # #     np.linalg.norm(pcVals_project_back[:, :2, :], axis=1)[:,np.newaxis,:] *\
#     # #         np.linalg.norm(pcVals_project_back[:, :k, :], axis=1)[:,np.newaxis,:]
#     # T1 = time.time()        
#     # pc_loadings_scale = pcVals_project_back[:, :2, :] /\
#     #     np.linalg.norm(pcVals_project_back[:, :2, :], axis=1)[:,np.newaxis,:] 
    
#     adata.obsm['feature_loading_scale'] = pc_loadings_scale
#     T2 = time.time()
#     print(f'Finish feature loading in {T2-T1}')
    
#     # Feature loadings on each local gauge
#     gauge_vh_emb = adata.obsm['VH_embedding']
#     feature_loading_emb = adata.obsm['feature_loading_scale'] 
#     feature_loadings_embedding = np.matmul(feature_loading_emb.transpose(0,2,1), gauge_vh_emb.transpose(0,2,1)) # Project to gauge_embedding
#     adata.obsm['feature_loading_embedding'] = feature_loadings_embedding.transpose(0,2,1)
    
    
    

 
def plot_feature(
        adata:AnnData,
        feature='',
        embedding='X_featmap',
        cluster_key='clusters',
        plot_within_cluster=[],
        pseudotime_adjusted=False,
        pseudotime='dpt_pseudotime',
        trend='positive',
        ratio=0.2,
        density=1,
        smooth=0.5,
        n_neighbors=None,
        min_mass=1,
        autoscale=True,):
    """
    Plot a given feature (e.g., gene) in two dimensional visualization

    Parameters
    ----------
    adata : AnnData
        An annotated data matrix.
    feature : string
        Feature name to be plotted.
    embedding : string
        Embedding background for feature plot. The default is 'X_featmap'.
    cluster_key : string
        Cluster name indicator. The default is 'clusters'.
    plot_within_cluster : list
        A list of clusters in which the feaure is to plot. The default is [].
    pseudotime_adjusted : bool
        Whether to adjust the feature direction by pseudotime. The default is False.
    pseudotime : string
        Pseudotime indicator. The default is 'dpt_pseudotime'.
    trend : string of {'positive','negative'}
        The direction along pseudotime. The default is 'positive'.
    ratio : float
        Filtering ratio by expression to filter varition by low expression. The default is 0.5.
    density : float
        Grid desity for plot. The default is 1.
    smooth : float
        For kde estimation. The default is 0.5.
    n_neighbors : int
        Number of neighbours for kde. The default is None.
    min_mass : float
        Minumum denstiy to show the grid plot. The default is 1.
    autoscale : bool
        Scale the arrow plot. The default is True.

   """
    # Compute the feature loading embedding
    # feature_loading(adata)
   
    vkey=f'feature_{feature}_loading'

    feature_id = np.where(adata.var_names == feature)[0][0]
    adata.obsm[vkey] = adata.obsm['feature_loading_embedding'][:,:,feature_id]

    # Set grid as the support
    X_emb=adata.obsm[embedding]
    # rotational_matrix = adata.uns['emb_umap']._densmap_kwds['VH_embedding']
    # rotational_matrix = adata.obsm['VH_embedding']
    # r_emb = adata.obsm['rad_emb_no_log']
    s = Scms(X_emb, 0.5, min_radius=5)
    
    V_emb=adata.obsm[vkey] 
    idx_valid = np.isfinite(X_emb.sum(1) + V_emb.sum(1))
    X_emb = X_emb[idx_valid]
    V_emb = V_emb[idx_valid]

    # prepare grid
    n_obs, n_dim = X_emb.shape
    density = 1 if density is None else density
    smooth = 0.5 if smooth is None else smooth

    grs = []
    for dim_i in range(n_dim):
        m, M = np.min(X_emb[:, dim_i]), np.max(X_emb[:, dim_i])
        m = m - 0.01 * np.abs(M - m)
        M = M + 0.01 * np.abs(M - m)
        gr = np.linspace(m, M, int(50 * density))
        grs.append(gr)

    meshes_tuple = np.meshgrid(*grs)
    X_grid = np.vstack([i.flat for i in meshes_tuple]).T

    # p1, _, _, _, C = s._kernel_density_estimate_anisotropic(
    #   X_grid, rotational_matrix, r_emb)
    p1, _, _, _ = s._kernel_density_estimate(
      X_grid)
     
    # estimate grid variation
    if n_neighbors is None:
        n_neighbors = int(n_obs / 50)
    nn = NearestNeighbors(n_neighbors=n_neighbors, n_jobs=-1)
    nn.fit(X_emb)
    dists, neighs = nn.kneighbors(X_grid)

    scale = np.mean([(g[1] - g[0]) for g in grs]) * smooth
    weight = normal.pdf(x=dists, scale=scale)
    p_mass = weight.sum(1)
    
    # p_mass = p1
    V_grid = (V_emb[neighs] * weight[:, :, None]).sum(1)
    # V_grid = V_emb[neighs] 
    V_grid /= np.maximum(1, p_mass)[:, None]
    if min_mass is None:
        min_mass = 1    
    
    # Restrict the plot within given clusters
    def grid_within_cluster(X_grid):
        nn = NearestNeighbors(n_neighbors=1, n_jobs=-1)
        nn.fit(X_emb)
        _, neighs = nn.kneighbors(X_grid)
        
        # plot_within_cluster = ['Beta']
        if len(plot_within_cluster) > 0:
            grid_in_cluster = []
            for cluster in plot_within_cluster:
                idx_in_cluster = np.where(np.array(adata.obs[cluster_key] == cluster))[0]
                for i in range(neighs.shape[0]):
                    if neighs[i,0] in idx_in_cluster:
                        grid_in_cluster.append(i)
        return grid_in_cluster

    # start ploting feature 
    feature_id = np.where(adata.var_names == feature)[0][0]
    # average expression in grid points over NNs
    expr_grid = []
    
    if isinstance(adata.X, np.ndarray):
        expr_count = adata.X.copy()[:,feature_id]
    else:
        expr_count = adata.X.toarray().copy()[:,feature_id]

    
    expr_grid = (expr_count[neighs] * weight).sum(1)
    expr_grid /= np.maximum(1, p_mass)
    
    # Filter the expr_velo by low expression 
    threshold = max(expr_grid) * ratio
    # feature_velo_loading = pc_loadings_grid[:,:,feature_id]
    V_grid[expr_grid<threshold]=np.nan
    
    min_mass *= np.percentile(p_mass, 99) / 100
    # min_mass = 0.01
    X_grid, V_grid = X_grid[p_mass > min_mass], V_grid[p_mass > min_mass]
    if autoscale:
          V_grid /= 2* quiver_autoscale(X_grid, V_grid)
          
    # Adjust the v direction by the sign of local expression change
    # V_grid = V_grid * 10
    displace_grid = X_grid + V_grid
    grid_idx = np.unique(np.where(np.isnan(displace_grid) == False)[0])
    _, displace_grid_neighs = nn.kneighbors(displace_grid[grid_idx])
    _, start_grid_neighs = nn.kneighbors(X_grid[grid_idx])
    displace_expr = np.mean(expr_count[displace_grid_neighs[:,:100]], axis=1) - np.mean(expr_count[start_grid_neighs[:,:100]],axis=1)
    displace_expr_sign = np.sign(displace_expr)
    # displace_expr_sign[displace_expr_sign == 0] = 1
    V_grid[grid_idx] = np.multiply(V_grid[grid_idx], displace_expr_sign[:, np.newaxis])
    
    
    # Keep arrows along the positive (negative) trend of time flow 
    if pseudotime_adjusted:
        time_ = np.array(adata.obs[pseudotime])
        
        displace_grid_adjusted = X_grid + V_grid
        grid_idx_adjusted = np.unique(np.where(np.isnan(displace_grid_adjusted) == False)[0])
        _, displace_grid_neighs = nn.kneighbors(displace_grid_adjusted[grid_idx_adjusted])
        _, start_grid_neighs = nn.kneighbors(X_grid[grid_idx_adjusted])
        displace_time = np.mean(time_[displace_grid_neighs[:,:100]], axis=1) - np.mean(time_[start_grid_neighs[:,:100]],axis=1)
        displace_time_sign = np.sign(displace_time)
        
        if trend == 'positive':
            displace_time_sign[displace_time_sign < 0] = 0
        else:
            displace_time_sign[displace_time_sign > 0] = 0
            displace_time_sign[displace_time_sign < 0] = 1
    
        V_grid[grid_idx_adjusted] = np.multiply(V_grid[grid_idx_adjusted], displace_time_sign[:, np.newaxis])

   
    plt.contourf(meshes_tuple[0], meshes_tuple[1], p1.reshape(int(50 * density),int(50 * density)),
                  levels=20, cmap='Blues')
    emb = adata.obsm[embedding]
    # color = np.array(adata.obs['leiden']).astype(int)
    # plt.scatter(emb[:,0],emb[:,1], s=1, c=color, cmap='Set2', alpha=0.1)
    plt.scatter(emb[:,0],emb[:,1], s=1, alpha=0.1)
    plt.title(feature)
    plt.xticks([])
    plt.yticks([])
    if len(plot_within_cluster) > 0:
        grid_in_cluster = grid_within_cluster(X_grid)
        plt.quiver(X_grid[grid_in_cluster,0], X_grid[grid_in_cluster,1],V_grid[grid_in_cluster,0],V_grid[grid_in_cluster,1],color='black',alpha=1)
    else:
        plt.quiver(X_grid[:,0], X_grid[:,1],V_grid[:,0],V_grid[:,1],color='black',alpha=1,scale=2)
    plt.show()
    plt.clf()
    # plt.savefig(f'./data/flow/gene_{feature}.pdf')


def feature_variation_embedding(
        adata,
        layer = 'variation_feature',
        variation_preprocess_flag=False,
        random_state=42
        ):
    
    adata_var = ad.AnnData(X=adata.layers[layer].copy(), )
    adata_var.X[np.isnan(adata_var.X)]=0
    
    adata_var.obs_names = adata.obs_names
    adata_var.var_names = adata.var_names
    adata_var.obs['clusters'] = adata.obs['clusters'].copy()
    adata_var.layers['counts'] = adata.X.copy()
    
    # Normalization
    # sc.pl.highest_expr_genes(adata_var, n_top=20,)
    sc.pp.normalize_total(adata_var, target_sum=1e4 )
    sc.pp.log1p(adata_var, )
    
    if variation_preprocess_flag:
        # Filtering variation for DGV 
        adata_var.layers['var_filter'] = adata_var.X.copy()
        # Filter low variation
        idx = adata_var.layers['var_filter'] < np.max(adata_var.layers['var_filter']) * 0.2
        # idx = adata_var.layers['var_filter'] < np.quantile(adata_var.layers['var_filter'], 0.2)
        # print(f'Low var ratio is {np.sum(idx) / (idx.shape[0]*idx.shape[1])}')
        adata_var.layers['var_filter'][idx] = 0
        
        # Filter variation by low count
        if isinstance(adata.X, np.ndarray):
            idx = adata.X < np.max(adata.X) * 0.2
        else:
            idx = adata.X.toarray() < np.max(adata.X.toarray()) * 0.2

        # idx = adata.X.toarray() < np.quantile(adata.X.toarray()[np.nonzero(adata.X.toarray())], 0.2)

        # idx = adata.X < np.max(adata.X) * 0.2
        # print(f'Low var ratio by expression is {np.sum(idx) / (idx.shape[0]*idx.shape[1])}')
        adata_var.layers['var_filter'][idx] = 0
        # Normalization
        sc.pp.normalize_total(adata_var, target_sum=1e4, layer='var_filter' )
        sc.pp.log1p(adata_var, layer='var_filter')
    
    # Variation embedding
    data_original = adata_var.X.copy()
    data_original[np.isnan(data_original)] = 0
    
    # PCA by svd
    u, s, vh = scipy.sparse.linalg.svds(
        data_original, k= min(data_original.shape[1]-1, 50), which='LM', random_state=42)
    # u, s, vh = scipy.linalg.svd(gene_val_norm, full_matrices=False)
    # PCA coordinates in first 100 dims
    emb_svd = np.matmul(u, np.diag(s))
    
    import umap
    emb_umap = umap.UMAP(random_state=random_state, n_neighbors=30,min_dist=0.5, spread=1, n_components=2).fit(emb_svd)
    adata_var.obsm['X_featmap_v'] = emb_umap.embedding_
    sc.pl.embedding(adata_var, 'featmap_v', legend_fontsize=10,color=['clusters'], projection='2d', size=20, )
    
    # sc.pl.embedding(adata_var, 'umap_v', legend_fontsize=10,color=['clusters_original'], projection='2d', size=20, )
    adata.obsm['X_featmap_v'] = adata_var.obsm['X_featmap_v']
    
    return adata_var
    

#%%

# adata.obsm['variation_featmap'] = gauge_emb_scale[:,0,:]
# plot_gauge(adata, embedding='X_featmap', vkey='X_gauge_v2' ) 
