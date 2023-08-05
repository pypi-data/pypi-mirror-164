# Vlfeat_py

A python wrapper for the functions in vlfeat. Its not a wrapper on the [Vlfeat C API](https://www.vlfeat.org/sandbox/api/index.html) but rather a wrapper on the functions listed in the [Vlfeat C API](https://www.vlfeat.org/sandbox/api/index.html)

## Features

* Extracts out SIFT Keypoints and Descriptors for an image
* Extracts out Dense SIFT Keypoints and Descriptors for an image
* Extracts the Region seeds and the frames for an MSER filter in an image

## Quick Start

### Installation

To install the package, run the following command

```bash
pip install vlfeat_py
```

To install from the main branch (warning: development version. Things could break)

```bash
pip install git+https://github.com/lucasace/vlfeat_py.git
```

### Usage

To apply any of the supported descriptors for example SIFT, you can use the following code

```python
import cv2
import vlfeat_py as vl

img = cv2.imread("path/to/image.jpg", cv2.IMREAD_GRAYSCALE)
[sift_keypoints, sift_descriptors] = vl.sift_desc(img)

```

## Supported Descriptors

### SIFT

```python
[sift_keypoints, sift_descriptors] = vl.sift_desc(img)
```

### Dense SIFT

```python
[dense_sift_keypoints, dense_sift_descriptors] = vl.dsift_desc(img, np.array([0, 0, img.shape[0], img.shape[1]]))
```

### MSER

```python
[region_seeds, frames] = vl.mser_desc(img)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

