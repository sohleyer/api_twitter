from add_followers import *
from clean_friends import *
from utilitary import *


def add_followers(usr_name):
    """Follow the followers of the specified user.
    
    Args:
        usr_name (str): user name
    """
    api = get_API()

    # save followers in csv file
    save_followers(api, usr_name, ''.join(['followers_id_', usr_name, '.csv']))
    # import followers
    followers_list = import_data(''.join(['datas/followers_id_', usr_name, '.csv']), 'id')
    # follow
    follow(api, followers_list[0:50], 'friends_cache.csv')


# def add_followers_with_location(filename):
#     """Follow the followers filtered by location of the specified user.
    
#     Args:
#         usr_name (str): user name
#     """
#     api = get_API()

#     followers_list = import_data(''.join(['datas/followers_id_with_location/', filename]),'id')
#     follow(api, followers_list[450:500], 'friends_cache.csv')


def clean(my_id_str='Ruche_io',n):
    """Delete followed accounts (i.e. friends) which not follow back.
    
    Args:
        my_id_str (str): my accound id
        n (int): number of accounts to delete
    """
    api = get_API()

    save_followers(api, my_id_str, 'my_followers.csv')
    save_friends(api, my_id_str, 'my_friends.csv')
    friends_list = import_data('datas/my_friends.csv','id')
    usr_name_to_id(api, 'do_not_touch_id.csv')
    clean_(api, 'my_followers.csv', friends_list, n)


def follow_my_followers(my_id_str='Ruche_io'):
    """Follow accounts following me.
    
    Args:
        my_id_str (str): my accound id
    """
    api = get_API()

    save_followers(api, my_id_str, 'my_followers.csv')
    my_followers_list = import_data('datas/my_followers.csv','id')
    follow(api, my_followers_list, 'friends_cache.csv')


if __name__ == '__main__':
    #clean()
    #add_followers_with_location('followers_id_lillefrance_in_Lille.csv')
    add_followers('all0nsenfants')