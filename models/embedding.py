"""
embedding.py
------------

This module is responsible for generating embeddings using
the Sentence Transformer model.

Author: Vihit Raval
Project: SocialMind AI
"""

import os
import torch
# Limit PyTorch CPU threads to 1 to prevent memory spikes and OOM crashes on Render
torch.set_num_threads(1)

from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Handles loading the Sentence Transformer model and
    generating embeddings for posts and search queries.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        """
        Initialize and load the transformer model.

        Args:
            model_name (str): Name of the Sentence Transformer model.
        """

        print("Loading Sentence Transformer model...")

        # Resolve path to local model if available
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        local_model_path = os.path.join(base_dir, "models", model_name)

        if os.path.exists(local_model_path):
            print(f"Loading model from local path: {local_model_path}")
            self.model = SentenceTransformer(local_model_path)
        else:
            print(f"Local path not found. Loading model from Hugging Face Hub: {model_name}")
            self.model = SentenceTransformer(model_name)

        print("Model loaded successfully.")

    def generate_post_embeddings(self, posts):
        """
        Generate embeddings for all social media posts.

        Args:
            posts (list): List of dictionaries containing posts.

        Returns:
            numpy.ndarray: Embedding vectors.
        """

        texts = []

        for post in posts:

            text = post.get("content", "").strip()

            texts.append(text)

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings

    def generate_query_embedding(self, query):
        """
        Generate embedding for a user's search query.

        Args:
            query (str)

        Returns:
            numpy.ndarray
        """

        query = query.strip()

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding

    def embedding_dimension(self):
        """
        Returns the embedding vector dimension.

        Returns:
            int
        """

        return self.model.get_sentence_embedding_dimension()

    def model_information(self):
        """
        Return model information.

        Returns:
            dict
        """

        return {
            "model_name": self.model._first_module().auto_model.name_or_path,
            "embedding_dimension": self.embedding_dimension()
        }