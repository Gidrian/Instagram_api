# Instagram_api
Here we'll be experimenting with the instagram API

# First we install the dependencies needed for this

pip install psycopg2

pip install instagrapi

postgres database commands:
CREATE TABLE accounts (
	user_id serial PRIMARY KEY,
	username VARCHAR ( 30 ) UNIQUE NOT NULL,
	full_name VARCHAR ( 50 ),
	is_private BOOLEAN NOT NULL,
	profile_pic_url TIMESTAMP NOT NULL,
        last_login TIMESTAMP 
);

'profile_pic_url': HttpUrl('https://instagram.fasu10-1.fna.fbcdn.net/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT9DSUsPLTMvSS1TvHxzOcjh2umOPnjbMTss09tFEkuxDg&oe=631B9627&_nc_sid=7bff83', scheme='https', host='instagram.fasu10-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg', query='stp=dst-jpg_s150x150&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT9DSUsPLTMvSS1TvHxzOcjh2umOPnjbMTss09tFEkuxDg&oe=631B9627&_nc_sid=7bff83'), 'profile_pic_url_hd': HttpUrl('https://instagram.fasu10-1.fna.fbcdn.net/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT-0PjBTLuAJu_1yU1caT6fqDLbfFXO9YJfyEqhEaWeQog&oe=631B9627&_nc_sid=7bff83', scheme='https', host='instagram.fasu10-1.fna.fbcdn.net', tld='net', host_type='domain', port='443', path='/v/t51.2885-19/281673026_535833524689116_5634914813728772541_n.jpg', query='stp=dst-jpg_s320x320&_nc_ht=instagram.fasu10-1.fna.fbcdn.net&_nc_cat=100&_nc_ohc=cY_cyPm77fsAX9Z1zxB&edm=ABfd0MgBAAAA&ccb=7-5&oh=00_AT-0PjBTLuAJu_1yU1caT6fqDLbfFXO9YJfyEqhEaWeQog&oe=631B9627&_nc_sid=7bff83'), 'is_verified': False, 'media_count': 36, 'follower_count': 47, 'following_count': 76, 'biography': '𝕊𝕖𝕥 𝕪𝕠𝕦𝕣 𝕙𝕖𝕒𝕣𝕥 𝕒𝕓𝕝𝕒𝕫𝕖 🔥\n𝕄𝕒𝕟𝕜𝕚𝕟𝕕 𝕨𝕒𝕤 𝕓𝕠𝕣𝕟 𝕠𝕟 𝕖𝕒𝕣𝕥𝕙 𝕓𝕦𝕥 𝕟𝕖𝕧𝕖𝕣 𝕞𝕖𝕒𝕟𝕥 𝕥𝕠 𝕕𝕚𝕖 𝕙𝕖𝕣𝕖🚀🪐\nℂ𝕠𝕞𝕡𝕦𝕥𝕖𝕣 𝕊𝕔𝕚𝕖𝕟𝕔𝕖 ⚡\n𝕌ℙ𝕋ℙ - ℕ𝕋𝕌𝕊𝕋', 'external_url': None, 'account_type': None, 'is_business': False, 'public_email': None, 'contact_phone_number': None, 'public_phone_country_code': None, 'public_phone_number': None, 'business_contact_method': 'UNKNOWN', 'business_category_name': None, 'category_name': 'Gamer', 'category': None, 'address_street': None, 'city_id': None, 'city_name': None, 'latitude': None, 'longitude': None, 'zip': None, 'instagram_location_id': None, 'interop_messaging_user_fbid': None}




import collections
from email import message
from instagrapi import Client

# cl = Client()

# cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# user_id = cl.user_id_from_username("Adr.bck")
# medias = cl.user_medias(user_id, 20)
# print(medias)

#Comment photo
def photo_comment(media_id, comment_str):
    comment = cl.media_comment(media_id, comment_str) #comment
    comment.dict()
    
#Reply to comment
def comment_reply(media_id, reply_str, comment_to_reply):
    comment = cl.media_comment(media_id, reply_str, replied_to_comment_id=comment_to_reply.pk)
    comment.dict()

#Scrape all comments, #Comments are ordered from newest to oldest
def comment_scrape(media_id):
    comments = cl.media_comments(media_id)
    print(comments)   

def comment_like(comment_pk): 
    cl.comment_like(comment_pk)
    
def comment_unlike(comment_pk): 
    cl.comment_unlike(comment_pk)    

def comment_pin(comment_pk): 
    cl.comment_pin(comment_pk)    
    
def comment_unpin(comment_pk): 
    cl.comment_unpin(comment_pk)    

def comment_delete(media_id, comment_pk):
    cl.comment_bulk_delete(media_id, comment_pk)
    
def user_info(username):
    info = cl.user_info_by_username(username).dict()
    print(info)
    
def user_followers(user_id):
    followers= cl.user_followers(user_id)
    print(followers)

def user_following(user_id):
    following= cl.user_following(user_id)
    print(following)    

def user_follow(user_id):
    cl.user_follow(user_id)

def user_unfollow(user_id):
    cl.user_unfollow(user_id)

def user_remove_follower(user_id):
    cl.user_remove_follower(user_id)
        
    
    
# Media types:
# Photo - When media_type=1
# Video - When media_type=2 and product_type=feed
# IGTV - When media_type=2 and product_type=igtv
# Reel - When media_type=2 and product_type=clips
# Album - When media_type=8

def media_get(user_id):
    media = cl.user_medias(user_id)
    print(media)
    
def media_where_user_tagged(user_id):
    medias = cl.usertag_medias(user_id)
    print(medias)
    
def media_delete(media):
    media_delete(media.pk)
    
def media_like(media):
    media_like(media.pk)
    
def media_unlike(media):
    media_unlike(media.pk) 
    
def media_pin(media):
    media_pin(media.pk)

def media_unpin(media):
    media_unpin(media.pk)

def stories_list(user_id):
    stories = cl.user_stories(user_id)
    print(stories)
    
def message_collect(): #collet messages from newest to oldest, at least the 20 firsts
    messages = cl.direct_threads(0)
    print(messages)

def message_pending_collect():
    messages_pending = cl.direct_pending_inbox()
    print(messages_pending)
    
def message_send(msg_string, thread):
    cl.direct_send(msg_string, thread_ids=[thread.id])
    
    
ACCOUNT_USERNAME = "Gidrianhck"
ACCOUNT_PASSWORD = "Gibbigalaxyyeah1."    
cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)







media_id = cl.media_id(cl.media_pk_from_url('https://www.instagram.com/p/CiEeModMRb7/')) #Post to comment


user_info('Adr.bck')
# collections = cl.collection_medias_by_name('Adr.bck')
# print(collections)
thread = cl.direct_threads(0)#(0)[0] #get last 10 messages if aplicable
# message = cl.direct_messages(thread.id)#[0] #Get the last 20 messages of a conversation
print(thread)
user_info(1941128470)
media_get(user_id)
user_followers(cl.user_id)
