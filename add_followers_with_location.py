from constants import my_id
import csv
import time
import random

from utilitary import *
api=get_API()


# ____save_followers_____________________________________________________

def save_followers_with_location(api, usr_str, location, filename=None):
    if not filename:
        filename = ''.join(['followers_id_', usr_str, '_in_', location])
        print('Dans le fichier:', filename)
    followers_list = api.followers(usr_str)
    print('number of followers of', usr_str, ':', len(followers_list))
    with open(''.join(['datas/followers_id_with_location/', filename]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in followers_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


if __name__ == '__main__':
    save_followers_with_location(api, 'lillefrance', 'Lille')