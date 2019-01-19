import socket

import json
from class1 import USER, USERS_DF
from class2 import COUPLE_DF




couple = COUPLE_DF()
USERS_baza = USERS_DF()

print("1")

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()
    print("2")

    while True:
        print("3")

        conn, addr = sock.accept()

        print("4")

        with conn:
            print("5")

            while True:

                print("6")

                data = conn.recv(1024)
                if not data:
                    break

                USERS_baza.read()
                couple.read()

                data = data.decode("utf8")
                usr = json.loads(data)
                user = USER(usr["name"],usr["telegram_id"],key = usr["key"])
                if usr["key"]:
                    USERS_baza.us_append(user)
                    couple.us_append2(user)



                else:
                    USERS_baza.us_append(user)
                    couple.us_append1(user)

                USERS_baza.write()
                couple.write()

                USERS_baza.print()
                couple.print()



