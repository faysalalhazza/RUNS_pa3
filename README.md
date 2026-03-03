RUNS - Social Media Web App
### COP 4813 - Web Application Programming | PA3: Data Models

**Team Members:** [Faisal Alhazza,Gabby,Nickelli]

## Setup Instructions

1. **Install Django:**
   ```
   pip install django
   ```

2. **Run migrations to create the database:**
   ```
   cd webapps
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a test user (for demo purposes):**
   ```
   python manage.py shell
   ```
   Then in the shell:
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

4. **Run the development server:**
   ```
   python manage.py runserver
   ```

5. **Visit:** http://localhost:8000/

---

## Inline Questions

### Q1: Database Schema Design
The app uses **two tables** beyond Django's built-in auth tables:

- **runs_userprofile**: Extends the built-in `auth_user` table with a `OneToOneField` foreign key to `auth_user.id`, plus an optional `middle_name` field (VARCHAR). The default auto-incrementing integer is used as the primary key.

- **runs_post**: Stores each post with the following columns:
  - `id` (INTEGER, auto-increment primary key)
  - `content` (VARCHAR, max 42 characters)
  - `author_id` (INTEGER, foreign key → `auth_user.id`)
  - `created_at` (DATETIME, auto-set on creation)
  - `location` (VARCHAR, optional)

The built-in Django `auth_user` table provides: `id`, `username`, `first_name`, `last_name`, `password`, `email`, and other auth fields.

**Foreign key used:** `runs_post.author_id` references `auth_user.id`, and `runs_userprofile.user_id` references `auth_user.id`.

### Q2: Primary Key of First Record
When using Django's default primary key (auto-incrementing integer), the primary key of the **first record** created is **1**. Django starts the auto-increment counter at 1 for SQLite databases.

### Q3: Time Spent & Feedback
**Time spent:** Approximately [X] hours.

**Feedback:** [Add your thoughts here — e.g., the assignment was well-scoped, the data modeling concepts were clearly explained, etc.]

---

## External Resources
- Django Documentation: https://docs.djangoproject.com/
- Django Auth System: https://docs.djangoproject.com/en/stable/topics/auth/
- Google Fonts (Permanent Marker, Space Mono): https://fonts.google.com/

