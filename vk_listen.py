from vk_class import server , user_vk, vk_df
from tockens import tocken_vk



def listen():
    print("listen")

    vk = server(tocken_vk)
    vk.test()
    while True:
        #vk.test()
        try:
            vk.listen(user_vk, vk_df)
        except:
            print("some eror")

listen()
