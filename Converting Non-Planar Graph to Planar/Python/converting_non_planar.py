from random import randint


class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def intersection(p1, p2, q1, q2):
    det = (p2.x - p1.x) * (q2.y - q1.y) - (q2.x - q1.x) * (p2.y - p1.y)
    if det == 0:
        return False
    else:
        lamb = ((q2.y - q1.y) * (q2.x - p1.x) + (q1.x - q2.x) * (q2.y - p1.y)) / det
        gamma = ((p1.y - p2.y) * (q2.x - p1.x) + (p2.x - p1.x) * (q2.y - p1.y)) / det
        return (0 < lamb < 1) and (0 < gamma < 1)


NUMBER_VERTICES = 10
WIDTH = HEIGHT = 100  # dimensions of the canvas

vertices = []
path = []
print("* Converting Non-Planar Graph to Planar *")
print("Number of vertices :", NUMBER_VERTICES, "| Dimensions of the canvas : (" + str(WIDTH), ";", str(HEIGHT) + ")\n")
print("Vertices coordinates :")
for i in range(NUMBER_VERTICES):
    vertices.append(Vertex(randint(0, WIDTH), randint(0, HEIGHT)))
    print(i, ": (" + str(vertices[i].x), ";", str(vertices[i].y) + ")")
    path.append(i)  # the vertices are initially linked in their order of generation

number_intersections = 1  # suppose there is initially at least one intersection
while number_intersections > 0:
    number_intersections = 0
    for i in range(len(vertices) - 2):
        for j in range(i + 2, len(vertices) - 1):
            if i != j and (i + 1) != j:
                inter = intersection(vertices[i], vertices[i + 1], vertices[j], vertices[j + 1])
                if inter:
                    vertices[i + 1], vertices[j] = vertices[j], vertices[i + 1]  # swap the two vertices
                    path[i + 1], path[j] = path[j], path[i + 1]
                    number_intersections += 1

print("Path :", path)
print("Adjacency matrix :")
adjacency_matrix = [[0 for col in range(NUMBER_VERTICES)] for row in range(NUMBER_VERTICES)]
for i in range(NUMBER_VERTICES - 1):
    adjacency_matrix[path[i]][path[i + 1]] = 1
    adjacency_matrix[path[i + 1]][path[i]] = 1
for row in adjacency_matrix:
    print(*row)
