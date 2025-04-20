# 🧠 AI Tower Pathfinder

A fullstack Flask web application simulating an AI navigating through an 8-floor tower. Using **Breadth-First Search (BFS)**, the AI avoids hazards, unlocks doors, and collects keys to reach the summit.

---

## 🚀 Features

- Web-based interface using HTML, CSS, and JavaScript
- Flask backend handles BFS logic and path reconstruction
- 8 floors of 5x5 grid input
- Hazard levels (0-3), stairs (`S`), keys (`K`), locked doors (`L`), and manip keys (`M`)
- Safely manages key and hazard limits
- Displays reconstructed path to the summit

---

## 📦 Files

| File           | Description                                      |
|----------------|--------------------------------------------------|
| `BFS.py`       | Contains the BFS search and path logic           |
| `app.py`       | Flask server to handle frontend-backend comms    |
| `templates/`   | HTML templates for UI                            |
| `static/`      | JS and CSS files for frontend interactivity      |

---

## 🖥️ How to Run

```bash
# Step 1: Clone the repo
git clone https://github.com/your-username/AI-Tower-Pathfinder.git
cd AI-Tower-Pathfinder

# Step 2: Install Flask
pip install flask

# Step 3: Run the Flask app
python app.py

# Visit http://127.0.0.1:5000 in your browser to start using the app
```

---

## 📸 Screenshot
_Add a screenshot of your UI here to show how it looks!_

---

## 🧩 Credits
- Built with Flask, HTML, JavaScript, and Python
- BFS pathfinding logic designed for hazard-aware traversal

---

## 📜 License
MIT License

