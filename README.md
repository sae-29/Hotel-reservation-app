# 🏨 StayGrid — Smart Hotel Room Reservation System

A high-performance hotel reservation system with an intelligent room allocation algorithm that minimizes guest travel distance. Book rooms on the same floor or intelligently distribute across multiple floors using an optimized algorithm.

**Live Demo**: ([https://hotel-reservation-app-d9v6.onrender.com/])

---

## ✨ Features

- **Smart Room Allocation**: Automatically books rooms based on proximity & floor clustering
- **Same-Floor Preference**: Uses sliding window algorithm O(n) to find tightest room clusters
- **Multi-Floor Optimization**: Minimizes travel distance with weighted combination algorithm
- **97-Room Hotel**: 10 floors with realistic room numbering (101-110, 201-210, etc.)
- **Real-Time Dashboard**: Modern glassmorphism UI with live occupancy visualization
- **Booking History**: Track all bookings with timestamps and room allocations
- **Random Occupancy**: Fill hotel with random bookings for testing
- **One-Click Reset**: Clear all bookings instantly
- **Zero Dependencies Frontend**: Vanilla JavaScript (no React, Vue, or frameworks)

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+ + Flask 2.3 |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Database** | In-memory (session-based) |
| **Deployment** | Railway, Render, Heroku, PythonAnywhere |

---

## 📁 Project Structure

```
hotel-reservation-app/
├── app.py                      # Flask server & API routes
├── models.py                   # HotelModel class (97 rooms, 10 floors)
├── services.py                 # BookingService with allocation algorithms
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── templates/
    └── index.html              # Modern UI with glassmorphism design
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed
- Git (optional, for version control)

### Installation & Run Locally

```bash
# Clone or download the project
cd hotel-reservation-app

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

**Open in browser**: http://localhost:5000

The server will start on `http://127.0.0.1:5000` by default.

---

## 🌐 Hosting & Deployment (Get a Live URL)


### **Render**

1. **Push to GitHub** (same steps as Option 1)

2. **Deploy on Render**:
   - Go to [render.com](https://render.com)
   - Click **"New +"** → **"Web Service"**
   - Connect your GitHub repo
   - Fill in these settings:
     - **Name**: `hotel-reservation-app`
     - **Environment**: `Python 3`
     - **Build command**: `pip install -r requirements.txt`
     - **Start command**: `python app.py`
   - Click **"Create Web Service"**
   - Live URL appears after deployment (usually 5-10 mins)

---


## 🧠 Algorithm Explanation

### Same-Floor Booking (O(n))
- **Goal**: Find closest cluster of N consecutive rooms on one floor
- **Method**: Sliding window scans each floor
- **Result**: Guests stay together, minimize hallway distance

### Multi-Floor Booking (Optimized)
- **Goal**: Distribute rooms across floors while minimizing total travel
- **Scoring**: `(floor_difference × 2) + position_difference`
- **Result**: Balanced distribution when same-floor unavailable

### Room Numbering
- **Floors 1-9**: 10 rooms each (101-110, 201-210, ..., 901-910)
- **Floor 10**: 7 rooms (1001-1007)
- **Position 1**: Closest to lift/stairs (least travel)

---

## 📝 License

MIT License - Free to use and modify

---

## 📞 Support

- **Issues**: Check the code comments in `app.py`, `models.py`, `services.py`
- **Deployment Help**: Each platform has detailed docs linked above
- **Local Testing**: Run `python app.py` and visit http://localhost:5000
