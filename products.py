
import os #operation system
#讀取檔案
def read_file(filename): #設定參數以可以不限制單一檔名
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過並繼續到下一迴
			name, price = line.strip().split(',') #spilt用逗點分隔成小清單
			products.append([name, price])
	return products
	

#讓使用者輸入
def user_input(products): #將內容沒有的東西變成參數
	while True:
		name = input('請輸入商品名稱')
		if name == 'q':
			break
		price = input('請輸入價格')
		price = int(price)
		products.append([name, price]) #建立二維清單，直接在這建立小清單
	print(products)
	return products


#印出購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open (filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n') #寫入欄位名稱 逗點表示分欄
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #逗點表示分欄 #str型別轉換成字串 #加號兩邊的型別要一樣



def main(): #將執行程式碼存起來
	filename = 'products.csv'
	if os.path.isfile(filename): #檢查檔案在不在
		print('yeah!找到檔案')
		products = read_file(filename)		
	else:
		print('找不到檔案')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()
