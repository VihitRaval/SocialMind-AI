"""
test_search.py
--------------

Test the complete AI-powered search pipeline.

Author: Vihit Raval
Project: SocialMind AI
"""

from services.search_service import SearchService


def print_header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_post(post, index):
    print(f"\nResult #{index}")
    print("-" * 70)
    print(f"Platform   : {post['platform']}")
    print(f"Author     : {post['author']}")
    print(f"Similarity : {post['similarity']:.4f}")
    print(f"Likes      : {post['likes']}")
    print(f"Comments   : {post['comments']}")
    print(f"Shares     : {post['shares']}")
    print(f"Content    : {post['content']}")
    print("-" * 70)


def main():

    print_header("SocialMind AI - Semantic Search Test")

    # Initialize search service
    service = SearchService()

    print(f"Total Posts Loaded : {service.total_posts()}")

    print("\nPlatform Statistics:")

    stats = service.platform_statistics()

    for platform, count in stats.items():
        print(f"{platform:<12} : {count}")

    print("\nSearch Engine Information")

    info = service.search_engine_information()

    print(f"Embedding Dimension : {info['embedding_dimension']}")
    print(f"Indexed Posts       : {info['total_posts']}")

    while True:

        print("\n")

        query = input("Enter Search Query (type 'exit' to quit): ").strip()

        if query.lower() == "exit":
            print("\nThank you for using SocialMind AI!")
            break

        results = service.search(query)

        if not results:
            print("\nNo relevant posts found.")
            continue

        print_header(f"Top {len(results)} Results")

        for index, post in enumerate(results, start=1):
            print_post(post, index)


if __name__ == "__main__":
    main()