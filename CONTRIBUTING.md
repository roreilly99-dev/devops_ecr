# Contributing to Perth Events Scraper

Thank you for your interest in contributing to the Perth Events Scraper project! This document provides guidelines and instructions for contributing.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python/Node version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:
- A clear description of the feature
- Use cases and benefits
- Any implementation ideas you have

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/roreilly99-dev/devops_ecr.git
   cd devops_ecr
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style guidelines
   - Add tests for new functionality
   - Update documentation as needed

4. **Test your changes**
   ```bash
   # Backend tests
   cd backend
   pytest
   
   # Frontend linting
   cd my-app
   npm run lint
   npm run build
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues
   - Ensure all CI checks pass

## 📝 Code Style

### Python (Backend)
- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for functions and classes
- Keep functions focused and small
- Use meaningful variable names

Example:
```python
def fetch_events(category: str, limit: int = 100) -> List[Event]:
    """
    Fetch events from the database.
    
    Args:
        category: Event category to filter by
        limit: Maximum number of events to return
        
    Returns:
        List of Event objects
    """
    # Implementation here
```

### JavaScript/React (Frontend)
- Use ES6+ features
- Prefer functional components with hooks
- Use meaningful component and variable names
- Keep components focused and reusable
- Add comments for complex logic

Example:
```javascript
/**
 * EventCard component displays a single event
 */
export default function EventCard({ event }) {
  // Component implementation
}
```

## 🧪 Testing

### Backend Tests
- Write tests for all new functions
- Aim for >80% code coverage
- Use pytest fixtures for common setup
- Test edge cases and error handling

```python
def test_event_creation():
    """Test creating a basic event"""
    event = Event(
        title="Test Event",
        category=EventCategory.DINING,
        # ... other fields
    )
    assert event.title == "Test Event"
```

### Frontend Tests
- Lint all code before committing
- Test major user interactions
- Ensure responsive design works

## 📚 Documentation

- Update README.md for significant features
- Add inline comments for complex logic
- Update API documentation for endpoint changes
- Include examples in documentation

## 🔍 Adding New Scrapers

When adding a new event scraper:

1. **Create scraper file** in `backend/scrapers/`
2. **Inherit from BaseScraper**
3. **Implement scrape() method**
4. **Add tests** for the scraper
5. **Update run_all.py** to include new scraper
6. **Document** the source and update rate

Example:
```python
from .base_scraper import BaseScraper
from models.event import Event, EventCategory, EventType, Location

class NewEventScraper(BaseScraper):
    """Scraper for XYZ event source"""
    
    def __init__(self):
        super().__init__("NewEventScraper")
    
    def scrape(self) -> List[Event]:
        """Scrape events from source"""
        events = []
        # Your implementation
        return events
```

## 🏗️ Infrastructure Changes

For Terraform/infrastructure changes:
- Test changes in a development environment
- Document new resources and their purpose
- Consider costs of new resources
- Update infrastructure documentation

## 🚀 Release Process

1. All changes go through Pull Requests
2. PRs must pass all CI checks
3. At least one review is required
4. Merge to main triggers deployment
5. Tag releases with semantic versioning

## 📋 Commit Messages

Use conventional commit format:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add cinema scraper for Moonlight Cinema
fix: resolve date parsing error in sports scraper
docs: update API endpoint documentation
```

## ⚖️ Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Assume good intentions

## 🆘 Getting Help

- Create an issue for questions
- Check existing issues and documentation
- Reach out to maintainers

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

Thank you for contributing to Perth Events Scraper! 🎉
