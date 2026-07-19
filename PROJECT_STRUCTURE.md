# Project Structure

This document outlines the detailed folder layout and the architectural layers of the **SocialMind AI** search platform.

---

## Workspace Layout

```text
SocialMind-AI/
├── LICENSE                        # Project MIT License terms
├── README.md                      # Core documentation, instructions and overview
├── CHANGELOG.md                   # Logs changes made in each release
├── CONTRIBUTING.md                # Developer contribution guidelines
├── CODE_OF_CONDUCT.md             # Standard code of conduct terms
├── SECURITY.md                    # Project security and disclosure policy
├── PROJECT_STRUCTURE.md           # This structure document
├── RELEASE_NOTES.md               # v1.0.0 official submission release notes
├── app.py                         # Main Flask server entry point & router definitions
├── requirements.txt               # Main python packages list
├── runtime.txt                    # Runtimes configurations (specifies Python version on Render)
├── build.sh                       # Automation script for setup and deployments
├── render.yaml                    # Infrastructure blueprint configurations for Render
│
├── data/                          # Seeding Datasets
│   ├── facebook.json              # Mockup Facebook post feeds (100 posts)
│   ├── instagram.json             # Mockup Instagram post feeds (100 posts)
│   └── linkedin.json              # Mockup LinkedIn post feeds (100 posts)
│
├── database/                      # Relational & Vector DB components
│   ├── create_database.py         # DB Initializer script (creates SQLite schemas)
│   ├── import_data.py             # Data parser & importer (reads JSONs and saves to SQLite)
│   ├── precompute_embeddings.py   # Embedding precalculator script (saves to numpy vector file)
│   ├── socialmind.db              # Local SQLite database file (ignored in Git)
│   └── embeddings.npy             # Precomputed numpy embeddings arrays file (ignored in Git)
│
├── docs/                          # Internship Documentation
│   ├── User_Manual.md             # System manual and setup descriptions
│   ├── User_Manual.docx           # Word processor version of user manual
│   └── User_Manual.pdf            # PDF version of user manual
│
├── models/                        # ML Transformer Models
│   ├── download_model.py          # Script to download model offline from Hugging Face
│   ├── embedding.py               # Embedding controller class wrapper
│   ├── semantic_search.py         # Cosine Similarity search implementation
│   └── all-MiniLM-L6-v2/          # Pre-downloaded sentence transformer weights folder (ignored in Git)
│
├── screenshots/                   # Project Visual Captures (for README and documentation)
│   ├── README.md                  # Guides on capturing professional screenshots
│   ├── homepage.png               # Screenshot of application landing page
│   ├── search_results.png         # Screenshot of successful semantic searches
│   ├── no_results.png             # Screenshot of empty search fail-safes
│   ├── about_api.png              # Capture of About API JSON output response
│   └── health_api.png             # Capture of Health API JSON output response
│
├── services/                      # Business Logic Service Layer
│   └── search_service.py          # Search bridge layer connecting Flask web router to models
│
├── static/                        # Frontend Static Assets
│   ├── css/
│   │   └── style.css              # Custom styling sheet containing glassmorphic UI variables
│   ├── js/
│   │   └── main.js                # Form validators, spinners loader, guide filters
│   └── images/
│       └── logo.png               # SocialMind AI platform brand logo
│
├── templates/                     # Flask Render Views (HTML templates)
│   ├── index.html                 # Main landing dashboard UI
│   ├── results.html               # Semantic results rendering UI
│   ├── interview_guide.html       # Technical study portal UI
│   ├── 404.html                   # 404 Page Not Found error handler UI
│   └── 500.html                   # 500 Server Error fallback UI
│
├── utils/                         # Helper Utilities
│   ├── data_loader.py             # Database connections and fetch functions
│   └── interview_questions.py     # Questions and answers generator for the study portal
│
├── test_loader.py                 # Developer data utility sanity-check script
├── test_search.py                 # Interactive terminal search tester script
└── test_semantic_search.py        # Independent backend search test script
```

---

## Architectural Layers

1. **Presentation Layer (HTML/CSS/JS)**: Responsive web interfaces designed with standard styling guidelines, using Bootstrap 5 and customized style rules for glassmorphic elements. Main inputs are verified on the browser level with main scripts before being dispatched.
2. **Controller Layer (app.py)**: Acts as the router mapping web URL routes to services, handling query parameters, and capturing application-level exceptions (404 and 500 pages).
3. **Service Layer (services/search_service.py)**: Acts as a clean interface to load posts, call statistical metrics, and send clean inputs to the AI Search Engine.
4. **Machine Learning Model Layer (models/)**: Wraps `SentenceTransformer` to encode text into a dense vector index and calculates cosine alignment ranges via `scikit-learn` to rank items.
5. **Persistence Layer (database/)**: Manages data flow via `sqlite3`, loading data files, and indexing vectors inside numpy files to save startup execution overhead.
