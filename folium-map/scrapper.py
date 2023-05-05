from bs4 import BeautifulSoup

with open('indiatoday.html', 'r') as file:
    html = file.read()



soup= BeautifulSoup(html,'html.parser')

container = soup.find('div', {'class': 'story__grid'})

news_list=[]



for h in container.findAll('a'):
     if h.has_attr('title'):
         new_title= h.text
         if "india today" not in new_title:
              if "today" not in new_title:
                    if "news" not in new_title:
                     if "tak" not in new_title:
                             news_list.append(new_title)


print(news_list)

