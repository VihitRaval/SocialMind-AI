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

    # Empty Search
    if not query:

        return render_template(

            "results.html",

            query="",

            results=[],

            total_results=0,

            search_time=0,

            model_name="all-MiniLM-L6-v2",

            error_message="Please enter a valid search query."

        )

    start_time = time.perf_counter()

    error_message = None

    try:

        results = search_service.search(query)

        if len(results) == 0:

            error_message = (
                f'No matching posts were found for "{query}". '
                "Try searching for AI Internship, Machine Learning, or Python."
            )

    except Exception as error:

        print("=" * 60)
        print("SEARCH ERROR")
        print(error)
        print("=" * 60)

        results = []

        error_message = (
            "Something went wrong while processing your search. "
            "Please try again."
        )

    end_time = time.perf_counter()

    search_time = round(end_time - start_time, 4)

    return render_template(

        "results.html",

        query=query,

        results=results,

        total_results=len(results),

        search_time=search_time,

        model_name="all-MiniLM-L6-v2",

        error_message=error_message

    )

# =====================================================
# Technical Interview Guide Page
# =====================================================

@app.route("/interview-guide")
def interview_guide():
    from utils.interview_questions import get_interview_questions, get_categories
    questions = get_interview_questions()
    categories = get_categories()
    return render_template(
        "interview_guide.html",
        questions=questions,
        categories=categories
    )


# =====================================================
# About API
# =====================================================

@app.route("/about")
def about():

    model = search_service.search_engine_information()

    stats = search_service.platform_statistics()

    return {

        "project": "SocialMind AI",

        "version": "1.0.0",

        "description": "AI-Powered Social Media Post Fetching and Filtering System",

        "project_overview": "An AI-powered Social Media Search & Intelligent Filtering System that performs semantic search on social media posts using natural language processing.",

        "project_goal": "To demonstrate the application of Semantic Search and Sentence Transformers in retrieving and filtering social media data with high relevance and speed.",

        "build_date": "2026-07-19",

        "github_repository": "https://github.com/VihitRaval/SocialMind-AI",

        "live_demo": "https://socialmind-ai.onrender.com",

        "developer": {
            "name": "Vihit Raval",
            "role": "Artificial Intelligence & Machine Learning Intern",
            "education": "Bachelor of Engineering in Information Technology",
            "email": "vihit.raval@example.com",
            "github": "https://github.com/VihitRaval"
        },

        "internship_information": {
            "domain": "Artificial Intelligence & Machine Learning",
            "duration": "Summer 2026",
            "status": "Completed"
        },

        "backend": "Flask",

        "database": "SQLite",

        "ai_model": "Sentence Transformers (all-MiniLM-L6-v2)",

        "embedding_dimension": model["embedding_dimension"],

        "total_posts": model["total_posts"],

        "platforms": stats,

        "supported_platforms": [
            "Instagram",
            "Facebook",
            "LinkedIn"
        ],

        "technologies": [
            "Python",
            "Flask",
            "SQLite",
            "Sentence Transformers",
            "Scikit-learn",
            "HTML",
            "CSS",
            "Bootstrap",
            "JavaScript"
        ],

        "status": "Running"
    }


# =====================================================
# Health Check API
# =====================================================

@app.route("/health")
def health():

    try:

        # Get project statistics
        total_posts = search_service.total_posts()

        platform_stats = search_service.platform_statistics()

        model_info = search_service.search_engine_information()

        return {

            "status": "Healthy",

            "application": "SocialMind AI",

            "version": "1.0.0",

            "database": {

                "status": "Connected",

                "type": "SQLite"

            },

            "ai_model": {

                "name": "Sentence Transformers (all-MiniLM-L6-v2)",

                "embedding_dimension": model_info["embedding_dimension"],

                "status": "Loaded"

            },

            "posts": {

                "total": total_posts,

                "platforms": platform_stats

            },

            "server": {

                "status": "Running"

            }

        }

    except Exception as error:

        return {

            "status": "Unhealthy",

            "error": str(error)

        }, 500
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


# =====================================================
# Run Flask
# =====================================================

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    # Disable debug mode in production (only enable if FLASK_DEBUG=1/true)
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() in ("true", "1")
    
    app.run(
        host="0.0.0.0",
        port=port,
        debug=debug_mode
    )