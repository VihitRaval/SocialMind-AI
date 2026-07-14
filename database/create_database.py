import os
import sqlite3


def create_database():
    # Connect to the SQLite database
    # If the database does not exist, it will be created automatically.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "database", "socialmind.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    connection = sqlite3.connect(db_path)

    # Create a cursor object
    cursor = connection.cursor()

    # Create the posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            platform TEXT NOT NULL,
            author TEXT NOT NULL,
            author_type TEXT,
            profile_image TEXT,
            content TEXT NOT NULL,
            hashtags TEXT,
            posted_date TEXT,
            likes INTEGER,
            comments INTEGER,
            shares INTEGER,
            post_url TEXT
        )
    """)

    # Save changes
    connection.commit()

    # Close the connection
    connection.close()

    print("✅ Database created successfully.")
    print("✅ 'posts' table is ready.")


if __name__ == "__main__":
    create_database()