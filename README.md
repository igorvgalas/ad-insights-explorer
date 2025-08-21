# Ad Insights Explorer Lite

A lightweight full-stack application to fetch, analyze, and display post data from the JSONPlaceholder API.

---

## Features

### Backend (FastAPI)
- Fetches real-time posts from JSONPlaceholder.
- Detects:
  - Short titles
  - Duplicate titles
  - Too many similar titles using semantic similarity
- Provides summary:
  - Anomalies
  - Top users with unique words in post
  - Most common words in posts
- Caching and fallback with TTL
- Logging and error handling
- Full test coverage (unit & integration)

### Frontend (React + React Query + TanStack Table + Chackra UI)
- Anomalies Table with sorting & filtering
- Summary Panel with insights
- Easily testable and modular structure

---

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

📄 Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### API Endpoints

| Endpoint      | Description                     |
|---------------|---------------------------------|
| `/posts`      | Fetch all posts                 |
| `/anomalies`  | Detect anomalies in titles      |
| `/summary`    | Generate post insights summary  |

### Testing

```bash
cd backend
pytest tests/
```

Test coverage includes:
- Detectors (short, duplicate, similar)
- PostFetcher (mocked httpx)
- API endpoints (integration via `httpx.AsyncClient`)

---

##  Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

### Folder Structure

```
frontend/
├── src/
│   ├── components/     # UI components
│   ├── hooks/          # React Query + logic
│   ├── pages/          # Pages
│   └── services/       # API functions
```

---

## ✍️ Author

Ihor Halas – [GitHub](https://github.com/YOUR_USERNAME)