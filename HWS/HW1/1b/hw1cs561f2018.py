class SolveScooters:
    # n: the length of the area
    # p: the number of police officers
    def create_areas(self, n, p):
        # init the two dimensional list
        area = [[0 for i in range(n)] for i in range(n)]
        for line in lines:
            data = line.split(",")
            area[int(data[0])][int(data[1])] += 1
        occupied = {
            'col': set(),
            'sum': set(),
            'diff': set(),
        }
        max_score = [0]
        self.dfs(n, p, 0, occupied, 0, 0, 0, max_score, area)
        return max_score[0]

    # the fun part.
    # row: the number of rows that have been placed
    # occupied: the area that cannot be placed
    # count: the number of police officers placed
    # interval: the number of rows left empty
    def dfs(self, n, p, row, occupied, count, interval, score, max_score, area):
        # if len(officers) == n:
        if count == p:
            if max_score[0] < score:
                max_score[0] = score
            return
        # check every column in one level (one row)
        for col in range(n):
            if not self.check_valid(row, occupied, col):
                continue
            # if the new node is valid, then add it to the list
            occupied['col'].add(col)
            occupied['sum'].add(row + col)
            occupied['diff'].add(row - col)
            score += area[row][col]
            row += 1
            count += 1
            self.dfs(n, p, row, occupied, count, interval, score, max_score, area)
            # backtracking! return to the father node above to try other child nodes
            row -= 1
            count -= 1
            score -= area[row][col]
            occupied['col'].remove(col)
            occupied['sum'].remove(row + col)
            occupied['diff'].remove(row - col)

        if interval < n - p:
            row += 1
            interval += 1
            self.dfs(n, p, row, occupied, count, interval, score, max_score, area)
            # backtracking!
            interval -= 1
            row -= 1

    # check if the new police officer's position is conflicted with old ones
    def check_valid(self, row, occupied, col):
        if col in occupied['col'] or row + col in occupied['sum'] or row - col in occupied['diff']:
            return False
        else:
            return True


with open("input3.txt") as input_file:
    lines = input_file.read().splitlines()
    size = int(lines.pop(0))
    nums = int(lines.pop(0))
    lines.pop(0)
solution = SolveScooters()
max_point = solution.create_areas(size, nums)
with open("output.txt", "w") as output_file:
    output_file.write(str(max_point) + "\n")