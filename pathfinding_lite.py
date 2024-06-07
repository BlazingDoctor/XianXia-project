from regions_lite import Region, find_intersected_regions, test

class Node():
    def __init__(self, parent=None, position=None):
        self.parent, self.position = parent, position
        self.g = self.h = self.f = 0
    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end, regions):  # Change: Added 'regions' parameter
    start_node = Node(None, start)
    end_node = Node(None, end)
    open_list, closed_list = [start_node], []
    while open_list:
        current_node = min(open_list, key=lambda o: o.f)
        open_list.remove(current_node)
        closed_list.append(current_node)
        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if 0 <= node_position[0] < len(maze) and 0 <= node_position[1] < len(maze[0]):  # Change: Removed 'maze[node_position[0]][node_position[1]] == 0'
                new_node = Node(current_node, node_position)
                if new_node not in closed_list:
                    terrain_cost = get_region_weight(node_position[0], node_position[1], regions)  # Change: Added terrain cost calculation
                    new_node.g = current_node.g + terrain_cost  # Change: Used 'terrain_cost' instead of '+1'
                    new_node.h = ((new_node.position[0] - end_node.position[0])**2 + (new_node.position[1] - end_node.position[1])**2) * terrain_cost  # Change: Multiplied the heuristic by 'terrain_cost'
                    new_node.f = new_node.g + new_node.h
                    if all(new_node.g < open_node.g for open_node in open_list if new_node == open_node):
                        open_list.append(new_node)
def get_region_weight(x, y, regions):
    for region in regions:
        if region.contains_point(x, y):
            #print(f"Found region at ({x}, {y}): {region.path_finding_weight}")
            return region.path_finding_weight
        # else:
        #     print(f"No region found at ({x}, {y})")
            
            
    #print(f"No region found at ({x}, {y})")
    return 1  # Default weight if no region matches

# def astar(maze, start, end):
#     start_node = Node(None, start)
#     end_node = Node(None, end)
#     open_list, closed_list = [start_node], []
#     while open_list:
#         current_node = min(open_list, key=lambda o: o.f)
#         open_list.remove(current_node)
#         closed_list.append(current_node)
#         if current_node == end_node:
#             path = []
#             while current_node:
#                 path.append(current_node.position)
#                 current_node = current_node.parent
#             return path[::-1]
#         children = []
#         for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
#             node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
#             if 0 <= node_position[0] < len(maze) and 0 <= node_position[1] < len(maze[0]) and maze[node_position[0]][node_position[1]] == 0:
#                 new_node = Node(current_node, node_position)
#                 if new_node not in closed_list:
#                     new_node.g = current_node.g + 1
#                     new_node.h = (new_node.position[0] - end_node.position[0])**2 + (new_node.position[1] - end_node.position[1])**2
#                     new_node.f = new_node.g + new_node.h
#                     if all(new_node.g < open_node.g for open_node in open_list if new_node == open_node):
#                         open_list.append(new_node)

def main():
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #will break if out of bounds, no input sanitization
    start, end = (0, 0), (8, 7)

    regions = [
        Region(5, 0, 100, 100, "forest", 4),
        Region(100, 0, 100, 100, "desert", 3),
        Region(0, 100, 100, 100, "water", 2),
        Region(100, 100, 100, 100, "mountain", 1)
    ]
    print(astar(maze, start, end, regions))

if __name__ == '__main__':
    main()
