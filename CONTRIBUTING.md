# Contributing to SocialMind AI

Thank you for your interest in contributing to **SocialMind AI**! As an open-source project developed for educational and internship evaluation, we welcome clean code improvements, bug fixes, and suggestions.

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. **Fork the Repository**: Create a personal copy of the repository on GitHub.
2. **Clone the Fork**: Clone the project to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/SocialMind-AI.git
   ```
3. **Set Up Local Workspace**: Follow the local setup guide in the [README.md](README.md#local-setup) to set up a virtual environment and load mock data.
4. **Create a Feature Branch**: Keep changes localized to a branch describing the feature or bug:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Guidelines

- **Keep Code Safe**: Ensure modifications do not break semantic vector generation or SQLite query operations.
- **Run Tests**: Verify modifications using local tests:
   ```bash
   python test_search.py
   python test_loader.py
   python test_semantic_search.py
   ```
- **Code Style**: Adhere to clean Python formatting. Use appropriate comments for major functions.
- **Commit Messages**: Write clear, imperative commits:
   ```text
   feat: add support for Twitter post loading
   fix: handle database exception when precompute_embeddings fails
   ```

## Submitting Pull Requests

1. Commit your changes and push them to your GitHub fork:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request (PR) against the `main` branch of the official repository.
3. Describe the change clearly in the PR description, referencing any related issue.
4. Wait for code review and feedback. Thank you for contributing!
