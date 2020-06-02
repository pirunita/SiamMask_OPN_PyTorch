---
title : Guidance module + SiamMask + Onion-peel
version : 0.0.1
writer: khosungpil
type : Version document
objective : Samsung SDS
---

# Guidance module + SiamMask + Onion-peel

## Environment ##
* OS: ubuntu 16.04
* CPU Resource: Inter(R) Core(TM) i7-6700 CPU @ 3.40GHz
* GPU Resource: GTX 1080ti 1x
* Docker Version: 19.03.8

## Directory ##
~~~
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

## Usage ##