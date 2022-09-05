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
    
    
ACCOUNT_USERNAME = "Username"
ACCOUNT_PASSWORD = "Password"    
cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)



user_info(cl.username)
user_followers(cl.user_id)