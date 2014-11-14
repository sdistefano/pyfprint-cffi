#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyfprint
import colorsys
from PIL import Image, ImageDraw

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()

for i in range(1):
	fp, img = dev.enroll_finger()
	minutiae = img.minutiae()
	filename = '/tmp/dedo_%d' % i
	img.save_to_file(filename)
	im = Image.open(filename).convert("RGB")
	draw = ImageDraw.Draw(im)
	r = 5
	for minutia in minutiae:
		m = minutia.data

		if m.reliability <= 0.3:
			continue

		if False:
			if m.type == 0:
				col = (255, 64, 0)
			elif m.type == 1:
				col = (0, 64, 255)
		else:
			col = tuple(map(lambda n: int(255*n), colorsys.hsv_to_rgb(0.75* m.reliability,1,1)))

		if m.type == 0:
			draw.ellipse((m.x - r, m.y - r, m.x + r, m.y + r), outline=col)
		elif m.type == 1:
			draw.rectangle((m.x - r, m.y - r, m.x + r, m.y + r), outline=col)

		print (
				m.x,
				m.y,
				m.ex,
				m.ey,
				m.direction,
				m.reliability,
				m.type,
				m.appearing,
				m.feature_id,
			)
im.show()
dev.close()
pyfprint.fp_exit()
