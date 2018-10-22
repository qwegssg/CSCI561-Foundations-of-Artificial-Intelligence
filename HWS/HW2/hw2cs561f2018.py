class Efficiency:

    def init(self, b_lahsa, p_spla, app_list, week_spla, week_lahsa, curr_spla, curr_lahsa):

        # next_pick_spla = []
        # # first round for SPLA:
        # for candidate in app_list:
        #     # choose the qualified candidates for SPLA, calculate the efficiency
        #     if candidate[10:13] == "NYY":
        #         # calculate the contribution of one candidate
        #         score = 0
        #         for index in range(7):
        #             # if candidate request for room for a day and the day has remaining room
        #             if int(candidate[13 + index:14 + index]) == 1 and week_spla[index] < p_spla:
        #                 week_spla[index] += 1
        #                 curr_spla = curr_spla + 1
        #                 score = score + 1
        #         # pruning!!!! though qualified, if the contribution is zero, then rule out
        #         if score == 0:
        #             app_list.remove(candidate)
        #             continue
        #
        #         next_pick_spla.append({id: candidate[0:5], score: curr_spla})
        #         app_list.remove(candidate)


        # set a flag to determine the next organization
        is_spla = True
        # # create a list to record the choosing list
        # chosen_list = []
        self.max_efficiency(b_lahsa, p_spla, app_list, week_spla, week_lahsa, curr_spla, curr_lahsa, is_spla)

    def max_efficiency(self, b_lahsa, p_spla, app_list, week_spla, week_lahsa, curr_spla, curr_lahsa, is_spla):
        print("hahahahaahahah")
        print(curr_spla)
        # # if there is no more candidates can be picked
        # if self.isOver():
        #     return

        # SPLA's turn:
        if is_spla:
            for candidate in app_list:
                # choose the qualified candidates for SPLA, calculate the efficiency
                if candidate[10:13] == "NYY":
                    # calculate the contribution of one candidate
                    score = 0
                    for index in range(7):
                        # if candidate request for room for a day and the day has remaining room
                        if int(candidate[13 + index:14 + index]) == 1 and week_spla[index] < p_spla:
                            week_spla[index] += 1
                            curr_spla = curr_spla + 1
                            score = score + 1
                    # pruning!!!! though qualified, if the contribution is zero, then rule out
                    if score == 0:
                        app_list.remove(candidate)
                        continue

                    # chosen_list.append(candidate)
                    app_list.remove(candidate)
                    # print(week_spla)

                    # change turn to another organization
                    is_spla = not is_spla
                    self.max_efficiency(b_lahsa, p_spla, app_list, week_spla, week_lahsa, curr_spla, curr_lahsa, is_spla)





        # make sure the daily usage is not exceeded
        # for day_usage in week_spla:
        #     if day_usage < p_spla:
        #         print("Applicants are welcomed!!!!")


    def isOver(self):

        return



with open("input0.txt") as input_file:
    lines = input_file.read().splitlines()
    b_lahsa = int(lines[0])
    p_spla = int(lines[1])
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
        if index + 1 in lahsa_set:
            for i in range(7):
                if int(applicant[13 + i:14 + i]) == 1:
                    week_lahsa[i] += int(applicant[13 + i:14 + i])
                    curr_lahsa = curr_lahsa + 1
        else:
            app_list.append(applicant)

    # print(app_list)
    # print(week_spla)
    # print(week_lahsa)
    # print(curr_spla)
    # print(curr_lahsa)

    # deal with the app list???



    efficiency = Efficiency()
    efficiency.init(b_lahsa, p_spla, app_list, week_spla, week_lahsa, curr_spla, curr_lahsa)

with open("output.txt", "w") as output_file:
    output_file.write("rytryt" + "\n")

