
from pathlib import Path

root = Path(__file__).parent

with open(root / "train.txt", encoding="utf-8") as f:
    image_paths = [line.strip() for line in f if line.strip()]

errors = []

for image_path in image_paths:
    image = root / image_path
    label = root / "labels" / "train" / (image.stem + ".txt")

    if not image.exists():
        errors.append(f"Missing image: {image}")
        continue

    if not label.exists():
        errors.append(f"Missing annotation: {label}")
        continue

    for line_number, line in enumerate(
        label.read_text(encoding="utf-8").splitlines(), start=1
    ):
        values = line.split()

        if len(values) != 5:
            errors.append(f"Invalid format: {label.name}, line {line_number}")
            continue

        try:
            class_id = int(values[0])
            x, y, width, height = map(float, values[1:])
            if class_id not in (0, 1, 2):
                raise ValueError("Invalid class ID")
            if not all(0 <= v <= 1 for v in (x, y, width, height)):
                raise ValueError("Coordinates outside 0–1")
            if width <= 0 or height <= 0:
                raise ValueError("Invalid box dimensions")
        except ValueError as error:
            errors.append(f"{label.name}, line {line_number}: {error}")

print(f"Images listed: {len(image_paths)}")
print(f"Errors found: {len(errors)}")

for error in errors:
    print(error)

if not errors:
    print("Basic dataset validation passed!")
