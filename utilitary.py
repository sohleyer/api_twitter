import csv
import tweepy
from auth.auth_ruche import consumer_key,consumer_secret, access_token, access_token_secret
from constants import do_not_touch_usr, my_do_not_touch_usr


# ___get_API________________________________________________________


def get_API():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify = True)


#  ___import_datas____________________________________________________

def import_data(infile_name):
    followers_list = []
    with open(infile_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            followers_list.append(row['id'])
    return followers_list


#  ___usr_name_to_id____________________________________________________

def usr_name_to_id(api, usr_name_list, outfile_name):
    with open(''.join(['datas/', outfile_name]), 'w', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for usr_name in usr_name_list:
            print(usr_name)
            usr_object = api.get_user(usr_name)
            if usr_object.protected is False:
                writer.writerow({'id': usr_object.id_str})
    print('usr_name to id OK, file in the data folder')



if __name__ == '__main__':
    api = get_API()
    #usr_name_id(api, do_not_touch_usr+my_do_not_touch_usr, 'do_not_touch_id.csv')