# ChessInsight ♟️

A modern, full-stack chess analysis application that provides powerful insights into chess games and positions.

## 🌟 Overview

ChessInsight is a comprehensive chess analysis platform built with modern web technologies. It combines a powerful Python backend with chess engine integration and a sleek React frontend to deliver an intuitive chess analysis experience.

## ✨ Features

- 🎯 **Chess Position Analysis** - Analyze any chess position with advanced algorithms
- 🔍 **Game Insights** - Get detailed insights into chess games
- 🚀 **Fast & Responsive** - Built with modern, performant technologies
- 🎨 **Modern UI** - Beautiful, responsive interface built with React and TailwindCSS
- 🐳 **Docker Support** - Easy deployment with Docker and Docker Compose
- 📊 **RESTful API** - Well-documented API for extensibility

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Python Chess** - Chess logic and analysis
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Lightweight database
- **Uvicorn** - ASGI server

### Frontend
- **React 19** - Latest React features
- **TypeScript** - Type-safe JavaScript
- **Vite** - Next-generation build tool
- **TailwindCSS 4** - Utility-first CSS framework
- **TanStack React Query** - Powerful data synchronization
- **React Router v7** - Client-side routing
- **Axios** - HTTP client

## 📁 Project Structure

```
ChessInsight/
├── backend/                 # FastAPI backend application
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Core configurations
│   │   ├── db/             # Database models
│   │   ├── services/       # Business logic
│   │   └── main.py         # Application entry point
│   ├── Dockerfile
│   ├── requirements.txt
│   └── README.md
│
├── frontend/               # React frontend application
│   ├── src/
│   │   ├── api/           # API client and services
│   │   ├── hooks/         # Custom React hooks
│   │   ├── pages/         # Page components
│   │   └── assets/        # Static assets
│   ├── Dockerfile
│   ├── package.json
│   └── README.md
│
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** (recommended)
  - OR -
- **Python 3.9+** and **Node.js 18+** (for local development)

### Option 1: Docker Compose (Recommended)

The easiest way to run the entire application:

```bash
# Clone the repository
git clone <repository-url>
cd ChessInsight

# Start all services
docker-compose up

# Or run in detached mode
docker-compose up -d
```

The application will be available at:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

### Option 2: Local Development

#### Backend Setup

```bash
cd backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
echo "VITE_API_BASE_URL=http://localhost:8000" > .env

# Run the development server
npm run dev
```

## 📚 Documentation

### API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Component Documentation

Detailed documentation for each component:
- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)

## 🔧 Configuration

### Environment Variables

#### Backend (.env in backend/)
```env
ENV=development
DATABASE_URL=sqlite:///./chessinsight.db
API_HOST=0.0.0.0
API_PORT=8000
```

#### Frontend (.env in frontend/)
```env
VITE_API_BASE_URL=http://localhost:8000
```

### Docker Compose

The `docker-compose.yml` file configures both services. Modify it to change ports or environment variables:

```yaml
services:
  backend:
    ports:
      - "8000:8000"
  frontend:
    ports:
      - "5173:5173"
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 🛣️ Roadmap

- [ ] Chess position input via FEN notation
- [ ] Stockfish engine integration for move suggestions
- [ ] Game database and PGN import
- [ ] Opening book and repertoire builder
- [ ] Puzzle generator
- [ ] User authentication and game history
- [ ] Real-time multiplayer analysis
- [ ] Mobile app

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Development Workflow

### Making Changes

1. **Backend changes**: Modify files in `backend/app/`
   - FastAPI auto-reloads on file changes
   - View logs: `docker-compose logs -f backend`

2. **Frontend changes**: Modify files in `frontend/src/`
   - Vite provides instant HMR
   - View logs: `docker-compose logs -f frontend`

### Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Rebuilding After Dependencies Change

```bash
# Rebuild all services
docker-compose build

# Rebuild and restart
docker-compose up --build
```

## 🐛 Troubleshooting

### Port Already in Use

If you see port conflict errors:
```bash
# Check what's using the port
lsof -i :8000  # Backend
lsof -i :5173  # Frontend

# Kill the process or change ports in docker-compose.yml
```

### Database Issues

Reset the database:
```bash
cd backend
rm chessinsight.db  # Remove the database file
# Restart the backend to recreate
```

### Frontend Can't Connect to Backend

1. Check that backend is running: `curl http://localhost:8000/health`
2. Verify `VITE_API_BASE_URL` in frontend/.env
3. Check CORS settings in backend/app/main.py

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

Dev Kumar

## 🙏 Acknowledgments

- FastAPI for the amazing Python web framework
- React team for the incredible frontend library
- python-chess for comprehensive chess logic
- The open-source community for inspiration and tools

## 📞 Support

If you have any questions or run into issues:
- Open an issue in the repository
- Check existing documentation in `/backend/README.md` and `/frontend/README.md`

---

**Happy Chess Analysis!** ♟️

