"""
This is the meme generator module. This module includes a class ImageCaptioner
that  generates memes wit the image,body and author provided.
"""

from QuoteEngine.QuoteModel import QuoteModel
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os


class ImageCaptioner(object):
    """
    The class ImageCaptioner also contains methods:

        init: saves the output directory specified.
        make_meme: reads in an image, transforms and adds a caption to the image (body and author)

    Example:
    meme = MemeEngine("./tmp")
    output_path = meme.make_meme("path to image", "body of quote", "author of quote")

    The output_path is the that path where the meme is stored.
    """

    def __init__(self, output_dir):
        """Init method."""
        self.out_path = output_dir

    def make_meme(self, image, body, author, width=500) -> str:
        """Make the meme from image,body and author."""
        try:
            img = Image.open(image)
            aspect_ratio = img.width/img.height
            (new_width, new_height) = (500, int(500*aspect_ratio))
            im = img.resize((new_width, new_height))

            quote = QuoteModel(body, author).__repr__()
            pos1 = random.randint(10, 50)
            pos2 = random.randint(10, 100)

            font = ImageFont.truetype("arial.ttf", 20)
            draw = ImageDraw.Draw(im)
            draw.text((pos1, pos2), text=quote, font=font)
            file_path = r'{}/{}.png'.format(self.out_path,
                                            random.randint(0, 1000))
            im.save(file_path)
            return file_path
        except Exception as e:
            raise Exception(e)
