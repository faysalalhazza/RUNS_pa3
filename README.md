# RUNS - Social Media Web App
### COP 4813 — PA3: Data Models

**Team:** Faisal Alhazza, Gabby, Nickelli  
**GitHub:** https://github.com/faysalalhazza/RUNS_pa3  
**Branch:** pa3

---

## How to Run
```bash
pip install django
cd webapps
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit: http://localhost:8000

## Test User Setup
```bash
python manage.py shell
```
```python
from django.contrib.auth.models import User
from runs.models import UserProfile, Post

u = User.objects.create_user(username='NPB25_', first_name='Test', last_name='User', password='testpass123')
UserProfile.objects.create(user=u)
Post.objects.create(author=u, content='Hello World!')
Post.objects.create(author=u, content='Im tired')
Post.objects.create(author=u, content="What's Forrest Gump's password? 1forrest1.")
exit()
```

---

## Q1 — Database Schema

We used two tables on top of Django's built-in auth_user:

- **runs_userprofile** — extends the default user with an optional middle name field. Has a OneToOne foreign key to auth_user.
- **runs_post** — stores each post: content (max 42 chars), author (FK to auth_user), timestamp, and location (optional).

Default auto-increment primary keys on everything. No custom PKs needed.

## Q2 — First Record Primary Key

It's 1. Django/SQLite starts counting from 1.

## Q3 — Time & Feedback

Took us around 8-10 hours. The OneToOne relationship between UserProfile and Django's built-in User took a bit to figure out but made sense once we got it working. Pretty solid assignment overall — would've helped to see a model relationship example in class beforehand.

---

## External Resources
- Django docs: https://docs.djangoproject.com/
- Bootstrap: https://getbootstrap.com/
- Google Fonts: https://fonts.google.com/