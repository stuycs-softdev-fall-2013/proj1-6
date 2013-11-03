# database/authentication utils for Flask app

import pymongo
import config as conf

client = pymongo.MongoClient(conf.db)
db = client.SDJJbloginator

users = db.users
posts = db.posts

def posts():
	return posts.find()

def query(query):
	# returns dictionary with keys {"posts", "profiles", "comments"}
	# values are arrays containing query results for each
	# querying should be conducted with a regex match on the query string
    return

# post should contain author, title, data, subjet line, body, comments
def post(post):
	return posts.find({ "id" : post })

def userpost(username, post):
    temp = users.find_one({'username':username})['posts']
    postsize = posts.count()
    temp.extend([postsize + 1]) #new postid
    users.update({'username':username},{'$set':{'posts':temp}}) #adds the postid of new post in the user's list of postids theyve written
    posts.insert({'postid':postsize + 1,'user':username,'post':post,'comments':[]}) #adds new post

def usercomment(username, post, comment):
    temp = posts.find_one({'post':post})
    postnum = temp['postid']
    temp = temp['comments']
    temp = temp + [comment] 
    commentid = len(temp) - 1
    posts.update({'post':post},{'$set':{'comments':temp}}) #updates new comment to post's list of comments
    temp = [x for x in users.find({'username':username},fields={'_id':False})]
    temp = temp[0]['comments']
    temp.extend([postnum*31415 + commentid*27182]) #arbitrary for now
    users.update({'username':username},{'$set':{'comments':temp}}) #udates user's list of comments with arbitrary comment id


def deletepost(username, post): #is it neccessary to edit all postids proceeding the deleted post? 
    postnum = posts.find_one({'post':post})['postid']
    posts.remove({'post':post})
    temp = users.find_one({'username':username})['posts'].remove(postnum)
    users.update({'username':username},{'$set':{'comments':temp['posts']}})

def deletecomment(username, post, comment):
    temp = posts.find_one({'post':post})
    postnum = temp['postid']
    commentid = temp['comments'].index(comment)
    temp['comments'].remove(comment)
    posts.update({'post':post},{'$set':{'comments':temp['comments']}})
    temp = users.find_one({'username':username})
    temp['comments'].remove(postnum*31415 + commentid*27182)
    users.update({'username':username},{'$set':{'comments':temp['comments']}})


def profiles():
	return users.find()

# profile should contain username, date joined, comments
def profile(username):
	return users.find({ "username" : username })

def authenticate(username, passwordj):
	user = users.find_one({ "username" : username})
	if user is not None and password == user["password"]:
		return True
	return False

def login(username):
	session["username"] = username

def register(username,password):
    chk = users.find_one({'username':username})
    if(chk == None):
       users.insert({'username':username,'password':password,'posts':[],'comments':[]})
       return True
    else:
        return False