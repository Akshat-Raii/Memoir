# memoir 📝 FastAPI Notes App

This project is a **FastAPI-based Notes Application** that allows users to add and manage notes with a simple web interface.

---

## 🚀 Features

- ⚡ Built with **FastAPI** for high-performance backend.
- 🗂 Uses **MongoDB** for storing notes.
- 📝 Supports adding notes through a web form.
- 🎨 Integrated with **Jinja2 Templates** for rendering HTML pages.
- 📦 Static files served (**CSS, JS, images**) for frontend styling.

---

## 📂 Project Structure

- **main.py** → Contains routes for adding and displaying notes, with MongoDB integration.
- **index.py** → Initializes the FastAPI app, mounts static files, and includes routes.
- **templates/** → Jinja2 templates for rendering HTML pages.
- **static/** → CSS/JS and other frontend assets.
- **models/**, **schemas/**, **routes/** → Organized code structure for scalability.

---

## ⚡ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** MongoDB
- **Templating:** Jinja2
- **Frontend Assets:** Static files (CSS/JS)

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/FastAPI-NotesApp.git](https://github.com/your-username/FastAPI-NotesApp.git)
cd FastAPI-NotesApp
```

### 2. Create a virtual environment & activate it

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
# venv\Scripts\activate    # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up MongoDB
Make sure you have MongoDB running locally or use a cloud provider (e.g., MongoDB Atlas). Update your MongoDB URI in main.py or a .env file.

### 5. Run the FastAPI app

```bash
uvicorn index:app --reload
```

### 6. Open in browser

Navigate to: http://127.0.0.1:8000


## 🙌 Contributing
Contributions are welcome! 🎉
Feel free to fork this repo, create a new branch, and submit a pull request.