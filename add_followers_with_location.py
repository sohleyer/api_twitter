import csv
import tweepy
from auth.auth_audience import consumer_key_audience,consumer_secret_audience, access_token_audience, access_token_secret_audience


def save_followers_with_location(api, usr_str, location, number_of_page,
                                 filename=None, first_time=False, cursor=-1):
    if not filename:
        filename = ''.join(['followers_id_', usr_str, '_in_', location,'.csv'])
        print('Dans le fichier:', filename)

    followers_list =[]
    Cursor_pages = tweepy.Cursor(api.followers, id=usr_str, cursor=cursor).pages(number_of_page)

    for page in Cursor_pages:
        for follower in page:
            if location in follower.location:
                followers_list.append(follower.id_str)
                print(follower.name, ':', follower.location)

    print(Cursor_pages.next_cursor)
    print('number of followers of', usr_str,'in', location, ':', len(followers_list))

    with open(''.join(['datas/followers_id_with_location/', filename]), 'a', encoding='utf-8', errors='ignore') as csvfile:
        fieldnames = ['id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

        if first_time:
            writer.writeheader()

        for follower_id in followers_list:
            writer.writerow({'id': follower_id})
    print("data imported, csv writed")


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key_audience, consumer_secret_audience)
    auth.set_access_token(access_token_audience, access_token_secret_audience)

    api_audience = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #OK POUR LANCER
    first_time = False
    save_followers_with_location(api_audience, 'lillefrance', 'Lille', number_of_page=40, first_time=first_time, cursor=1535236984513649085)