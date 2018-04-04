from add_followers import *
from clean_friends import *
from utilitary import *


def add_followers_main(usr_name):
    api = get_API()

    save_followers(api, usr_name, ''.join(['followers_id_', usr_name, '.csv']))
    followers_list = import_data(''.join(['datas/followers_id_', usr_name, '.csv']), 'id')
    follow(api, followers_list[0:50], 'friends_cache.csv')

def add_followers_with_location_main(filename):
    api = get_API()

    followers_list = import_data(''.join(['datas/followers_id_with_location/', filename]),'id')
    follow(api, followers_list[450:500], 'friends_cache.csv')

def clean_main():
    api = get_API()

    save_followers(api, 'Ruche_io', 'my_followers.csv')
    save_friends(api, 'Ruche_io', 'my_friends.csv')
    friends_list = import_data('datas/my_friends.csv','id')
    usr_name_to_id(api, 'do_not_touch_id.csv')
    clean(api, 'my_followers.csv', friends_list, 50)


def follow_my_followers_main():
    api = get_API()

    save_followers(api, 'Ruche_io', 'my_followers.csv')
    my_followers_list = import_data('datas/my_followers.csv','id')
    follow(api, my_followers_list, 'friends_cache.csv')


if __name__ == '__main__':
    #clean_main()
    #add_followers_with_location_main('followers_id_lillefrance_in_Lille.csv')
    add_followers_main('all0nsenfants')