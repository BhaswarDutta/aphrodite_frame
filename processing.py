from PIL import Image, ImageOps

BORDER = 20

# Target dimensions
RATIOS = {
    "1:1": (1080, 1080),
    "4:5": (1080, 1350),
}


def is_portrait(img: Image.Image) -> bool:
    return img.height > img.width


def process_image(image: Image.Image, ratio: str) -> Image.Image:
    """
    Process image to fit target ratio without cropping.
    Adds white padding + border.
    """

    base_width, base_height = RATIOS[ratio]

    # Resize logic
    if is_portrait(image):
        new_height = base_height - BORDER
        new_width = int((new_height / image.height) * image.width)
    else:
        new_width = base_width - BORDER
        new_height = int((new_width / image.width) * image.height)

    resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Padding logic
    if is_portrait(image):
        white_space = (base_width - BORDER) - resized.width
        padding = (white_space // 2, 0, white_space // 2, 0)
    else:
        white_space = (base_height - BORDER) - resized.height
        padding = (0, white_space // 2, 0, white_space // 2)

    padded = ImageOps.expand(resized, border=padding, fill="white")

    # Final border
    final = ImageOps.expand(padded, border=BORDER, fill="white")

    return final
