"""
utils/interview_questions.py
-----------------------------

This module provides a pre-defined set of 52 professional interview questions
and detailed answers relating to the SocialMind AI project.
"""

def get_categories():
    return [
        {
            "id": "ai",
            "name": "Artificial Intelligence",
            "icon": "bi-cpu-fill"
        },
        {
            "id": "flask",
            "name": "Flask",
            "icon": "bi-terminal-fill"
        },
        {
            "id": "database",
            "name": "Database",
            "icon": "bi-database-fill"
        },
        {
            "id": "deployment",
            "name": "Deployment",
            "icon": "bi-cloud-arrow-up-fill"
        },
        {
            "id": "git",
            "name": "Git & GitHub",
            "icon": "bi-git"
        },
        {
            "id": "python",
            "name": "Python",
            "icon": "bi-filetype-py"
        },
        {
            "id": "engineering",
            "name": "Software Engineering",
            "icon": "bi-gear-wide-connected"
        }
    ]

def get_interview_questions():
    return [
        # ==========================================
        # ARTIFICIAL INTELLIGENCE
        # ==========================================
        {
            "id": 1,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "What is Semantic Search?",
            "easy_explanation": "Imagine walking into a library and asking for 'something that makes me happy'. A standard index card lookup would only find books with the word 'happy' in the title. Semantic search, however, understands you want lighthearted fiction, comedy, or uplifting memoirs, even if the word 'happy' is never explicitly used. It searches by meaning instead of exact words.",
            "technical_explanation": "Semantic search leverages Natural Language Processing (NLP) and vector embeddings to capture the contextual and semantic intent behind a user query. Instead of relying on Lexical Matching (TF-IDF, BM25), the search engine converts input text into high-dimensional dense vectors using deep learning models. It then computes distance metrics, like Cosine Similarity, against a database of document vectors to retrieve records closest in semantic space.",
            "project_example": "In SocialMind AI, searching for 'Machine Learning' will retrieve posts containing 'Neural Networks', 'Deep Learning', or 'AI model parameters' even if they don't explicitly contain the phrase 'Machine Learning', because the Sentence Transformer maps these concepts to similar coordinate positions.",
            "real_world_usage": "Google Search, Spotify playlist search, and e-commerce platforms use semantic search to display correct results for synonyms or conversational search queries.",
            "best_practices": "Keep your search embeddings updated as new domain terms emerge, and select an appropriate similarity threshold (e.g., 0.40) to filter out unrelated noise.",
            "interview_tip": "Clearly differentiate lexical search from semantic search, highlighting that lexical search fails at processing synonyms and search intent, while semantic search excels at both."
        },
        {
            "id": 2,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "What are Embeddings?",
            "easy_explanation": "Think of embeddings as translating human words into a list of coordinates or 'numbers' that represent their features. For example, if we rate words based on 'is it an animal?', 'can it fly?', and 'is it small?', a canary might be represented as [0.9, 0.9, 0.8], while a submarine might be represented as [0.0, 0.0, 0.0]. These lists of numbers represent concepts in a way computers can mathmatically compare.",
            "technical_explanation": "Embeddings are dense, low-dimensional, continuous vector representations of discrete items (like tokens, sentences, or images) in a high-dimensional vector space. Deep learning models map features to n-dimensional space (e.g., 384 dimensions for all-MiniLM-L6-v2) such that items with semantic similarity are clustered close to one another. Each dimension captures an abstract semantic property learned during pre-training.",
            "project_example": "In `models/embedding.py`, we use `self.model.encode(texts)` to convert post contents into 384-dimensional floating point arrays using Sentence Transformers.",
            "real_world_usage": "Embeddings are used in recommendation systems (like Netflix suggesting movies), machine translation, clustering algorithms, and Generative AI prompt context retrieval (RAG).",
            "best_practices": "Always use the exact same embedding model for both indexing your database and encoding user search queries; otherwise, the vector spaces will not align.",
            "interview_tip": "Describe embeddings as a form of dimensionality reduction that maps categorical variables (like text) into continuous vector spaces while preserving their semantic relationships."
        },
        {
            "id": 3,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "Why Sentence Transformers?",
            "easy_explanation": "If standard AI models look at single words one by one, Sentence Transformers look at the entire sentence as a whole. It's like reading a full sentence in one go to understand the overall context, rather than trying to guess the meaning by adding up individual words.",
            "technical_explanation": "Sentence Transformers are a modification of the pre-trained BERT network using Siamese and triplet network structures to generate highly descriptive, fixed-size sentence embeddings. While vanilla BERT requires passing both sentences into the model to calculate similarity (which is computationally expensive), Sentence Transformers generate embeddings for each sentence independently, allowing similarity calculation using simple cosine operations.",
            "project_example": "In `models/embedding.py`, we load the pre-trained `all-MiniLM-L6-v2` model from Hugging Face or a local directory to efficiently encode social media posts.",
            "real_world_usage": "Sentence Transformers are widely used for document clustering, duplicate question detection, semantic search, and clustering customer support tickets.",
            "best_practices": "Utilize local caching or precomputed embeddings when possible to minimize startup latency and GPU/CPU computational loads during runtime.",
            "interview_tip": "Highlight that Sentence Transformers resolve the scaling bottleneck of vanilla BERT, reducing the search computational complexity from O(N^2) comparisons to O(N) by generating reusable, independent sentence vectors."
        },
        {
            "id": 4,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "What is Cosine Similarity?",
            "easy_explanation": "Imagine two arrows pointing from the same spot. If they point in the exact same direction, the similarity is 1. If they are at right angles, it's 0. If they point in opposite directions, it's -1. Cosine similarity measures the angle between these arrows (vectors) to determine how closely their meanings match.",
            "technical_explanation": "Cosine similarity measures the cosine of the angle between two non-zero vectors in an inner product space. It is calculated as the dot product of the vectors divided by the product of their magnitudes (Euclidean lengths). The value ranges from -1 to 1, where 1 indicates identical directionality, 0 indicates orthogonality, and -1 indicates opposite directionality. For text embeddings, it reflects similarity in meaning regardless of text length.",
            "project_example": "In `models/semantic_search.py`, we import `cosine_similarity` from `sklearn.metrics.pairwise` and compute similarity scores between the query vector and all post vectors.",
            "real_world_usage": "Plagiarism detectors, document recommendation engines, and collaborative filtering systems use cosine similarity to compare user behavior and document overlap.",
            "best_practices": "Normalize vectors beforehand if performing high-frequency similarity math, or use built-in library functions like scikit-learn's optimized pairwise calculators.",
            "interview_tip": "Mention that cosine similarity is preferred over Euclidean distance for text search because it is scale-invariant; it measures direction rather than magnitude, ensuring longer documents aren't penalized."
        },
        {
            "id": 5,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "Difference between Semantic Search and Keyword Search?",
            "easy_explanation": "Keyword search is like looking for a specific needle in a haystack—it only succeeds if you search for the exact shape of that needle. Semantic search looks for anything that performs the needle's job, like a pin or a nail, because it understands the context of what you are trying to do.",
            "technical_explanation": "Keyword search (lexical search) searches for exact literal matches of query words in documents using inverted indices (like Elasticsearch or Lucene). It struggles with synonyms, polysemy, and grammatical variations. Semantic search maps both query and documents into a shared continuous vector space, allowing it to retrieve documents that share conceptual meaning even if they share zero vocabulary words with the query.",
            "project_example": "Our `utils/data_loader.py` contains a basic keyword search (`LIKE ?` SQL query), whereas `models/semantic_search.py` implements the AI semantic search. The latter returns much more relevant results for conceptual queries.",
            "real_world_usage": "E-commerce sites transition from keyword matching to hybrid/semantic systems to prevent zero-result pages when users type synonyms (e.g., 'sneakers' vs. 'running shoes').",
            "best_practices": "Combine both in a 'hybrid search' setup, using lexical search for exact brand names/SKUs and semantic search for abstract descriptions.",
            "interview_tip": "Explain that keyword search works well for precise, exact-match queries (like names, IDs, or model numbers), whereas semantic search is superior for conceptual, natural language queries."
        },
        {
            "id": 6,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "What is Vector Search?",
            "easy_explanation": "Think of vector search as finding the closest houses on a map. If you are standing at a particular coordinate, vector search calculates the distance to all other houses and lists the ones that are closest to you.",
            "technical_explanation": "Vector search is the process of querying a database of high-dimensional vectors to find the 'Nearest Neighbors' (K-Nearest Neighbors/KNN) relative to a query vector. This is done by measuring distance in multi-dimensional space. For small datasets, flat brute-force searching is sufficient; for larger scales, Approximate Nearest Neighbor (ANN) algorithms (like HNSW, IVF) are utilized for speed.",
            "project_example": "In SocialMind AI, `SemanticSearch.search()` conducts a flat vector search by computing cosine similarity scores between the query vector and the precomputed post embeddings stored in database.",
            "real_world_usage": "Vector databases like Pinecone, Milvus, Qdrant, and pgvector are built to execute vector search queries across millions of embeddings in milliseconds.",
            "best_practices": "Precompute and serialize embeddings (like we do in `embeddings.npy`) instead of generating them on the fly for every search request, reducing search latency significantly.",
            "interview_tip": "Differentiate between flat vector search (exact linear scan) and Approximate Nearest Neighbor (ANN) search, explaining that ANN trades off minor accuracy for speed improvements in massive datasets."
        },
        {
            "id": 7,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "How are embeddings generated?",
            "easy_explanation": "An AI model reads through text, breaks it down into small parts, evaluates the grammatical rules and connections, and translates all of that context into a unique list of numbers that act like a digital fingerprint.",
            "technical_explanation": "Embedding generation starts with text tokenization, where text is split into sub-word tokens. These tokens are fed into a neural network (typically a Transformer encoder). The model passes tokens through multiple self-attention layers to capture relationships between words. The output hidden states are then aggregated (typically via mean pooling or CLS token extraction) to produce a single dense vector.",
            "project_example": "In `models/embedding.py`, the `EmbeddingModel` inputs text strings to `self.model.encode(texts, convert_to_numpy=True)`, which returns a 2D numpy array of embeddings.",
            "real_world_usage": "Generating embeddings is the core pipeline step in building custom Search Engines, Recommendation Engines, and training Large Language Models.",
            "best_practices": "Ensure input text is cleaned (removing excess white space or HTML tags) and truncated to the model's maximum context length (typically 256 or 512 tokens for sentence models) to avoid losing information.",
            "interview_tip": "Be ready to describe the 'mean pooling' step—explaining how the model combines individual token vectors from the transformer layers into a single sentence-level vector."
        },
        {
            "id": 8,
            "category": "Artificial Intelligence",
            "category_id": "ai",
            "question": "How does ranking work in semantic search?",
            "easy_explanation": "Imagine grading test papers. The teacher compares each paper to the answer sheet, assigns a percentage grade, sorts the papers from highest to lowest score, and throws out any papers that scored below a failing mark.",
            "technical_explanation": "Ranking involves evaluating similarity scores (e.g., Cosine Similarity) between the query embedding and database vectors, sorting the records in descending order, and filtering out results below a minimum threshold score (e.g., 0.40) to maintain quality. The top-k sorted items are returned as the final results.",
            "project_example": "In `models/semantic_search.py` lines 80-99, we compute similarity scores, filter out scores below `similarity_threshold=0.40`, sort the remaining items in descending order of similarity, and return the top `k` results.",
            "real_world_usage": "Streaming services rank media recommendations; search engines rank web pages, blending semantic relevance scores with user interaction metrics.",
            "best_practices": "Iterate on the similarity threshold based on user feedback. Too high a threshold results in empty searches, while too low includes irrelevant content.",
            "interview_tip": "Explain that ranking can be fine-tuned. You can mix semantic similarity scores with popularity scores (like likes or views) to create a hybrid ranking system."
        },

        # ==========================================
        # FLASK
        # ==========================================
        {
            "id": 9,
            "category": "Flask",
            "category_id": "flask",
            "question": "Why Flask?",
            "easy_explanation": "Flask is like a minimalist starter kit for building websites. Unlike massive frameworks that force you to build things their way, Flask gives you a simple core and lets you choose your own tools for databases, forms, and AI helpers.",
            "technical_explanation": "Flask is a WSGI micro-framework written in Python. It does not require specific tools or libraries, meaning it has no database abstraction layer, form validation, or pre-built components. It relies on the Werkzeug WSGI toolkit and the Jinja2 template engine, giving developers complete architectural freedom to structure applications, making it ideal for integration with custom ML pipelines.",
            "project_example": "We use Flask in `app.py` because it allows us to easily bridge the simple database queries and python-based Sentence Transformer code without the unnecessary overhead of Django.",
            "real_world_usage": "Companies like Pinterest, LinkedIn, and Netflix use Flask to build lightweight microservices and API gateways due to its low overhead and simplicity.",
            "best_practices": "Use the Application Factory pattern to construct your Flask application context, preventing circular imports and simplifying testing workflows.",
            "interview_tip": "Define Flask as a micro-framework and explain that its core philosophy is to provide an extensible foundation, leaving database and authentication choices to the developer."
        },
        {
            "id": 10,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is Flask Routing?",
            "easy_explanation": "Routing is like a traffic guide for web addresses. When a user types a URL like '/about' or '/search' into their browser, the routing system directs that request to the specific Python function in charge of rendering that page.",
            "technical_explanation": "Routing in Flask maps specific client request URLs to corresponding python handler functions (referred to as view functions). This mapping is established using the `@app.route()` decorator. Flask handles HTTP methods (GET, POST, etc.) and URL parameters dynamically via route configuration.",
            "project_example": "In `app.py`, `@app.route('/')` maps to the home page, while `@app.route('/search', methods=['POST'])` maps search submissions to the `search()` view function.",
            "real_world_usage": "Every web app uses routing to define their API endpoints (e.g. `/api/v1/users`) and web page URLs (e.g. `/dashboard`).",
            "best_practices": "Ensure routes specify the exact HTTP methods they handle (e.g. `methods=['GET', 'POST']`) and handle trailing slashes consistently.",
            "interview_tip": "Explain that Flask routing uses Werkzeug's routing map underneath, resolving dynamic URL variables using converters like `<int:id>` or `<string:name>`."
        },
        {
            "id": 11,
            "category": "Flask",
            "category_id": "flask",
            "question": "What are Blueprints in Flask?",
            "easy_explanation": "Imagine building a large house. Instead of putting all the blueprints on a single giant sheet of paper, you draw the kitchen, bedrooms, and bathrooms on separate sheets to make the work organized and clean.",
            "technical_explanation": "Blueprints are modular structures in Flask used to organize application components. A Blueprint defines routes, templates, and static directories independently from the main application object. It is then registered to the application in the factory function, facilitating clean separation of concerns and component reusability.",
            "project_example": "While SocialMind AI is currently single-module, a larger version would separate API routes (e.g., `/api/posts`) and Frontend pages (e.g., `/interview-guide`) into distinct Blueprints.",
            "real_world_usage": "Large-scale Flask apps use Blueprints to partition user authentication, billing modules, dashboard pages, and administrative portals.",
            "best_practices": "Use Blueprints in any application with more than 10 routes to prevent a monolithic, unmaintainable main file.",
            "interview_tip": "Describe Blueprints as a way to construct modular applications, highlighting that they record operations to be registered on an application later, enabling lazy application construction."
        },
        {
            "id": 12,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is Jinja2?",
            "easy_explanation": "Jinja2 is like a smart fill-in-the-blank template for HTML files. Instead of writing a different HTML file for every database record, you write one layout and use placeholder codes like `{{ variable }}` to let Python fill in the details.",
            "technical_explanation": "Jinja2 is a fast, expressive, and extensible templating engine for Python, integrated directly into Flask. It compiles templates into Python code. Key features include variable interpolation using `{{ ... }}`, control statements like `{% for ... %}` and `{% if ... %}`, and template inheritance (extends/block). It also automatically escapes HTML input to prevent Cross-Site Scripting (XSS).",
            "project_example": "In `templates/index.html`, we use Jinja syntax `{{ total_posts }}` and `{{ platform_stats['Instagram'] }}` to print statistics loaded dynamically from the SQLite database.",
            "real_world_usage": "Generating dynamic web pages, building HTML email templates, and auto-generating config files in systems engineering.",
            "best_practices": "Keep logic in templates to a minimum. Do database queries and data transformations in Python, passing ready-to-display variables to Jinja.",
            "interview_tip": "Mention Jinja2's auto-escaping security feature. This blocks XSS attacks by default, converting symbols like `<` and `>` into HTML entities."
        },
        {
            "id": 13,
            "category": "Flask",
            "category_id": "flask",
            "question": "How do Flask Templates work?",
            "easy_explanation": "Templates separate visual design from logic. Python handles the math and databases, and then passes the finished numbers to an HTML template file that handles how it looks, keeping the code clean.",
            "technical_explanation": "Flask template rendering relies on the Jinja2 engine. The `render_template()` function searches the `templates/` directory, compiles the HTML, merges it with passed Python variables, and returns a compiled HTTP response string with a 200 OK status.",
            "project_example": "In `app.py` line 48, `render_template('index.html', total_posts=total_posts)` takes the database count and injects it into the HTML before sending it to the client.",
            "real_world_usage": "Content Management Systems (CMS) and dashboard portals render distinct user dashboards from a singular template layout.",
            "best_practices": "Structure templates with a parent layout (e.g. `layout.html`) and child templates utilizing `{% extends %}` to avoid duplicate HTML tags across files.",
            "interview_tip": "Focus on the separation of concerns. Templates manage presentation logic (UI), while view functions manage business logic (queries and math)."
        },
        {
            "id": 14,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is the Flask request object?",
            "easy_explanation": "The request object is like a mailbox where Flask stores everything a user sends. If a user fills out a search box or logs in, Flask checks the request object to read what they typed.",
            "technical_explanation": "The Flask `request` object is a thread-local global proxy representing the current client HTTP request context. It exposes parameters like `request.method` (GET/POST), `request.args` (query string parameters), `request.form` (POST form variables), `request.json` (parsed JSON body), and headers.",
            "project_example": "In `app.py` line 63, `request.form.get('query')` fetches the string typed into the search bar when the form is submitted via POST.",
            "real_world_usage": "Reading incoming parameters, handling form uploads, processing API payloads, and extracting authorization headers.",
            "best_practices": "Always use `.get()` with default values (e.g. `request.form.get('query', '')`) to avoid throwing `KeyError` crashes when client data is missing.",
            "interview_tip": "Explain that `request` is a context-local proxy. This means it points to the request data of the current active thread, allowing concurrent request handling without data leaks."
        },
        {
            "id": 15,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is url_for()?",
            "easy_explanation": "Instead of writing raw link paths like '/static/css/style.css', `url_for()` dynamically calculates the correct URL. It's like asking a guide for directions instead of drawing a permanent map that might break if files are moved.",
            "technical_explanation": "The `url_for()` function in Flask is used for URL reversing. It accepts the name of a view function (or static endpoint) and returns the corresponding URL route. This decouples code references from structural URL changes and automatically handles URL escaping.",
            "project_example": "In `templates/index.html` line 14, `<link rel=\"stylesheet\" href=\"{{ url_for('static', filename='css/style.css') }}\">` dynamically points to the CSS file.",
            "real_world_usage": "Linking stylesheets, assets, or navigating between different dashboard routes.",
            "best_practices": "Always use `url_for()` instead of hardcoded paths (`/static/css/style.css`) in your templates to make deployment under subpaths seamless.",
            "interview_tip": "State that `url_for()` makes application paths robust, ensuring links do not break even if you change route path decorations in `app.py`."
        },
        {
            "id": 16,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is render_template()?",
            "easy_explanation": "It is a Python function that compiles the dynamic HTML page. You give it a template file name and some data, and it merges them together to send a complete web page to the browser.",
            "technical_explanation": "The `render_template()` helper compiles an HTML template from the application's template folder using the Jinja2 engine, binds it to the provided context arguments, and returns a response object ready for the WSGI server.",
            "project_example": "In `app.py` line 119, `return render_template('results.html', query=query, results=results)` builds the search results page.",
            "real_world_usage": "Renders pages dynamically on user interaction in Flask server-side applications.",
            "best_practices": "Return `render_template` directly at the end of view functions, passing only the necessary data variables.",
            "interview_tip": "Note that it returns a compiled string matching the content-type `text/html`, and Flask wraps it in a standard HTTP response wrapper."
        },
        {
            "id": 17,
            "category": "Flask",
            "category_id": "flask",
            "question": "How is the Static Folder configured in Flask?",
            "easy_explanation": "The static folder is a special drawer where you keep things that don't change, like styles, images, and script files. Flask knows to look inside this drawer when a user asks for logo files or stylesheets.",
            "technical_explanation": "By default, Flask assumes a subdirectory named `static` exists in the application root directory to host static assets. This is configured via `static_folder` and exposed under the `/static` URL path, handled internally by Werkzeug's static file handler.",
            "project_example": "Our project structure uses `static/css/style.css` and `static/js/main.js` which are loaded using the static endpoint in Flask templates.",
            "real_world_usage": "Hosting CSS frameworks, client scripts, company logos, and site icons.",
            "best_practices": "Organize your static directory into clear subfolders like `css/`, `js/`, and `images/` to maintain clean project organization.",
            "interview_tip": "Explain that in high-traffic production environments, static files are often bypassed in Flask and served directly by Nginx or CDNs to optimize speed."
        },
        {
            "id": 18,
            "category": "Flask",
            "category_id": "flask",
            "question": "What is the Application Factory Pattern?",
            "easy_explanation": "Instead of creating your website configuration as a permanent static object at startup, you create a recipe (factory function) that builds the application whenever it is run, allowing you to easily build copies for testing or production.",
            "technical_explanation": "The Application Factory pattern is a design layout where the Flask app object is created inside a function (typically `create_app()`) rather than as a global object. Configs, blueprints, and database connections are registered within this function. This pattern isolates configurations and prevents circular imports.",
            "project_example": "In our simple configuration, `app = Flask(__name__)` is defined globally in `app.py`. Scaling this project would involve wrapping this in a `def create_app(config_class):` function.",
            "real_world_usage": "Large-scale enterprise Flask applications that run distinct configurations for development, staging, testing, and production environments.",
            "best_practices": "Structure extension initializations (like SQLite databases or login managers) globally but bind them inside the factory using `.init_app(app)`.",
            "interview_tip": "State that the factory pattern is vital for unit testing, as it allows you to create separate instances of the app with mocked databases and clean configurations for each test case."
        },

        # ==========================================
        # DATABASE
        # ==========================================
        {
            "id": 19,
            "category": "Database",
            "category_id": "database",
            "question": "Why SQLite?",
            "easy_explanation": "SQLite is like a notebook file. It saves your database tables directly inside a normal file on your computer. You don't need to install database servers, run setup processes, or connect to cloud databases—it just works out of the box.",
            "technical_explanation": "SQLite is an in-process, serverless, self-contained relational database management engine. It reads and writes directly to ordinary disk files. It complies with ACID standards and does not run as a standalone server process. This eliminates network latency and makes local deployment simple.",
            "project_example": "In `utils/data_loader.py` line 6, we locate `database/socialmind.db` and establish direct local SQLite connections.",
            "real_world_usage": "Embedded systems, mobile apps (iOS/Android), prototyping, test environments, and low-to-medium traffic web applications.",
            "best_practices": "Use SQLite for read-heavy or single-user environments, and migrate to PostgreSQL if your app requires concurrent write operations.",
            "interview_tip": "Emphasize that SQLite is embedded, meaning it runs inside the application process rather than communicating over a TCP network port, maximizing read efficiency."
        },
        {
            "id": 20,
            "category": "Database",
            "category_id": "database",
            "question": "How is data stored in SQLite?",
            "easy_explanation": "Everything is stored in a single file on your hard drive. Inside that file, SQLite structures data into tables, pages, and indexes, writing updates directly to the file.",
            "technical_explanation": "SQLite databases are serialized into a single cross-platform file. Internally, the file is organized into fixed-size database pages (typically 4096 bytes). Tables and indexes are structured as B-trees. During updates, writes are safely recorded to a Rollback Journal or WAL (Write-Ahead Log) to prevent data corruption.",
            "project_example": "Our posts database is saved as `database/socialmind.db` and is committed directly to git to keep sample records portable.",
            "real_world_usage": "Local configurations storage, client databases in web browsers, and light web apps.",
            "best_practices": "Enable Write-Ahead Logging (WAL) mode to allow concurrent readers while a write operation is active.",
            "interview_tip": "Mention that SQLite uses dynamic typing; columns can hold any data type regardless of the declared column schema (except for INTEGER PRIMARY KEY)."
        },
        {
            "id": 21,
            "category": "Database",
            "category_id": "database",
            "question": "What is the Database Schema in SocialMind AI?",
            "easy_explanation": "The schema is the blueprint of our database tables. It defines what columns we have (like the post content, likes, author, platform) and what type of data belongs in each column.",
            "technical_explanation": "The schema defines database tables and relationships. For SocialMind AI, the `posts` table schema consists of columns like `id` (INTEGER PRIMARY KEY), `platform` (TEXT), `author` (TEXT), `content` (TEXT), `likes` (INTEGER), `comments` (INTEGER), `shares` (INTEGER), `hashtags` (TEXT), `url` (TEXT), and `timestamp` (TEXT).",
            "project_example": "In `utils/data_loader.py` lines 58-79, we query these columns like `content`, `author`, and `hashtags` to filter search responses.",
            "real_world_usage": "Database schemas form the foundation of backend engineering, ensuring structure across applications.",
            "best_practices": "Always declare types and column constraints (like NOT NULL or UNIQUE) to protect data integrity at the database layer.",
            "interview_tip": "Highlight that relational databases enforce a rigid schema, ensuring that data written from the application always adheres to defined columns and datatypes."
        },
        {
            "id": 22,
            "category": "Database",
            "category_id": "database",
            "question": "What is a Primary Key?",
            "easy_explanation": "A primary key is like a passport number. It is a unique code given to each item in a database table. No two items can share the same code, ensuring we can pinpoint any record without mistakes.",
            "technical_explanation": "A Primary Key is a column or set of columns in a relational database table that uniquely identifies each row. It must contain unique values, cannot contain NULL, and is automatically indexed by the database engine to speed up queries.",
            "project_example": "In our `posts` table, the `id` column is the `INTEGER PRIMARY KEY`. It increments automatically for every new post indexed.",
            "real_world_usage": "Unique database indexing, joining tables using foreign keys, and fetching specific records (e.g. `SELECT * FROM users WHERE id = 1`).",
            "best_practices": "Use auto-incrementing integers or UUIDs as primary keys, avoiding mutable natural keys like email addresses.",
            "interview_tip": "Explain that primary keys automatically build a clustered index, which optimizes search performance when querying records by their key ID."
        },
        {
            "id": 23,
            "category": "Database",
            "category_id": "database",
            "question": "Why not MongoDB (NoSQL) for this project?",
            "easy_explanation": "MongoDB is a database designed for highly variable document structures and scales across many servers. For SocialMind AI, our data is structured and fits inside clean tables, so running MongoDB would require installing a complex external server for no real benefit.",
            "technical_explanation": "MongoDB is a document-oriented NoSQL database. While MongoDB excels at storing unstructured JSON-like documents at scale, SQLite was selected because SocialMind AI uses a structured dataset with consistent fields. SQLite's embedded nature simplifies local setup and avoids the resource overhead of running a separate MongoDB server.",
            "project_example": "SQLite is a single file and compiles natively. It runs on Render's free instances without needing external database addons.",
            "real_world_usage": "Big data setups, catalog engines, real-time messaging databases, and apps with dynamic data models.",
            "best_practices": "Choose NoSQL when data is unstructured and scales horizontally; choose SQL when records have fixed schemas and require relational consistency.",
            "interview_tip": "Explain that SQLite simplifies deployment and operations for single-server solutions, whereas MongoDB is better suited for high-write, schema-less, and horizontally scaled systems."
        },
        {
            "id": 24,
            "category": "Database",
            "category_id": "database",
            "question": "How are posts retrieved from the database?",
            "easy_explanation": "Python sends a SQL query to the database asking for records, receives the records, and then translates the raw database tables into list objects that Python can easily manipulate and display.",
            "technical_explanation": "We execute standard SQL queries using Python's `sqlite3` library. We set `conn.row_factory = sqlite3.Row` to retrieve results as dictionaries rather than tuples, allowing column access by name. Finally, we convert the rows into standard dictionary objects.",
            "project_example": "In `utils/data_loader.py` line 22, `conn.row_factory = sqlite3.Row` makes it easy to fetch database rows and parse them using `posts = [dict(row) for row in cursor.fetchall()]`.",
            "real_world_usage": "Every web app backend retrieves data from database tables to pass to APIs or templates.",
            "best_practices": "Always close the connection (e.g., `conn.close()`) inside a `finally` block or use context managers (`with`) to prevent connection leaks.",
            "interview_tip": "Highlight the role of `sqlite3.Row` in mapping SQL fields to Python dict keys. This prevents index errors if column orders change in the schema."
        },
        {
            "id": 25,
            "category": "Database",
            "category_id": "database",
            "question": "How do we manage SQLite connections dynamically in Python?",
            "easy_explanation": "Imagine database connections as telephone lines. If you leave too many lines open, the line gets busy. Python opens a connection when it needs to run a query and immediately hangs up (closes it) when done.",
            "technical_explanation": "We manage connection lifecycles by instantiating new SQLite connections on-demand and closing them immediately after the database operation finishes. In multi-threaded Flask instances, sharing a single connection can lead to concurrency errors, so a connection-per-thread strategy is critical.",
            "project_example": "In `utils/data_loader.py` lines 10-29, we call `conn = get_connection()`, fetch posts, and immediately execute `conn.close()` to release the lock.",
            "real_world_usage": "Web apps managing database resource limits using connection pools.",
            "best_practices": "Use a context manager (`with sqlite3.connect(...) as conn:`) or Flask's global request context (`g`) to open and close connections safely.",
            "interview_tip": "Explain that SQLite by default does not support concurrent writes and locks the file. Closing connections promptly is essential to prevent write lockouts."
        },

        # ==========================================
        # DEPLOYMENT
        # ==========================================
        {
            "id": 26,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "Why Render?",
            "easy_explanation": "Render is like a modern cloud hosting service. You link it to your GitHub project, and every time you upload your code updates, Render builds, tests, and deploys the new website automatically in the background.",
            "technical_explanation": "Render is a Platform-as-a-Service (PaaS) provider. It integrates with GitHub repositories to trigger automated builds and continuous deployments. Render supports native runtime environments, handles TLS certificates, manages web servers (Gunicorn), and configures custom build steps.",
            "project_example": "Our `render.yaml` file configures the web service environment, defining build commands and runtime specifications.",
            "real_world_usage": "SaaS startups, web apps, cron jobs, and background workers.",
            "best_practices": "Define application configurations in a declarative file like `render.yaml` to ensure consistent and reproducible infrastructure deployment.",
            "interview_tip": "Contrast PaaS (Render, Heroku) with IaaS (AWS, GCP). PaaS handles server maintenance, auto-scaling, and OS updates, allowing developers to focus on writing code."
        },
        {
            "id": 27,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "Why Gunicorn?",
            "easy_explanation": "Flask's built-in web server is like a single-lane road—it can only handle one car at a time. Gunicorn is like a multi-lane highway, allowing multiple users to connect to the website simultaneously without slow-downs.",
            "technical_explanation": "Gunicorn (Green Unicorn) is a Python WSGI HTTP server. It uses a pre-fork worker model, where a master process manages multiple worker processes. These workers handle incoming HTTP requests concurrently, bypassing Python's Global Interpreter Lock (GIL) constraints.",
            "project_example": "In `render.yaml` line 8, our start command is `gunicorn app:app`, which instructs Render to run our app using Gunicorn in production.",
            "real_world_usage": "Serving Python web applications in production environments (running Flask, Django, or FastAPI frameworks).",
            "best_practices": "Set the number of Gunicorn workers using the formula: `(2 * number of CPU cores) + 1` to optimize server performance.",
            "interview_tip": "Emphasize that the default Flask development server is not secure, stable, or scalable. It is single-threaded and should never be used in production."
        },
        {
            "id": 28,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "What is requirements.txt?",
            "easy_explanation": "Think of it as a grocery list of all the software libraries our project needs to run. When we deploy to the cloud, the server reads this list and installs every package automatically.",
            "technical_explanation": "The `requirements.txt` file is a package manager configuration file listing project dependencies. It lists the names and exact version ranges of pip packages needed to run the application, ensuring consistency across environments.",
            "project_example": "Our `requirements.txt` file includes `flask`, `sentence-transformers`, `scikit-learn`, `numpy`, and `torch`, which are required to run SocialMind AI.",
            "real_world_usage": "Python dependency management, deployment environment setups, and Docker containers.",
            "best_practices": "Pin dependency versions exactly (e.g. `flask==3.0.3`) to prevent auto-updates from breaking application compatibility.",
            "interview_tip": "Explain that version pinning prevents bugs caused by upstream package changes, making deployment pipelines predictable and secure."
        },
        {
            "id": 29,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "How are Environment Variables handled?",
            "easy_explanation": "Environment variables are settings stored outside of our code. We use them for secrets like passwords, API keys, or settings (like switching between testing and production modes) to keep them secure.",
            "technical_explanation": "Environment variables are configuration settings injected into the application environment. Flask accesses them using the `os` library (e.g., `os.environ.get('PORT')`). This keeps secrets out of source control.",
            "project_example": "In `app.py` line 277, we configure the runtime port using `port = int(os.environ.get('PORT', 5000))`.",
            "real_world_usage": "Managing database credentials, API secrets, JWT signature keys, and active runtime variables.",
            "best_practices": "Use a `.env` file for local development (which is added to `.gitignore`) and define production variables directly in your cloud hosting provider.",
            "interview_tip": "Highlight that hardcoding secrets in code is a critical vulnerability. Storing configuration in the environment adheres to the Twelve-Factor App methodology."
        },
        {
            "id": 30,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "How does production deployment differ from local development?",
            "easy_explanation": "Development mode is like working on a construction site—warning signs are active, detailed error messages are exposed, and files update instantly. Production is like the finished building—it is secured, optimized for speed, and logs are kept hidden from the public.",
            "technical_explanation": "In production, the Flask development server is replaced by a production WSGI server (Gunicorn). Flask's `debug` mode is disabled to prevent security vulnerabilities like interactive stack trace debuggers. Performance settings, such as PyTorch CPU threads (`torch.set_num_threads(1)`), are configured to prevent memory spikes on shared instances.",
            "project_example": "In `app.py` lines 278-284, we read `FLASK_DEBUG` from environment variables, defaulting to `False` in production.",
            "real_world_usage": "Standard practice for web services, database backends, and server deployments.",
            "best_practices": "Automate deployment tasks like precomputing embeddings in a build script (`build.sh`) so the production server doesn't waste CPU resources at startup.",
            "interview_tip": "Always mention that keeping `debug=True` in production is a critical security risk, as it allows attackers to execute arbitrary code via the interactive debugger."
        },
        {
            "id": 31,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "What is a WSGI server and why is it needed?",
            "easy_explanation": "A WSGI server is like a translator. Web servers like Nginx speak internet protocols, while Flask speaks Python. The WSGI server translates between the two so they can talk.",
            "technical_explanation": "WSGI (Web Server Gateway Interface) is a specification that defines how web servers communicate with Python web applications. WSGI servers implement this interface, translating HTTP requests from the web server into a format the Python application can process, and returning the application's response.",
            "project_example": "We use Gunicorn as our WSGI server to run our Flask application (`app:app`) on Render.",
            "real_world_usage": "Deploying Python frameworks (Flask, Django) in production behind web servers like Nginx.",
            "best_practices": "Configure your WSGI server to write application logs to standard output so they can be aggregated by your cloud hosting provider.",
            "interview_tip": "Explain that WSGI is a standard protocol. It decouples the web server from the web framework, allowing you to switch web servers or frameworks without code changes."
        },
        {
            "id": 32,
            "category": "Deployment",
            "category_id": "deployment",
            "question": "How do you write a build shell script for production?",
            "easy_explanation": "A build script is like a checklist script. It runs automatically when the code is deployed, installing libraries, setting up folders, and preparing the database before the website starts.",
            "technical_explanation": "A build shell script automates compilation and deployment steps. It typically includes commands to install dependencies, run database migrations, download static files, and precompute data structures like embeddings to minimize runtime overhead.",
            "project_example": "Our `build.sh` script runs `pip install`, downloads models, and generates database assets before starting the Gunicorn server.",
            "real_world_usage": "CI/CD pipelines, automated deployments, and Docker builds.",
            "best_practices": "Make build scripts fail-fast by using `set -e` at the start, ensuring the build stops immediately if any command returns a non-zero exit code.",
            "interview_tip": "Explain that running setup tasks during the build phase instead of the run phase improves application startup time and prevents server timeouts."
        },

        # ==========================================
        # GIT & GITHUB
        # ==========================================
        {
            "id": 33,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is Git?",
            "easy_explanation": "Git is like a time machine for your code. It keeps track of every save you make, allowing you to view changes, compare versions, or travel back in time if you break something.",
            "technical_explanation": "Git is a distributed version control system. It tracks changes in source code files, records historical commit logs, manages branches for parallel development, and facilitates collaboration by allowing developers to push and pull changes to and from remote repositories.",
            "project_example": "We use Git to track updates to files like `app.py` and templates, committing changes locally before pushing them.",
            "real_world_usage": "Software development across all industries, open-source projects, and DevOps configuration management.",
            "best_practices": "Commit early and often with clear, descriptive commit messages, and avoid committing build artifacts or virtual environments.",
            "interview_tip": "Highlight that Git is distributed, meaning every developer has a full copy of the project history on their local machine, rather than relying on a central server."
        },
        {
            "id": 34,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is GitHub?",
            "easy_explanation": "If Git is the time machine on your personal computer, GitHub is the online hub where teams upload their timelines. It makes sharing code, reviewing work, and working together simple.",
            "technical_explanation": "GitHub is a cloud-based hosting service for Git repositories. It provides collaboration tools, pull request code reviews, issue tracking, and CI/CD pipelines (GitHub Actions) to automate testing and deployment workflows.",
            "project_example": "The SocialMind AI code is hosted on GitHub, allowing Render to monitor commits and automatically deploy updates.",
            "real_world_usage": "Open-source collaboration, team code reviews, project management, and developer portfolios.",
            "best_practices": "Use pull requests for all code changes, and protect your main branch by requiring reviews before code is merged.",
            "interview_tip": "Differentiate Git (the local command-line version control tool) from GitHub (the cloud platform that hosts Git repositories and provides collaboration features)."
        },
        {
            "id": 35,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is Version Control?",
            "easy_explanation": "Version control is like a history book for a project. It tracks who made changes, what files were updated, and when, so you can restore earlier versions if needed.",
            "technical_explanation": "Version Control Systems (VCS) track changes to files over time. Distributed VCS (like Git) mirror the complete repository history on all client machines. This enables offline history tracking, branch testing, and recovery from data loss.",
            "project_example": "We track files like `app.py` in Git. This allows us to revert modifications if a new feature causes the server to crash.",
            "real_world_usage": "Managing codebase changes in software development, tracking infrastructure-as-code files, and collaborative writing projects.",
            "best_practices": "Write clear, atomic commits that focus on a single change, making the project history easy to read and debug.",
            "interview_tip": "Highlight that version control enables team collaboration, tracking conflict sources, and restoring previous code versions in production if bugs occur."
        },
        {
            "id": 36,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "How do Git Branches work?",
            "easy_explanation": "Think of branching like creating a duplicate copy of your project folder. You can test a new feature in this copy without affecting the original. Once it works, you merge the changes back into the main folder.",
            "technical_explanation": "A Git branch is a lightweight, moveable pointer to a specific commit. The default branch is typically named `main`. Creating a branch isolates new code changes from the stable main branch, enabling developers to work on features concurrently.",
            "project_example": "We create feature branches (e.g. `feature/interview-guide`) to develop new pages, keeping the `main` branch clean and deployable.",
            "real_world_usage": "Developing features, fixing bugs, and experimenting without disrupting the stable production codebase.",
            "best_practices": "Name branches clearly using prefixes like `feature/` or `bugfix/`, and delete branches after merging to keep the repository clean.",
            "interview_tip": "Explain that branches in Git are lightweight pointers to commits. This makes creating and switching between branches fast, unlike traditional version control systems."
        },
        {
            "id": 37,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is a Git Commit?",
            "easy_explanation": "A commit is like saving your progress in a video game. It records a snapshot of your files at that exact moment, along with a message explaining what you did.",
            "technical_explanation": "A Git commit is a SHA-1 cryptographic hash pointing to a tree structure of staged file changes. It includes author metadata, a timestamp, a commit message, and a reference to the parent commit, creating a permanent link in the project history.",
            "project_example": "Committing layout changes in `index.html` with the message: `Add interview guide navigation link to navbar`.",
            "real_world_usage": "Creating checkpoints in codebase development, making changes easy to track, revert, and review.",
            "best_practices": "Write descriptive, imperative commit messages (e.g., 'Fix SQLite connection leak in data loader') and avoid vague messages like 'fixed stuff'.",
            "interview_tip": "Explain that a commit represents an atomic change, making it easy to isolate and revert specific modifications if a bug is introduced."
        },
        {
            "id": 38,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What are Git Push and Pull?",
            "easy_explanation": "Pushing is like uploading your local game save file to the cloud. Pulling is like downloading the latest updates from the cloud to update your local files.",
            "technical_explanation": "`git push` uploads local branch commits to a remote repository. `git pull` fetches updates from the remote repository and immediately merges them into the current active local branch, combining `git fetch` and `git merge` in a single command.",
            "project_example": "Running `git push origin main` to upload commits, triggering automated deployment pipelines on Render.",
            "real_world_usage": "Syncing code changes between local machines and remote servers like GitHub or GitLab.",
            "best_practices": "Always run `git pull` and test changes locally before pushing your commits to avoid breaking the shared remote build.",
            "interview_tip": "Note that `git pull` can trigger merge conflicts if remote and local changes overlap, which must be resolved before committing."
        },
        {
            "id": 39,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is a Git Merge and how are conflicts resolved?",
            "easy_explanation": "Merging is combining two project timelines. If you and a teammate edit the same line of the same file, Git gets confused and asks you to choose which change to keep—this is resolving a conflict.",
            "technical_explanation": "A merge integrates commits from a source branch into a target branch. If changes do not overlap, Git performs a 'fast-forward' merge. If changes overlap, Git flags a 'merge conflict'. To resolve it, you manually edit the conflicted files, choose the correct lines, stage the files, and commit the merge.",
            "project_example": "Merging `feature/interview-guide` into `main`. Overlapping edits in `app.py` must be manually resolved before committing.",
            "real_world_usage": "Merging team member branches into the shared master codebase during development.",
            "best_practices": "Keep feature branches updated by regularly merging `main` into them to catch and resolve conflicts early.",
            "interview_tip": "Explain that merge conflicts are normal in collaborative environments. Resolving them requires communication to ensure no critical logic is lost."
        },
        {
            "id": 40,
            "category": "Git & GitHub",
            "category_id": "git",
            "question": "What is .gitignore?",
            "easy_explanation": "It is a text file that lists folders and files Git should ignore. This keeps heavy directories (like virtual environments) or private files (like passwords) from being uploaded to GitHub.",
            "technical_explanation": "A `.gitignore` file contains glob patterns matching files and directories that Git should ignore. Ignored files are not tracked in the index, preventing developers from committing sensitive credentials, OS-specific files, or dependency folders.",
            "project_example": "Our `.gitignore` file lists `.venv/`, `__pycache__/`, and `.DS_Store` to keep our repository clean.",
            "real_world_usage": "Excluding log directories, compilation outputs, secret environment files, and large data files from source control.",
            "best_practices": "Create your `.gitignore` file during project initialization to prevent tracking unwanted files from the start.",
            "interview_tip": "Explain that if a file is already tracked by Git, adding it to `.gitignore` will not stop tracking it. You must untrack it first using `git rm --cached`."
        },

        # ==========================================
        # PYTHON
        # ==========================================
        {
            "id": 41,
            "category": "Python",
            "category_id": "python",
            "question": "What is a Virtual Environment in Python?",
            "easy_explanation": "A virtual environment is like a private workspace folder for a project. It ensures that the software libraries installed for one project don't conflict with libraries installed for other projects on your computer.",
            "technical_explanation": "A virtual environment (`.venv`) is an isolated directory containing a copy of the Python interpreter and a private set of installed libraries. This prevents version conflicts between global dependencies and different projects.",
            "project_example": "Our project workspace includes a `.venv/` directory where packages like Flask and Sentence Transformers are installed.",
            "real_world_usage": "Developing multiple Python applications with conflicting package dependencies on a single machine.",
            "best_practices": "Always run your projects inside a virtual environment, and exclude the `.venv/` directory from version control using `.gitignore`.",
            "interview_tip": "Explain that virtual environments isolate python dependency paths, ensuring that `pip install` commands only modify the local environment."
        },
        {
            "id": 42,
            "category": "Python",
            "category_id": "python",
            "question": "What is List Comprehension and how is it used in Python?",
            "easy_explanation": "It is a shorthand way to create a list. Instead of writing a long loop to copy, filter, or process items, you can write the loop in a single clean line of code.",
            "technical_explanation": "List comprehension provides a concise syntax to create lists from existing iterables. It is faster than standard loops because it runs at C-speed inside the Python interpreter.",
            "project_example": "In `utils/data_loader.py` line 26: `posts = [dict(row) for row in cursor.fetchall()]` converts SQL row objects into a list of dictionaries.",
            "real_world_usage": "Filtering data, formatting lists, and mapping collections of objects in data processing pipelines.",
            "best_practices": "Use list comprehensions for simple transformations, and stick to standard loops for complex logic to maintain readability.",
            "interview_tip": "Explain that list comprehensions are syntax-optimized in Python, making them faster and more readable than standard loops for simple tasks."
        },
        {
            "id": 43,
            "category": "Python",
            "category_id": "python",
            "question": "How are Python dictionaries used for structured data?",
            "easy_explanation": "A dictionary is like a labeled box. Instead of looking up items by their index number, you look them up by a descriptive label (a key) like 'title' or 'likes'.",
            "technical_explanation": "Python dictionaries are hash tables that store key-value pairs. They provide O(1) average time complexity for lookups, insertions, and deletions, making them highly efficient for storing structured data records.",
            "project_example": "In `services/search_service.py` line 75, we use `stats[platform] = stats.get(platform, 0) + 1` to track post counts.",
            "real_world_usage": "Parsing JSON payloads, mapping configuration parameters, and representing data rows.",
            "best_practices": "Use the `.get()` method to retrieve values, as it returns a default value instead of throwing a `KeyError` if the key is missing.",
            "interview_tip": "Explain that from Python 3.7 onwards, dictionaries preserve insertion order, which is useful when displaying sequenced database columns."
        },
        {
            "id": 44,
            "category": "Python",
            "category_id": "python",
            "question": "What is the difference between list and tuple in Python?",
            "easy_explanation": "Lists are like notebooks—you can add, delete, or rewrite pages. Tuples are like printed books—once printed, they cannot be changed.",
            "technical_explanation": "Lists are mutable arrays; they can be resized, appended, or modified. Tuples are immutable sequences; they cannot be changed after creation. Because tuples are static, they occupy less memory and can be used as dictionary keys.",
            "project_example": "We use lists for arrays that need editing (e.g. `results.append(post)`), and tuples for static database parameters (e.g., `(platform,)`).",
            "real_world_usage": "Lists manage dynamic queues; tuples protect database coordinates, config constants, and read-only records.",
            "best_practices": "Use tuples for data that should not change to prevent accidental modifications, and lists for dynamic data collections.",
            "interview_tip": "Highlight that tuples are faster and use less memory than lists due to their immutability, which allows Python to optimize memory allocation."
        },
        {
            "id": 45,
            "category": "Python",
            "category_id": "python",
            "question": "How does Python resolve file paths dynamically using os.path?",
            "easy_explanation": "Instead of typing rigid paths like 'C:/Folder/file.txt', we tell Python to calculate where the folder is relative to the code, so the program runs on any computer without modification.",
            "technical_explanation": "We use `os.path` functions to resolve absolute file paths relative to the current file (`__file__`). This ensures paths resolve correctly regardless of the operating system or active working directory.",
            "project_example": "In `utils/data_loader.py` line 5, we use `os.path.dirname(os.path.dirname(os.path.abspath(__file__)))` to find the project root directory.",
            "real_world_usage": "Locating asset files, database files, and model configs in portable web applications.",
            "best_practices": "Always use `os.path.join` to build file paths instead of string concatenation, as it handles operating system-specific slash separators automatically.",
            "interview_tip": "State that dynamic path resolution is essential for deployment, ensuring that paths resolve correctly on both local development machines and cloud servers."
        },
        {
            "id": 46,
            "category": "Python",
            "category_id": "python",
            "question": "What is the difference between == and is in Python?",
            "easy_explanation": "== checks if two items have the same value (e.g., two identical books). 'is' checks if they are the exact same physical object in memory (e.g., the exact same copy of a book).",
            "technical_explanation": "The `==` operator compares the values of two objects for equality. The `is` operator compares the identity of two objects, checking if they refer to the same memory address (`id()`).",
            "project_example": "In `models/semantic_search.py` line 45, we compare sizes using `!=` for values. In checking status states, we use `if error_message is None` for reference identity.",
            "real_world_usage": "Comparing user input values vs. checking if a variable points to a singleton like `None`, `True`, or `False`.",
            "best_practices": "Always use `is` when comparing variables to `None` for style consistency, and use `==` for comparing values (numbers, strings, lists).",
            "interview_tip": "Explain that `is` is a fast check because it compares memory addresses directly, while `==` runs custom methods (like `__eq__`) which can be slower."
        },

        # ==========================================
        # SOFTWARE ENGINEERING
        # ==========================================
        {
            "id": 47,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "What is the MVC (Model-View-Controller) architecture?",
            "easy_explanation": "Imagine a restaurant. The chef cooks the food (Model), the waiter takes your order and coordinates (Controller), and the plate presents the food to you (View). This separates tasks so everyone focuses on one job.",
            "technical_explanation": "MVC is a software design pattern that divides an application into three interconnected parts: Model (data structure and business logic), View (user interface presentation), and Controller (manages user inputs and directs data flow).",
            "project_example": "In SocialMind AI, database models and embedding pipelines serve as the Model, Jinja HTML files are the View, and Flask routes in `app.py` act as the Controller.",
            "real_world_usage": "Frameworks like Django, Ruby on Rails, and ASP.NET are built on the MVC design pattern.",
            "best_practices": "Keep your Controller logic thin by moving database queries and business logic into separate services or Model modules.",
            "interview_tip": "Explain that MVC improves code maintainability. Developers can update UI layouts (Views) without changing database operations (Models)."
        },
        {
            "id": 48,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "What is clean code and why are docstrings important?",
            "easy_explanation": "Clean code is written so that other developers can read it like a book. Docstrings are clear instructions written inside the code that explain what a function does.",
            "technical_explanation": "Clean code is readable, modular, and maintainable, adhering to styling guidelines (like PEP 8). Docstrings (`''' ... '''`) document classes and functions, explaining arguments, return types, and exceptions to help new developers.",
            "project_example": "Our project code includes docstrings at the top of files and inside helper functions (e.g., `services/search_service.py` line 17).",
            "real_world_usage": "Working in software teams, maintaining open-source libraries, and automated documentation generation using Sphinx.",
            "best_practices": "Write self-documenting code with clear variable names, and use docstrings to explain 'why' a function exists rather than just 'how' it works.",
            "interview_tip": "Emphasize that readable code is easier to debug and test. Clean code reduces technical debt and makes team collaboration seamless."
        },
        {
            "id": 49,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "What is modular programming?",
            "easy_explanation": "Modular programming is like building with Lego bricks. Instead of building a toy from one giant piece of plastic, you build small blocks that connect together, making it easy to swap parts out.",
            "technical_explanation": "Modular programming divides a software system into separate, independent modules. Each module encapsulates a specific functionality, exposing a clean interface while hiding its internal implementation details.",
            "project_example": "We separate database loaders (`utils/data_loader.py`) from the AI embedding logic (`models/embedding.py`) and application routes (`app.py`).",
            "real_world_usage": "Structuring large codebases, managing microservices, and writing reusable NPM or PyPI packages.",
            "best_practices": "Follow the Single Responsibility Principle: each module or class should have exactly one reason to change.",
            "interview_tip": "State that modular programming simplifies testing. Developers can write unit tests for individual modules in isolation without loading the entire application."
        },
        {
            "id": 50,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "What is REST and how does Flask represent APIs?",
            "easy_explanation": "REST is a standard set of rules for communication on the web. It uses standard HTTP actions like GET to retrieve data and POST to submit data, ensuring different systems can exchange information.",
            "technical_explanation": "REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server protocol (HTTP) and standard methods (GET, POST, PUT, DELETE) to access resources identified by URIs.",
            "project_example": "Our `/about` and `/health` routes in `app.py` return JSON payloads, acting as stateless REST API endpoints.",
            "real_world_usage": "Third-party APIs (like Stripe or GitHub), mobile-to-backend communication, and microservices.",
            "best_practices": "Return standard HTTP status codes (e.g., 200 for success, 404 for not found, 500 for server errors) in your API responses.",
            "interview_tip": "Explain that REST is stateless, meaning each client request must contain all the information needed to authorize and fulfill it, simplifying server scaling."
        },
        {
            "id": 51,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "What is performance optimization in web search applications?",
            "easy_explanation": "It is about making search results load as fast as possible. Instead of recalculating search database results every time a user clicks search, we precompute data and limit resource usage to keep the site responsive.",
            "technical_explanation": "Performance optimization in search apps involves techniques like precomputing heavy vectors, database indexing, caching query results, and limiting thread usage on resource-constrained deployment environments.",
            "project_example": "In `models/semantic_search.py`, we load precomputed vectors (`embeddings.npy`) at startup instead of generating them for all posts on every search.",
            "real_world_usage": "Optimizing search portals, e-commerce engines, and social media feeds to load under 100 milliseconds.",
            "best_practices": "Identify search bottlenecks using profilers, and optimize database queries before investing in expensive caching layers.",
            "interview_tip": "Mention that precomputing embeddings is a key optimization. It shifts heavy model encoding tasks from search time to build time, protecting server CPUs."
        },
        {
            "id": 52,
            "category": "Software Engineering",
            "category_id": "engineering",
            "question": "How are custom application error handlers designed?",
            "easy_explanation": "When something goes wrong (like a page not found or a database crash), instead of showing a scary browser default error page, we display a custom designed page that matches our site's look and guides users back to safety.",
            "technical_explanation": "Flask provides the `@app.errorhandler()` decorator to catch specific HTTP status codes or exceptions. The handler function returns a custom styled HTML template alongside the correct HTTP status code (e.g., 404 or 500) to client browsers.",
            "project_example": "In `app.py` lines 261-268, we handle 404 (Not Found) and 500 (Internal Server Error) with custom view handlers rendering templates.",
            "real_world_usage": "Customizing error pages in production web applications to maintain brand consistency and guide users.",
            "best_practices": "Log the detailed stack trace of 500 errors to your server logs for debugging, but keep production error messages generic for users to prevent security leaks.",
            "interview_tip": "Highlight that error handlers must return the correct HTTP status code (e.g., 404 or 500) rather than a default 200 OK, ensuring search engine web crawlers index pages correctly."
        }
    ]
