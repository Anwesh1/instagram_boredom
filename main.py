import requests
import time

#####################################################################################################

# Used the API from RapidAPI found at this link: https://rapidapi.com/logicbuilder/api/instagram-data1

#####################################################################################################

USERNAME = "" #enter your username
X_RAPIDAPI_KEY = "" #enter the rapidapi key 
X_RAPIDAPI_HOST = "" #enter the rapidapi host

def get_follow(string) -> list: #make sure to pass in a string that is either "followings" or "followers" 
    try:  
        if (string == "followers") or (string == "followings"):
            url = f"https://instagram-data1.p.rapidapi.com/{string}"
    except:
        print("String provided was not followers or followings")
        return
    
    querystring = {"username":USERNAME}
    headers = {
        'x-rapidapi-key': X_RAPIDAPI_KEY,
        'x-rapidapi-host': X_RAPIDAPI_HOST
    }
    list = []
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    for item in response["collector"]:
        list.append(item["username"])
    while response["has_more"] is True:
        time.sleep(15) #API breaks if there's too many calls
        querystring = {"username":USERNAME,"end_cursor":response["end_cursor"]}
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        for item in response["collector"]:
            list.append(item["username"])

    return list

def not_following_you_back(followers,followings) -> list: #make sure that 2 lists are passed to this function, one is for followers and the other is for followings

    not_following = []

    for item in followings:
        if item not in followers:
            not_following.append(item)

    return not_following

def you_not_following_back(followers,followings) -> list: #make sure that 2 lists are passed to this function, one is for followers and the other is for followings

    not_following = []

    for item in followers:
        if item not in followings:
            not_following.append(item)

    return not_following
