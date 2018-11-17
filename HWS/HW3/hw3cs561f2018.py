import numpy as np


# np.random.seed(1)
# a = np.random.random()
# b = 2
# print(a)
# print(b)
#
# map = np.zeros([10, 5])
# print(map[1][2])
# print(type(map[1][2]))

def value_iteration(u_map, size, exit_x, exit_y):
    # print(exit_x)
    # print(exit_y)
    epsilon = 0.1
    gamma = 0.9
    # create the init reward map, hard copy!
    r_map = u_map.copy()
    # print(u_map)
    # print(u_map[1, 7])
    # print(u_map[2, 8])
    while True:
        delta = 0
        # value iteration: update every state's utility
        for index_y in range(size):
            for index_x in range(size):
                # avoid updating the utility of exit!
                if index_y == exit_y and index_x == exit_x:
                    continue
                action_utility = next_state(index_y, index_x, u_map, size)
                # bellman update
                max_utility = r_map[index_y, index_x] + gamma * np.max(action_utility)
                delta = max(delta, np.abs(max_utility - u_map[index_y, index_x]))
                u_map[index_y, index_x] = max_utility
        if delta < epsilon * (1 - gamma) / gamma:
            break
    # generate the corresponding optimal policy
    policy = np.zeros([map_size, map_size])
    for index_y in range(size):
        for index_x in range(size):
            # avoid updating the utility of exit!
            if index_y == exit_y and index_x == exit_x:
                policy[index_y, index_x] = 0
                continue
            # 1: n; 2: s; 3: e; 4: w
            policy[index_y, index_x] = np.argmax(next_state(index_y, index_x, u_map, size)) + 1
    return policy



# return the utility list of each action
def next_state(index_y, index_x, u_map, size):
    action_list = np.zeros(4)
    u_n = u_map[index_y - 1, index_x] if in_bound(index_y - 1, index_x, size) else u_map[index_y, index_x]
    u_e = u_map[index_y, index_x + 1] if in_bound(index_y, index_x + 1, size) else u_map[index_y, index_x]
    u_s = u_map[index_y + 1, index_x] if in_bound(index_y + 1, index_x, size) else u_map[index_y, index_x]
    u_w = u_map[index_y, index_x - 1] if in_bound(index_y, index_x - 1, size) else u_map[index_y, index_x]
    action_list[0] = 0.7 * u_n + 0.1 * (u_e + u_s + u_w)
    action_list[1] = 0.7 * u_s + 0.1 * (u_e + u_n + u_w)
    action_list[2] = 0.7 * u_e + 0.1 * (u_n + u_s + u_w)
    action_list[3] = 0.7 * u_w + 0.1 * (u_e + u_s + u_n)
    return action_list


def in_bound(x, y, size):
    if 0 <= x < size and 0 <= y < size:
        return True
    return False


with open("input1.txt") as input_file:
    lines = input_file.read().splitlines()
    map_size = int(lines[0])
    car_num = int(lines[1])
    ob_num = int(lines[2])
    grid = np.ones([map_size, map_size])
    grid = -1 * grid
    # init the rewards of obstacles
    for index in range(ob_num):
        coordinate = lines[3 + index].split(",")
        grid[int(coordinate[0]), int(coordinate[1])] = -101

    for index in range(car_num):
        grid_map = grid.copy()
        # init the rewards of exit
        coordinate = lines[3 + ob_num + car_num + index].split(",")
        grid_map[int(coordinate[0]), int(coordinate[1])] = 99
        # transform the row and column of the grid!!!!
        op_policy = value_iteration(grid_map.T, map_size, int(coordinate[0]), int(coordinate[1]))
        print(op_policy)

        # do simulation
        for j in range(10):
            result = 0
            coordinate = lines[3 + ob_num + index].split(",")
            pos = op_policy[int(coordinate[1]), int(coordinate[0])]
            # seed 0 - 9 ????????????
            np.random.seed(j)
            swerve = np.random.random_sample(1000000)
            k = 0
            # while pos != 0:
            #     move = policies[i][pos]
            # if swerve[k] > 0.7:
            #     if swerve[k] > 0.8:
            #         if swerve[k] > 0.9:
            #         else:
            #             k += 1