# ZWIBuilder
Builder of ZWI files (https://handwiki.org/wiki/ZWI_file_format) using external HTML files. The goal if this program is to create self-contained files with encyclopedic articles. Currently, it only works with WP. You need python3, bash (which are typically available under Linux/Mac). 

Here are the steps to create a ZWI file:

(1) First, perfom search using factseek.org and find some article from WP. LOok at this article. This step prepares the article, checks internal links and create well-formatted document structure on factseek.org. It also creates verious cached images for equaitions etc. on the external source. 

(2) Run this program as:

````
chmod 755 ARUN
./ARUN [URL]
````

where URL points to the factseek.org document. Note that this can only work if you run this program within about 1 h of viewing, since cached images may be removed  on the external source. For example, view this article first uisng a web browser:

````
https://factseek.org/r/wikipedia.php?q=Quark
````

Then, make the ZWI file as:

````
ARUN "https://factseek.org/r/wikipedia.php?q=Quark"
````

This will create Quark.zwi.  The program also attemots to view it in firefox.

This program is in progress.

S.C. (KSF)

