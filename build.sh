#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initialize SQLite database
python database/create_database.py
python database/import_data.py

# Download NLP model and precompute semantic embeddings
python models/download_model.py
python database/precompute_embeddings.py
