ZWI files  (https://handwiki.org/wiki/ZWI_file_format) are zip-compressed HTML files (with all media and JSON metadata) used for storing articles offline.
They are similar to HTMLZ or ePub used by e-book readers. However, ZWI are best tuned to keep encyclopedia articles, especially articles that are created using Wiki-style programs (Mediawiki, TWiki, Dokuwiki) that use Wikitext (or Wikicode) as the primary source for content.

ZWI files can be created using plugins developed for Mediawiki and Dokuwiki  (already exist). When using these ZWI-plugins for wiki-programs, the created ZWI file includes the original Wikitext/Wikicode, all revisions  and the parsed HTML file (with images). In such plugins, Wikitext is the primary source for Wiki-style encyclopedias, while the HTML is a ``derivation''  created by these encyclopedia after parsing Wikitext (such wikis may have large number of templates used to create such HTML, so it is hard to create them using any external program). 

However, not every encyclopedia can integrate such plugins (or want to include such plugins). Therefore, it is necessary to create a program that creates ZWI files from the HTML provided by external encyclopedias.  

Once such ZWI files are created, encyclopedia articles can be "detached" from the databases of original encyclopedias. Such files can be viewed offline, distributed over the network, visualized using desktop/smartphone applications and edited using some offline or online editors. 

This ZWIBuilder is a program that creates ZWI files from  external HTML files, withoutdirect access to Wikitext. The goal of this program is to create self-contained files with encyclopedic articles with all media.  Currently, this program only works with WP. It needs to be validated for other encyclopedias. 

# What do you need 

You need Python3, Bash (which are typically available under Linux/Mac) and Beautiful Soup python library.

# Testing this tool

Here are the steps to create a ZWI file using external encyclopediua:

(1) First, search for a word using factseek.org and find some article from WP. Look at this article. This step prepares the article's html, checks internal links and create well-formatted document structure on factseek.org. It also creates various cached images for equations etc. on the external source. 

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
Note that all iamges should be located in "data/media/images".

Note that the included "meta.json" file has a very basic structure. It is not used during article viewing. It will be used
for external program to visualize this article. It can easily be extended by adding more metadat entries.


This program is in progress.

S.C. (KSF)

