import os
cwd=os.getcwd()+"\\files"
s=""
for subdir, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".css"):
            s+='<link rel="stylesheet" type="text/css" href="'+file+'"/>'
with open("0 cssfiles.txt",'w') as f:
  f.write(s)
