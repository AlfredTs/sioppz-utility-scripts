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
		megaDir = 'mega_output/'+op

		#os.system(r'ffmpeg -framerate 12 -i '+megaDir+r'/%05d.jpg -c:v libx264 -pix_fmt yuv420p -y video/'+op+r'.mp4')
		print(r'ffmpeg -framerate 12 -i '+megaDir+r'/%05d.jpg -c:v libx264 -pix_fmt yuv420p -y video/'+op+r'.mp4')

#interpolate(2,"test")
interpolate(2, 'Opus325846_steel_PB Opus325846_gold_PB Opus325846_steel_PW Opus325846_gold_PW')
interpolate(3, 'Opus185131_steel_PB Opus185131_steel_PW')
