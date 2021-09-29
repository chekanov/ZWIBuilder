# ZWIBuilder
Builder of ZWI files using HTML for KSF. The goal if this program is to create a self-contained files with encyclopeci article. Currently, only works with WP.
You need python3, bash and Linux. 

Here are the steps to create a ZWI file:

(1) First, perfom search using factseek.org and find sime article from WP. View it. This step prepares the article, checks internal links and create well-formatted document structure on factseek.org. It also creates verious cached images for equaitions etc. on the external source like WP) 

(2) Run this program as this:

chmod 755 ARUN
ARUN [URL]

where URL points to factseek.org document. Note that this can only work if you run this program within about 1 h of viewing, since cached images may desapeare on the external source. For example, view this article first:

https://factseek.org/r/wikipedia.php?q=Quark

Then, make the ZWI file as:

ARUN https://factseek.org/r/wikipedia.php?q=Quark

The program is in progress.

