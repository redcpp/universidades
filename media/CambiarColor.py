# Python 2.7
from PIL import Image
import glob

for img_file in glob.glob('*.png'):
	print img_file
	
	''' Image must be PNG '''
	im = Image.open(img_file, 'r')
	pix_vals = list(im.getdata())
	rgb_values = 243,243,243

	position=0
	for rgba in pix_vals:
		if rgba[3]:
			pix_vals[position] = rgb_values+(rgba[3],)
		position+=1

	im2 = Image.new(im.mode, im.size)
	im2.putdata(pix_vals)
	im2.save(img_file)