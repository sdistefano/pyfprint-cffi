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

while True:
	print("finger to identify, please")

	i = None

	while i is None:
		i, *rest = dev.identify_finger(fps)

	print ("identified " + names[i] + "!")

dev.close()
pyfprint.fp_exit()
