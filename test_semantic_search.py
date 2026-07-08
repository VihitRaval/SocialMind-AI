from utils.data_loader import get_all_posts

from models.semantic_search import SemanticSearch


posts = get_all_posts()

search_engine = SemanticSearch(posts)


query = input("Enter search query: ")


results = search_engine.search(query)


print("\n")

print("=" * 60)

print("Top Matching Posts")

print("=" * 60)


for index, post in enumerate(results, start=1):

    print(f"\nResult {index}")

    print(f"Platform : {post['platform']}")

    print(f"Author   : {post['author']}")

    print(f"Score    : {post['similarity']:.4f}")

    print(f"Content  : {post['content']}")

    print("-" * 60)