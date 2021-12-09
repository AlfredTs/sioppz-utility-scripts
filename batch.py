import os
import shutil
from datetime import datetime

#'Opus325846_steel_LB Opus325846_gold_LB Opus325846_steel_LW Opus325846_gold_LW'
def report(message):
	print(datetime.now().strftime("%H:%M:%S")+":"+message)

def interpolate(RIFEexp, OPS):
	o = 'output/'
	proxyDir = o+'proxy'
	reproxyDir = o+'proxy_rifed'	
	
	for op in OPS.split(' '):
		outDir = 'output/'+op
		megaDir = 'mega_output/'+op
		if not os.path.exists(outDir):
			os.mkdir(outDir)

		report("Starting first RIFE")
		os.system('python3 inference_video_moded.py --exp=3 --img=input/'+op+'/ --folder='+outDir)
		if not os.path.exists(megaDir):
			os.mkdir(megaDir)
		
		report("Starting second RIFE")
		os.system('python3 inference_video_moded.py --exp='+str(RIFEexp)+' --img='+outDir+'/ --folder='+megaDir)

		rifedFiles = sorted(os.listdir(megaDir))
		report("Starting transition generation")
		shutil.copyfile(megaDir+"/"+rifedFiles[0],"first.jpg")
		shutil.copyfile(megaDir+"/"+rifedFiles[-1],"last.jpg")
		
		#Connecte Ends
		shutil.rmtree(proxyDir)
		os.mkdir(proxyDir)
		
		shutil.rmtree(reproxyDir)
		os.mkdir(reproxyDir)
		
		os.system('python3 inference_img.py --img last.jpg first.jpg --exp=3')
		report("First pass done, moving files around")
		for f in os.listdir(o):
			if f.find(".png")>0:
				shutil.copyfile(o+f, proxyDir+'/'+f)

		#Adjusting name to match RIFE expectations
		i = 0
		for f in sorted(os.listdir(proxyDir)):
			os.rename(proxyDir+'/'+f,proxyDir+'/'+str(i)+"."+f.split(".")[1])
			i+=1
		
		report("Second pass")
		os.system('python3 inference_video_moded.py --exp='+str(RIFEexp)+' --img='+proxyDir+'/ --folder='+reproxyDir)

		report("Renaming and ofsetting numbering")
		base = len(rifedFiles[0].split('.')[0])
		offset = len(rifedFiles)
		for f in sorted(os.listdir(reproxyDir)):
			extension = "."+f.split(".")[1]
			newName = ('%7d' % (int(f.split(".")[0])+offset)).replace(" ","0")+extension

			os.rename(reproxyDir+'/'+f,reproxyDir+'/'+newName)
		
		report("copy the files to the mega_output")
		for f in os.listdir(reproxyDir):
			shutil.copyfile(reproxyDir+"/"+f, megaDir+"/"+f)
		report("ecnoding")
		os.system(r'ffmpeg -framerate 12 -i '+megaDir+r'/%07d.jpg -c:v libx264 -pix_fmt yuv420p -y video/'+op+r'.mp4')

#interpolate(2,"test")
interpolate(2, 'Opus325846_steel_LB Opus325846_gold_LB Opus325846_steel_LW Opus325846_gold_LW')
interpolate(3, 'Opus185131_steel_LB Opus185131_steel_LW')