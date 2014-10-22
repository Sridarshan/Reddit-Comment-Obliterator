import login
from getpass import getpass

def getComments(session, username):
	comments = session.get("http://www.reddit.com/user/%s/comments/.json" % username)
	comments_json = comments.json()
	return comments_json

def main():
	username = raw_input("Username : ")
	password = getpass("Password : ")
	session, response = login.login(username, password);
	if response.status_code == 200:
		print "Log in successful"
		delete = raw_input("Delete all comments (Y/N) : ")
		if "Y" in delete:
			comments_json = getComments(session, username)
			modhash = comments_json['data']['modhash']
			for x in comments_json['data']['children']:
				thing_id = x['data']['name']
				data = {
					'api_type':'json',
					'text':'',
					'thing_id':thing_id,
					'uh':modhash
				}
				r = session.post("http://www.reddit.com/api/editusertext", data = data)
				if r.status_code == 200:
					data = {
						'id': thing_id,
						'uh':modhash
					}
					r = session.post("http://www.reddit.com/api/del", data = data)
					if r.status_code == 200:
						print 'o'			
	else:
		print "Login Failed"

if __name__ == "__main__":
	main()
	


