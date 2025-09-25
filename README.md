# 📝 Django Quiz System

A simple and interactive quiz system built with **Django**.  
Users can answer multiple-choice questions, view their scores, and admins can add new questions via a form.

---

## 🚀 Features

- 🎯 Take a quiz with multiple-choice questions  
- 📊 Score calculation and results page  
- ➡️ Navigate question-by-question or take all at once  
- ✍️ Admins can insert new questions through a form  
- 🎨 Clean and responsive UI  

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS (custom styling)  
- **Database:** SQLite (default, can be swapped with PostgreSQL/MySQL)  

---

## 📂 Project Structure

quiz_project/ # Main project folder
│
├── quizapp/ # Core app
│ ├── migrations/
│ ├── templates/ # HTML templates
│ │ └── quizapp/
│ │ ├── quiz_home.html
│ │ ├── result_home.html
│ │ └── insert_question.html
│ ├── forms.py # Django forms
│ ├── models.py # Question model
│ ├── views.py # App views
│ └── urls.py # App routes
│
├── db.sqlite3 # Default database
├── manage.py # Django management file
└── README.md # Documentation
