# ChessInsight Backend

The backend service for ChessInsight, a chess analysis application built with FastAPI.

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.x
- **Database**: SQLite with SQLAlchemy ORM
- **Chess Engine**: python-chess library
- **Server**: Uvicorn ASGI server
- **Containerization**: Docker

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── v1/          # API version 1 endpoints
│   │       └── health.py
│   ├── core/            # Core configurations
│   │   └── config.py
│   ├── db/              # Database models and connections
│   ├── services/        # Business logic and services
│   │   └── stockfish_test.py
│   └── main.py          # Application entry point
├── Dockerfile
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Installation

### Local Development

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Docker Development

Build and run the backend container:
```bash
docker build -t chessinsight-backend .
docker run -p 8000:8000 chessinsight-backend
```

Or use docker-compose from the project root:
```bash
cd ..
docker-compose up backend
```

## Running the Application

### Local Development

Start the development server with hot-reload:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base URL**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Production

For production deployment:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Endpoints

### Health Check
- **Endpoint**: `GET /api/v1/health`
- **Description**: Check if the service is running
- **Response**:
  ```json
  {
    "status": "ok",
    "message": "ChessInsight is running"
  }
  ```

### Root
- **Endpoint**: `GET /`
- **Description**: Root endpoint
- **Response**:
  ```json
  {
    "message": "ChessInsight backend running"
  }
  ```

## Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
ENV=development
DATABASE_URL=sqlite:///./chessinsight.db
API_HOST=0.0.0.0
API_PORT=8000
```

## Dependencies

Key dependencies include:

- `fastapi` - Modern web framework for building APIs
- `uvicorn[standard]` - ASGI server
- `pydantic` - Data validation using Python type annotations
- `python-dotenv` - Environment variable management
- `sqlalchemy` - SQL toolkit and ORM
- `aiosqlite` - Async SQLite support
- `python-chess` - Chess library for game analysis

## Development

### Adding New Endpoints

1. Create a new router file in `app/api/v1/`
2. Define your endpoints using FastAPI decorators
3. Include the router in `app/main.py`

Example:
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def example_endpoint():
    return {"message": "Example"}
```

### Database Migrations

(To be implemented with Alembic)

## Testing

Run tests with pytest:
```bash
pytest
```

## CORS Configuration

The backend is configured to accept requests from:
- http://localhost:5173 (Vite dev server)
- http://127.0.0.1:5173

Update `app/main.py` to add additional origins if needed.

## License

MIT

## Support

For issues and questions, please open an issue in the repository.

