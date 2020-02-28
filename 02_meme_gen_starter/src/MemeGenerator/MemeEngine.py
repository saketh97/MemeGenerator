from QuoteEngine.QuoteModel import QuoteModel
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import os


class ImageCaptioner(object):
    def __init__(self, output_dir):
        self.out_path = output_dir

    def make_meme(self, image, body, author, width=500) -> str:
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
