# SocialMind AI - Screenshot Guidelines for GitHub README

This guide outlines exactly how to capture and organize professional screenshots of the **SocialMind AI** search platform for your repository, portfolio, and presentations.

## Screenshot File Index

Please save your screenshot files directly to this folder (`screenshots/`) matching the exact names below:
1. **`homepage.png`**: The full-view landing page showing the updated layout, navigation bar, hero information, project statistics, workflow card, and custom footer.
2. **`search_results.png`**: The search results layout showing dynamic percentages, matched platform badges, and similarities.
3. **`no_results.png`**: The query fail-safe showing suggestions and secondary query cards.
4. **`about_api.png`**: The JSON payload from the `/about` endpoint route.
5. **`health_api.png`**: The JSON health state from the `/health` endpoint route.

---

## Professional Capturing Checklist

### 1. Browser Setup & Cleanup
* **Use Google Chrome or Microsoft Edge**: Standard chromium rendering engine is recommended for uniform shadows and glassmorphic blurs.
* **Hide Browser UI Controls**: Use the Chrome DevTools device mode (`Cmd + Shift + M` on Mac) to view pages, or use a screenshot browser extension that cuts out address bars, scrollbars, and bookmarks.
* **Deactivate Extensions**: Temporarily disable third-party extension badges (e.g. password managers, translation tags) that overlay pages.

### 2. Capture Sizes & Resolutions
* **Recommended Resolution**: **1920x1080 (1080p FHD)** or **2560x1440 (2K QHD)**. High-resolution captures preserve text crispness on high-density Retina or 4K screens.
* **Desktop View (`homepage.png` / `search_results.png`)**: Resize your browser window to a standard 16:9 ratio. Zoom the browser to 100% to keep fonts sharp.
* **Mobile / Responsive Check**: Make sure your cards and workflow boxes are correctly aligned (no layout overflows) when capturing smaller desktop views.

### 3. API Screen Grabs (`about_api.png` / `health_api.png`)
* **Use a JSON Formatter**: Install a browser extension like **JSON Viewer** or use Firefox's native JSON viewer to present key-value properties with clean dark-themed syntax coloring, rather than plain text blocks.
* **Hide Headers**: Capture only the response viewport area.

---

## Detailed Viewport Configurations

### 📸 `homepage.png`
* **Path to load**: `/` (Home page)
* **What to show**:
  * The top glassmorphic navbar with its subtle blue border.
  * The main search input field (active or with suggestion text).
  * The statistics cards showing total and platform counts.
  * *Tip*: Scroll down slightly so the navbar transition is triggered (adding the `.navbar-scrolled` style), revealing the beautiful transparency overlay.

### 📸 `search_results.png`
* **Path to load**: Post `/search` with a query like `"AI Internship"` or `"Machine Learning"`.
* **What to show**:
  * Match relevance percentages (e.g., `🎯 94.5%`).
  * Social tags (Instagram, Facebook, LinkedIn) matched next to profile photos.
  * Scroll so that 2–3 cards are fully visible in the frame.

### 📸 `no_results.png`
* **Path to load**: Search for a query that returns empty results (e.g. `"xyz123"`).
* **What to show**:
  * The centered "🔍 No Results Found" warning card.
  * The system-provided quick-suggestion badges below it.

### 📸 `about_api.png` & `health_api.png`
* **Paths to load**: `/about` and `/health` respectively.
* **What to show**:
  * Beautifully formatted JSON displaying project stats, backend configs, SQLite database connection indicators, and model names.
