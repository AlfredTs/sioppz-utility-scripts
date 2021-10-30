suffix = "_1080p.mp4"

for f in $(ls):
do
	arr=(${f//"."/ });
	if [ ${arr[1]} == "mp4" ];
	then
		ffmpeg -i $f -vf "scale=iw*.5:ih*.5" 1080p/${arr[0]}_1080p.mp4
	fi
done;
