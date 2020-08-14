from PIL import Image, ImageDraw, ImageFont
from rgb_color import RGBColor
import random

def generateSwatch():
    # Create three randomly generated RGBColor objects
    colorA = RGBColor(r=random.randrange(216),
                      g=random.randrange(216),
                      b=random.randrange(216))
    index = random.randrange(3)
    colorB = RGBColor(copy=colorA)
    colorB.setRGBValue(index, colorA.getRGBValue(index) + 20)
    colorC = RGBColor(copy=colorA)
    colorC.setRGBValue(index, colorA.getRGBValue(index) + 40)

    # Create an Image object used to contain the color blocks
    # and their details
    img = Image.new("RGB", (1920, 1080), "#FFFFFF")

    # Draws the three color blocks into the image
    img.paste(colorA.getHexStr(), (75, 75, 615, 615))
    img.paste(colorB.getHexStr(), (690, 75, 1230, 615))
    img.paste(colorC.getHexStr(), (1305, 75, 1845, 615))

    # Draws six aesthetic lines on the image
    draw = ImageDraw.Draw(img) 
    draw.line([(570, 961), (614, 961)],
              fill="#000000", width=2)
    draw.line([(613, 918), (613, 962)],
              fill="#000000", width=2)
    draw.line([(1185, 961), (1229, 961)],
              fill="#000000", width=2)
    draw.line([(1228, 918), (1228, 962)],
              fill="#000000", width=2)
    draw.line([(1800, 961), (1844, 961)],
              fill="#000000", width=2)
    draw.line([(1843, 918), (1843, 962)],
              fill="#000000", width=2)

    # Draws each color block's information under each
    # respective block (RGB, CMYK, and hexadecimal codes)
    font = ImageFont.truetype("tahomabd.ttf", 38)
    draw.multiline_text((75, 694), colorA.getColorInfoStr(),
                        fill="#000000", font=font, spacing=(8))
    draw.multiline_text((690, 694), colorB.getColorInfoStr(),
                        fill="#000000", font=font, spacing=(8))
    draw.multiline_text((1305, 694), colorC.getColorInfoStr(),
                        fill="#000000", font=font, spacing=(8))

    # Draws an aesthetic/information string underneath each
    # color block
    font2 = ImageFont.truetype("tahomabd.ttf", 17)
    info_str = "[R, G, B]\n[C, M, Y, K]\nHexadecimal"
    draw.multiline_text((75, 901), info_str,
                        fill="#000000", font=font2, spacing=4)
    draw.multiline_text((690, 901), info_str,
                        fill="#000000", font=font2, spacing=4)
    draw.multiline_text((1305, 901), info_str,
                        fill="#000000", font=font2, spacing=4)

    # Draw the bot's name in the bottom right
    font3 = ImageFont.truetype("tahomabd.ttf", 29)
    draw.text((1717, 1002), "SwatchBot",
              fill="#000000", font=font3, spacing=(6))

    # Save the completed image locally
    img.save("swatch.png")

def PFPGen():
    # Creates the Twitter account's profile picture
    
    # Scales the size of the image and its components
    s = 1

    # White, 1x1 background
    img = Image.new("RGB", (300 * s, 300 * s), "#FFFFFF")

    # Twitter Blue
    colorA = RGBColor(r=29, g=161, b=242)

    # Pastes a color block into the background
    img.paste(colorA.getHexStr(), (75 * s, 55 * s, 225 * s, 205 * s))

    # Writes 'SwatchBot' underneath the block and to the left
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("tahomabd.ttf", 20 * s)
    draw.multiline_text((75 * s, 225 * s), "SwatchBot",
                        fill="#000000", font=font, spacing=6)

    # Save the completed image locally
    img.save("swatchbotpfp.png")

def HeaderGen():
    # Creates the Twitter account's header image
    
    # Scales the size of the image and its components
    s = 2

    # White, 16x9 background
    img = Image.new("RGB", (1280 * s, 720 * s), "#FFFFFF")

    # Creates red, green, and blue RGBColor objects
    colorA = RGBColor(r=255, g=0, b=0)
    colorB = RGBColor(r=0, g=255, b=0)
    colorC = RGBColor(r=0, g=0, b=255)

    # Pastes three color blocks into the background
    img.paste(colorA.getHexStr(), (50 * s, 50 * s, 410 * s, 410 * s))
    img.paste(colorB.getHexStr(), (460 * s, 50 * s, 820 * s, 410 * s))
    img.paste(colorC.getHexStr(), (870 * s, 50 * s, 1230 * s, 410 * s))

    # Writes 'SwatchBot' underneath the third block
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("tahomabd.ttf", 50 * s)
    draw.multiline_text((870 * s, 460 * s), "SwatchBot",
                        fill="#000000", font=font, spacing=6)

    # Save the completed image locally
    img.save("swatchbotheader.png")
    