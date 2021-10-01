# ZWIBuilder

# Introduction

ZWI files  (https://handwiki.org/wiki/ZWI_file_format) are zip-compressed HTML files (with all media and JSON metadata) used for storing articles offline.
They are similar to HTMLZ or ePub used by e-book readers. However, ZWI are best tuned to keep encyclopedia articles, especially articles that are created using Wiki-style programs that use Wikitext (or Wikicode) as the primary source.

ZWI files can be created using plugins developed for Mediawiki and Dokuwiki. When using these ZWI-plugins, the created ZWI file includes the original Wikitext/Wikicode, all revisions  and the parsed HTML file (with images). In such plugins, Wikitext is the primary source for Wiki-style encyclopedias, while HTML is a derivation  created by these encyclopedia (that may have large number of templates used to create such HTML). 

However, not every encyclopedia can integrate such plugins (or want). Therefore, it is necessary to create a program that creates ZWI files from the HTML provided by external encyclopedias.  

Once such ZWI files are created, encyclopedia articles can be "detached" from the original encyclopedia, can be viewed offline, ditributeed over the network, visualized using desktop/smaratphone applicatins and eddited using some applications. 

ZWIBuilder is a program that creates ZWI files from  external HTML files, without direct access to Wikicode. The goal of this program is to create self-contained files with encyclopedic articles with all media.  Currently, this program only works with WP. It needs to be validated for other encyclopedias. 

#What do you need to run it

You need Python3, Bash (which are typically available under Linux/Mac). 

#Testing this tool

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

This will create Quark.zwi.  The program also attemts to view this article in firefox (press "y" at the end).

If you want to view this article manually, just do this:


````
unzip Quark.zwi
firefox article.html

````

Note that "meta.json" has a very basic structure. It can be extended by adding more metadata.


This program is in progress.

S.C. (KSF)

