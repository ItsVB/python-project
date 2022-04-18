import random as r

w = 0
player_data = {"name": None, "R": 0, "B": 0, "4s": 0, "6s": 0}
striker_ls = ["striker1", "striker2"]

MI = {"RS": 0, "HP": 0, "KP": 0, "IK": 0, "SY": 0, "AT": 0, "JB": 0, "ST": 0, "QK": 0, "TB": 0, "RC": 0}
CSK = {"MsD": 0, "RG": 0, "SC": 0, "SR": 0, "RJ": 0, "RU": 0, "MA": 0, "DC": 0, "DB": 0, "ST": 0, "AR": 0}
t1_keys = list(MI.keys())
t2_keys = list(CSK.keys())

team_ls = [["MI", t1_keys, MI], ["CSK", t2_keys, CSK]]
player_dic = {"baller": player_data.copy(), "striker1": player_data.copy(), "striker2": player_data.copy()}

ran_outcome = ["0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "2", "2", "2", "2", "3", "3", "4", "4", "4", "6", "6",
               "W", "wide"]


def choose():
    print("Enter 0 for balling and 1 for bating")
    c = int(input())
    if c == 0:
        print("\n>>>>>>>> You choosed balling <<<<<<<<")
        return c
    elif c == 1:
        print("\n>>>>>>>> You choosed bating <<<<<<<<")
        return c
    else:
        print("\n>>>>>>>> Wrong choice <<<<<<<")
        choose()


def toss():
    input("\n>>>Press Enter to toss the coin : ")

    toss = r.randint(0, 1)
    if toss == 0:
        print("\n>>>>>>>>>>>>> MI wins toss <<<<<<<<<<<<<<<<<<\n")
        c = choose()
    else:
        print("\n>>>>>>>>>>>>> CSK wins toss <<<<<<<<<<<<<<<<<<\n")
        c = choose()
    return toss, c


def printData(turn, w):
    if player_dic["striker1"]["B"] > 0:
        str_p1 = int((player_dic["striker1"]["R"] / player_dic["striker1"]["B"]) * 100)
    else:
        str_p1 = 0
    if player_dic["striker2"]["B"] > 0:
        str_p2 = int((player_dic["striker2"]["R"] / player_dic["striker2"]["B"]) * 100)
    else:
        str_p2 = 0

    print("\n=========================== SCORE BOARD ==================================")
    print("\nStriker Team \tTotal Runs \tWickets")
    print(team_ls[turn - 1][0], " \t\t  ", sum(team_ls[turn - 1][2].values()), "\t\t", w)
    print("\nStriker Name \t R(B) \t\t 4s \t 6s \t\t S ")
    print(player_dic["striker1"]["name"], "\t\t", player_dic["striker1"]["R"], "(", player_dic["striker1"]["B"], ")",
          "\t", player_dic["striker1"]["4s"], "\t", player_dic["striker1"]["6s"], "\t\t", str_p1)
    print(player_dic["striker2"]["name"], "\t\t", player_dic["striker2"]["R"], "(", player_dic["striker2"]["B"], ")",
          "\t", player_dic["striker2"]["4s"], "\t", player_dic["striker2"]["6s"], "\t\t", str_p2)
    print("\nBaller Name \t B")
    print(player_dic["baller"]["name"], "\t\t", player_dic["baller"]["B"])
    print("\n----------------------------------------------------------------------\n")


def setBaller(turn):
    player_dic["baller"] = player_data.copy()
    print("\n", team_ls[turn][0], " Select your baller from : \n\n", team_ls[turn][1])
    player_dic["baller"]["name"] = input("\n>>> ")
    print("")


def setSt1(turn):
    player_dic["striker1"] = player_data.copy()
    print("\n", team_ls[turn - 1][0], " select your  strikers from : \n", team_ls[turn - 1][1])
    player_dic["striker1"]["name"] = input("\n>>> ")
    team_ls[turn - 1][1].remove(player_dic["striker1"]["name"])


def setSt2(turn):
    player_dic["striker2"] = player_data.copy()
    print("\n", team_ls[turn - 1][0], " select your  strikers from : \n", team_ls[turn - 1][1])
    player_dic["striker2"]["name"] = input("\n>>> ")
    team_ls[turn - 1][1].remove(player_dic["striker2"]["name"])


def str_change(s):
    print("\n--------------STRIKER IS CHANGING ...-----------------")
    if s == 0:
        s = 1
    elif s == 1:
        s = 0
    return s


def gamePlay(turn, w, target, overs):
    setSt1(turn)
    setSt2(turn)
    flag = 0

    s = 0
    i = 0
    w = 0
    while i < overs:
        print("\n>>>>>>>>>>>>>>>>>>>>>>>> Over No. : ", i + 1, " <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
        setBaller(turn)
        if i > 0:
            s = str_change(s)

        j = 0
        while j < 6:
            printData(turn, w)
            str_name = player_dic[striker_ls[s]]["name"]
            print("\n>>> Striker is ", str_name)
            print(">>> Baller is ", player_dic["baller"]["name"])
            input("\nPress Enter for balling......")
            run = r.choice(ran_outcome)
            player_dic["baller"]["B"] = j + 1
            player_dic[striker_ls[s]]["B"] += 1

            if run == "0" or run == "1" or run == "2" or run == "3" or run == "4" or run == "6":
                if run == "4":
                    player_dic[striker_ls[s]]["4s"] += 1
                elif run == "6":
                    player_dic[striker_ls[s]]["6s"] += 1

                print("\n", str_name, " got ", run, " runs...")
                player_dic[striker_ls[s]]["R"] += int(run)
                team_ls[turn - 1][2][str_name] += int(run)

                if (run == "1" or run == "3"):
                    s = str_change(s)

            elif run == "wide":
                print("\nThis is wide...")
                player_dic[striker_ls[s]]["R"] += 1
                team_ls[turn - 1][2][str_name] += 1
                j -= 1
            elif run == "W":
                w += 1
                print("\n>>>>>>>>>>>>>>>This is wicket...<<<<<<<<<<<<<<<<<\n\n", str_name, " lost",
                      "\nSelect another striker...\n")
                if s == 0:
                    setSt1(turn)
                elif s == 1:
                    setSt2(turn)

            if target > 0 and sum(team_ls[turn - 1][2].values()) > target:
                print("\n\n>>>>>>>>>>>>>>>>>>>>>>", team_ls[turn - 1][0], " WINS THE MATCH <<<<<<<<<<<<<<<<<<<<<<<")
                flag = 1
                break
            j += 1
        i += 1

    if flag == 0:
        if target > 0 :
            print("\n\n>>>>>>>>>>>>>>>>>>>>>>", team_ls[turn][0], " WINS THE MATCH <<<<<<<<<<<<<<<<<<<<<<<")
        print("\n\n======================= FIRST HALF IS OVER ========================\n\n")
        team_ls[0][1] = list(MI.keys())
        team_ls[1][1] = list(CSK.keys())
        target = sum(team_ls[turn - 1][2].values())
        print(">>>>>>>>>>>>>>>>>> TARGET GIVEN IS OF ", target, " RUNS <<<<<<<<<<<<<<<<<<<\n\n")

    return target


overs = int(input("\nENTER NUMBER OF OVERS FOR THE MATCH : "))
tos = toss()
if tos == (0, 0) or tos == (1, 1):
    tr = gamePlay(0, w, 0, overs)
    gamePlay(1, w, tr, overs)
else:
    tr = gamePlay(1, w, 0, overs)
    gamePlay(0, w, tr, overs)