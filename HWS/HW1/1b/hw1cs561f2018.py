class SolveScooters:

    def create_areas(self, n):
        graph = []
        visited_area = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, [], visited_area, graph)
        return graph

    def dfs(self, n, permutation, visited_area, graph):
        if len(permutation) == n:
            graph.append(self.construct_graph(permutation))
            return

        row = len(permutation)
        for col in range(n):
            if not self.check_valid(permutation, visited_area, col):
                continue
            permutation.append(col)
            visited_area['col'].add(col)
            visited_area['sum'].add(row + col)
            visited_area['diff'].add(row - col)

            self.dfs(n, permutation, visited_area, graph)
            visited_area['col'].remove(col)
            visited_area['sum'].remove(row + col)
            visited_area['diff'].remove(row - col)
            permutation.pop()

    # check if the new police officer's position is conflicted with old ones
    def check_valid(self, permutation, visited_area, col):
        row = len(permutation)
        if col in visited_area['col']:
            return False
        if row + col in visited_area['sum']:
            return False
        if row - col in visited_area['diff']:
            return False
        return True

    def construct_graph(self, permutation):
        graph = []
        n = len(permutation)
        for col in permutation:
            row_string = ''.join(['p' if c == col else '.' for c in range(n)])
            graph.append(row_string)
        return graph



solution = SolveScooters()
print(solution.create_areas(4))