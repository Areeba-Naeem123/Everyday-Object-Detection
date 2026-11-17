# Object Detection Labels

This directory contains the bounding-box annotations for the Everyday Object Detection dataset.

## Annotation Format

Annotations are stored in YOLO Detection format.

Each annotation file contains:

`class_id x_center y_center width height`

Coordinates are normalized between 0 and 1.

## Class Mapping

| Class ID | Class |
|---|---|
| 0 | cup |
| 1 | mobile_phone |
| 2 | bottle |

## Directory Structure

- `train/` — Contains annotation files corresponding to the 24 training images.

Annotations were created using CVAT and exported in Ultralytics YOLO Detection format.
