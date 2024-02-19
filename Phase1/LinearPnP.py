"""
persepctive n point 
"""
import random
import numpy as np

def persepctive_n_point():    
    x_pt = np.array([[1,2], [3,4]])
    x_real = np.array([[5,6,1], [7,8,1]])
    K_mat = np.array([[1,6,3],[4,5,6],[7,8,9]]).reshape(3,3)
    p_mat = LinearPnP(x_pt, x_real, K_mat)



def LinearPnP(x_img_list,x_real_list, K_mat):
    x_img, y_img = x_img_list[:,0], x_img_list[:,1]
    x_real, y_real, z_real = x_real_list[:,0],x_real_list[:,1], x_real_list[:,2]
    zeros =  np.zeros(len(x_img_list))
    ones = np.ones(len(x_real_list))
    A1 = np.vstack([ x_real, y_real, z_real, ones,zeros,zeros, ones,zeros, -1* x_img * x_real, -x_img * y_real, -x_img * z_real, -x_img]).T
    A2 = np.vstack([ zeros,zeros,zeros,  zeros, x_real, y_real,  z_real, ones, -y_img * x_real,  -y_img * y_real, -y_img * z_real, -y_img ]).T
    A = np.vstack([A1, A2])

    #perform SVD on the system of equations
    U, D, V_T = np.linalg.svd(A)                       
    p_mat = V_T[-1, :]                                      
    p_mat = p_mat.reshape((3, 4))  

    #calculate Rotation mat and position vector 
    R_mat = np.dot(np.linalg.inv(K_mat) , p_mat[0:3,0:3])
    U, D, V_T = np.linalg.svd(R_mat) 
    R_mat = np.dot(U, V_T)
    d_1 = D[0]
    T = np.dot(np.linalg.inv(K_mat) , p_mat[:,3]) / d_1  

    # determinant of Rotation matrix should be 1, so resvese signs if Det = -1 
    R_mat_det = np.linalg.det(R_mat)
    
    if R_mat_det < 0:
        R_mat = -R_mat
        T = -T 

    C = np.dot(-R_mat.T, T)
    
    return R_mat, C  




 
def pnp_ransac():
    pass

if __name__ == "__main__":
    persepctive_n_point()