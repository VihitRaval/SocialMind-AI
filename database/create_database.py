import sqlite3


def create_database():
    # Connect to the SQLite database
    # If the database does not exist, it will be created automatically.
    connection = sqlite3.connect("database/socialmind.db")

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