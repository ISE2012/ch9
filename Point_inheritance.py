class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy)**(1/2)

class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y) # Calling Superclass Methods
        self.z = z
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dz = self.z - other.z
        return (dx * dx + dy * dy + dz * dz)**(1/2)
        
def main():
    point_3d_A = Point3D(1,2,3)
    point_3d_B = Point3D(4,5,6)
    distance_A_B = point_3d_A.distance(point_3d_B)
    
    print("X point_3d_A:", point_3d_A.x)
    print("Y point_3d_A:", point_3d_A.y)
    print("Z point_3d_A:", point_3d_A.z)
    print("--"*10)
    print("X point_3d_B:", point_3d_B.x)
    print("Y point_3d_B:", point_3d_B.y)
    print("Z point_3d_B:", point_3d_B.z)
    print("--"*10)
    print("Distance between A and B:", distance_A_B) 
    
main()

