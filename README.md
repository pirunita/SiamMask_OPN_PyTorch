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
~~~
bash demo.sh
~~~


# Reference #

[CVPR 2019] Fast Online Object Tracking and Segmentation: A Unifying Approach
<a href="https://github.com/foolwood/Siammask">[Github]</a>
<br>
[ICCV 2019] Onion-Peel Networks for Deep Video Completion
<a href="https://github.com/seoungwugoh/opn-demo">[Github]</a>