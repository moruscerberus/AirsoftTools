# AirsoftTools

**AirsoftTools** is a sleek, mobile-friendly ballistics and safety calculator tailored for airsoft players.

Created with ❤️ by **moruscerberus**

---

## 📸 Features

- Muzzle velocity & joules calculator
- Unit conversion (FPS ↔ m/s)
- 🎯 Hit accuracy based on deviation & wind
- 📊 Range chart (powered by Chart.js)
- 🧠 Swedish 2020 Tabellen safety classification
- 🔐 Save/load configs to browser
- 🔗 Shareable config links (UTM-style)
- 📥 Export results to CSV
- 🌙 Dark mode toggle
- 🧭 Fully mobile responsive
- ⚙ MIT Licensed

---

## 🚀 Quick Start

### 🧱 Requirements

- Docker (recommended)
- OR: Python 3.10+ with pip (manual setup)

---

## 🐳 Deploy with Docker

### 1. Clone the repository

```bash
git clone https://github.com/moruscerberus/AirsoftTools.git
cd AirsoftTools
```

### 2. Build the Docker image

```bash
docker build -t airsofttools .
```

### 3. Run the container

```bash
docker run -d -p 8000:8000 --name airsofttools airsofttools
```

Now access:

```
http://localhost:8000
```

Or from your LAN IP:

```
http://127.0.0.1:8000
```

---

## ⚙ Manual Installation (Local Dev)

```bash
# Clone the repo
git clone https://github.com/moruscerberus/AirsoftTools.git
cd AirsoftTools

# Set up Python virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Django dev server
python manage.py runserver
```

Then open:

```
http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
├── base/                   # HTML/CSS/JS UI
├── AirsoftTools/           # Django app for serving/indexing
├── Dockerfile              # 🐳 Container config
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧠 Planned Features

| Feature                          | Status     |
| -------------------------------- | ---------- |
| Add More Safety Standards        | 🕐 Planned |
| PWA Support (Offline Mode)       | 🕐 Planned |
| Legal Mode Toggle by Country     | ✅ Done    |
| Community Presets Upload/Import  | ✅ Done    |
| Engagement Distance Highlighting | ✅ Done    |
| Advanced Toggle (UX)             | ✅ Done    |

---

## 🤝 Contributing

Got ideas or bugfixes? PRs welcome!
Fork the repo, make changes, and open a pull request 🚀

---

## 📄 License

**MIT License**
© 2025 moruscerberus
Developed with care by [@moruscerberus](https://github.com/moruscerberus)
