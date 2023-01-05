"""Graph-search based image operations.
Alex Polivka
This code abides by the JMU Honor Code
This code was implemented based off the flood
fill psuedo code provided in our textbook for.

Steps:
    * pip install Pillow
    * Complete and test flood_fill
    * Modify flood_fill so that it stops after marking 100 pixels.
     Change the bag type from stack to queue or vice-versa and observe
     the effect.
   * Complete the count_components method.

"""
from PIL import Image
from collections import deque  # EFFICIENT STACK *AND* QUEUE OPERATIONS.


def neighbors(img, pixel):
    """Get the valid neighbors of the provided pixel location.

    Args:
        img - PIL Image object
        pixel - two-tuple (x, y)

    Returns:
        A list with all valid neighboring pixels represented as
        two-tuples.
    """
    width, height = img.size
    nbrs = []
    if pixel[0] > 0:
        nbrs.append((pixel[0] - 1, pixel[1]))
    if pixel[1] > 0:
        nbrs.append((pixel[0], pixel[1] - 1))
    if pixel[0] < width - 1:
        nbrs.append((pixel[0] + 1, pixel[1]))
    if pixel[1] < height - 1:
        nbrs.append((pixel[0], pixel[1] + 1))
    return nbrs


def flood_fill(image, start_pixel, fill_color=(0, 0, 255)):
    """Fill all four-connected pixels with the provided fill color.

    Args:
        image - PIL Image object
        pixel - Fill start location represented as a two-tuple (x, y)
        fill_color - The color to use to fill.

    """

    px = image.load()  # Create an object that can be used to access
                       # individual pixels
    start_color = px[start_pixel]

    # create queue
    queue = []
    queue.append(start_pixel)

    # based off psuedo code from the 
    # WhateverFirstSearch method
    while queue:
        value = queue.pop()
        if px[value] == start_color:
            px[value] = fill_color
            for x in neighbors(image, value):
                queue.append(x)
    
def count_components(image):
    """Count the connected components in the provided image.

    Args:
        image - PIL Image object

    Returns:
        integer number of four-connected components.
    """

    # Create an image that can be used to mark visited pixels
    marks = Image.new('RGB', image.size, color=(0, 0, 0))


def main():
    with Image.open("face.png") as im:
        flood_fill(im, (0, 0))
        im.show()


if __name__ == "__main__":
    main()

