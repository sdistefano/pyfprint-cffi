#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyfprint

pyfprint.fp_init()
devs = pyfprint.discover_devices()
dev = devs[0]
dev.open()
fps = []

messages_to_string = {
        pyfprint.ENROLL_FAIL: "ENROLL_FAIL",
        pyfprint.ENROLL_PASS: "ENROLL_PASS",
        pyfprint.ENROLL_RETRY: "ENROLL_RETRY",
        pyfprint.ENROLL_RETRY_TOO_SHORT: "RETRY_TOO_SHORT",
        pyfprint.ENROLL_RETRY_CENTER_FINGER: "RETRY_CENTER_FINGER",
        pyfprint.ENROLL_RETRY_REMOVE_FINGER: "RETRY_REMOVE_FINGER",
}

for i in range(2):
    print("enroll #%d, finger please" % i)
    fp = None
    while fp == None:
        fp, img_or_msg = dev.enroll_finger_nolock()
        if not fp: print(messages_to_string[img_or_msg])

    print("got", fp, img_or_msg)
    fps.append(fp)

while True:
    print("finger to identify, please")
    i, fp, img, r = dev.identify_finger(fps)
    print (i, fp, img, r)


dev.close()
pyfprint.fp_exit()
