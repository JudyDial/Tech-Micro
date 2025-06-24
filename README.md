# Tech-Micro

Tech-Micro is a Django-based web application project for a consultation firm. This repository contains the source code for the website, including static assets, templates, and Django app configuration.

## Features
- Django web framework setup
- Modular app structure
- Static files (CSS, JS, images) organized for easy management
- Ready-to-use templates for rapid development

## Project Structure
```
Tech-Micro/
├── manage.py
├── requirements.txt
├── TechMicro/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── website/             # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   └── templates/
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip
- (Optional) Virtual environment tool (venv, virtualenv, etc.)

### Installation
1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd Tech-Micro
   ```
2. **Create and activate a virtual environment (recommended):**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
6. **Access the site:**
   Open your browser and go to `http://127.0.0.1:8000/`

## Project Usage
- Place your static files in `website/static/`
- Place your HTML templates in `website/templates/`
- Add your Django models, views, and URLs in the `website/` app

## License
This project is licensed under the terms of the LICENSE file in this repository.
