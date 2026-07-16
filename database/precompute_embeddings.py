import os
import numpy as np
import sqlite3
from sentence_transformers import SentenceTransformer

def precompute_embeddings():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "socialmind.db")
    model_dir = os.path.join(base_dir, "models", "all-MiniLM-L6-v2")
    output_path = os.path.join(base_dir, "database", "embeddings.npy")
    
    print("Precomputing embeddings...")
    print(f"Database path: {db_path}")
    print(f"Model path: {model_dir}")
    print(f"Output path: {output_path}")
    
    # 1. Fetch posts sorted by id
    if not os.path.exists(db_path):
        print("❌ Database file not found. Please run database creation/import first.")
        return
        
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT content FROM posts ORDER BY id ASC")
    posts = [row["content"] for row in cursor.fetchall()]
    connection.close()
    
    print(f"Found {len(posts)} posts in database.")
    if not posts:
        print("❌ No posts found to embed.")
        return
        
    # 2. Load the model from local directory
    if not os.path.exists(model_dir):
        print("❌ Local model not found. Downloading it first...")
        model = SentenceTransformer("all-MiniLM-L6-v2")
        model.save(model_dir)
    else:
        model = SentenceTransformer(model_dir)
        
    # 3. Generate embeddings
    print("Encoding post contents...")
    embeddings = model.encode(
        posts,
        convert_to_numpy=True,
        show_progress_bar=True
    )
    
    # 4. Save numpy array
    np.save(output_path, embeddings)
    print(f"✅ Precomputed embeddings shape: {embeddings.shape}")
    print("✅ Precomputed embeddings saved successfully.")

if __name__ == "__main__":
    precompute_embeddings()
