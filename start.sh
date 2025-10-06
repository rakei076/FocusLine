#!/bin/bash

# FocusLine Quick Start Script

echo "FocusLine - 日本ニュースタイムライン"
echo "=================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit .env and add your OPENAI_API_KEY"
    echo "Note: The system will work without it, but with limited AI capabilities"
fi

# Start services
echo ""
echo "Starting FocusLine with Docker Compose..."
docker-compose up -d

echo ""
echo "Services starting..."
sleep 5

echo ""
echo "✓ Backend API: http://localhost:8000"
echo "✓ API Documentation: http://localhost:8000/api/v1/docs"
echo "✓ Frontend: http://localhost:3000"
echo ""
echo "View logs with: docker-compose logs -f"
echo "Stop services with: docker-compose down"
