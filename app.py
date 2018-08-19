# import  bs4
# import urllib.request
# markup=urllib.request.urlopen("https://www.flipkart.com/search?q=mobile&page=2").read()

# product_name,price,url,image_url=[],[],[],[]
# soup=bs4.BeautifulSoup(markup,"html.parser")
# for product in soup.find_all('div',class_='_1UoZlX'):
#     product_name.append(product.find('div',class_='_3wU53n'))
#     price.append(product.find('div',class_='_1vC4OE'))
#     url.append(product.find('a',class_='_31qSD5'))
#     image_url.append(product.find('img',class_='_1Nyybr'))

# for _ in range(len(product_name)):
#     print(product_name[_])
#     print(price[_])
#     print(url[_])
#     print(image_url[_])




with open('urls.txt','r') as f:
	for line in f:
		line = line.strip()
		if not line or line.startswith("#"):
			continue  # skip blank and commented out lines
		print(line)