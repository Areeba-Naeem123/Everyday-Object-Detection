# Everyday Object Detection Dataset

## Project Overview

This project demonstrates image annotation for object detection using bounding boxes. The dataset contains everyday objects annotated manually using CVAT and exported in Ultralytics YOLO format.

## Dataset Information

| Detail | Description |
|---|---|
| Total images | 24 |
| Annotation tool | CVAT |
| Annotation type | Bounding boxes |
| Export format | Ultralytics YOLO Detection 1.1 |
| Validation | Python dataset validation |

## Object Categories

The dataset contains three object classes:

| Class ID | Label |
|---|---|
| 0 | cup |
| 1 | mobile_phone |
| 2 | bottle |

## Annotation Process

1. Collected 24 object images from Pexels.
2. Created an annotation project in CVAT.
3. Defined three object categories.
4. Drew bounding boxes around visible objects.
5. Assigned the appropriate class labels.
6. Reviewed annotations for quality.
7. Exported annotations in YOLO format.

## Dataset Structure

```text
Everyday-Object-Detection/
├── data.yaml
├── train.txt
├── data/
│   └── images/
│       └── train/
├── labels/
│   └── train/
└── check_dataset.py
```

## Dataset Validation

A Python validation script was used to check image paths, corresponding annotation files, YOLO annotation format, class IDs, and normalized bounding-box values.

**Validation results:**
- Images listed: 24
- Errors found: 0
- Basic validation: Passed

## Tools and Technologies

- CVAT
- Python
- Ultralytics YOLO annotation format
- GitHub

## My Contribution

I collected the images, created the CVAT annotation project, manually annotated objects using bounding boxes, reviewed the annotations, exported the dataset in YOLO format, and performed basic validation using Python.

## Purpose

This project demonstrates practical skills in image annotation, object detection dataset preparation, bounding-box labeling, and annotation quality checking.

---

*This is a small portfolio project demonstrating my image annotation skills.*
