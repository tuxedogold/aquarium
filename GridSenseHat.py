from sense_hat import SenseHat


class GridSenseHat(SenseHat):
        def __init__(self):
                SenseHat.__init__(self)
                self.set_rotation(180)
        def set_grid_pixels(self,grid):
                pixels = [j for i in grid for j in i]
                self.set_pixels(pixels)
		
