from auth.auth_ruche import consumer_key,consumer_secret, access_token, access_token_secret
from constants import my_id
import tweepy
import csv
import time


# ___get_API________________________________________________________


def get_API():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True)


# ____save_followers_____________________________________________________

def save_followers(api, usr_str, filename):
    followers_list = api.followers_ids(usr_str)
    print('number of followers of', usr_str, ':', len(followers_list))
    with open(''.join(['datas/', filename]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in followers_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


#  ___import_datas____________________________________________________

def import_data(infile_name):
    followers_list = []
    with open(infile_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            followers_list.append(row['id'])
    return followers_list


#  ___follow____________________________________________________

def follow(api, followers_id_list, outfile_name):
    if my_id in followers_id_list:
        followers_id_list.remove(my_id)
    with open(''.join(['datas/', outfile_name]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in followers_id_list:
            api.create_friendship(follower_id)
            time.sleep(2)
            print('friendship_created !')
            writer.writerow({'id': follower_id})


