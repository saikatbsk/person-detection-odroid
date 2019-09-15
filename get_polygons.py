import os
import glob

def get_polygons(directory):
    txt_files = glob.glob(os.path.join(directory, '*.txt'))

    polygons = {}

    for txt_file in txt_files:
        polygon = []
        with open(txt_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                polygon.append([int(p) for p in line.rstrip().split(',')])

        zone_name = os.path.splitext(os.path.basename(txt_file))[0]
        polygons[zone_name] = polygon

    return polygons

"""
if __name__ == "__main__":
    polygons = get_polygons('zone_files')
    print(polygons)

    from shapely.geometry import Polygon
    p1 = Polygon(polygons[0])
    p2 = Polygon(polygons[1])
    print(p1.intersects(p2))
"""
