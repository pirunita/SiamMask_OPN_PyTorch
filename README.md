---
title : Guidance module + SiamMask + Onion-peel
version : 0.0.1
writer: khosungpil
type : Version document
objective : Samsung SDS
---

# Environment #
* OS: ubuntu 16.04
* CPU Resource: Inter(R) Core(TM) i7-6700 CPU @ 3.40GHz
* GPU Resource: GTX 1080ti 1x
* Docker Version: 19.03.8

# Directory #
~~~
├── demo.sh

├── docker_setting.sh

├── Siammask_sharp
    ├── SiamMask_DAVIS.pth
    ├── config
    ├── models
    ├── tools
    └── utils
        
├── OnionPeel
    ├── OPN.pth
    └── TCN.pth

├── data
    └── tennis
        └── *.jpg

└── results
    ├── final
        └── *.jpg
    ├── masks
        └── *.png
    ├── final.gif
    └── mask.gif
~~~

# Usage #
## Requirement ##
### Docker version ###
~~~
docker pull khosungpil/sds:1.0

or

bash docker_setting.sh
~~~
### Pretrained model ###
SiamMask_DAVIS: <a href="https://drive.google.com/file/d/1EebLJU0QVi322BYnL7uwHFTOYsm5tTDB/view?usp=sharing">[Download]</a> <br>
OPN: <a href="https://drive.google.com/file/d/1o-NQPsPac5AZixlDkxhm34bOOcy-2Zn6/view?usp=sharing">[Download]</a><br>
TCN: <a href="https://drive.google.com/file/d/1MUM_OH7yIjm2KShZJ4stmA6dXEuX-5jd/view?usp=sharing">[Download]</a><br>


## Demo ##
1. Run ./demo.sh
~~~
bash demo.sh
~~~

2. Select bounding box
3. When press 'a' in keyboard, then determine bounding box.
<p align="center">
<img src='./src/1.png' width="40%" height="40%"><img src='./src/2.png' width="40%" height="40%">


4. When press 'b' in keyboard, then inference each models.
5. You can check the masks in the results/masks throught Siammask
6. You can check the results in the results/final throught Onion-pell
7. Finally, you can check the gif file in the results

<p align="center">
<img src='./src/input.gif', width="30%" height="30%">
<img src='./src/mask.gif' width="30%" height="30%"><img src='./src/final.gif' width="30%" height="30%">


# Reference #

[CVPR 2019] Fast Online Object Tracking and Segmentation: A Unifying Approach
<a href="https://github.com/foolwood/Siammask">[Github]</a>
<br>
[ICCV 2019] Onion-Peel Networks for Deep Video Completion
<a href="https://github.com/seoungwugoh/opn-demo">[Github]</a>