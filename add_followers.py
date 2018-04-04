from constants import my_id
import csv
import time
import random


def save_followers(api, usr_str, filename):
    """Save followers of a user in a CSV file.
    
    Args:
        api (tweepy API): tweepy API instance
        usr_str (str): user string
        filename (str): filename to write
    """
    followers_list = api.followers_ids(usr_str)
    print('number of followers of', usr_str, ':', len(followers_list))
    with open(''.join(['datas/', filename]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in followers_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


def follow(api, followers_id_list, outfile_name):
    """Follow account in followers id list
    
    Args:
        api (tweepy API): tweepy API instance
        followers_id_list (list): list of id to follow
        outfile_name (str): output file name
    """
    if my_id in followers_id_list:
        followers_id_list.remove(my_id)
    with open(''.join(['datas/', outfile_name]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in followers_id_list:
            api.create_friendship(follower_id)
            time.sleep(random.uniform(10,20))
            print('friendship_created ! with', follower_id)
            writer.writerow({'id': follower_id})


