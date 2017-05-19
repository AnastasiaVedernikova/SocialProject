import requests
import json
import pandas
#
# key = "AIzaSyAVC3j8XSx8PwNI5s7Bl-zS4WBYGGd2Zcw"
# key1 = "AIzaSyAbhxbui2ST5IcP0bmJ3to_XAgRdqe2N10"
# url1 = "https://www.youtube.com/watch?v=J8_Au4u1EKo"
# url2 = "https://www.googleapis.com/youtube/v3/search?part=snippet&location=37.42307,22.08427&locationRadius=50km&q=en&key="+key+"&type=video"
# url = "https://www.googleapis.com/youtube/v3/search?part=snippet&order=viewCount&publishedAfter=2015-06-08T00%3A00%3A00Z&key="+key+\
# "&type=video&maxResults=50&relevanceLanguage=en&videoDuration=short"
# newurl = "https://www.googleapis.com/youtube/v3/search?part=snippet&key="+key+\
# "&type=video&relevanceLanguage=en&videoDuration=short"
# content = json.loads(requests.get(url).text)
# print(content)
#
# def get_youtoube_content(content):
#     id = []
#     kind=[]
#     description = []
#     title = []
#     time =[]
#     for i in content["items"]:
#         a=i["id"]
#         b=i["snippet"]
#         id.append(a["videoId"])
#         kind.append(a["kind"])
#         description.append(b["description"])
#         title.append(b["title"])
#         time.append(b["publishedAt"])
#     data = pandas.DataFrame({"id":id, "type":kind,"description":description ,"title":title,"time":time })
#     return(data)
#
# data=get_youtoube_content(content)
# stat_url="https://www.googleapis.com/youtube/v3/videos?part=statistics&key="+key+"&maxResults=50&id="+str(list(data["id"])).replace("[","").replace("]","").replace("'","")
# stat_content = json.loads(requests.get(stat_url).text)
#
# def get_youtoube_content_stat(content):
#     id = []
#     commentCount=[]
#     dislikeCount = []
#     favoriteCount = []
#     likeCount=[]
#     viewCount=[]
#     for i in content["items"]:
#         id.append(i["id"])
#         b=i["statistics"]
#         commentCount.append(b["commentCount"])
#         dislikeCount.append(b["dislikeCount"])
#         favoriteCount.append(b["favoriteCount"])
#         likeCount.append(b["likeCount"])
#         viewCount.append(b["viewCount"])
#     data = pandas.DataFrame({"id":id, "commentCount":commentCount,"dislikeCount":dislikeCount ,"favoriteCount":favoriteCount,"likeCount":likeCount, "viewCount":viewCount })
#     return(data)
#
# data_stat=get_youtoube_content_stat(stat_content)
#
# data=pandas.merge(data, data_stat,"inner", on="id" )
#print(data)

import json
def YouTubeVideoInfo(video_id):
    """
    gets information about video from YouTube
    :param video_id: url of video in YouTube
    :return: print channel, title, number of likes, dislikes, views
    """
    api_key="AIzaSyAVC3j8XSx8PwNI5s7Bl-zS4WBYGGd2Zcw"
    InfUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=snippet"
    LikesUrl="https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&key="+api_key+"&part=statistics"
    Infdata = json.loads(requests.get(InfUrl).text)
    Likedata = json.loads(requests.get(LikesUrl).text)

    Idata=Infdata['items'][0]['snippet']
    title = Idata['title']
    channelTitle = Idata['channelTitle']

    Ldata=Likedata['items'][0]['statistics']
    likes = Ldata['likeCount']
    dislikes = Ldata['dislikeCount']
    views = Ldata['viewCount']

    print("Channel: "+channelTitle)
    print("Title: "+title)
    print("Likes: "+likes)
    print("Dislikes: "+dislikes)
    print("Views: "+views)


video_id = "J8_Au4u1EKo"
YouTubeVideoInfo(video_id)


