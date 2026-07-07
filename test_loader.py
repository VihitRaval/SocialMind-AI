from utils.data_loader import *

print("=" * 60)

print("Total Posts")
print(len(get_all_posts()))

print("=" * 60)

print("Instagram Posts")
print(len(get_posts_by_platform("Instagram")))

print("=" * 60)

print("Facebook Posts")
print(len(get_posts_by_platform("Facebook")))

print("=" * 60)

print("LinkedIn Posts")
print(len(get_posts_by_platform("LinkedIn")))

print("=" * 60)

print("Python Search")
print(len(search_posts("Python")))

print("=" * 60)

print("Top 5 Liked Posts")

for post in get_top_liked_posts(5):
    print(post["author"], "-", post["likes"])