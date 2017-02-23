""" Twitter miner to download the number of followers and friends for a list of accounts """

import tweepy
import time
import json
import logging
import sys
import datetime

__author__ = "Luis Natera"
__license__ = "GPL"
__version__ = "0.5"
__maintainer__ = "Luis Natera"
__email__ = "nateraluis@gmail.com"
__status__ = "Prototype"

# Twitter keys and accounts to analyse. Place them in config folder
KEYFILE = "config/mykey5.json"
accounts_file = open("config/accounts.txt", "r")
accounts = accounts_file.read().split(',')

# Load the twitter keys
def get_key(keyfile):
	try:
		with open(keyfile) as fin:
			key = json.load(fin)
	except FileNotFoundError as e:
		print ("Key not found")
		sys.exit(1)
	return key

# Authenticate in twitter
def authenticate(key):
	api = authenticate(key)
	return auth


# Main code to run
def main():
	# Twitter auth
	key = get_key(KEYFILE)
	auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
	auth.set_access_token(key['access_token'], key['access_secret'])
	api = tweepy.API(auth)

	# Generate a new file to save the data
	list = open ("Accounts_info" + ".csv", 'w')
	list.write("Id,Followers,Friends,Rate,Date" +' \n')

	# Get number of folowers and friends

	for account in accounts:
		try:
			user_followers = api.get_user(screen_name=account)
			no_followers = user_followers.followers_count
			user_friends = api.get_user(screen_name=account)
			no_friends = user_friends.friends_count
			if no_friends == 0:
				rate = 0
			else:
				rate = no_followers/no_friends
			list.write(account + "," + str(no_followers) + "," + str(no_friends) + "," + str(rate) + "," +  str(datetime.datetime.now()) +'\n')
			print (account + " done")
			# time.sleep(3)
		except Exception:
			pass

		"""except tweepy.TweepError:
			print ("Getting a time out, we will wait 15 minutes, grab a coffe!")
			time.sleep(60*15)
			print ("Startting again")
			for account in accounts:
				user_followers = api.get_user(screen_name=account)
				no_followers = user_followers.followers_count
				user_friends = api.get_user(screen_name=account)
				no_friends = user_friends.friends_count
				if no_friends == 0:
					rate = 0
				else:
					rate = no_followers/no_friends
				list.write(account + "," + str(no_followers) + "," + str(no_friends) + "," + str(rate)+ str(datetime.datetime.now()) +'\n')
				print (account + " done")
		except StopIteration:
				break
				#Solve it start again from the beginning

	# Download and write the data in the file
	while True:
		try:
			user = next(users)
			list.write(user.screen_name + "," + accountvar + '\n')
			count = count + 1
			print("Downloading: " + str(count) + "/" + str(no_followers))
			time.sleep(3)
		except tweepy.TweepError:
			print ("Getting a time out, wait 15 minutes :)")
			time.sleep(60*15)
			print ("Startting again")
			user = next(users)
			list.write(user.screen_name + "," + accountvar + '\n')
			count = count+1
			print("Downloading: " + str(count) + "/" + str(no_followers))
			time.sleep (3)
		except StopIteration:
			break
"""
# Execute the program
if __name__=="__main__":
	main()
