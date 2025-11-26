class Graph:
    def __init__(self, vertices: list[int], edges:list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges
        self.visited_vertices = list()
        self.index = 0

    def dfs(self) -> list[int]:
        states = {"white": [v for v in self.vertices],
                  "grey": list(),
                  "black": list()}
        # если я правильно поняла, вершина является посещенной, если она просто попала в список grey
        def dfs_step(vertex):
                states["grey"].append(vertex)
                self.visited_vertices.append(vertex)
                states["white"].remove(vertex)
                for edge in self.edges:
                    if vertex == edge[0]:
                        if edge[1] in states["white"]:
                            dfs_step(edge[1])
                    if vertex == edge[1]:
                        if edge[0] in states["white"]:
                            dfs_step(edge[0])
                states["black"].append(vertex)
                states["grey"].remove(vertex)
        for vertex in self.vertices:
            if vertex in states["white"]:
                dfs_step(vertex)
        return self.visited_vertices

    def __iter__(self):
        if self.visited_vertices == []:
            self.visited_vertices = self.dfs()
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.visited_vertices):
            raise StopIteration
        vertex = self.visited_vertices[self.index]
        self.index += 1
        return vertex