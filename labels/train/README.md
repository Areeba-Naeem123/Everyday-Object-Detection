# YOLO Training Annotations

This folder contains the YOLO-format bounding-box annotations corresponding to the 24 training images.

## Annotation Details

Each `.txt` file corresponds to an image with the same filename.

Each annotation line follows the YOLO Detection format:

`class_id x_center y_center width height`

All bounding-box coordinates are normalized between 0 and 1.

## Class Mapping

| Class ID | Object |
|---|---|
| 0 | cup |
| 1 | mobile_phone |
| 2 | bottle |

## Annotation Tool

Annotations were created manually using CVAT and exported in Ultralytics YOLO Detection format.
