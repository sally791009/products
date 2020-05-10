products = []
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入價格')
	p = [name, price]
	products.append([name, price]) #建立二維清單，直接在這建立小清單
print(products)
products[0][0] #存取二維清單