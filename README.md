# 🏨 StayGrid — Smart Hotel Room Reservation System

A high-performance hotel reservation system with an intelligent room allocation algorithm that minimizes guest travel distance. Book rooms on the same floor or intelligently distribute across multiple floors using an optimized algorithm.

**Live Demo**: [Deploy to see it in action](#-hosting--deployment)

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

### Option 1: **Railway** ⭐ (Recommended - Easiest)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/hotel-reservation-app.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Railway**:
   - Go to [railway.app](https://railway.app)
   - Click **"New Project"** → **"Deploy from GitHub"**
   - Select your repository
   - Click **"Deploy"**
   - Get Live URL in 2-3 minutes!

3. **Configuration** (optional):
   - Railway auto-detects Python + Flask
   - No additional setup needed
   - Your app is live at `https://your-app.railway.app`

---

### Option 2: **Render** (Free tier available)

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

### Option 3: **Heroku** (Paid tier only now)

1. **Push to GitHub** (same as Option 1)

2. **Deploy**:
   - Go to [heroku.com](https://heroku.com)
   - Click **"New"** → **"Create New App"**
   - Connect your GitHub repo
   - Click **"Deploy Branch"**

*Note: Heroku discontinued free tier, but you can try the 5-50 paid tier*

---

### Option 4: **PythonAnywhere** (Easy, Python-focused)

1. **Upload files**:
   - Go to [pythonanywhere.com](https://pythonanywhere.com)
   - Sign up (free account available)
   - Upload your files via dashboard

2. **Configure**:
   - Create a new web app
   - Select Flask + Python 3.10
   - Point to your `app.py`
   - Reload the app

3. **Get URL**: Your app runs at `https://YOUR_USERNAME.pythonanywhere.com`

---

### Option 5: **DigitalOcean App Platform** (More control)

1. **Push to GitHub** (same as Option 1)

2. **Deploy**:
   - Go to [digitalocean.com/products/app-platform](https://www.digitalocean.com/products/app-platform)
   - Click **"Create App"** → select your GitHub repo
   - Configure resource type: **Basic** ($5/month minimum)
   - Deploy

---

## 📡 API Reference

### Get Hotel State
```http
GET /api/state
```
**Response**: Full hotel occupancy data (all 97 rooms with status)

---

### Book Rooms
```http
POST /api/book
Content-Type: application/json

{
  "count": 2
}
```

**Parameters**:
- `count` (integer): Number of rooms to book (1-5)

**Response**:
```json
{
  "booked": [101, 102],
  "travel": 0,
  "state": { /* full hotel state */ }
}
```

---

### Random Occupancy
```http
POST /api/random
Content-Type: application/json

{
  "count": 10
}
```

**Effect**: Randomly fills N rooms across available rooms

---

### Reset All Bookings
```http
POST /api/reset
```

**Effect**: Clears all bookings, resets hotel to full availability

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

## 🎨 UI Features

- **Real-Time Occupancy Grid**: Visual floor-by-floor room status
- **Booking Form**: Easy room count selection (1-5 rooms)
- **History Panel**: Track all bookings with timestamps & room numbers
- **Modern Design**: Glassmorphism effect, Red Bull color scheme
- **Responsive**: Works on desktop and tablet

---

## 🤝 Contributing

Feel free to fork, modify, and improve! Some ideas:
- Add room type selection (Standard, Deluxe, Suite)
- Implement date-range booking
- Add user authentication
- Database persistence (SQLite, PostgreSQL)
- Mobile app version

---

## 📝 License

MIT License - Free to use and modify

---

## 📞 Support

- **Issues**: Check the code comments in `app.py`, `models.py`, `services.py`
- **Deployment Help**: Each platform has detailed docs linked above
- **Local Testing**: Run `python app.py` and visit http://localhost:5000
