
# 🤖 AutoCAD-Style Robotic Arm Controller (React + Python + Raspberry Pi)

This project brings together the power of **Raspberry Pi**, **Python**, **Inverse Kinematics**, and **React** to control a physical 2D robotic arm from a browser interface – just like a simplified AutoCAD drawing machine.

> A perfect blend of embedded systems, mechanical control, web technologies, and real-time computation.

---

## 📦 Project Structure

```
RoboticArmDrawing/
├── backend/
│   ├── app.py                 # Flask server to receive coordinate input and control servos
│   ├── inverse_kinematics.py  # IK calculations for robotic arm
│   └── utils/
│       └── svg_to_coords.py   # SVG parsing and path extraction
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js             # Canvas drawing interface
│       └── api.js             # Send coordinates to backend
├── hardware/
│   ├── wiring_diagram.png     # Servo and sensor wiring
│   └── calibration_notes.md   # Calibration angles and offsets
└── README.md
```

---

## ⚙️ Features

- ✍️ Browser-based 2D drawing interface
- 🔁 Inverse kinematics for (x, y) → θ1, θ2 angle conversion
- 📐 SVG to robotic path translation
- 🎯 Curve smoothing (Catmull-Rom / Bezier)
- ⚡ Real-time feedback and angle error correction
- 🌐 RESTful API integration with `Flask`
- 🎮 Smooth servo movement using PWM

---

## 🧰 Hardware Requirements

- Raspberry Pi 3/4 with RPi.GPIO or pigpio
- 2 or 3 DOF Robotic Arm with SG90/MG995 servo motors
- Power Supply (5V-6V, 2A+)
- Potentiometers / Rotary encoders (optional for feedback)
- Jumper wires, breadboard or PCB
- Optional: Camera for position validation

---

## 🧪 Software Stack

| Component     | Tech Used       |
|---------------|-----------------|
| Frontend      | React + Canvas  |
| Backend       | Python + Flask  |
| Hardware Ctrl | RPi.GPIO        |
| SVG Parser    | svgpathtools    |
| Smoothing     | Numpy, Custom   |

---

## 🚀 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/RoboticArmDrawing.git
cd RoboticArmDrawing
```

### 2. Backend (Flask + IK)

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### 3. Frontend (React)

```bash
cd frontend
npm install
npm start
```

### 4. Wiring Servos

- Connect servo PWM pins to GPIO 17, 18, 27 (as per your wiring).
- Power servos from external 5-6V.
- Optional: Add potentiometers for feedback.

---

## 🧠 How It Works

### 🧮 Inverse Kinematics

```python
import math

def inverse_kinematics(x, y, l1=10, l2=10):
    cos_angle = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2 = math.acos(cos_angle)
    theta1 = math.atan2(y, x) - math.atan2(l2 * math.sin(theta2), l1 + l2 * math.cos(theta2))
    return math.degrees(theta1), math.degrees(theta2)
```

### 🖼️ SVG to Coordinate Conversion

```python
from svgpathtools import svg2paths

def extract_svg_points(svg_file):
    paths, _ = svg2paths(svg_file)
    coords = []
    for path in paths:
        for segment in path:
            coords.append((segment.start.real, segment.start.imag))
    return coords
```

### 📐 Curve Smoothing (Catmull-Rom)

```python
def smooth_curve(points):
    # Simple Catmull-Rom smoothing
    return interpolate(points)  # Pseudocode
```

---

## 🧠 Feedback System (Optional)

- Add **rotary encoders** or **analog potentiometers** to joints.
- Use `ADC` to read angle values from each servo.
- Compare with expected angles and adjust PWM.

---

## 🧪 Troubleshooting

| Issue | Solution |
|-------|----------|
| Arm doesn’t move | Check GPIO and power supply |
| Incorrect angles | Calibrate `servo_min` and `servo_max` |
| App not loading | Make sure backend is running on `localhost:5000` |

---

## 📄 License

MIT License – Free to use, modify and distribute.

---

## 📢 Author

**Harisha Warnakulasuriya**  
_Robotics, AI, and Embedded Systems Developer_

---

**Happy Drawing! 🖊️🤖**
