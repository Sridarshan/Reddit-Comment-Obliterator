import requests

def login(username, password):
	payload = {'api_type':'json', 'passwd':password,'rem':True,'user':username}
	client = requests.session()
	import time
	userAgent = 'Reddit-Python-Tutorial by /u/pupl43 ', int(time.time())
	client.headers = {'user-agent': userAgent}
	r = client.post("http://www.reddit.com/api/login", data = payload)
	return client, r

