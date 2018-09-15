class SolveScooters:

    # n: the length of the area
    # p: the number of police officers
    def create_areas(self, n, p):
        # result is a list of lists, if existing
        result = []
        # max = 0
        visited_area = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        self.dfs(n, p, [], visited_area, 0, 0, result)
        return result
        # return len(result)

    # the fun part
    # count: the number of police officers placed
    # interval: the number of rows left empty
    def dfs(self, n, p, graph_list, visited_area, count, interval, result):
        # if len(graph_list) == n:
        if count == p:
            result.append(self.construct_graph(graph_list))
            return

        row = len(graph_list)
        # check every column in one level (one row)
        for col in range(n):
            if not self.check_valid(graph_list, visited_area, col):
                continue
            # if the new node is valid, then add it to graph list
            # graph_list.append(col)
            graph_list.append(str(row) + "," + str(col))
            count += 1
            visited_area['col'].add(col)
            visited_area['sum'].add(row + col)
            visited_area['diff'].add(row - col)

            self.dfs(n, p, graph_list, visited_area, count, interval, result)

            # backtracking! return to the father node above to try other child nodes
            visited_area['col'].remove(col)
            visited_area['sum'].remove(row + col)
            visited_area['diff'].remove(row - col)
            graph_list.pop()
            count -= 1

        if interval < n - p:
            graph_list.append(-1)
            interval += 1
            self.dfs(n, p, graph_list, visited_area, count, interval, result)
            # backtracking!
            graph_list.pop()
            interval -= 1

    # check if the new police officer's position is conflicted with old ones
    def check_valid(self, graph_list, visited_area, col):
        row = len(graph_list)
        if col in visited_area['col']:
            return False
        if row + col in visited_area['sum']:
            return False
        if row - col in visited_area['diff']:
            return False
        return True

    # every graph is a list
    def construct_graph(self, graph_list):
        # graph = []
        # n = len(graph_list)
        # for col in graph_list:
        #     row_string = ''.join(['p' if c == col else '.' for c in range(n)])
        #     graph.append(row_string)
        # return graph
        graph = set()
        for p in graph_list:
            graph.add(p)
        return graph



    def get_max(self):
        max_point = 0
        with open("input1.txt") as input_file:
            lines = input_file.read().splitlines()
            result = self.create_areas(int(lines[0]), int(lines[1]))
            print(result)
            for graph in result:
                point = 0
                for line in lines:
                    # data = line.split(",")
                    # print(line)
                    if line in graph:
                        point += 1
                if point > max_point:
                    max_point = point
        with open("output.txt", "w") as output_file:
            output_file.write(str(max_point) + "\n")


solution = SolveScooters()
# print(solution.create_areas(4, 2))
# result = solution.create_areas(4, 2)
solution.get_max()