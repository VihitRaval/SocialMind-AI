# 🚀 SocialMind AI

> **AI-Powered Social Media Post Fetching and Filtering System**

**Live Website:** [https://socialmind-ai-nmwg.onrender.com](https://socialmind-ai-nmwg.onrender.com)

An AI-powered web application that intelligently searches and filters social media posts from **Instagram**, **Facebook**, and **LinkedIn** using **Natural Language Processing (NLP)**, **Sentence Transformers**, and **Semantic Search** instead of traditional keyword matching.

---

## 📌 Project Overview

SocialMind AI is developed as part of an **Artificial Intelligence & Machine Learning Internship**.

The application fetches social media posts from multiple platforms, stores them in a SQLite database, generates semantic embeddings using Sentence Transformers, and retrieves the most relevant posts based on the user's search query.

---

# ✨ Features

- 🔍 AI-powered Semantic Search
- 🤖 Sentence Transformer Embeddings
- 📊 Cosine Similarity Ranking
- 💾 SQLite Database
- 🌐 Flask Web Application
- 📱 Responsive Bootstrap UI
- 🎯 Intelligent Search Results
- 📈 Search Statistics
- ⚡ Fast Search Performance
- 🛡️ Error Handling
- 🧩 Modular Project Architecture

---

# 🏗️ Technology Stack

| Category | Technology |
|-----------|------------|
| Backend | Python, Flask |
| Database | SQLite |
| AI / ML | Sentence Transformers, Scikit-learn |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript |
| Version Control | Git & GitHub |
| IDE | Visual Studio Code |

---

# 📂 Project Structure

```text
SocialMind-AI/

│── app.py
│── requirements.txt
│── README.md

├── data/
│   ├── instagram.json
│   ├── facebook.json
│   └── linkedin.json

├── database/
│   ├── create_database.py
│   ├── import_data.py
│   └── socialmind.db

├── models/
│   ├── embedding.py
│   └── semantic_search.py

├── services/
│   └── search_service.py

├── utils/
│   └── data_loader.py

├── templates/
│   ├── index.html
│   ├── results.html
│   ├── 404.html
│   └── 500.html

├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── images/

├── test_loader.py
└── test_search.py
```

---

# 🧠 AI Search Workflow

```text
User Search Query
        │
        ▼
Flask Application
        │
        ▼
Search Service
        │
        ▼
Semantic Search Engine
        │
        ▼
Sentence Transformer
        │
        ▼
Generate Embeddings
        │
        ▼
Cosine Similarity
        │
        ▼
Rank Results
        │
        ▼
Display Most Relevant Posts
```

---

# 📊 Dataset

The project contains mock datasets from three social media platforms:

| Platform | Posts |
|----------|------:|
| Instagram | 100 |
| Facebook | 100 |
| LinkedIn | 100 |

**Total Posts:** **300**

---

# ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/VihitRaval/SocialMind-AI.git
```

### Navigate to the project

```bash
cd SocialMind-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄️ Create Database

```bash
python database/create_database.py
```

---

# 📥 Import Dataset

```bash
python database/import_data.py
```

---

# ▶️ Run Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5001
```

---

# 🔎 Sample Search Queries

- AI Internship
- Machine Learning
- Artificial Intelligence
- Python Developer
- Deep Learning
- Data Science
- Software Engineer
- Backend Developer
- Frontend Developer

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home](screenshots/homepage.png)

### 🔍 Search Results

![Results](screenshots/search_results.png)

### ❌ No Results

![No Results](screenshots/no_results.png)

### ℹ️ About API

![About](screenshots/about_api.png)

### ❤️ Health API

![Health](screenshots/health_api.png)

---

# 🚀 Future Enhancements

- Live Social Media API Integration
- User Authentication
- Search History
- Advanced Filters
- Dark Mode
- Cloud Deployment
- Docker Support
- PostgreSQL Database
- Admin Dashboard
- Real-time Analytics

---

# 🎯 Learning Outcomes

During this project, I gained practical experience in:

- Flask Development
- Semantic Search
- Sentence Transformers
- Natural Language Processing
- SQLite Database Management
- Frontend Development
- Responsive Web Design
- AI Model Integration
- Service Layer Architecture
- Git & GitHub Workflow

---

# 👨‍💻 Author

**Vihit Raval**

Bachelor of Engineering (Information Technology)

Artificial Intelligence & Machine Learning Intern

GitHub: https://github.com/VihitRaval

---

# 📜 License

This project is developed for educational and internship purposes.
