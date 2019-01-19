import pandas as pd



class USER:
    def __init__(self, name, telegram_id, id=None, key=None):
        self.name = name
        self.telegram_id = telegram_id
        self.key = key
        self.user_id = id


class USERS_DF:

    def __init__(self):
        self.df = pd.DataFrame(columns=["user_id", "name", "telegram_id", "key"])
        self.s4et4ik = len(self.df)

    def us_append(self, USER):
        id = "user_" + str(self.s4et4ik)
        key = USER.key or ("key_" + str(self.s4et4ik))
        self.s4et4ik = self.s4et4ik + 1

        USER.key = key
        USER.user_id = id
        dict = [id, USER.name, USER.telegram_id, USER.key]
        if len(self.df.loc[self.df.telegram_id == USER.telegram_id]) == 0:
            try:
                self.df.loc[len(self.df)] = dict
            except IOError:
                return ""
        #return (self)

    def print(self):
        print(self.df.head())

    def get_user(self, key):
        num = self.df.loc[self.df.key == key]
        return (num)

    def read(self):
        try:
            self.df = pd.read_csv("USERS.csv")[["user_id","name","telegram_id", "key"]]
        except IOError:
            return ""

    def write(self):
        self.df.to_csv("USERS.csv")

