#!/usr/bin/env python
# -*- coding: utf-8 -*-
# S.Chekanov
# Task: fetch a cahed file 

import requests
import sys,re,os
import shutil 
import hashlib

xurl=sys.argv[1]
name = xurl.split("=")[-1]
print("Article name=",name)

obj = re.findall('(\w+)://([\w\-\.]+)/(\w+).(\w+)', xurl) 
#print(obj)
xl=obj[0]
baseurl=xl[0]+"://"+xl[1]+"/"+xl[2]
#print("URL=", baseurl)

source=xl[3]
#print("source=", source)

xmd5=hashlib.md5(name.encode()).hexdigest()

dir1=xmd5[0:1]
dir2=xmd5[0:2]
xfull=baseurl+"/cache/en/html/"+source+"/"+dir1+"/"+dir2+"/"+name+".html.gz"
#print("Cached files=",xfull)

r = requests.get(xfull, stream = True)

filename=name+".html.gz"
with open(filename,'wb') as f:
                      shutil.copyfileobj(r.raw, f)
print("File ",filename," saved")
