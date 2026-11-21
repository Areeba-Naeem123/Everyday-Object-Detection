# Everyday Object Detection Dataset

## Project Overview

This project demonstrates practical image annotation skills for object detection using bounding boxes. It contains a manually annotated dataset of everyday objects created using CVAT and exported in Ultralytics YOLO Detection format.

The project focuses on object identification, bounding-box annotation, class labeling, dataset organization, and basic annotation validation.

## Dataset Information

| Detail | Description |
|---|---|
| Total images | 24 |
| Annotation tool | CVAT |
| Annotation type | Bounding boxes |
| Export format | Ultralytics YOLO Detection 1.1 |
| Dataset split | Training |
| Number of classes | 3 |
| Validation | Custom Python validation script |

**Dataset Scope:** This is a small demonstration dataset designed to showcase manual object annotation and YOLO dataset preparation. It is not intended to be a production-scale training dataset.

## Object Categories

The dataset contains three object classes:

| Class ID | Label |
|---|---|
| 0 | cup |
| 1 | mobile_phone |
| 2 | bottle |

## Annotation Previews

The following examples demonstrate manually created bounding-box annotations for the three object categories.

### Cup Annotation

![Cup annotation](annotation-previews/cup-annotation.png)

### Mobile Phone Annotation

![Mobile phone annotation](annotation-previews/mobile-phone-annotation.png)

### Bottle Annotation

![Bottle annotation](annotation-previews/bottle-annotation.png)

## Annotation Process

1. Collected 24 everyday object images from Pexels.
2. Created an annotation project in CVAT.
3. Defined three object categories: cup, mobile_phone, and bottle.
4. Drew bounding boxes around visible objects.
5. Assigned the appropriate class labels.
6. Reviewed annotations for quality and consistency.
7. Exported annotations in Ultralytics YOLO Detection format.
8. Organized images and annotation files into the YOLO dataset structure.
9. Performed basic dataset validation using Python.

## Dataset Structure

```text
Everyday-Object-Detection/
│
├── README.md
├── data.yaml
├── train.txt
├── check_dataset.py
│
├── data/
│   ├── README.md
│   └── images/
│       └── train/
│           ├── README.md
│           └── 24 image files
│
├── labels/
│   ├── README.md
│   └── train/
│       ├── README.md
│       └── 24 annotation files
│
└── annotation-previews/
    ├── README.md
    ├── cup-annotation.png
    ├── mobile-phone-annotation.png
    └── bottle-annotation.png
```

## YOLO Annotation Format

Each annotation file follows the YOLO Detection format:

`class_id x_center y_center width height`

Where:

- `class_id` represents the object category.
- `x_center` represents the normalized horizontal center.
- `y_center` represents the normalized vertical center.
- `width` represents the normalized bounding-box width.
- `height` represents the normalized bounding-box height.

All bounding-box coordinates are normalized between 0 and 1.

### Class ID Mapping

- `0` — cup
- `1` — mobile_phone
- `2` — bottle

Each image has a corresponding `.txt` annotation file with the same base filename.

## Dataset Validation

The dataset was checked using a custom Python validation script (`check_dataset.py`).

**Validation Results:**

| Validation Check | Result |
|---|---|
| Total images listed | 24 |
| Errors found | 0 |
| Image paths | Passed |
| Image and annotation file matching | Passed |
| YOLO annotation format | Passed |
| Class ID validation | Passed |
| Normalized coordinate validation | Passed |

**Result:** Basic dataset validation passed successfully.

Note: Automated validation checks file paths and annotation structure. It does not replace manual visual inspection of bounding boxes or guarantee that every object has been annotated correctly.

## Tools and Technologies

- **CVAT** — Image annotation and bounding-box labeling
- **Python** — Dataset validation
- **Ultralytics YOLO format** — Object detection annotations
- **GitHub** — Dataset organization and project documentation
- **Pexels** — Image source

## My Contribution

I personally:

- Collected and organized 24 object images.
- Created the CVAT annotation project.
- Defined object categories and class IDs.
- Manually annotated objects using bounding boxes.
- Reviewed annotations for quality and consistency.
- Exported the dataset in YOLO Detection format.
- Organized image and annotation files.
- Developed and executed a Python script for basic dataset validation.

## Project Purpose

This project demonstrates practical skills in:

- Image annotation
- Bounding-box labeling
- Object classification
- CVAT annotation workflows
- YOLO dataset preparation
- Dataset organization
- Basic annotation quality validation

---

*This is a small portfolio project demonstrating practical image annotation and object detection dataset preparation skills.*
