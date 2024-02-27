
# Structure from Motion (SfM) and Neural Radiance Fields (NeRF) Project


| ![image1](./NeRF/test_gif.gif) | ![image2](./sfm_p/Phase1/outputs/Registered_camera_poses_with_nonlinear_PnP2.png) |
|:--:|:---:|
| NeRF | SFM |



This repository contains the academic project for 3D scene reconstruction from multiple images with different viewing angles using Computer Vision techniques called Neural Radiance Fields (NeRF) and Structure from Motion (SfM). The project was conducted as part of the course Computer Vision-RBE-549 during the spring semester of 2024. The official university course project page can be found [here](https://pear.wpi.edu/teaching/rbe549/spring2024.html).


## Table of Contents
- [About The Project](#about-the-project)
- [Repository Structure](#repository-structure)
- [Technologies](#technologies)
- [Installation & Usage](#installation--usage)
- [Contributing](#contributing)


## About The Project
The project was implemented in a month of February 2024. It consists of 2 phases: SfM and NeRF. NeRF is to be implemented. 

SfM:
This phase consists of reconstruction of the 3D scene and camera pose estimation of a monocular camera using a computer vision technique called Structure from Motion (SfM). Here, we are creating the entire rigid structure from a set of images with different viewpoints (or equivalently a camera in motion). By extracting and using common features between multiple images, we are obtaining a 3D point cloud of the scene. The methodology includes feature matching, estimation of a fundamental and essential matrix, triangulation, PnPRANSAC and bundle adjustment technique to obtain a 3D point cloud of a scene.Implement feature matching, epipolar geometry, RANSAC, visibility matrix, and bundle adjustment techniques for SfM. Develop a data loader, parser, network, and loss function for NeRF.Generate a 3D reconstruction of the scene using the combined SfM and NeRF techniques.


## Repository Structure
The repository is structured as follows:

- `/Phase1`: This folder contains all the source code for the Structure from Motion.
- `/Phase2`: This folder will hold all the source code for the Neural Radiance Fields (NeRF).
- `/report`: This folder contains the academic report documenting the project, including the methodology, experimental results, and conclusions.
- `/sfm_p/Data`: This folder contains the data provided on the course project page 

## Technologies used
The project utilizes the following technologies:


- SfM: Structure from Motion for estimating the 3D structure of the scene.
- NeRF: Neural Radiance Fields for volumetric scene representation.
- Epipolar Geometry & RANSAC: Techniques for accurate estimation of 3D points from multiple views.


## Installation
To run the project on a local machine, follow these steps:

1. Clone the repository:

```shell
git clone https://github.com/SwatiShirke/SfM-NeRF.git
 ```
 
Install the required dependencies. You can use the provided requirements.txt file to install the necessary packages. Run the following command:


```shell
pip install -r requirements.txt
 ```
 
Run the project using the provided scripts or commands. Refer to the documentation or project files for specific instructions on running the SfM and NeRF algorithms.

## References

[1] Agarwal, S., Snavely, N., Simon, I., Seitz, S. M., & Szeliski, R. (2011).
Building Rome in a Day. Proceedings of the International Conference on
Computer Vision (ICCV), 1792-1799. University of Washington, Cornell
University, Microsoft Research.
[2] C.Wu,”VisualSFM A Visual Structure from MotionSystem,”Computer
Vision at Stony Brook University,Available:http://ccwu.me/vsfm/
[3] Wikipedia contributors.(2022,February18).Eight-point
algorithm. In Wikipedia. Retrieved February 21, 2024, from
https://en.wikipedia.org/wiki/Eight-point algorithm
[4] SciPy Cookbook. (n.d.). Bundle Adjustment. Retrieved from
https://scipycookbook.readthedocs.io/items/bundle adjustment.html
[5] Prasannanatu. (2022, February 21). SfM and NeRF Implementation.
GitHub. https://github.com/Prasannanatu/sfm and nerf.git


## Tags

- Computer Graphics
- Comupter Vision
- 3D Reconstruction
- Neural Radiance Fields
- Structure from Motion
- View Synthesis 


