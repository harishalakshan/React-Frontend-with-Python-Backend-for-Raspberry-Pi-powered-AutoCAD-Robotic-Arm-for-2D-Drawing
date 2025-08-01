# Robotic Arm 2D Drawing with React and Python Backend

This project connects a React.js frontend with a Python Flask backend to control a Raspberry Pi-powered robotic arm for drawing 2D shapes.

## Project Structure

- `backend/`: Flask API and servo control scripts
- `frontend/`: React UI to draw 2D shapes
- `docs/`: Documentation and flowcharts

## How to Run

### Backend (on Raspberry Pi)
```bash
cd backend
pip install flask flask-cors RPi.GPIO
python3 app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## Features

- Inverse Kinematics support
- SVG to servo translation
- Smoothing algorithms
- Real-time feedback with error correction

