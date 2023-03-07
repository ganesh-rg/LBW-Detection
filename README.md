# LBW Detection Using Computer Vision

This is our approach to the problem statement given to us in JMR Hackathon, which was conducted in NIT Calicut on 4th and 5th of March, 2023

## Problem Statement
Track and predict the ball on cricket pitch right from the release action of the bowler's hand to hitting the batsman bat/ pad or stumps. A video of the ball thrown at the pitch will be given as an to detect, track and predict the ball movement.

## Goal
To predict if its a LBW or not

## Tools Used
OpenCV\
Python
\
\
Detailed Approach is given in the documentation.

## Our Approach in breif

We first try to track the ball and project the trajectory after it hits the batsman.\
Taking the left end of the pitch on bowlers side as origin and x direction moving to right and y direction moving towards the batsmans end and z direction moving upwards, we try to predict the x, y and z co-ordinated of the ball.\
Since only the front (perspective) view is give, determining the y and z co-ordinates becomes challenging.
So we try to track not only the ball, but also the pitch and batsman.Also, since the batsman covers the stumps, determining the co-ordinated of the stumps becomes difficult.
\
\
\
\
## Pitch
![alt text](https://github.com/ganesh-rg/LBW-Detection/blob/main/Images/pitch.png)
\
\
\
\
\
## Ball Detection
![alt text](https://github.com/ganesh-rg/LBW-Detection/blob/main/Images/ball_detect.png)
\
\
\
\
\
\
## Pitch Detection
![alt text](https://github.com/ganesh-rg/LBW-Detection/blob/main/Images/pitch_detect.png)
\
\
\
\
\
## All in one
![alt text](https://github.com/ganesh-rg/LBW-Detection/blob/main/Images/Final.png)




