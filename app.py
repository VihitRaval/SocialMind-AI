"""
app.py
-------

Main Flask application for SocialMind AI.

Author: Vihit Raval
Project: SocialMind AI
"""

from flask import Flask, render_template, request
from services.search_service import SearchService

# ---------------------------------------------------
# Flask Application
# ---------------------------------------------------

app = Flask(__name__)

print("=" * 60)
print("Starting SocialMind AI...")
print("=" * 60)

# ---------------------------------------------------
# Initialize AI Search Service
# ---------------------------------------------------

search_service = SearchService()

print("SocialMind AI is Ready!")
print("=" * 60)


# ---------------------------------------------------
# Home Page
# ---------------------------------------------------

@app.route("/")
def home():
    """
    Display the homepage.
    """
    return render_template("index.html")


# ---------------------------------------------------
# Search Route
# ---------------------------------------------------

@app.route("/search", methods=["POST"])
def search():

    # Get search query
    query = request.form.get("query", "").strip()

    # Empty query
    if not query:
        return render_template(
            "results.html",
            query=query,
            results=[],
            total_results=0
        )

    # AI Semantic Search
    results = search_service.search(query)

    return render_template(
        "results.html",
        query=query,
        results=results,
        total_results=len(results)
    )


# ---------------------------------------------------
# About Page (Optional)
# ---------------------------------------------------

@app.route("/about")
def about():

    info = search_service.search_engine_information()

    return {
        "Project": "SocialMind AI",
        "AI Model": "Sentence Transformers",
        "Embedding Dimension": info["embedding_dimension"],
        "Indexed Posts": info["total_posts"]
    }


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.route("/health")
def health():

    return {
        "status": "Running",
        "project": "SocialMind AI"
    }


# ---------------------------------------------------
# Run Flask
# ---------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )