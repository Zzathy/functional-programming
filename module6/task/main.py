from PIL import Image, ImageEnhance, ImageFilter, ImageDraw, ImageFont

logo = Image.open(open(r"C:\code\python\functional\module6\task\images\umm.jpeg", 'rb'))
background = Image.open(open(r"C:\code\python\functional\module6\task\images\umm2.jpeg", 'rb'))


background = background.convert("L").rotate(30).filter(ImageFilter.BLUR)

logo = logo.resize((200, 200))
logo = ImageEnhance.Brightness(logo).enhance(1.9)
logo = ImageEnhance.Contrast(logo).enhance(1.7)
background.paste(logo, (200, 100))

draw = ImageDraw.Draw(background)
text = "Informatika JOSSS!"
font = ImageFont.truetype(r"C:\code\python\functional\module6\task\fonts\Arial.ttf", 24)

_, _, text_width, text_height = draw.textbbox((0, 0), text, font=font)
text_x = (background.width - text_width) // 2
text_y = 20
draw.text((text_x, text_y), text, font=font, fill='black')

background.save("module6/task/images/result.jpg")
background.show()
