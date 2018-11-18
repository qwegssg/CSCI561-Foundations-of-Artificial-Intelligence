import numpy as np


# Rectangular Coordinates: u_map[y, x], r_map[y, x], policy[y, x]
def value_iteration(u_map, r_map, size, exit_x, exit_y):
    epsilon = 0.1
    gamma = 0.9
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
        # terminate condition
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
            # argmax: get the index of the maximum value
            policy[index_y, index_x] = np.argmax(next_state(index_y, index_x, u_map, size)) + 1
    return policy


# return the utility list of each action
def next_state(index_y, index_x, u_map, size):
    action_list = np.zeros(4)
    # if the next state is out of boundary, then stay in the current state
    u_n = u_map[index_y - 1, index_x] if in_bound(index_y - 1, index_x, size) else u_map[index_y, index_x]
    u_e = u_map[index_y, index_x + 1] if in_bound(index_y, index_x + 1, size) else u_map[index_y, index_x]
    u_s = u_map[index_y + 1, index_x] if in_bound(index_y + 1, index_x, size) else u_map[index_y, index_x]
    u_w = u_map[index_y, index_x - 1] if in_bound(index_y, index_x - 1, size) else u_map[index_y, index_x]
    action_list[0] = 0.7 * u_n + 0.1 * (u_e + u_s + u_w)
    action_list[1] = 0.7 * u_s + 0.1 * (u_e + u_n + u_w)
    action_list[2] = 0.7 * u_e + 0.1 * (u_n + u_s + u_w)
    action_list[3] = 0.7 * u_w + 0.1 * (u_e + u_s + u_n)
    return action_list


def in_bound(y, x, size):
    if 0 <= x < size and 0 <= y < size:
        return True
    return False


with open("input1.txt") as input_file:
    lines = input_file.read().splitlines()
    map_size = int(lines[0])
    car_num = int(lines[1])
    ob_num = int(lines[2])
    # init grid map
    grid = np.ones([map_size, map_size])
    grid = -1 * grid
    # init the rewards of obstacles
    # attention: the actual map is needed to be transposed!!!!
    for index in range(ob_num):
        coordinate = lines[3 + index].split(",")
        grid[int(coordinate[0]), int(coordinate[1])] = -101
    # deal with the car one by one
    for index in range(car_num):
        grid_map = grid.copy()
        # init the reward of exit
        coordinate = lines[3 + ob_num + car_num + index].split(",")
        grid_map[int(coordinate[0]), int(coordinate[1])] = 99
        # transpose the grid!!!! hard copy!
        u_map = grid_map.T.copy()
        # init the reward map, hard copy!
        r_map = u_map.copy()
        op_policy = value_iteration(u_map, r_map, map_size, int(coordinate[0]), int(coordinate[1])).copy()
        print(op_policy)

        # do simulation
        total = 0
        for j in range(10):
            result = 0
            coordinate = lines[3 + ob_num + index].split(",")
            move_y = int(coordinate[1])
            move_x = int(coordinate[0])
            pos = op_policy[move_y, move_x]
            # seed 0 - 9 ????????????
            np.random.seed(j)
            swerve = np.random.random_sample(1000000)
            k = 0
            while pos != 0:
                # 1: n; 2: s; 3: e; 4: w
                if pos == 1:
                    if swerve[k] > 0.7:
                        if swerve[k] > 0.8:
                            if swerve[k] > 0.9:
                                move_y = move_y + 1 if in_bound(move_y + 1, move_x, map_size) else move_y
                            else:
                                move_x = move_x - 1 if in_bound(move_y, move_x - 1, map_size) else move_x
                        else:
                            move_x = move_x + 1 if in_bound(move_y, move_x + 1, map_size) else move_x
                    else:
                        move_y -= 1
                if pos == 2:
                    if swerve[k] > 0.7:
                        if swerve[k] > 0.8:
                            if swerve[k] > 0.9:
                                move_y = move_y - 1 if in_bound(move_y - 1, move_x, map_size) else move_y
                            else:
                                move_x = move_x + 1 if in_bound(move_y, move_x + 1, map_size) else move_x
                        else:
                            move_x = move_x - 1 if in_bound(move_y, move_x - 1, map_size) else move_x
                    else:
                        move_y += 1
                if pos == 3:
                    if swerve[k] > 0.7:
                        if swerve[k] > 0.8:
                            if swerve[k] > 0.9:
                                move_x = move_x - 1 if in_bound(move_y, move_x - 1, map_size) else move_x
                            else:
                                move_y = move_y - 1 if in_bound(move_y - 1, move_x, map_size) else move_y
                        else:
                            move_7 = move_y + 1 if in_bound(move_y + 1, move_x, map_size) else move_y
                    else:
                        move_x += 1
                if pos == 4:
                    if swerve[k] > 0.7:
                        if swerve[k] > 0.8:
                            if swerve[k] > 0.9:
                                move_x = move_x + 1 if in_bound(move_y, move_x + 1, map_size) else move_x
                            else:
                                move_y = move_y + 1 if in_bound(move_y + 1, move_x, map_size) else move_y
                        else:
                            move_7 = move_y - 1 if in_bound(move_y - 1, move_x, map_size) else move_y
                    else:
                        move_x -= 1
                result += r_map[move_y, move_x]
                pos = op_policy[move_y, move_x]
                k += 1
            total += result
            # print(result)
        print(total / 10.0)