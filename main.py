import sys
import wget
import os
import requests
from bs4 import BeautifulSoup
import random
import errors
import pathlib


img_dir = None
# create the images folder
try:
	os.mkdir('images')
	img_dir = pathlib.path(__file__).resolve().parent
	img_dir = img_dir.joinpath("image")
except:
	pass

version = '0.1.0'


# colors
R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'  # white


def banner():
	os.system('cls')
	print(G + """
 ▄██
  ██
  ██▄████▄   ▄██▀██▄▀███▄███  ▄██▀██▄▀███▄███  ▄▄█▀██
  ██    ▀██ ██▀   ▀██ ██▀ ▀▀ ██▀   ▀██ ██▀ ▀▀ ▄█▀   ██
  ██     ██ ██     ██ ██     ██     ██ ██     ██▀▀▀▀▀▀
  ██▄   ▄██ ██▄   ▄██ ██     ██▄   ▄██ ██     ██▄    ▄
  █▀█████▀   ▀█████▀▄████▄    ▀█████▀▄████▄    ▀█████▀

""" + W)
	print('\n' + G + '[>]' + C + ' Created By : ' + W + 'borore')
	print(G + '[>]' + C + ' Version    : ' + W + version + '\n')


def network():
	try:
		conn = requests.get('http://www.google.com/', timeout=5)
		print(G + '[+]' + C + ' Checking Internet Connection...' + W, end='')
		print(G + ' Working' + W + '\n')
	except requests.ConnectionError:
		print(R + '[!]' + C +
			  ' You are Not Connected to the Internet...Quiting...' + W)
		sys.exit(0)


def random_user_agents():
	""" returns random user-agents from the list """
	UA = user_agent_list = [
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
		'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36']

	return random.choice(UA)


# root url
URL = 'https://wallpaperscraft.com/catalog/hi-tech/page2'


def get_markup(url):
	""" sends a request to get a markup """

	headers = {'User-Agent': random_user_agents()}

	try:
		markup = requests.get(url, headers=headers)
		if markup.status_code == 200:
			return markup.text
		else:
			raise errors.WallpaperExceptions(
				"""Page not found. Check the url and try again""")
	except:
		print("Try again")


def parse(markup):
	""" parse the markup and extracts the html 'a' tags
	which has the href links to the images
	"""
	soup = BeautifulSoup(markup, 'lxml')

	anchors_tags = soup.find_all('a', {'class': 'wallpapers__link'})

	hrefs = []

	for a_tag in anchors_tags:
		hrefs.append(a_tag.get("href"))

	return hrefs


def download(hrefs):
	""" download the images """

	download_url = 'https://images.wallpaperscraft.com/image/'

	links = []

	for i in hrefs:
		i = i.replace("/wallpaper/", '')
		link = download_url+f'{i}'+'_1920x1080.jpg'
		links.append(link)

	# change the dir to images
	os.chdir(img_dir)

	total = len(links)

	for link in links:
		print(link)
		try:
			wget.download(link)
			total -= 1
			print(f"\nDownload complete. {total} remaining")
		except KeyboardInterrupt:
			print(R+"please wait until the download completes"+W)
		except:
			print(C+"\nimage not found. Trying to download next\n"+W)
			continue


def search_catalog():
	category = input("Enter the category you want: (default is all): ")
	start_page = int(input("Enter page number to start with: (default => 1): "))
	end_page = int(input("Enter page number to end with: (default => 1): "))

	# root url for all images to be downloaded
	# based on their category
	catalog_url = 'https://wallpaperscraft.com/catalog/'

	if start_page > 0 and category != 'all':
		for i in range(start_page, end_page+1):
			# temporary url used to download page 1,2,3....
			temp_url = catalog_url+category+f'/page{i}'
			print("\nURL: ", temp_url)
			print("Page number: ", i)
			markup = get_markup(temp_url)
			hrefs = parse(markup)
			download(hrefs)
	else:
		markup = get_markup(URL)
		hrefs = parse(markup)
		download(hrefs)


if __name__ == '__main__':
	# download(parse(get_markup(URL)))

	try:
		banner()
		network()
		search_catalog()
	except KeyboardInterrupt:
		sys.exit(0)
