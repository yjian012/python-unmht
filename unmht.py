import email
import os
import os.path
from email.policy import default
import re

specPat=re.compile(b"[%:\*<>]")
srcPat=re.compile(b"src=\"(.*?)\"")
cssPat=re.compile(b"href=\"(.*\.css)")
bgPat=re.compile(b"background=[\"]?(.*?)[\"]?[ >]")
def srcRip(srcIn):
  srcOut=srcIn.group().split(b"/")[-1]
  que=srcOut.find(b'?')
  if que!=-1:
    srcOut=srcOut[:que]
  return b"src=\""+re.sub(specPat,b'_',srcOut)+b"\""
def cssRip(cssIn):
  cssOut=cssIn.group().split(b"/")[-1]
  que=cssOut.find(b'?')
  if que!=-1:
    cssOut=cssOut[:que]
  return b"href=\""+re.sub(specPat,b'_',cssOut)
def bgRip(bgIn):
  return b"background="+re.sub(specPat,b'_',bgIn.group().split(b"/")[-1]+b" ")
def extract_mhtml(file_path: str, output_dir: str="."):
    """Extracts resources from an MHTML file and saves them to a directory.

    Args:
        file_path (str): Path to the MHTML file.
        output_dir (str): Directory where extracted files will be saved.
    """
    os.makedirs(output_dir, exist_ok=True)

    with open(file_path, "rb") as fp:
        msg = email.message_from_binary_file(fp, policy=default)

    boundary = msg.get_boundary()
    if not boundary:
        raise ValueError("MHTML file is missing the boundary string.")
    
    for part in msg.iter_parts():
        content_type = part.get_content_type()
        content_id = part.get("Content-ID")
        content_location = part.get("Content-Location")
        
        #if content_type=="text/html":
          #print(content_location)
        if content_location:
            filename = os.path.basename(content_location)
            if not filename:
              filename="index.html"
        else:
            if not content_type or not content_id:
              continue
            ext = os.path.basename(content_type)
            filename = os.path.basename(content_id) + "." + ext
        que=filename.find('?')
        if que!=-1:
          filename=filename[:que]
        filename=re.sub("[%:\*<>]",'_',filename)
        if filename.endswith("@mhtml.blink"):
          filename=filename[:-12]+(".css")
        content=part.get_payload(decode=True)
        if content_type=="text/html":
          if not (filename.endswith("htm") or filename.endswith("html")):
            filename+=".html"
          content=re.sub(srcPat,srcRip,content)
          content=re.sub(cssPat,cssRip,content)
          content=re.sub(bgPat,bgRip,content)
        with open(os.path.join(output_dir, filename), "wb") as out_file:
            out_file.write(content)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Extract resources from an MHTML file.")
    parser.add_argument("file_path", help="Path to the MHTML file.")
    parser.add_argument("-o", "--output-dir", default="/files", help="Directory to save extracted files.")
    args = parser.parse_args()

    extract_mhtml(args.file_path, args.output_dir)
