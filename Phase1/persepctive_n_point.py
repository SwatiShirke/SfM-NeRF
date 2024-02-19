"""
persepctive n point 
"""
import random
import numpy as np

def persepctive_n_point():    
    x_pt = np.array([[1,2], [3,4]])
    x_real = np.array([[5,6,1], [7,8,1]])
    p_mat = estimate_p_mat(x_pt,x_real)



def estimate_p_mat(x_img_list,x_real_list):
    x_img, y_img = x_img_list[:,0], x_img_list[:,1]
    x_real, y_real, z_real = x_real_list[:,0],x_real_list[:,1], x_real_list[:,2]
    zeros =  np.zeros(len(x_img_list))
    ones = np.ones(len(x_real_list))
    A1 = np.vstack([ x_real, y_real, z_real, ones,zeros,zeros, ones,zeros, -1* x_img * x_real, -x_img * y_real, -x_img * z_real, -x_img]).T
    A2 = np.vstack([ zeros,zeros,zeros,  zeros, x_real, y_real,  z_real, ones, -y_img * x_real,  -y_img * y_real, -y_img * z_real, -y_img ]).T
    A = np.vstack([A1, A2])

    # Perform SVD on the system of equations
    U, D, V_T = np.linalg.svd(A)                       
    P_mat = V_T[-1, :]                                      
    P_mat = P_mat.reshape((3, 4))  
    return P_mat



 
def pnp_ransac():
    pass

if __name__ == "__main__":
    persepctive_n_point()