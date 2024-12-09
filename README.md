
# Django Digital Resume Builder  

A professional digital resume builder powered by Django. This project enables users to create, manage, and showcase resumes with dynamic sections, including skills, education, portfolio, testimonials, blogs, and more.

---

## Features  

### Dynamic Resume Builder  
- **Personal Information**: Upload profile photo, add contact details, and write a professional bio.  
- **Skills**: Manage technical and soft skills with proficiency indicators and optional icons/images.  
- **Portfolio**: Showcase projects with images, descriptions, and rich-text content.  
- **Testimonials**: Highlight client or peer feedback with quotes, roles, and thumbnail images.  
- **Certificates**: Add and manage certifications with dates and descriptions.  
- **Blog Integration**: Write and display blog posts with full-text editor support (CKEditor).  

### Additional Features  
- **Responsive Design**: Optimized for both mobile and desktop.  
- **Dynamic Routing**: Blog and portfolio detail pages use slugs for clean URLs.  
- **Admin Dashboard**: Manage all content from Django's admin interface.  
- **Contact Form**: Users can submit inquiries with email notifications.  

---

## Technologies Used  

- **Backend**: Django, Python  
- **Frontend**: HTML5, CSS3, Bootstrap  
- **Rich Content**: CKEditor for blog and portfolio content editing  
- **Database**: SQLite (default, configurable to other RDBMS)  

---

## Setup Instructions  

### Prerequisites  
- Python >= 3.8  
- Django >= 4.x  
- Install `pip` for managing dependencies  

### Installation  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/Mohamed-Taha-Essa/Django-digital-resume.git  
   cd Django-digital-resume  
   ```  

2. **Set up a virtual environment**:  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Windows: venv\Scripts\activate  
   ```  

3. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. **Apply migrations**:  
   ```bash  
   python manage.py migrate  
   ```  

5. **Run the development server**:  
   ```bash  
   python manage.py runserver  
   ```  

6. **Access the application**:  
   - Default: `http://127.0.0.1:8000/`  

---

## Project Structure  

```plaintext  
Django-digital-resume/  
│  
├── resume/  
│   ├── models.py       # Database models for skills, portfolio, blogs, etc.  
│   ├── views.py        # Views to handle resume sections  
│   ├── urls.py         # URL routing for the application  
│   ├── forms.py        # Forms for contact submission  
│   ├── templates/      # HTML templates for rendering  
│   ├── static/         # Static files (CSS, JS, images)  
│   ├── signals.py      # Signal handlers for creating user profiles  
│   ├── context_processors.py  # Custom context processors  
│  
├── manage.py           # Django management script  
├── settings.py         # Project settings  
└── requirements.txt    # Project dependencies  
```  

---

## Key Code Highlights  

### Models  
- `Skill`, `UserProfile`, `Portfolio`, `Blog`, and `Certificate` models for dynamic resume sections.  
- `ContactProfile` to store contact form submissions.  

### Views  
- `IndexView`: Renders the homepage with dynamic content like testimonials, portfolio, and skills.  
- `BlogView` & `PortfolioView`: Paginated lists of blog posts and portfolio projects.  
- `ContactView`: Handles form submissions with success messages.  

### Signals  
- Automatically creates a `UserProfile` instance when a new user is created.  

---

## Screenshots  

_Add screenshots of the homepage, portfolio, blog, and admin panel._  

---

## Contributing  

1. **Fork the repository**.  
2. **Create a new branch** for your feature:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. **Commit your changes**:  
   ```bash  
   git commit -m "Add feature description"  
   ```  
4. **Push to your branch**:  
   ```bash  
   git push origin feature-name  
   ```  
5. Submit a **pull request**.  




