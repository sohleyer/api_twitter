import csv
import copy
import time
from add_followers import import_data
from constants import do_not_touch_usr, my_do_not_touch_usr


# ____save_followers (persons I follow)_____________________________________________________

def save_friends(api, usr_str, filename):
    friends_list = api.friends_ids(usr_str)
    print('number of friends:', len(friends_list))
    with open(''.join(['datas/', filename]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in friends_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


#  ___clean____________________________________________________

def clean(api, followers_file, friends_list):
    followers_list = import_data(''.join(['datas/', followers_file]))
    friends_to_delete = copy.copy(friends_list)

    for friend in do_not_touch_usr:
        if friend in friends_to_delete:
            friends_to_delete.remove(friend)

    for friend in my_do_not_touch_usr:
        if friend in friends_to_delete:
            friends_to_delete.remove(friend)

    for follower in followers_list:
        if follower in friends_to_delete:
            friends_to_delete.remove(follower)

    print('number of friends to delete:', len(friends_to_delete))
    for friend_to_delete_id in friends_to_delete:
        api.destroy_friendship(friend_to_delete_id)
        time.sleep(2)
        print('friendship deleted !')
    print('friends are clean !')