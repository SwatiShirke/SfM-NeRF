"""
This is RANSAC implementation for PnP algorithm 
"""
import random
import numpy as np
from LinearPnP import *

def PnPRANSAC( x_img_list, x_real_list, K_mat, max_iteration, err_threshold,n_point):

    max_feature_inliers = []
    max_real_inliers = []

    for iteration in range(max_iteration):
        index_list = random.sample( range(len(x_img_list)) ,n_point)
        x_img_pt_list  = np.array( x_img_list[index_list])        
        x_real_pt_list = np.array(x_real_list [index_list ])
        R, C = LinearPnP(x_img_pt_list, x_real_pt_list, K_mat)
        C = C.reshape((3,1))
        T = np.dot(-R, C)
        R_T = np.concatenate((R, T), axis=1)        
        p_mat = np.dot(K_mat,  R_T).reshape(3,4)       
        
        p1, p2, p3 = p_mat
        feature_inliers_list = []
        real_inliers_list = []
        for j in range(len(x_img_list)):
            u, v = x_img_list[j,0], x_img_list[j,1]
            error = (u - np.dot(p1.T, x_real_list[j])/ np.dot(p3.T, x_real_list[j]))**2 + (v - np.dot(p2.T, x_real_list[j])/ np.dot(p3.T, x_real_list[j]))**2

            if error < err_threshold:
                feature_inliers_list.append( x_img_list[j] )
                real_inliers_list.append( x_real_list[j] )

        if len(feature_inliers_list) > len(max_feature_inliers):
            max_feature_inliers = feature_inliers_list
            max_real_inliers = real_inliers_list

    ##re-estimate roattion  matrix and camera centre vector 
    R, C = LinearPnP(x_img_pt_list, x_real_pt_list, K_mat)

    return R, C 


if __name__ == "__main__":
    x_pt = np.array([[1,2], [3,4]])
    x_real = np.array([[5,6,1,1], [7,8,1,1]])
    K_mat = np.array([[1,6,3],[4,5,6],[7,8,9]]).reshape(3,3)
    R, C = PnPRANSAC(x_pt, x_real, K_mat, 1, 0.5,2)
    print(R)
    print(C)