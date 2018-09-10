# Manages a grid of values


class Grid():

    def __init__(self):
        self.width = None
        self.height = None

    def get_size(self):
        return [self.width, self.height]

    def set_size(self, width, height):
        self.check_gridsize(width, height)
        self.width = int(width)
        self.height = int(height)

    def check_gridsize(self, width, height):
        width = int(width)
        height = int(height)
        try:
            assert ((width > 0) and (height > 0))
        except:
            raise Exception("Invalid grid size width:%d height:%d"
                            % (width, height))
        return True
