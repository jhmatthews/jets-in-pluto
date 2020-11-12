#/bin/sh

#ffmpeg -y -i out_xrb/xrb_%03d.png -pix_fmt yuv420p xrb.mp4
ffmpeg -y -i out_xrb_overdense/xrb_overdense_%03d.png -pix_fmt yuv420p xrb_overdense.mp4
