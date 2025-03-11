class Cylinder:
    def __init__(self,height, radius=1):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_surface_area()
        self.volume = self.get_volume()

    def get_surface_area(self):
        self.surface_area = round(self.height * (2 * (22/7) * self.radius),2)
        return self.surface_area
    
    def get_volume(self):
        self.volume = round(self.height * ((22/7)**2 * self.radius),2)
        return self.volume
    
cyl = Cylinder(10)
print(f" height = {cyl.height} , radius = {cyl.radius}")
print("Surface area = {}".format(cyl.surface_area))
print("Volume is " + str(cyl.volume))
print(dir(cyl))

