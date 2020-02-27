from QuoteEngine.QuoteModel import QuoteModel
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class MemeEngine(object):
    def __init __(self, output_dir):
        self.out_path = f'{output_dir}/memeimg.jpg'

    def make_meme(self, image, body, author,width = 500) -> str:
        try:
            img = Image.open(in_path)
            aspect_ratio = img.width/img.height
            (new_width, new_height) = (500, 500*aspect_ratio)
            img = img.resize((new_width, new_height))

            quote = QuoteModel(body, author).__repr__()
            draw = ImageDraw.Draw(img)
            pos1 = random.randint(10, img.height)
            pos2 = random.randint(10, img.width)
            draw.text((pos1, pos2),text = quote)

            im.save(self.out_path)
            return self.out_path

        except Exception as e:
                 raise Exception('generate_postcard not implemented')
