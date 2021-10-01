# ZWIBuilder

# Introduction

ZWI files  (https://handwiki.org/wiki/ZWI_file_format) are zip-compressed HTML files (with all media and JSON metadata) used for storing articles offline.
They are similar to HTMLZ or ePub used by e-book readers. However, ZWI are best tuned to keep encyclopedia articles, especially articles that are created using Wiki-style programs that use Wikitext (or Wikicode) as the primary source.

ZWI files can be created using plugins developed for Mediawiki and Dokuwiki. When using these plugins, ZWI file will include the original Wikitext/Wikicode and parsed HTML. The Wikicode is the primary source for Wiki-style encyclopedias, while HTML is a derivation  created by these encyclopedia (that may have large number of templates used to create). 

However, not every encyclopedia can integrate such plugins. Therefore, it is necessary to create a program that creates ZWI files from HTML provided by external encyclopedias.  

ZWIBuilder is a program that creates ZWI files from  external HTML files, without direct access to wikicode. The goal if this program is to create self-contained files with encyclopedic articles with all media, so such articles can be viewed offline  and distributted over the network. 
Currently, this program only works with WP. It needs to be validated for other encyclopedias. You need Python3, bash (which are typically available under Linux/Mac). 

Here are the steps to create a ZWI file using external encyclopediua:

(1) First, search for a word using factseek.org and find some article from WP. Look at this article. This step prepares the article's html, checks internal links and create well-formatted document structure on factseek.org. It also creates verious cached images for equaitions etc. on the external source. 

(2) Run this program as:

````
chmod 755 ARUN
./ARUN [URL]
````

where URL points to the URL from factseek.org document. Note that this can only work if you run this program within about 1 h after viewing on factseek.org since cached images may be removed  on the external source. For example, view this article first uisng a web browser:

````
https://factseek.org/r/wikipedia.php?q=Quark
````

Then, make the ZWI file as:

````
ARUN "https://factseek.org/r/wikipedia.php?q=Quark"
````

This will create Quark.zwi.  The program also attems to view it in firefox (press "y" at the end).

This program is in progress.

S.C. (KSF)

