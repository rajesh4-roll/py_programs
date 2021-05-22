"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    image = SimpleImage(PATCH_NAME)
    # final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # TODO: your code here
    final_image = SimpleImage.blank(image.width * N_COLS, image.height * N_ROWS)
    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(1.5,0,1.5)
            final_image = add_patch(final_image,patch,row,col)
    final_image.show()

def add_patch(final_image, patch, row, col):
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x, y)
            final_image.set_pixel(x + (col*(patch.width)),y + (row*(patch.height)), pixel)
    return final_image

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()