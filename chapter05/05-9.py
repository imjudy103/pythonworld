import os
os.chdir("c:/doit")
f = os.popen("dir")
print(f.read())