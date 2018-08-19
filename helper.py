from models import ProductRecord
import bs4
import datetime


def save_database(title, product_url, price):

	value=ProductRecord(title, product_url, price,datetime.datetime.now())
	value.save()


def extract_values(markup):
	product_name,price,url,image_url=[],[],[],[]
	soup=bs4.BeautifulSoup(markup,"html.parser")
	for product in soup.find_all('div',class_='_1UoZlX'):
	    product_name.append(product.find('div',class_='_3wU53n'))
	    price.append(product.find('div',class_='_1vC4OE'))
	    url.append(product.find('a',class_='_31qSD5',href=True))
	    
	return product_name,price,url

def extract_save_data(product_name,price,url):

	for _ in range(len(product_name)):
		save_database(product_name[_],url[_],price[_])
