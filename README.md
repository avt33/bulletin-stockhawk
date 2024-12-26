# StockHawk Knowledge Base

A Flask-based knowledge base application for StockHawk.

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your environment variables
6. Initialize the database: `flask db upgrade`
7. Run the application: `flask run`

## Features

- User authentication
- Admin dashboard
- Rich text editor with image upload
- Folder organization
- Search functionality
- Tag support

## Deployment

The application is configured for deployment on Vercel. 