from add_followers import *
from clean_friends import *
from utilitary import *


def add_followers_main():
    api = get_API()

    save_followers(api, 'all0nsenfants', 'followers_id_AE.csv')
    followers_list = import_data('datas/followers_id_AE.csv')
    follow(api, followers_list[200:300], 'friends_cache.csv')


def clean_main():
    api = get_API()
    save_followers(api, 'Ruche_io', 'my_followers.csv')
    save_friends(api, 'Ruche_io', 'my_friends.csv')
    friends_list = import_data('datas/my_friends.csv')
    clean(api, 'my_followers.csv', friends_list[400:500])


def follow_my_followers_main():
    api = get_API()
    save_followers(api, 'Ruche_io', 'my_followers.csv')
    my_followers_list = import_data('datas/my_followers.csv')
    follow(api, my_followers_list, 'friends_cache.csv')


if __name__ == '__main__':
    follow_my_followers_main()