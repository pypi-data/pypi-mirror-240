# detects and analyzes shapes in images using parallel processing. 

## pip install multiprocshapefinder

### Tested against Python 3.11 / Windows 10


### Advantages:

#### Parallel Processing: 

The module utilizes parallel processing (cpus parameter) to speed up the shape detection process, 
which can be advantageous for analyzing multiple images simultaneously.

#### Flexible Input: 

It accepts images in various formats, providing flexibility in the source of the images.

#### Caching: 

The option to use caching (usecache) can save time on the same images.

#### Visualization: 

The module provides a function (draw_results) for visualizing the detected shapes on the original images,
making it easier for users to interpret and verify the results.

#### Configurability: 

The module exposes various parameters, such as Canny edge detection thresholds and contour approximation factors, 
allowing users to fine-tune the shape detection process based on their requirements.


```python

# Importing functions from the multiprocshapefinder module
from multiprocshapefinder import find_all_shapes, draw_results

# List of image URLs to be processed
images = [
    r"https://raw.githubusercontent.com/hansalemaos/screenshots/main/findshapes_1.png",
]  # accepts almost all formats (url/path/buffer/base64/np/PIL) - https://github.com/hansalemaos/a_cv_imwrite_imread_plus

# Calling find_all_shapes function to detect and analyze shapes in the given images
df = find_all_shapes(
    images,
    threshold1=10,
    threshold2=90,
    approxPolyDPvar=0.01,
    cpus=5,  # Number of CPU cores to use for parallel processing
    chunks=1,  # Number of chunks to split the image processing into
    print_stderr=True,  # Print error messages to stderr
    print_stdout=False,  # Do not print standard output messages
    usecache=True,  # Use caching for intermediate results
)

# Printing the resulting DataFrame containing shape information
print(df)

# Calling draw_results function to visualize the detected shapes on the original image
draw_results(
    df,
    images[0],  # Using the first image in the list - filter the DF (df.loc) if len(images)>1
    min_area=5,  # Minimum area threshold for shapes to be considered
    shapes=("rectangle", "triangle", "circle", "pentagon", "hexagon", "oval"),  # Shapes to be visualized
    cv2show=True,  # Display the result using OpenCV
)


```