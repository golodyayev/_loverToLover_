import socket
import json

sock = socket.socket()

sock.connect(("127.0.0.1", 10001))

USER = {"name":"masha", "telegram_id":"12223", "key" : "key_4"}

user = json.dumps(USER)


sock.sendall(user.encode("utf8"))

sock.close()

