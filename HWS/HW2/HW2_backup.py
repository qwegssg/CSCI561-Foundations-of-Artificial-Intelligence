class Efficiency:

    def init(self, valid_list, week_detail_lahsa, week_detail_spla, curr_lahsa, curr_spla):
        # set a flag to determine the next organization
        is_spla = True

        # curr_list = []
        result = self.max_efficiency(valid_list, week_detail_lahsa, week_detail_spla, curr_lahsa, curr_spla, is_spla)
        print(result)

    def max_efficiency(self, valid_list, week_detail_lahsa, week_detail_spla, curr_lahsa, curr_spla, is_spla):
        # if there is no more candidates can be picked
        if self.is_over(valid_list):
            return [curr_lahsa, curr_spla]

        # SPLA's turn:
        if is_spla:
            score_list = []
            for candidate in valid_list:
                # choose the qualified candidates for SPLA, calculate the efficiency
                if candidate[10:13] == "NYY":

                    # calculate the contribution of one candidate
                    # score = 0

                    for can_index in range(7):
                        # if candidate request for room for a day and the day has remaining room
                        if int(candidate[13 + can_index:14 + can_index]) == 1 and week_detail_spla[can_index] < total_space_s:
                            week_detail_spla[can_index] += 1
                            curr_spla = curr_spla + 1
                    #         score = score + 1
                    # # pruning!!!! though qualified, if the contribution is zero, then rule out
                    # if score == 0:
                    #     valid_list.remove(candidate)
                    #     continue

                    print(curr_spla)
                    print(week_detail_spla)

                    # chosen_list.append(candidate)

                    valid_list.remove(candidate)

                    # change turn to another organization
                    is_spla = not is_spla
                    result = self.max_efficiency(valid_list, week_detail_lahsa, week_detail_spla, curr_lahsa, curr_spla, is_spla)
                    score_list.append(result[1])

            return [curr_lahsa, curr_lahsa + max(score_list)]

        # LAHSA's turn
        if not is_spla:
            score_list = []
            for candidate in valid_list:
                if candidate[5:6] == "F" and int(candidate[6:9]) > 17 and candidate[9:10] == "N":
                    # calculate the contribution of one candidate
                    # score = 0
                    for can_index in range(7):
                        # if candidate request for room for a day and the day has remaining room
                        if int(candidate[13 + can_index:14 + can_index]) == 1 and week_detail_lahsa[can_index] < total_space_l:
                            week_detail_lahsa[can_index] += 1
                            curr_lahsa = curr_lahsa + 1
                    #         score = score + 1
                    # # pruning!!!! though qualified, if the contribution is zero, then rule out
                    # if score == 0:
                    #     valid_list.remove(candidate)
                    #     continue

                    # chosen_list.append(candidate)
                    valid_list.remove(candidate)

                    # change turn to another organization
                    is_spla = not is_spla
                    result = self.max_efficiency(valid_list, week_detail_lahsa, week_detail_spla, curr_lahsa, curr_spla, is_spla)
                    score_list.append(result[0])

            # if there is no more qualified candidates, then LAHSA is over
            if len(score_list) == 0:
                return [curr_lahsa, curr_spla]

            return [curr_lahsa, max(score_list)]





        # make sure the daily usage is not exceeded
        # for day_usage in week_detail_spla:
        #     if day_usage < p_spla:
        #         print("Applicants are welcomed!!!!")


    def is_over(self, valid_list):
        if len(valid_list) == 0:
            return True
        return False



with open("input0.txt") as input_file:
    lines = input_file.read().splitlines()
    total_space_l = int(lines[0])
    total_space_s = int(lines[1])
    l_so_far = int(lines[2])
    s_so_far = int(lines[3 + l_so_far])
    total = int(lines[4 + l_so_far + s_so_far])
    # print(l_so_far)
    # print(s_so_far)
    # print(total)

    # create remaining applicants list, calculate the init state
    app_list = []
    spla_set = set()
    lahsa_set = set()
    for index in range(s_so_far):
        spla_set.add(int(lines[4 + l_so_far + index]))

    for index in range(l_so_far):
        lahsa_set.add(int(lines[3 + index]))

    week_spla = [0, 0, 0, 0, 0, 0, 0]
    week_lahsa = [0, 0, 0, 0, 0, 0, 0]
    curr_spla = 0
    curr_lahsa = 0
    for index in range(total):
        applicant = lines[5 + l_so_far + s_so_far + index]
        if index + 1 in spla_set:
            for i in range(7):
                if int(applicant[13 + i:14 + i]) == 1:
                    week_spla[i] += int(applicant[13 + i:14 + i])
                    curr_spla = curr_spla + 1
        elif index + 1 in lahsa_set:
            for i in range(7):
                if int(applicant[13 + i:14 + i]) == 1:
                    week_lahsa[i] += int(applicant[13 + i:14 + i])
                    curr_lahsa = curr_lahsa + 1
        else:
            app_list.append(applicant)

    # print(lahsa_set)
    # print(spla_set)
    # print(app_list)
    # print(week_spla)
    # print(week_lahsa)
    # print(curr_spla)
    # print(curr_lahsa)

    # deal with the app list???


    efficiency = Efficiency()
    efficiency.init(app_list, week_lahsa, week_spla, curr_lahsa, curr_spla)

with open("output.txt", "w") as output_file:
    output_file.write("rytryt" + "\n")

