from bs4 import BeautifulSoup
import requests

print ("Which company would you like to see the stock information for: ")

print("1. NBK")
print("2. KHOT")
print("3. NAPESCO")
print("4. HCC")
print("5. ALKOUT")
print("0. Exit")
ch = input("Enter a number: ")
print()
while ch != '0':
	if ch >= str(1) and ch <=str(5):
		if int(ch) == 1:
			source = requests.get('https://english.mubasher.info/markets/BK/stocks/NBK/profile')
		elif int(ch)==2:
			source = requests.get('https://english.mubasher.info/markets/BK/stocks/KHOT/profile')
		elif int(ch)==3:
			source = requests.get('https://english.mubasher.info/markets/BK/stocks/NAPESCO/profile')
		elif int(ch)==4:
			source = requests.get('https://english.mubasher.info/markets/BK/stocks/HCC/profile')
		else:
			source = requests.get('https://english.mubasher.info/markets/BK/stocks/ALKOUT/profile')
		soup = BeautifulSoup(source.text, 'lxml')
		info = soup.find('div', class_='market-summary__block')
		for info in soup.find_all('div',class_='market-summary__block-row'):
			item = info.find('span', class_='market-summary__block-text').text
			item2 = info.find('span', class_='market-summary__block-number').text
			print(item+": "+item2)
		print()
	else:
  		print("Invalid input.")
	print("1. NBK")
	print("2. KHOT")
	print("3. NAPESCO")
	print("4. HCC")
	print("5. ALKOUT")
	print("0. Exit")
	print()
	ch = input("Enter a number: ")
	print()

