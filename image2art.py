from PIL import Image, ImageDraw, ImageFont
import cProfile

class Image2Art:
  CHAR_WIDTH = 10
  CHAR_HEIGHT = 18
  GSCALE = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
  FONT = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)
  
  def __init__(self, file_path, rgb=False):
    self.file_path = file_path
    self.pixels = None
    self.rgb = rgb
    self.get_pixels()
  
  def get_pixels(self):
    img = Image.open(self.file_path)

    w, h = img.size
    char_aspect_ratio = Image2Art.CHAR_WIDTH / Image2Art.CHAR_HEIGHT
    aspect_ratio = w / h
    self.w = 400
    self.h = int(self.w / aspect_ratio * char_aspect_ratio)
    img = img.resize((self.w, self.h))

    if self.rgb:
      img = img.convert("RGB")
    else:
      img = img.convert("L")

    self.pixels = img.load()
  
  def pix2char(self, pix):
    n = len(Image2Art.GSCALE) - 1
    return Image2Art.GSCALE[int(n/255*pix)]
  
  def save_art(self):
    img_width = Image2Art.CHAR_WIDTH * self.w
    img_height = Image2Art.CHAR_HEIGHT * self.h
    if self.rgb:
      output_image = Image.new("RGB", (img_width, img_height), color=(30, 30, 30))
    else:
      output_image = Image.new("L", (img_width, img_height), color=30)
    draw = ImageDraw.Draw(output_image)
    for i in range(self.h):
        for j in range(self.w):
          if self.rgb:
            r, g, b = self.pixels[j, i]
          else:
            g = self.pixels[j, i]
          x = Image2Art.CHAR_WIDTH * j
          y = Image2Art.CHAR_HEIGHT * i
          if self.rgb:
            draw.text((x, y), self.pix2char(int(1/3*(r+g+b))), font=Image2Art.FONT, fill=(r, g, b))
          else:
            draw.text((x, y), self.pix2char(g), font=Image2Art.FONT, fill=255)

    output_image.save(f"python_logo_ascii.png")

art = Image2Art("python_logo.png", False)
art.save_art()