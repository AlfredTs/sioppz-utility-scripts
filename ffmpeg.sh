ffmpeg -framerate 12 -i %07d.jpg -c:v libx264 -pix_fmt yuv420p ~/Videos/Opus951465_png_LW.mp4
ffmpeg -framerate 12 -i %05d.jpg -c:v libx264 -pix_fmt yuv420p ~/Videos/Opus951465_png_PW.mp4

ffmpeg -framerate 12 -i %05d.jpg -c:v libx264 -pix_fmt yuv420p ~/Videos/Opus185131_png_PW.mp4
ffmpeg -framerate 12 -i %07d.jpg -c:v libx264 -pix_fmt yuv420p ~/Videos/Opus185131_png_LW.mp4

#1405 forward
