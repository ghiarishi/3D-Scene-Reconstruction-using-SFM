# 3D-Scene-Reconstruction-using-SFM

In this repository, we have taken 2 input images of a certain location using the same camera, 
but both cameras have been rotated by a certain amount. As a result, here, I have successfully identified
the location where the person was standing when they took the photos. Additionally, I have also
recreated the 3D scene in order to create a panorama. 

Steps: 
1. Perform Least Squares Estimation

2. Perform RANSAC Estimation

3. Draw Epipolar Lines

4. Perform Pose Recovery in order to do 3D Reconstruction

5. Perform Triangulation

Input Images: 

![0014_2](https://user-images.githubusercontent.com/72302800/201511356-587bf5d7-d5a1-4378-be2c-5a1ce0e46c4d.png)
![0017_2](https://user-images.githubusercontent.com/72302800/201511357-d693b411-8408-4d40-b153-6a879b9d51d2.png)

![image](https://user-images.githubusercontent.com/72302800/201511376-a5b73803-b1d2-48ec-a331-c3ba5cb89d64.png)

All Epipolar Lines: 

![image](https://user-images.githubusercontent.com/72302800/201511388-f9040bbe-a6c2-46ac-b36f-7b0a47f70bb2.png)

Output: 

![image](https://user-images.githubusercontent.com/72302800/201511409-d8ed53a7-a550-4e91-8b35-000ee104197f.png)
