# 🛍️ Django E-Commerce Platform

## 🌟 Key Features
| Feature | Description | Tech Used |
|---------|-------------|-----------|
| **🔐 User Auth** | Secure registration, login, logout | Django Auth, Sessions |
| **🛒 Cart System** | Add/remove items, quantity adjustment | Django Sessions, AJAX |
| **📦 Order Management** | Checkout, order history, invoices | Django Models, PDF generation |
| **📱 Responsive UI** | Mobile-friendly product browsing | Bootstrap 5, Flexbox |
| **🔍 Product Catalog** | Categories, search, filters | Django ORM, Q Objects |

## � Project Structure
```bash
e_shop/
├── core/                   # Main app
│   ├── models.py           # Product, Order, UserProfile
│   ├── views.py            # Cart, Checkout, Product views
│   ├── templates/          # HTML files
│   │   ├── base.html       # Bootstrap layout
│   │   ├── cart.html       # Interactive cart
│   │   └── checkout.html   # Order form
├── static/
│   ├── css/                # Custom Bootstrap overrides
│   └── js/                 # Cart AJAX handlers
├── requirements.txt        # Django, Pillow, ReportLab
└── manage.py


## 📋 Prerequisites
- Python 3.8+
- Git
- pip
- Virtualenv (recommended)

# 🚀 Setup Guide
```
# Clone & Run (Development)
```bash
# Clone the repository
git clone https://github.com/muhammadtaha0022/e_shop.git && cd e_shop

# Set up virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Unix/MacOS:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Create admin user (optional)
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

