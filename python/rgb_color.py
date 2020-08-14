class RGBColor:

    # RGBColor is a wrapper class with a three-item list (rgbList)
    # that contains the red, green, and blue integer values for
    # a color in the form: [Red, Green, Blue] and provides a number
    # of functions that utilize rgbList

    # The RGBColor constructor accepts either three integers
    # or an existing RGBColor object to make a copy of
    def __init__(self, r=None, g=None, b=None, copy=None):
        self.rgbList = [0, 0, 0]
        if copy is None:
            if r != None:
                if r > 255: r = 255
                elif r < 0: r = 0
                self.rgbList[0] = r
            if g != None:
                if g > 255: g = 255
                elif g < 0: g = 0
                self.rgbList[1] = g
            if b != None:
                if b > 255: b = 255
                elif b < 0: b = 0
                self.rgbList[2] = b
        else:
            if type(copy) is RGBColor:
                self.__copy_constructor(copy)
            else:
                raise Exception("The RGBColor copy constructor received"
                                " an object of " + str(type(copy)) +
                                " rather than of RGBColor.")

    # Instantiates a unique copy of an RGBColor object
    def __copy_constructor(self, copy):
        rgb_values = copy.getRGBList()
        for i in range(len(rgb_values)):
            self.rgbList[i] = rgb_values[i]
    
    # Returns a copy of the RGBColor object's rgbList
    def getRGBList(self):
        listCopy = self.rgbList.copy()
        return listCopy

    # Sets the RGB value at a specified index of the RGBColor
    # object's rgbList (index corresponds as follows: 0=R, 1=G, 2=B)
    def setRGBValue(self, index, value):
        if index < 3 and index >= 0:
            self.rgbList[index] = value
        else:
            raise Exception("An invalid index of " + str(index)
                            + " was supplied.")

    # Returns the an RGB value at a specified index of the RGBColor
    # object's rgbList (index corresponds as follows: 0=R, 1=G, 2=B)
    def getRGBValue(self, index):
        if index < 3 and index >= 0:
            return self.rgbList[index]
        else:
            raise Exception("An invalid index of " + str(index)
                            + " was supplied.")

    # Returns the RGBColor object's equivalent hexadecimal value
    # as a string
    def getHexStr(self):
        hex_str = "#"

        value = self.getHexVal(self.rgbList[0])
        hex_str = hex_str + value
        value = self.getHexVal(self.rgbList[1])
        hex_str = hex_str + value
        value = self.getHexVal(self.rgbList[2])
        hex_str = hex_str + value

        return hex_str

    # Returns the hexadecimal value for a single value (0-255)
    def getHexVal(self, value):
        hex_val = hex(value)
        hex_val = hex_val[2:len(hex_val)]
        if len(hex_val) < 2:
            hex_val = "0" + hex_val
        return hex_val

    # Returns the RGBColor object's approximately equivalent CMYK
    # value as a string
    def getCMYKStr(self):
        r_div = self.rgbList[0] / 255
        g_div = self.rgbList[1] / 255
        b_div = self.rgbList[2] / 255

        rgbList_div = [r_div, g_div, b_div]

        rgb_max = 0.0
        for i in range(len(rgbList_div)):
            if rgb_max < rgbList_div[i]: rgb_max = rgbList_div[i]

        k_val = 1 - rgb_max

        # Prevents division by zero if k_val is 1 
        # (only occurs with RGB = [0, 0, 0])
        if k_val == 1:
            return "[0, 0, 0, 100]"

        c_val = (1 - r_div - k_val) / (1 - k_val)
        m_val = (1 - g_div - k_val) / (1 - k_val)
        y_val = (1 - b_div - k_val) / (1 - k_val)

        cmyk_str = "[" + str(int(100 * round(c_val, 2))) + \
                   ", " + str(int(100 * round(m_val, 2))) + \
                   ", " + str(int(100 * round(y_val, 2))) + \
                   ", " + str(int(100 * round(k_val, 2))) + "]"

        return cmyk_str

    # Returns the RGBColor object's RGB, CMYK, and hexadecimal values
    # as a string with a line break separating each section
    def getColorInfoStr(self):
        return "[" + str(self.rgbList[0]) + \
               ", " + str(self.rgbList[1]) + \
               ", " + str(self.rgbList[2]) + "]\n" + \
               self.getCMYKStr() + "\n" + self.getHexStr().upper()
