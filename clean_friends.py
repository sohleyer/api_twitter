import copy
import time
from utilitary import *
import random


def save_friends(api, usr_str, filename):
    """Save followed accounts of a given user
    
    Args:
        api (tweepy API): tweepy API instance
        usr_str (str): user name
        filename (TYPE): output file name
    """
    friends_list = api.friends_ids(usr_str)
    print('number of friends:', len(friends_list))
    with open(''.join(['datas/', filename]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for follower_id in friends_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


def clean_(api, followers_file, friends_list, n_last_to_delete):
    """Delete followed accounts (i.e. friends) which not follow back.
    
    Args:
        api (tweepy API): tweepy API instance
        followers_file (str): followers file
        friends_list (list): friends list
        n_last_to_delete (int): number of accounts to delete
    """
    followers_list_id = import_data(''.join(['datas/', followers_file]),'id')
    friends_to_delete = copy.copy(friends_list)
    do_not_touch_id = import_data('datas/do_not_touch_id.csv', 'id')

    for friend_id in do_not_touch_id:
        if friend_id in friends_to_delete:
            friends_to_delete.remove(friend_id)

    for follower_id in followers_list_id:
        if follower_id in friends_to_delete:
            friends_to_delete.remove(follower_id)

    print('number of friends to delete:', len(friends_to_delete))

    for friend_to_delete_id in friends_to_delete[-n_last_to_delete:]:
        api.destroy_friendship(friend_to_delete_id)
        time.sleep(random.uniform(10,20))
        print('friendship deleted !')
    print('friends are clean !')