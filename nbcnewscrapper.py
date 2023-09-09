# importing the required modules
from bs4 import BeautifulSoup as soup
import requests
import time

#News keywords for different genre.
keywords = ["", "/investigations","/politics", '/health',
             '/science''/?cid=eref:nbcnews:text','/culture-matters',
'/tech-media','/asian-america','/news/weather','/business','/nbcblk',
'/latino','/think','/health/coronavirus','/us-news','/health/coronavirus',
'/science/weird-science','/datagraphics''/nfl'] 

#Retriving the html page.
for key_words in keywords:
    url = "https://www.nbcnews.com"+str(key_words)
    try:
            httml = requests.get(url)
            httml_content = soup(httml.content, 'lxml')
            links = []
            path_tags_headlines = ["alacarte__text-wrapper","tease-card__info","wide-tease-item__info-wrapper flex-grow-1-m"]
            path_tags_links = ["alacarte__text-wrapper","tease-card__info","wide-tease-item__info-wrapper flex-grow-1-m","wide-tease-item__info-wrapper flex-grow-1-m"]
           
            for class_tags in path_tags_headlines:
                for link in httml_content.find_all("div" ,attrs={'class':class_tags}):
                    link.text
            
            for path_tag in path_tags_links:
                for news_link in httml_content.find_all("div", attrs={"class" : path_tag}):
                    links.append(news_link.find('a')['href'])
            print(f"getting the url: {url}")

            news_count  = 0

            #Getting the news info.
            for i in links:
                news_count+=1
                print("News : " ,news_count)
                page = requests.get(i)
                bsobl =soup(page.content,"lxml" )
                news_main = bsobl.find_all('article',attrs={ "class" : "styles_article__Ee5Ad article"} )

                for news in news_main:
                    heading = news.find("div", attrs= {"class": "article-hero-headline layout-grid-item grid-col-10-l"})
                    print("News Heading: :", heading.text)
                    datetime = news.find("div", attrs= {"class": "article-body__date-source"})
                    print("Date and Time  : " , datetime.text)
                    author = news.find("div", attrs= {"class":"article-inline-byline",
                                                    "data-activity-map" : "inline-byline-article-top"})
                    print("News author : " ,author.text)
                    print ("Link : " , i)   
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(5)
        print("Was a nice sleep, now let me continue...")

