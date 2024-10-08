# unmht

Very basic python tool that extracts resources from an MHTML file and saves them
to a directory for viewing / further processing.

Usage:

```
python3 unmht.py example.mhtml
```
Default output directory : "/files". To change, add option "-o path/to/directory".

`getCss.py` can generate html tags to include all extracted css files, makes it easier to copy into the main html file.

Fixed:

HTML file without extension is added ".html" extension.

Resources with question marks, eg 'src="/path/to/script.js?v=3"', the question mark and everything that follows are removed.

Resources with special characters, eg 'src="/path/to/some%20image%20file.jpg"' or css files whose location is "cid:****@mthml.blink", the special characters are replaced with underscores.

Known issues:

Sometimes some links to style sheets are removed from the main html file, I don't know why. The `getCss.py` is created for manually adding the tags.

It seems that it's unable to parse "multipart/alternative" content type.

Current goal:

Converting "mht" and "mhtml" files into single html files, similar to what SingleFile extension does. It seems that SingleFile can't process local html file that links to local resources. A workaround is, run a python server in a directory, then use unmht.py to extract the html and resource files into that folder, open server in browser, then use SingleFile to convert it into a single html file.

Ultimate goal:

Convert "mht" or "mhtml" file directly into a single html file. Probably it can be implemented by using a dict to get all resource locations and data, then replace the links in the html data with the actual resource data.

## Similar software

* [perl unmht](https://www.volkerschatz.com/unix/uware/unmht.html) (crude parsing, did not work for me)
* mpack (doesn’t preserve filenames)
* [mht2htm](https://pgm.bpalanka.com/mht2htm.html) (OMG pascal!)
