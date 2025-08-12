# Digital Image Processing - Assignment 0

## Overview
This is my **Assignment 0** for the Digital Image Processing course @IIITH.  
The goal was to get familiar with basic image and video manipulation techniques using Python.  
Each question was implemented as a separate script for modularity.

---

## Folder Structure

```bash
assign0/
- main.py #entry point to run specific questions
- questions/ #contains one file per question
    - q1.py
    - q2.py
    - q3.py
    - q4.py
    - q5.py
    - q6.py
    - q7.py
    - q8.py
    - q9.py

- utils/ #helper functions used
    - image_utils.py

- input_images/ #input images for processing
- output_images/ #outputs generated for each question
- videos/ #input/output videos for Q8 & Q9

- README.md #this file
```
---

## How to run

1. Place required input files in input_images/ or videos/
2. Edit main.py to call the desired question function, e.g.:

```python
from questions.q3 import run_q3

if __name__ == "__main__":
    run_q3()
```
3. Run the script:

```bash
python3 main.py
```

## Questions Summary
| Q# | Task                 | Description                                                                  |
| -- | -------------------- | ---------------------------------------------------------------------------- |
| 1  | Read Image → Array   | Reads an image file and converts it to a NumPy array.                        |
| 2  | Write Array → Image  | Saves a NumPy array as an image file.                                        |
| 3  | Brightness Change    | Adjusts image brightness by addition or multiplication.                      |
| 4  | Contrast Change      | Enhances image contrast using scaling and shifting.                          |
| 5  | Grayscale Conversion | Implements different grayscale methods (average, luminosity, etc.).          |
| 6  | Pseudocolor Mapping  | Applies color maps to grayscale images.                                      |
| 7  | Green Screen Replace | Replaces a green background with a new image.                                |
| 8  | Video I/O            | Extracts frames from a video and reconstructs it.                            |
| 9  | Image Transition     | Creates a smooth fade transition between two images and saves it as a video. |


## Author
Indira C Reddy.

B.Tech Student, IIIT Hyderabad