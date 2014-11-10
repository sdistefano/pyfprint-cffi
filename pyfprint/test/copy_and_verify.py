#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import pyfprint

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()
print("enroll")
fprint, img = dev.enroll_finger()

print("getting data")
d = fprint.data()

print("got:")
print(d)

print("copying")
fp2 = pyfprint.Fprint(d)
print("copied")

print("verifying original...")
fprint.verify_finger()
print("ok")

print("verifying copy...")
fp2.verify_finger()
print("ok")

dev.close()
pyfprint.fp_exit()
