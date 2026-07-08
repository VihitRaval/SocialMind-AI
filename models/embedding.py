from sentence_transformers import SentenceTransformer

# Load the pre-trained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_post_embeddings(posts):
    """
    Generate embeddings for all social media posts.

    Args:
        posts (list): List of dictionaries containing posts.

    Returns:
        list: List of embedding vectors.
    """

    texts = [post["content"] for post in posts]

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


def generate_query_embedding(query):
    """
    Generate embedding for a user search query.

    Args:
        query (str): User search text.

    Returns:
        numpy.ndarray
    """

    embedding = model.encode(
        query,
        convert_to_numpy=True
    )

    return embedding