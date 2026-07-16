import os
from sentence_transformers import SentenceTransformer

def download_model():
    model_name = "all-MiniLM-L6-v2"
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(base_dir, "models", model_name)
    
    print(f"Downloading model '{model_name}' to '{target_dir}'...")
    
    # Download and save the model locally
    model = SentenceTransformer(model_name)
    model.save(target_dir)
    
    print("✅ Model downloaded and saved locally successfully.")

if __name__ == "__main__":
    download_model()
