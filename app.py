"""
app.py
-------

Main Flask application for SocialMind AI.

Author: Vihit Raval
Project: SocialMind AI
"""

from flask import Flask, render_template, request
from services.search_service import SearchService
import time

# =====================================================
# Flask Application
# =====================================================

app = Flask(__name__)

print("=" * 70)
print("🚀 Starting SocialMind AI...")
print("=" * 70)

# =====================================================
# Initialize Search Service
# =====================================================

search_service = SearchService()

print("✅ Search Service Initialized Successfully")
print("=" * 70)


# =====================================================
# Home Page
# =====================================================

@app.route("/")
def home():

    stats = search_service.platform_statistics()

    total_posts = search_service.total_posts()

    model_info = search_service.search_engine_information()

    return render_template(
        "index.html",
        total_posts=total_posts,
        platform_stats=stats,
        model_info=model_info
    )


# =====================================================
# Search Page
# =====================================================

@app.route("/search", methods=["POST"])
def search():

    query = request.form.get("query", "").strip()

    if not query:

        return render_template(
            "results.html",
            query="",
            results=[],
            total_results=0,
            search_time=0,
            model_name="all-MiniLM-L6-v2"
        )

    start_time = time.perf_counter()

    try:

        results = search_service.search(query)

    except Exception as error:

        print(f"Search Error : {error}")

        results = []

    end_time = time.perf_counter()

    search_time = round(end_time - start_time, 4)

    return render_template(

        "results.html",

        query=query,

        results=results,

        total_results=len(results),

        search_time=search_time,

        model_name="all-MiniLM-L6-v2"

    )


# =====================================================
# About API
# =====================================================

@app.route("/about")
def about():

    model = search_service.search_engine_information()

    return {

        "Project": "SocialMind AI",

        "Description": "AI-Powered Social Media Search Engine",

        "AI Model": "Sentence Transformers",

        "Embedding Dimension": model["embedding_dimension"],

        "Indexed Posts": model["total_posts"]

    }


# =====================================================
# Health Check API
# =====================================================

@app.route("/health")
def health():

    return {

        "status": "Running",

        "application": "SocialMind AI",

        "database": "SQLite",

        "ai_model": "all-MiniLM-L6-v2"

    }


# =====================================================
# Run Flask
# =====================================================

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5001,

        debug=True

    )