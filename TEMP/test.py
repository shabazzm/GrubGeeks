from dbModels import db, Recipe_Calories, User_Posts, User_Accounts, Post_Replies
from basic import app

app.app_context().push()
db.create_all()

person1 = User_Accounts('johnM','johnm@yahoo.com', 'hashval1', 'salt1', 'hashalgor')
person2 = User_Accounts('Suek','suek@yahoo.com', 'hashval2', 'salt2', 'hashalgor')
person3 = User_Accounts('Dank','dank@yahoo.com', 'hashval3', 'salt3', 'hashalgor')
person4 = User_Accounts('AmandaL','amandal@yahoo.com', 'hashval4', 'salt4', 'hashalgor')
person5 = User_Accounts('Jas','jas@yahoo.com', 'hashval5', 'salt5', 'hashalgor')



db.session.add_all([person1, person2, person3, person4, person5])
db.session.commit()

print(person1.user_id)
print(person2.user_id)
print(person3.user_id)
print(person4.user_id)
print(person5.user_id)

post1 = User_Posts(1,'ramen noodles are awesome', 'ssafjjshfjkdshfjkdshkjfhjdskhfjkdshajkfhdsjkfhjksdhfkjhdsjkfhsjkadhfkdhfjkashdfjkhdsa', 'date1')
post2 = User_Posts(5,'Kitchen Disaster', 'ssafjjshfjkdshfjkdshkjfhjdskhfjkdshajkfhdsjkfhjksdhfkjhdsjkfhsjkadhfkdhfjkashdfjkhdsa', 'date1')
post3 = User_Posts(5,'20 min meals', 'ssafjjshfjkdshfjkdshkjfhjdskhfjkdshajkfhdsjkfhjksdhfkjhdsjkfhsjkadhfkdhfjkashdfjkhdsa', 'date1')

db.session.add_all([post1, post2, post3])
db.session.commit()

print(post1.post_id)
print(post2.post_id)
print(post3.post_id)
