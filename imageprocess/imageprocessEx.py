from PIL import Image
import sys 
import os
a=sys.argv[1]
b=sys.argv[2]
c=os.listdir(f"{a}/")
if(os.path.exists(b)):
    print("folder exists")
else:
    os.mkdir(b)
for i in os.listdir(f"{a}/"):
    q=os.path.splitext(i)[0]
    img=Image.open(f"{a}/{i}")
    img.save(f"{b}/{q}.png",'png')
print("Finished")
