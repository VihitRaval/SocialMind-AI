from sklearn.metrics.pairwise import cosine_similarity

from models.embedding import (
    generate_post_embeddings,
    generate_query_embedding
)


class SemanticSearch:

    def __init__(self, posts):

        self.posts = posts
        self.embeddings = generate_post_embeddings(posts)

    def search(self, query, top_k=10):
        """
        Perform semantic search.

        Args:
            query (str)

        Returns:
            Most relevant posts.
        """

        query_embedding = generate_query_embedding(query)

        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        results = []

        for index, score in enumerate(similarities):

            post = self.posts[index].copy()

            post["similarity"] = float(score)

            results.append(post)

        results.sort(
            key=lambda x: x["similarity"],
            reverse=True
        )

        return results[:top_k]