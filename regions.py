import json
import os
import time

class Region:
    def __init__(self, x, y, width, height, terrain_type, path_finding_weight):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.terrain_type = terrain_type
        self.path_finding_weight = path_finding_weight


    def contains_point(self, px, py):
        return self.x <= px < self.x + self.width and self.y <= py < self.y + self.height
#does not contain points for bottom and right border of a region
    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "terrain_type": self.terrain_type,
            "path_finding_weight": self.path_finding_weight
        }

    @staticmethod
    def from_dict(data):
        return Region(data["x"], data["y"], data["width"], data["height"], data["terrain_type"], data["path_finding_weight"])

    # def __repr__(self):
    #     return f"Region(x={self.x}, y={self.y}, width={self.width}, height={self.height}, terrain_type={self.terrain_type})"



def read_regions_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [Region.from_dict(item) for item in data]

def write_regions_to_json(file_path, regions):
    
    with open(file_path, 'w') as file:
        json.dump([region.to_dict() for region in regions], file, indent=4)

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return points

def pathfinding():
    print("shut")




def find_intersected_regions(regions, x0, y0, x1, y1):
    start_time = time.time()
    print(start_time)
    points = bresenham_line(x0, y0, x1, y1)
    intersected_regions = set()
    for region in regions:
        for x, y in points:
            if region.contains_point(x, y):
                intersected_regions.add(region)
                break
    end_time = time.time()
    print(end_time)
    print(f"Time taken: {end_time - start_time:.10f} seconds")
    
    return list(intersected_regions)

def main(input_file, output_file, x0, y0, x1, y1):
    regions = read_regions_from_json(input_file)
    intersected_regions = find_intersected_regions(regions, x0, y0, x1, y1)
    write_regions_to_json(output_file, intersected_regions)
    

def test():
    base_dir = "C:\\shared stuff\\non onedrive stuff folder\\programming\\personal projects\\XianXia script stuff\\staging region\\data"
    input_file = os.path.join(base_dir, 'test_input.json')
    output_file = os.path.join(base_dir, 'test_output.json') 
    #output_file is where intersected regions will be written
    test_regions = [
        Region(0, 0, 100, 100, "forest", 4),
        Region(100, 0, 100, 100, "desert", 3),
        Region(0, 100, 100, 100, "water", 2),
        Region(100, 100, 100, 100, "deznuts",1)
    ]

    toggle_write_input = True
    toggle_read_output = True
    toggle_delete_files = False

    if toggle_write_input:
        write_regions_to_json(input_file, test_regions)

    x0, y0 = 0, 100
    x1, y1 = 100, 200

    main(input_file, output_file, x0, y0, x1, y1)

    if toggle_read_output:
        intersected_regions = read_regions_from_json(output_file)
        for region in intersected_regions:
            print(region.x, region.y, region.width, region.height, region.terrain_type, region.path_finding_weight)

    if toggle_delete_files:
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)

test()
