# Changelog

All notable changes to the **SocialMind AI** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-07-19

This is the official v1.0.0 release of the SocialMind AI search engine, prepared as the final submission for the Artificial Intelligence & Machine Learning Internship.

### Added
- **AI-Powered Semantic Search**: Leverages Hugging Face's `sentence-transformers/all-MiniLM-L6-v2` to convert queries and posts into dense vector representations.
- **Cosine Similarity Ranking**: Computes similarity scores between search query embeddings and database post embeddings using `scikit-learn`'s `cosine_similarity`.
- **Precomputed Vector Index**: Added local embedding storage (`database/embeddings.npy`) via a precomputation script to speed up retrieval from milliseconds to microseconds.
- **Relational Seeding Layer**: Implemented SQLite schema (`database/create_database.py`) and data loaders (`database/import_data.py`) to seed 300 mockup social posts from Facebook, Instagram, and LinkedIn JSON records.
- **Flask Web Server**: Created backend controller routes for interactive searches, JSON metadata status endpoint (`/about`), and system health check status API (`/health`).
- **Interactive UI**: Built a responsive, glassmorphic layout using Bootstrap 5, featuring glowing backdrops, visual platform badges, interactive search history storage, and search-time statistics.
- **Technical Interview Guide**: Integrated an interactive guide page (`/interview-guide`) displaying core ML, database, and system design questions.
- **Comprehensive Project Standards**: Added MIT LICENSE, contributing guidelines, security policy, code of conduct, and release notes.

### Changed
- **Enriched About Metadata**: Augmented the `/about` endpoint to return project overview, developer credentials, internship domain, build date, and repo links.
- **Refined Layout Footers**: Standardized template footers across all screens to include social icons, email contact, copyright statements, active versions, and tech stack badges.
- **Production Build Process**: Configured `build.sh` script to automate dependencies update, database creation, data parsing, local model downloading, and vector indexing on Render.

### Cleaned
- **Workspace Sanitization**: Removed duplicate environments `.venv-1/` and `.venv-2/` and updated `.gitignore` rules for environment caches and database journals.
