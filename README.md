# Perth Events Scraper

A comprehensive web application that scrapes and displays events happening in Perth, including dining deals, outdoor cinema screenings, markets, and sports events.

## 🌟 Features

- **Web Scraping**: Automated collection of event data from various sources
  - Restaurant deals and special dinners
  - Outdoor cinema screenings
  - Markets
  - Sports events (AFL, NRL, cricket, basketball, tennis)

- **Interactive Calendar**: View events in a beautiful calendar format
- **List View**: Browse events in a list with filtering options
- **Category Filtering**: Filter events by type (dining, cinema, markets, sports)
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🏗️ Architecture

### Backend (Python)
- **FastAPI**: RESTful API for serving event data
- **Web Scraping**: BeautifulSoup and Requests for data collection
- **Database**: In-memory storage with support for DynamoDB/MongoDB
- **Testing**: Comprehensive test suite with pytest

### Frontend (Next.js)
- **React**: Modern UI with hooks and functional components
- **Next.js 15**: Server-side rendering and optimal performance
- **TailwindCSS**: Responsive and modern styling
- **React Big Calendar**: Interactive calendar component

### Infrastructure (AWS + Terraform)
- **ECS/Fargate**: Container orchestration
- **ECR**: Docker image registry
- **VPC**: Network isolation and security
- **ALB**: Load balancing and routing
- **S3 + CloudFront**: Static asset hosting and CDN

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker (optional)
- AWS Account (for deployment)

### Local Development

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn api.main:app --reload

# Run tests
pytest
```

The API will be available at `http://localhost:8000`

#### Frontend Setup

```bash
cd my-app

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

The frontend will be available at `http://localhost:3000`

### Running with Docker

```bash
# Backend
docker build -t perth-events-backend ./backend
docker run -p 8000:8000 perth-events-backend

# Frontend
docker build -t perth-events-frontend ./my-app
docker run -p 3000:3000 perth-events-frontend
```

## 📁 Project Structure

```
├── backend/               # Python backend
│   ├── api/              # FastAPI application
│   ├── models/           # Data models
│   ├── scrapers/         # Web scrapers
│   ├── utils/            # Utilities and database
│   ├── tests/            # Test suite
│   └── requirements.txt  # Python dependencies
│
├── my-app/               # Next.js frontend
│   ├── app/             # Next.js app directory
│   │   ├── components/  # React components
│   │   └── lib/         # Utilities and API client
│   ├── public/          # Static assets
│   └── package.json     # Node dependencies
│
├── infrastructure/       # Terraform configuration
│   ├── bootstrap/       # S3 backend setup
│   └── main/           # Main infrastructure
│       └── modules/    # Reusable modules
│
└── .github/
    └── workflows/       # CI/CD pipelines
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest --cov=. --cov-report=html
```

### Frontend Linting
```bash
cd my-app
npm run lint
```

## 🔄 CI/CD

The project includes GitHub Actions workflows for:

- **Backend Tests**: Automated Python testing and linting
- **Frontend Tests**: ESLint and build validation
- **Security Scanning**: Dependency and container vulnerability scanning
- **Terraform Deployment**: Infrastructure provisioning and application deployment

## 🌐 API Endpoints

- `GET /` - API information
- `GET /api/events` - List all events (with filters)
- `GET /api/events/{id}` - Get specific event
- `GET /api/categories` - List event categories
- `POST /api/scrape` - Trigger manual scraping
- `GET /health` - Health check

## 🛠️ Infrastructure

Infrastructure is defined using Terraform and includes:

- VPC with public/private subnets
- ECS cluster with Fargate
- Application Load Balancer
- ECR repositories
- IAM roles and policies
- Security groups

To deploy:

```bash
cd infrastructure/main
terraform init
terraform plan
terraform apply
```

## 📝 Adding New Scrapers

To add a new event source:

1. Create a new scraper in `backend/scrapers/`
2. Inherit from `BaseScraper`
3. Implement the `scrape()` method
4. Add to `run_all.py`

Example:

```python
from .base_scraper import BaseScraper
from models.event import Event, EventCategory, EventType, Location

class MyNewScraper(BaseScraper):
    def __init__(self):
        super().__init__("MyNewScraper")
    
    def scrape(self):
        events = []
        # Your scraping logic here
        return events
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Event data sourced from various Perth-based websites and organizations
- Built with modern web technologies and best practices
- Deployed on AWS infrastructure

## 📧 Contact

For questions or suggestions, please open an issue on GitHub.
