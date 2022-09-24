from newsapi import NewsApiClient
from PIL import Image
import requests
import os
from time import gmtime, strftime

newsapi = NewsApiClient(api_key=your_api)

#getting_query = input("Enter your query: ")
top_headlines = newsapi.get_top_headlines(country="in",category="health",language='en')

list_of_articles = top_headlines["articles"]


name = strftime("%Y-%m-%d_%H-%M-%S")
os.mkdir(name)

a = 0
for item in list_of_articles:
    if a!=10:
        print(item["title"])
        print(item["author"])
        print(item["description"])
        print(item["url"])
        

        #Downloading Image
        
        response = requests.get(item["urlToImage"])
        file = open(f"{name}/sample_image{a}.png", "wb")
        file.write(response.content)
        file.close()
        a+=1

        
        print("\n\n")
    else:
        break


print(f"Total values: {a}")