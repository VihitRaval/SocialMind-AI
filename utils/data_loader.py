import sqlite3

DATABASE_PATH = "database/socialmind.db"


def get_connection():
    """
    Create and return a database connection.
    """
    return sqlite3.connect(DATABASE_PATH)


def get_all_posts():
    """
    Fetch all posts from the database.
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")
    posts = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return posts


def get_posts_by_platform(platform):
    """
    Fetch posts from a specific platform.
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM posts WHERE platform = ?",
        (platform,)
    )

    posts = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return posts


def search_posts(keyword):
    """
    Search posts using a keyword.
    (Temporary search before semantic AI search.)
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM posts
        WHERE
            content LIKE ?
            OR author LIKE ?
            OR hashtags LIKE ?
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        )
    )

    posts = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return posts


def get_top_liked_posts(limit=10):
    """
    Return the most liked posts.
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM posts
        ORDER BY likes DESC
        LIMIT ?
        """,
        (limit,)
    )

    posts = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return posts