from add_followers import *
from clean_friends import *
from utilitary import *
import random


def add_followers_main():
    api = get_API()

    save_followers(api, 'EnsembleStCloud', 'followers_id_EnsembleStCloud.csv')
    followers_list = import_data('datas/followers_id_EnsembleStCloud.csv','id')
    follow(api, followers_list[65:], 'friends_cache.csv')


def clean_main():
    api = get_API()

    save_followers(api, 'Ruche_io', 'my_followers.csv')
    save_friends(api, 'Ruche_io', 'my_friends.csv')
    friends_list = import_data('datas/my_friends.csv','id')
    usr_name_to_id(api, 'do_not_touch_id.csv')
    clean(api, 'my_followers.csv', friends_list, 100)


def follow_my_followers_main():
    api = get_API()

    save_followers(api, 'Ruche_io', 'my_followers.csv')
    my_followers_list = import_data('datas/my_followers.csv','id')
    follow(api, my_followers_list, 'friends_cache.csv')


if __name__ == '__main__':
    add_followers_main()