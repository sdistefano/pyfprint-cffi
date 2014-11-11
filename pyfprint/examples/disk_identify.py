#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyfprint
import os.path
DIR = "/tmp/fps"

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()

names = []
fps = []

for name in os.listdir(DIR):
	fps.append(pyfprint.Fprint(open(DIR + "/" + name, 'br').read()))
	names.append(name)

print ("ready to match fingers!")

while True:
	i, fp, img, r = dev.identify_finger(fps)

	if r == pyfprint.C.FP_VERIFY_MATCH:
		print ("identified " + names[i] + "!")

	elif r == pyfprint.C.FP_VERIFY_NO_MATCH:
		print ("no match found")

	else:
		print ("hmm, didn't got that, retry?")


dev.close()
pyfprint.fp_exit()
