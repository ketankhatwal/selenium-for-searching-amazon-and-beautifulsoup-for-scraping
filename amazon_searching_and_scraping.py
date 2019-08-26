from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

item = input("Item you want to find :-")

driver = webdriver.Chrome(r"C:\Webdrivers\chromedriver.exe")
driver.get("https://amazon.in")

search_item = driver.find_element_by_name("field-keywords")

search_item.send_keys(item)
search_item.send_keys(Keys.ENTER)

url=driver.current_url
#driver.quit()
headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
r=requests.get(url,headers=headers).text
soup=BeautifulSoup(r,"lxml")

for item in soup.find_all("div",class_="sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"):
    title=str(item.find("h2",class_="a-size-mini a-spacing-none a-color-base s-line-clamp-2").text.strip())
    link=str("www.amazon.in"+item.find("a",class_="a-link-normal a-text-normal")['href'])
    price=str(item.find("span",class_="a-offscreen").text)
    print(title)
    print(link)
    print(price)
    print()
    
