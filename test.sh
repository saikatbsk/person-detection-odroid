#!/bin/bash

python3.6 real_time_object_detection.py \
    --prototxt MobileNetSSD_deploy.prototxt.txt \
    --model MobileNetSSD_deploy.caffemodel \
    --ip 127.0.0.1 \
    --port 5005
