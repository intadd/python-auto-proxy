import requests
from bs4 import BeautifulSoup
import random

def proxy_server():
	main_server='https://www.us-proxy.org/'

	all_proxy=[]
	res=requests.get(main_server)
	html=BeautifulSoup(res.text,'html.parser')
	for tr_tag in html.find_all('tr'):
		if(tr_tag.get_text().count('.')==3):
			proxy_info = []
			for td_tag in tr_tag.find_all('td'):
				proxy_info.append(td_tag.get_text())
			
			proxy_ip=proxy_info[0]+':'+proxy_info[1]
		
			all_proxy.append(proxy_ip)

	

	# all_proxy array has 200 proxy server information
	return all_proxy


def main():


	all_proxy=proxy_server()	

	proxies={
		'http':all_proxy[random.randrange(0,20)]
       		}
	try:
		res=requests.get('http://intaddpy.com',proxies=proxies)
		print (res.status_code)

	except:
		print (proxies)




if(__name__=='__main__'):
	main()
