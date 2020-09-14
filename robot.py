import requests
from bs4 import BeautifulSoup

url = 'https://www.rottentomatoes.com/m/{}'

headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
print('Search your maovie ratings')
name = input('Enter the Movie name: ')

movie = requests.get(url.format(name))

soup = BeautifulSoup(movie.text, 'html.parser')

ratings = soup.find_all(class_="mop-ratings-wrap__row js-scoreboard-container")

score = soup.find(class_="mop-ratings-wrap__percentage")

print('Rotten Tamatos Ratings Is :')

print(name ,'::', score.text)



#print(ratings)
#print(soup)




