# TaskBoard – B2B SaaS Team Task Management Platform

TaskBoard is a B2B SaaS team task management platform designed for modern organizations. It supports multiple organizations, team members, roles, permissions, subscriptions, and billing — making it ideal for teams that need structure, collaboration, and scalability.



## Features

- Organization-based workspace
- Multiple team members per organization
- Roles and permissions (admin, editor, etc.)
- Task management with status tracking
- Subscription and billing support
- Secure authentication and user management via Clerk

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Uvicorn
- Clerk (auth, users, orgs, billing)

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- Clerk React SDK

## Project Structure

```
/
├── backend/ # FastAPI backend
└── frontend/ # Next.js frontend
```


## Getting Started

### Backend Setup

```bash
cd backend
uv init .
uv add fastapi uvicorn sqlalchemy python-dotenv pyjwt clerk svix
uv run start.py
```

Backend will run at:

```bash
http://localhost:8000
```

### Frontend Setup

```
cd frontend
npm install
npm run dev
```

Frontend will run at:

```bash
http://localhost:5173
```

## Environment Variables

Both backend and frontend require environment variables for Clerk and database configuration.

Create `.env` files in both folders:

```bash
CLERK_SECRET_KEY=your_secret_key
CLERK_PUBLISHABLE_KEY=your_publishable_key
DATABASE_URL=your_database_url
```

## Scripts


### Frontend

```
npm run dev     # Start development server
npm run build   # Build for production
npm run lint    # Run linter
```

### Backend

```
uv run start.py
```

## License

This project is licensed under the MIT License.