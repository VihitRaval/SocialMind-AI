"""
search_service.py
-----------------

This module acts as a bridge between the Flask application
and the Semantic Search engine.

Author: Vihit Raval
Project: SocialMind AI
"""

from utils.data_loader import get_all_posts
from models.semantic_search import SemanticSearch


class SearchService:
    """
    Service layer responsible for loading posts,
    initializing the semantic search engine,
    and providing search functionality.
    """

    def __init__(self):
        """
        Load all posts and initialize Semantic Search.
        """

        print("Loading posts from database...")

        self.posts = get_all_posts()

        print(f"{len(self.posts)} posts loaded successfully.")

        print("Initializing Semantic Search Engine...")

        self.search_engine = SemanticSearch(self.posts)

        print("Search Engine is ready.\n")

    def search(self, query, top_k=10):
        """
        Perform semantic search.

        Args:
            query (str)
            top_k (int)

        Returns:
            list
        """

        return self.search_engine.search(
            query=query,
            top_k=top_k
        )

    def total_posts(self):
        """
        Return total number of posts.
        """

        return len(self.posts)

    def platform_statistics(self):
        """
        Count posts for each platform.
        """

        stats = {}

        for post in self.posts:

            platform = post["platform"]

            stats[platform] = stats.get(platform, 0) + 1

        return stats

    def search_engine_information(self):
        """
        Return AI model information.
        """

        return self.search_engine.search_statistics()