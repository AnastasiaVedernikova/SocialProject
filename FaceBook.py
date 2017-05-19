import requests
import facebook
# token=''
# graph = facebook.GraphAPI(token)
# lik = graph.get_connections(id='10153608167431961', connection_name='likes')
# print(lik)
# print("fkfjhga")

# graph = facebook.GraphAPI("897201b1635471ef69bb28b16cb5272c")
# profile = graph.get_object("me")
# friends = graph.get_connections("me", "friends")
# graph.put_object("me", "feed", message="I am writing on my wall!")
import requests

# def get_fb_token(app_id, app_secret):
#     payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
#     file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
#
#     print(file.text)


   # result = (file.text.split(" ")[0])
   # print file.text #to test the TOKEN
   # return result
# print(get_fb_token("1740576709290989", "897201b1635471ef69bb28b16cb5272c"))
#---------------------------------------------------
# token = "1740576709290989|fZbb70F1oiuE_sWqDuN3AuEFV34"
# graph = facebook.GraphAPI(token)
# post_id = "764357840398514"
# post = graph.get_object(id=post_id)
# print(post['likes'])
#---------------------------
#/10153608167431961?fields=likes.limit(0).summary(true)
#lik = graph.get_connections(id='1740576709290989', connection_name='likes')
# print(lik)
# profile = graph.get_object("me")
# friends = graph.get_connections("me", "friends")
# graph.put_object("me", "feed", message="I am writing on my wall!")


import requests
import facebook
token='1740576709290989|fZbb70F1oiuE_sWqDuN3AuEFV34'
graph = facebook.GraphAPI(token)
#likes
lik = graph.get_connections(id='764357840398514', connection_name='likes')

print("Post https://www.facebook.com/lviv.youth.center/photos/"
      "a.495970107237290.1073741829.467743623393272/764357840398514/?type=3&theater")
print("Likes: "+ str(len(lik['data'])))