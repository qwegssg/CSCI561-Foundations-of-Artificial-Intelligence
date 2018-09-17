class SolveScooters:

    # n: the length of the area
    # p: the number of police officers
    def create_areas(self, n, p):
        # result is a list of lists, if existing
        result = []
        occupied = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, p, [], occupied, 0, 0, result)
        return result

    # the fun part.
    # count: the number of police officers placed
    # interval: the number of rows left empty
    def dfs(self, n, p, officers, occupied, count, interval, result):
        # if len(officers) == n:
        if count == p:
            result.append(self.construct_graph(officers))
            return
        # check every column in one level (one row)
        row = len(officers)
        for col in range(n):
            if not self.check_valid(officers, occupied, col):
                continue
            # if the new node is valid, then add it to the list
            # officers.append(col)
            officers.append(str(row) + "," + str(col))
            count += 1
            occupied['col'].add(col)
            occupied['sum'].add(row + col)
            occupied['diff'].add(row - col)

            self.dfs(n, p, officers, occupied, count, interval, result)

            # backtracking! return to the father node above to try other child nodes
            occupied['col'].remove(col)
            occupied['sum'].remove(row + col)
            occupied['diff'].remove(row - col)
            officers.pop()
            count -= 1

        if interval < n - p:
            officers.append(-1)
            interval += 1
            self.dfs(n, p, officers, occupied, count, interval, result)
            # backtracking!
            officers.pop()
            interval -= 1

    # check if the new police officer's position is conflicted with old ones
    def check_valid(self, officers, occupied, col):
        row = len(officers)
        if col in occupied['col'] or row + col in occupied['sum'] or row - col in occupied['diff']:
            return False
        else:
            return True

    # every graph is a list
    def construct_graph(self, officers):
        # graph = []
        # n = len(officers)
        # for col in officers:
        #     row_string = ''.join(['p' if c == col else '.' for c in range(n)])
        #     graph.append(row_string)
        # return graph
        graph = set()
        for p in officers:
            graph.add(p)
        return graph



    def get_max(self):
        max_point = 0
        with open("input3.txt") as input_file:
            lines = input_file.read().splitlines()
            result = self.create_areas(int(lines[0]), int(lines[1]))
            # print(result)
            for graph in result:
                point = 0
                for line in lines:
                    # data = line.split(",")
                    # print(line)
                    if line in graph:
                        point += 1
                if point > max_point:
                    max_point = point
        print(max_point)
        with open("output.txt", "w") as output_file:
            output_file.write(str(max_point) + "\n")


solution = SolveScooters()
# print(solution.create_areas(4, 2))
# result = solution.create_areas(4, 2)
solution.get_max()