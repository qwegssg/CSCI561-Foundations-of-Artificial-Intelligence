class SolveScooters:

    def create_areas(self, n):
        # result is a list of lists, if existing
        result = []
        visited_area = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, [], visited_area, result)
        return result
        # return len(result)

    # the fun part
    def dfs(self, n, permutation, visited_area, result):
        if len(permutation) == n:
            result.append(self.construct_graph(permutation))
            return

        row = len(permutation)
        # check every column in one level (one row)
        for col in range(n):
            if not self.check_valid(permutation, visited_area, col):
                continue
            permutation.append(col)
            visited_area['col'].add(col)
            visited_area['sum'].add(row + col)
            visited_area['diff'].add(row - col)

            self.dfs(n, permutation, visited_area, result)
            # backtracking! return to the father node above to try other child nodes
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

    # every graph is a list
    def construct_graph(self, permutation):
        graph = []
        n = len(permutation)
        for col in permutation:
            row_string = ''.join(['p' if c == col else '.' for c in range(n)])
            graph.append(row_string)
        return graph


solution = SolveScooters()
print(solution.create_areas(4))