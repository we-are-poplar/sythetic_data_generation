import numpy as np
from PIL import Image, ImageEnhance
from random import uniform


def crop_transparent(img):
    """
    Crop surrounding transparency in an image.

    Params: img - Pillow image
    """
    np_img = np.array(img)
    not_transparent_0 = np_img[:, :, 3].max(axis=1) != 0
    start_index_0 = not_transparent_0.argmax()
    end_index_0 = img.size[0] - not_transparent_0[::-1].argmax()

    not_transparent_1 = np_img[:, :, 3].max(axis=0) != 0
    start_index_1 = not_transparent_1.argmax()
    end_index_1 = img.size[1] - not_transparent_1[::-1].argmax()
    result = Image.fromarray(
        np.array(img)[start_index_0:end_index_0, start_index_1:end_index_1, :]
    )

    return result


def paste_img_on_bg(object_img: Image, background: Image, output_width: int = 1920):
    """
    Paste an object onto a background image, randomising its scale and position.

    Parameters
    ----------
    object_img: Pillow image
    background: Pillow image
    output_width: int
    """
    # Rescale to ouput_width width
    scale_factor = output_width / background.size[0]
    bg_width, bg_height = background.size
    background = background.resize(
        (int(bg_width * scale_factor), int(bg_height * scale_factor))
    )

    # Load object img and rescale randomly
    object_rescale_factor = min(
        background.size[0] / object_img.size[0], background.size[1] / object_img.size[1]
    )
    random_scale = uniform(0.1, 1)
    random_width = int(object_rescale_factor * object_img.size[0] * random_scale)
    random_height = int(object_rescale_factor * object_img.size[1] * random_scale)
    object_img = object_img.resize((random_width, random_height))

    # Adjust object brightness
    enhancer = ImageEnhance.Brightness(object_img)
    factor = 0.85  # gives original image
    object_img = enhancer.enhance(factor)

    # Position object img randomly
    assert background.size[0] >= random_width
    assert background.size[1] >= random_height
    start_x = int(uniform(0, background.size[0] - random_width))
    start_y = int(uniform(0, background.size[1] - random_height))
    background.paste(object_img, (start_x, start_y), object_img)

    bbox = [start_x, start_y, random_width, random_height]

    # Draw bounding box

    # draw = ImageDraw.Draw(background)
    # draw.rectangle((start_width, start_height, start_width + random_width, start_height + random_height), outline=(255, 255, 255), width=5)

    return background, bbox


def init_coco_data():
    data = {
        "info": {},
        "licenses": [
            {
                "url": "http://creativecommons.org/licenses/by-nc-sa/2.0/",
                "id": 1,
                "name": "Attribution-NonCommercial-ShareAlike License",
            },
        ],
        "images": [],
        "annotations": [],
        "categories": [],
    }

    return data
