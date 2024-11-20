from PIL import Image
import numpy as np
import os

def ft_load(path: str) -> np.ndarray:
    """
    A function that loads an image with Pillow, prints its format, and its pixels content in RGB format.
    Handling, at least, JPG and JPEG format.

    Args:
    -path: a string
    
    Returns:
    -List of RGB pixel values or a compatible format.
    """
    try:
        if not os.path.exists(path):
            raise ValueError(f"File not found: {path}")

        if not (path.endswith(".jpg") or path.endswith(".jpeg")):
            raise ValueError("Unsupported format. Only JPG and JPEG formats are supported.")
        
        image = Image.open(path)
        pixel = np.asarray(image)
        print(f"The shape of image is: {pixel.shape}")
        return pixel
    
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")