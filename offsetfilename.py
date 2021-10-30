import os
dir = os.listdir()
for f in dir:
	os.rename(f, ("%7d" % (int(f.split(".")[0])+44960)).replace(" ","0")+".jpg")

