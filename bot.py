import sys
import time
from twython import Twython

APP_KEY = #your key
APP_SECRET = #your app key
OAUTH_TOKEN = #your token
OAUTH_TOKEN_SECRET = #you secret token

api = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

file = open("script.txt","r+")  
script = file.read()
words = script.splitlines()
file.close()

for i in words:
	try:
		api.update_status(status=i)
		time.sleep(1200)
	except:
		print "duplicate"
