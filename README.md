# SwatchBot

SwatchBot is a Twitter bot developed in Python. Each day at 12:00 PM EST (UTC-5)/EDT (UTC-4), the bot will post a randomly generated color swatch on the [SwatchBot Twitter account.](https://twitter.com/SwatchBot) SwatchBot is hosted on a Raspberry Pi Zero.

### Example Swatch
![Example Swatch](https://github.com/kylereddy/swatchbot/blob/master/example_swatch.png)

Each swatch includes three similar, random color squares. Below each square is that respective color's RGB values, approximate CMYK percentages, and equivalent hexadecimal code.

The code used to determine the three colors is currently as follows:
```python
colorA = RGBColor(r=random.randrange(216),
                  g=random.randrange(216),
                  b=random.randrange(216))
colorB = RGBColor(copy=colorA)
colorC = RGBColor(copy=colorA)
index = random.randrange(3)
colorB.setRGBValue(index, colorA.getRGBValue(index) + 20)
colorC.setRGBValue(index, colorA.getRGBValue(index) + 40

# (colorA = left, colorB = center, and colorC = right on the swatch)
```
