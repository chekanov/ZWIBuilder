#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script needs to run imidiatly after viewing wikipedia since WP caches files!
# It is recommended to run in withing a few minutes after watching the WP article 
# If you run this script after 1 day after viewing article, some articles will not be available
# S.Chekanov

from bs4 import *
import argparse
import requests
import re,os
import gzip 
import shutil # to save it locally
import zlib,zipfile
import sys, json, urllib.parse
from time import time 
import tempfile

dirpath = tempfile.mkdtemp()

stime=str(int(time()))
print("Time=",stime)
print("TMP dir=",dirpath)

#### input parameters ####
kwargs = {}
parser = argparse.ArgumentParser()
parser.add_argument('-q', '--quiet', action='store_true', help="don't show verbose")
parser.add_argument('-o', '--output', help="Save output to")
parser.add_argument("-i", '--input', help="Input HTML cached file")
parser.add_argument("-s", '--source', help="Source of encyclopedia")
parser.add_argument("-t", '--title', help="Title of the article")

args = parser.parse_args()
args.verbose = not args.quiet
print("Input=",args.input)
print("Output=",args.output)
print("Article title =",args.title)
print("Encyclopedia source=",args.source)
print("Is verbose=",args.verbose)

# this is where data go
img_dir="data/media/images"
css_dir="data/css"
folder_images=dirpath+"/"+img_dir
folder_css=dirpath+"/"+css_dir

# CREATE FOLDER
def folder_create(images):

    os.system("rm -rf "+folder_images);
    os.system("rm -rf "+folder_css);

    try:
        # folder creation
        os.system("mkdir -p "+folder_images)
        os.system("mkdir -p "+folder_css)
 
    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        pass

    # image downloading start
    download_images(images, folder_images)
  
 
# map to keep replacements for images 
imageReplacer={}
cssReplacer={}


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))

# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    
    # intitial count is zero
    count = 0
  
    # print total images found in URL
    print(f"Total {len(images)} Image Found!")


    if len(images) == 0: return;

    allImages=[]
    for i in range(len(images)):
        if (images[i].get('src') !=None): allImages.append(images[i].get('src'))
        if (images[i].get('srcset') !=None): 
                                     ss= images[i].get('srcset').split();
                                     for i in range(len(ss)):
                                             allImages.append(ss[i])
                                      
        if (images[i].get('data-srcset') !=None): 
                                     ss= images[i].get('data-srcset').split();
                                     for i in range(len(ss)): 
                                            allImages.append(ss[i])
        if (images[i].get('data-src') !=None): allImages.append(images[i].get('data-src'))

    for i in range(len(allImages)):
            image_link=allImages[i]
            if (image_link.find("//")==-1): continue

            if (args.verbose): print(i," ",allImages[i])
                        # 1.data-srcset
                        # 2.data-src
                        # 3.data-fallback-src
                        # 4.src
                        # 5.srcset 


            #newname=os.path.basename(image_link)
            newname = image_link.split("/")[-1]
            filename=folder_name+"/"+newname
            if (args.verbose):  print(count+1, ") downloading=",image_link," to "+filename)

            # correct link when starts with //
            xurl=image_link
            if (xurl.startswith("//")): xurl="https:"+image_link
            r = requests.get(xurl, stream = True)


            # check  svg used in for formulars. Wikipedia does not have file extention! 
            # formulars are made in SVG. The browser should know this by extension. 

            xnames=img_dir+"/"+newname
            if (newname.find(".")==-1):
                if (image_link.find("/svg/")>-1): 
                          filename=folder_name+"/"+newname+".svg";
                          xnames=img_dir+"/"+newname+".svg"; 

            # remeber replacements
            imageReplacer[image_link]=xnames


            # Check if the image was retrieved successfully
            if r.status_code == 200:
              # Set decode_content value to True, file's size will be zero.
              r.raw.decode_content = True

             
              with open(filename,'wb') as f:
                      shutil.copyfileobj(r.raw, f)

              count = count+1
              if (args.verbose): print('Image sucessfully Downloaded: ',filename)
            else:
              print(image_link,' couldn\'t be retreived')
              pass
    print("Downloaded=",count," images")        
    return count


#
def extractCSS(soup):
    count=0
    for link in soup('link'):
        if link.get('href'):
            if link.get('type') == 'text/css' or link['href'].lower().endswith('.css') or 'stylesheet' in (link.get('rel') or []): 
                new_type = 'text/css' if not link.get('type') else link['type']
                css = soup.new_tag('style', type=new_type)
                css['data-href'] = link['href']
                for attr in link.attrs:
                    if attr in ['href']:
                        continue
                    css[attr] = link[attr]
                    r_url=link['href']
                    if (args.verbose): print(css[attr],r_url) 
                    r = requests.get(r_url, allow_redirects=True)
                    newname = r_url.split("/")[-1]
                    filename=folder_css+"/"+newname
                    cssReplacer[ r_url ] = css_dir+"/"+newname 
                    count=count+1 
                    with open(filename,'w') as f:
                        f.write(r.text)
           
    print("Downloaded=",count," css files")        
    return count 


# MAIN FUNCTION START
def main(html):
   
    # content of URL
    #r = requests.get(url)
  
    # Parse HTML Code
    soup = BeautifulSoup(html, 'html.parser')

    # nicely looking
    # html = soup.prettify()   #prettify the html

    # find all images in URL
    images = soup.findAll('img')
  
    # Call folder create function
    folder_create(images)

    # extract CSS
    extractCSS(soup)

    xmedia=[]
    htmlnew=html
    print("-> Make CSS replacements")
    for key in  cssReplacer:
          xmedia.append(cssReplacer[key])
          if (args.verbose): print(key," replaced by ",cssReplacer[key])
          htmlnew=htmlnew.replace(key,cssReplacer[key])

    print("-> Make image replacements")
    n=0
    for key in  imageReplacer:
           xmedia.append(imageReplacer[key])
           if (args.verbose): print(n, ")", key," replaced by ",imageReplacer[key])
           htmlnew=htmlnew.replace(key,imageReplacer[key])
           n=n+1

    output=args.output
    z = zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED)  # this is a zip archive
    z.writestr("article.html", htmlnew)
    #for key in  imageReplacer:
    #    z.write(imageReplacer[key].encode(), imageReplacer[key].encode(), zipfile.ZIP_DEFLATED )
    zipdir(dirpath+'/data/', z)
    #htmltit=os.path.basename(args.input)
    #htmltit=htmltit.replace(".html.gz","")
    #htmltit=htmltit.replace(".html","")
    metadata = {"ZWIversion":"1","Title":args.title, "CreatorName":args.title,"Primary":"article.html","LastModified":stime}
    z.writestr("metadata.json", json.dumps(metadata))
    z.writestr("media.json", json.dumps(xmedia))
    z.close()

    print("Cleared =",dirpath)    
    cmd="rm -rf "+dirpath
    os.system(cmd) 
    print("Created =",args.output)
 

HTML="";
index=args.input

try:

                if index.endswith('.html'):
                   ret = open(index, 'r', encoding='utf-8').read()
                elif index.endswith('.html.gz'):
                  ret =  gzip.open(index, 'rt',encoding='utf-8').read()

                # prepare file  header and footer
                data_head=open('html_header.html', 'r', encoding='utf-8').read();
                data_footer=open('html_footer.html', 'r', encoding='utf-8').read();
                HTML=data_head+ret+data_footer;
                HTML=urllib.parse.unquote(HTML) # replace %28 %29 with ()
except IOError as err:
               print("Error")

# CALL MAIN FUNCTION
main(HTML)
