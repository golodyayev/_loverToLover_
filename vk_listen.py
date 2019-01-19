from vk_class import server , user_vk, vk_df
from tockens import tocken_vk




vk = server(tocken_vk)

#vk.test()
vk.listen(user_vk, vk_df)
