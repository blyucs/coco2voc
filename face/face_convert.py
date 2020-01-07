#!/usr/bin/env python3
import datetime
import json
import os
import re
import fnmatch
from PIL import Image
import numpy as np
import shutil

ROOT_DIR = './'
IMAGE_DIR = os.path.join(ROOT_DIR, "image")
LABEL_ROOT= os.path.join(ROOT_DIR, "label")
ANNOATION_ROOT = os.path.join(ROOT_DIR, "annotations")


def name_convert(name):
	d= {'lbl00':'base',
	    'lbl01':'facebase',
	    'lbl02':'leftbrow',
	    'lbl03':'rightbrow',
	    'lbl04':'lefteye',
	    'lbl05':'righteye',
	    'lbl06':'nose',
	    'lbl07':'uplip',
	    'lbl08':'mouth',
	    'lbl09':'downlip',
	    'lbl10':'hair',
	    }
	return d[name]

def main():

	if os.path.exists(ANNOATION_ROOT):
		shutil.rmtree(ANNOATION_ROOT)
	os.makedirs(ANNOATION_ROOT)
	# filter for jpeg images
	for root,dirs, files in os.walk(LABEL_ROOT):
		#image_files = filter_for_annotations(root, files)
		for file in files:
			tail_name = os.path.splitext(os.path.basename(file))[0].split('_')[2]
			print(tail_name)
			convert_name = name_convert(tail_name)
			if(convert_name == "base"):
				# continue
				pass #use base
			r_name = root.split('/')[2]+'_'+convert_name+"_0"+".png"
			# move_path=os.path.join(ANNOATION_ROOT,root.split('/')[1])
			# print("{}\n".format(r_name))
			shutil.copyfile(root+'/'+file, ANNOATION_ROOT+'/'+r_name)

if __name__=="__main__":
	main()
