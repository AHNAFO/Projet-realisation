from Source import Source

class LCGSource(Source):

    def __init__(self):
        super().__init__("LCG", "tab")

    def getNumberSequence(self, lengthTab):
        return