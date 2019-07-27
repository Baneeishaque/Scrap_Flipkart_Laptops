import pandas as pd
from BeautifulSoup import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Programs/chromedriver.exe")

products = []  # List to store name of the product
prices = []  # List to store price of the product
ratings = []  # List to store rating of the product

driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', href=True, attrs={'class': '_31qSD5'}):
    name = a.find('div', attrs={'class': '_3wU53n'})
    price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    rating = a.find('div', attrs={'class': 'hGSR34'})
    # print("Rating is ")
    # print(rating)
    # print(rating.text)
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name': products, 'Price': prices, 'Rating': ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')
