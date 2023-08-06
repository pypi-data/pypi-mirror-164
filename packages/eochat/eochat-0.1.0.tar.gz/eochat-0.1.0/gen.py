import os

#Create a directory in libsodium-stable/src/libsodium/
#Copy this file in there and go to that directory
#Run this program to generate a .txt file
#Copy and paste that in command line

compiler = r"gcc"

with open("run.txt","w") as f:
  for (dirpath, dirnames, filenames) in os.walk("../"):
    for filename in filenames:
      if filename.endswith('.c'):
        f.write("{} -c -Wall -O2 -o {}.o -I ../include/sodium {}\n".format(compiler,filename,os.path.join(dirpath,filename)))