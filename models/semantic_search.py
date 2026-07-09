"""
semantic_search.py
------------------

This module performs AI-powered semantic search using
Sentence Transformers and Cosine Similarity.

Author: Vihit Raval
Project: SocialMind AI
"""

from sklearn.metrics.pairwise import cosine_similarity

from models.embedding import EmbeddingModel


class SemanticSearch:
    """
    Performs semantic search on social media posts.
    """

    def __init__(self, posts):
        """
        Initialize Semantic Search.

        Args:
            posts (list): List of social media posts.
        """

        self.posts = posts

        # Load embedding model only once
        self.embedding_model = EmbeddingModel()

        print("Generating embeddings for all posts...")

        self.embeddings = self.embedding_model.generate_post_embeddings(posts)

        print(f"Successfully generated embeddings for {len(posts)} posts.\n")

    def search(self, query, top_k=10, similarity_threshold=0.40):
        """
        Perform semantic search.

        Args:
            query (str)
            top_k (int)
            similarity_threshold (float)

        Returns:
            list
        """

        if not query.strip():
            return []

        # Generate embedding for query
        query_embedding = self.embedding_model.generate_query_embedding(query)

        # Calculate cosine similarity
        similarity_scores = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        results = []

        # Match every post with its similarity score
        for index, score in enumerate(similarity_scores):

            if score >= similarity_threshold:

                post = self.posts[index].copy()

                post["similarity"] = round(float(score), 4)

                results.append(post)

        # Sort by highest similarity
        results.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        return results[:top_k]

    def total_posts(self):
        """
        Returns total indexed posts.
        """

        return len(self.posts)

    def embedding_dimension(self):
        """
        Returns embedding dimension.
        """

        return self.embedding_model.embedding_dimension()

    def search_statistics(self):
        """
        Returns information about the search engine.
        """

        return {
            "total_posts": self.total_posts(),
            "embedding_dimension": self.embedding_dimension()
        }