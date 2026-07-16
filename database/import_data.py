import os
import sqlite3
import json
from pathlib import Path

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
DATABASE_PATH = os.path.join(BASE_DIR, "database", "socialmind.db")

# JSON dataset paths
DATA_FILES = [
    os.path.join(BASE_DIR, "data", "instagram.json"),
    os.path.join(BASE_DIR, "data", "facebook.json"),
    os.path.join(BASE_DIR, "data", "linkedin.json")
]


def import_posts():
    # Connect to SQLite
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Clear existing posts to avoid duplicates on rebuilds
    cursor.execute("DELETE FROM posts")
    try:
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'posts'")
    except sqlite3.OperationalError:
        pass

    total_posts = 0

    for file_path in DATA_FILES:

        # Check if file exists
        if not Path(file_path).exists():
            print(f"❌ File not found: {file_path}")
            continue

        # Load JSON data
        with open(file_path, "r", encoding="utf-8") as file:
            posts = json.load(file)

        # Insert every post
        for post in posts:

            cursor.execute("""
                INSERT INTO posts (
                                    platform,
                                    author,
                                    author_type,
                                    profile_image,
                                    content,
                                    hashtags,
                                    posted_date,
                                    likes,
                                    comments,
                                    shares,
                                    post_url
                                )
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                            """, (
                                    post["platform"],
                                    post["author"],
                                    post["author_type"],
                                    f"https://ui-avatars.com/api/?name={post['author'].replace(' ', '+')}&background=2563eb&color=ffffff",
                                    post["content"],
                                    ",".join(post["hashtags"]),
                                    post["posted_date"],
                                    post["likes"],
                                    post["comments"],
                                    post["shares"],
                                    post["post_url"]
                                ))

            total_posts += 1

    # Save changes
    connection.commit()

    # Close database
    connection.close()

    print("=" * 50)
    print(f"✅ Successfully imported {total_posts} posts.")
    print("✅ Data is now stored in SQLite.")
    print("=" * 50)


if __name__ == "__main__":
    import_posts()