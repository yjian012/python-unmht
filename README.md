# unmht

Very basic python tool that extracts resources from an MHTML file and saves them
to a directory for viewing / further processing.

Usage:

```
python3 unmht.py example.mhtml
```
Default output : "/files". To change output directory, add option "-o path/to/directory".

`getCss.py` can generate html tags to include all extracted css files, makes it easier to copy into the main html file.

Fixed:

HTML file without extension are added ".html" extension.

Script source with question mark, eg 'src="/path/to/script.js?v=3"', question mark and afterwards are removed.

Css files whose location is "cid:****@mthml.blink" are extracted.


Known bug:

Sometimes some links to style sheets are removed from the main html file, I don't know why. The `getCss.py` is created for manually adding the tags.


Current goal:

I have a lot of "mht" and "mhtml" files where the sources are no longer accessible, but since they're not supported by firefox, I want to convert them into single html files. If I knew of SingleFile extension earlier, I would've used that since the beginning. It seems that SingleFile can't process local html file that links to local resources. Anyway, right now the method I use is: Using unmht.py to extract html and files in a folder where a python server is runninng, open in browser, then use SingleFile to convert to a single html file.

Ultimate goal:

Convert "mht" or "mhtml" file directly into a single html file. Probably it can be implemented by using a dict to get all resource locations and data, then replace the links in the html data with the actual resource data.

## Similar software

* [perl unmht](https://www.volkerschatz.com/unix/uware/unmht.html) (crude parsing, did not work for me)
* mpack (doesn’t preserve filenames)
* [mht2htm](https://pgm.bpalanka.com/mht2htm.html) (OMG pascal!)
