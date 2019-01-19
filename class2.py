
import pandas as pd
import ast


from random import *

class COUPLE_DF:

    def __init__(self):
        self.df = pd.DataFrame(columns=["couple_id", "user_id1", "user_id2", "key", "active"])
        self.s4et4ik = len(self.df)

    def us_append1(self, USER):

        id = "couple_" + str(self.s4et4ik)
        self.s4et4ik = self.s4et4ik + 1
        key = USER.key
        dict = [id, USER.telegram_id, None, USER.key, 0]

        self.df.loc[len(self.df)] = dict
        #return (self)


    def print(self):
        print(self.df.head())

    def us_append2(self, USER):
        self.df.loc[self.df.key == USER.key, 'user_id2'] = (USER.telegram_id)
        self.df.loc[self.df.key == USER.key, "active"] = 1
        #return (self)

    def cheker(self,key):
        lent = len(self.df.loc[self.df.key == key])
        return(lent)

    def get_couple(self):
        num = self.df.loc[self.df.active == 1]
        return (num)

    def read(self):
        try:
            self.df = pd.read_csv("COUPLE.csv")[["couple_id", "user_id1", "user_id2", "key", "active"]]
        except :
            return ""

    def write(self):
        self.df.to_csv("COUPLE.csv")


class data:

    def __init__(self):
        self.df = pd.DataFrame(
            columns=["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"])
        self.s4et4ik = len(self.df)

    def uppend(self, data):

        self.df = self.df[["couple_id", "QUESTIONS", "user_id1", "user_id2", "key","1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"]].append(data[["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"]])
        # return (self)

    def read(self):
        try:
            self.df = pd.read_csv("data.csv")[
                ["couple_id", "QUESTIONS", "user_id1", "user_id2", "key","1_1", "2_1", "3_1", "4_1", "5_1","1_2", "2_2", "3_2", "4_2", "5_2"]]
        except:
            return ("")

    def write(self):
        self.df.to_csv("data.csv")


class Current_day:

    def __init__(self):
        self.df = pd.DataFrame(
            columns=["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1", "1_2",
                     "2_2", "3_2", "4_2", "5_2"])
        self.s4et4ik = len(self.df)

    def clear(self):
        self.df = pd.DataFrame(
            columns=["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1", "1_2",
                     "2_2", "3_2", "4_2", "5_2"])

    def us_append_couples(self, COUPLE):

        self.df[["couple_id", "user_id1", "user_id2", "key"]] = COUPLE
        # return (self)

    def us_append_question(self, couple_id, key, array):
        self.df.loc[self.df.key == key, "QUESTIONS"] = str(array)

    def us_append(self, user_id, question, mark):
        user_id = "tg_" + str(user_id)
        print(len(self.df.loc[self.df.user_id1 == user_id]))

    def us_append_feedback(self, user_id, question, mark):
        user_id = "tg_" + str(user_id)
        if len(self.df.loc[self.df.user_id1 == user_id]) > 0:
            stolb = str(question + "_1")
            self.df.loc[self.df.user_id1 == user_id, stolb] = mark

        if len(self.df.loc[self.df.user_id2 == user_id]) > 0:
            stolb = str(question + "_2")
            self.df.loc[self.df.user_id2 == user_id, stolb] = mark

    def us_append_vk(self, user_id, question, mark):
        user_id = "vk_" + str(user_id)
        print(len(self.df.loc[self.df.user_id1 == user_id]))

    def us_append_feedback_vk(self, user_id, question, mark):
        user_id = "vk_" + str(user_id)
        if len(self.df.loc[self.df.user_id1 == user_id]) > 0:
            stolb = str(question + "_1")
            self.df.loc[self.df.user_id1 == user_id, stolb] = mark

        if len(self.df.loc[self.df.user_id2 == user_id]) > 0:
            stolb = str(question + "_2")
            self.df.loc[self.df.user_id2 == user_id, stolb] = mark

    def print(self):
        print(self.df.head())

    def read(self):
        try:
            self.df = pd.read_csv("CURRENT_DAY.csv")[
                ["couple_id", "QUESTIONS", "user_id1", "user_id2", "key", "1_1", "2_1", "3_1", "4_1", "5_1", "1_2",
                 "2_2", "3_2", "4_2", "5_2"]]
        except:
            return ("")

    def extract(self):
        data = pd.DataFrame(columns=["couple_id", "key", "number"])
        Y = self.df[["1_1", "2_1", "3_1", "4_1", "5_1", "1_2", "2_2", "3_2", "4_2", "5_2"]]
        Y = Y.fillna(0)
        for i in range(len(Y)):
            x1 = Y.loc[i]["1_1"] + Y.loc[i]["1_2"]
            x2 = Y.loc[i]["2_1"] + Y.loc[i]["2_2"]
            x3 = Y.loc[i]["3_1"] + Y.loc[i]["3_2"]
            x4 = Y.loc[i]["4_1"] + Y.loc[i]["4_2"]
            x5 = Y.loc[i]["5_1"] + Y.loc[i]["5_2"]

            testarray = ast.literal_eval(self.df.loc[i, "QUESTIONS"])

            if x1 >= max([x2, x3, x4, x5]):
                number = testarray[0]
            elif x2 >= max([x1, x3, x4, x5]):
                number = testarray[1]
            elif x3 >= max([x2, x1, x4, x5]):
                number = testarray[2]
            elif x4 >= max([x2, x1, x3, x5]):
                number = testarray[3]
            elif x5 >= max([x2, x1, x3, x4]):
                number = testarray[4]

            data.loc[i] = [self.df.loc[i, "couple_id"], self.df.loc[i, "key"], number]
        return (data)

    def write(self):
        self.df.to_csv("CURRENT_DAY.csv")


class questions:

    def __init__(self):
        self.df = pd.DataFrame(columns=["couple_id", "question", "day", "day_from"])
        self.s4et4ik = len(self.df)

    def append(self,couples):
        self.df.append(couples)



    def read(self):
        try:
            self.df = pd.read_csv("questions.csv")[["couple_id", "question", "day", "day_from"]]
        except :
            return ("")

    def write(self):
        self.df.to_csv("questions.csv")

