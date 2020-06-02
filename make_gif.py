import argparse
import glob
import imageio
import os
import time

import cv2

parser = argparse.ArgumentParser(description='make gif')    
    
parser.add_argument('--mask_path', default='./results/masks/')
parser.add_argument('--final_path', default='./results/final')
parser.add_argument('-result_path', default='./results/')

args = parser.parse_args()
    
if __name__ == '__main__':
    mask_files = sorted(glob.glob(os.path.join(args.mask_path, '*.png')))
    final_files = sorted(glob.glob(os.path.join(args.final_path, '*.jp*')))
    
    masks = [cv2.cvtColor(cv2.imread(mask), cv2.COLOR_BGR2RGB) for mask in mask_files]
    finals = [cv2.cvtColor(cv2.imread(final), cv2.COLOR_BGR2RGB) for final in final_files]
    
    
    mask_start = time.time()
    imageio.mimsave(os.path.join(args.result_path, 'mask.gif'), masks)
    print('mask mimsave, %.4f' %(time.time() - mask_start))
    
    final_start = time.time()    
    imageio.mimsave(os.path.join(args.result_path, 'final.gif'), finals)
    print('final mamsave, %.4f' %(time.time() - final_start))
    
    
