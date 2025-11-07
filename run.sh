#!/bin/bash
echo "🚀 Setting up Spam Email Detector..."

python3 -m venv venv
source venv/bin/activate

pip install flask flask-cors scikit-learn pandas

echo "📚 Training model..."
python3 backend/train_model.py

echo "🔥 Starting Flask server..."
python3 backend/app.py
