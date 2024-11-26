

### **Commercework** ###

CommerceWork is an e-commerce web application built with Django. It supports product browsing, cart management, order processing, and user authentication. The project is hosted live on Render at:
https://commercework.onrender.com

### **Features** ###

**User Authentication**: Register, log in, and reset passwords.

**Product Management**: Add, edit, delete, and view products.

**Cart System**: Add products to the cart and checkout.

**Order Management**: View order success pages and order history.

**Admin Features** : Manage users, orders, and products via the Django Admin panel.


### **Getting Started** ###

**Prerequisites**

Make sure you have the following installed:

Python 3.8+

`````
Git

pip (Python package installer)
`````

**Virtual environment (recommended)**


**Clone the Repository**

To clone the repository, run the following commands:

`````
git clone https://github.com/HamadMulti/commercework.git
cd commercework
`````

**Set Up a Virtual Environment**

Windows:
`````

python -m venv venv
venv\Scripts\activate
`````
macOS/Linux:
`````
python3 -m venv venv
source venv/bin/activate
`````
**Install Dependencies**

Run the following command to install the necessary dependencies:
`````
pip install -r requirements.txt
`````
**Apply Migrations**

Apply the database migrations with the following command:
`````
python manage.py migrate
`````
**Create a Superuser**

To access the Django Admin panel, create a superuser by running:
`````
python manage.py createsuperuser
`````
Follow the prompts to create an admin account.

**Run the Server**

Start the development server:
`````
python manage.py runserver
`````
Access the project in your browser at http://127.0.0.1:8000.

### **DEPLOYMENT ON RENDER.COM** ###

**1. Sign Up for Render:**
Create an account at https://render.com.


**2. Connect the Repository:**
Create a Web Service and connect the repository:
https://github.com/HamadMulti/commercework.git.


**3. Configure Build Command:**
Set the build command as follows:
`````
pip install -r requirements.txt

`````
**4. Specify Start Command:**
Specify the start command for the application:
`````
gunicorn ecommerce_app.wsgi

`````
**5. Set Environment Variables:**
Add the following environment variables in Render:
```
SECRET_KEY: Your Django project's secret key.
```
```
DEBUG: False
````
```
ALLOWED_HOSTS: commercework.onrender.com
```


**6. Finalize Deployment:**
After deployment, open Render's shell and run:
`````
python manage.py migrate
python manage.py collectstatic
`````
Your project will be live at the provided Render URL.



### **Project Structure** ###
`````
commercework/
├── .github/
│   └── workflows/
│       └── django.yml
├── ecommerce/
│   ├── migrations/
│   ├── static/
│   │   └── ecommerce/css/
│   ├── templates/ecommerce 
│   │   ├── add_product.html
│   │   ├── base.html
│   │   ├── cart.html
│   │   ├── delete_product.html
│   │   ├── edit_product.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── order_success.html
│   │   ├── orders.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_done.html
│   │   ├── password_reset_form.html
│   │   ├── product_list.html
│   │   └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── ecommerce_app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
`````
### **Continuous Intergration** ###

The .github/workflows/django.yml file automates testing and ensures the project builds successfully before deployment.

### **Contributing** ###

Contributions are welcome! Here’s how you can help:

**1. Fork the repository:**
`````
git fork https://github.com/HamadMulti/commercework.git
`````

**2. Create a new branch:**
`````
git checkout -b feature/your-feature
`````

**3. Make your changes and commit:**
`````
git commit -m "Added a new feature"

`````
**4. Push to the branch:**
`````
git push origin feature/your-feature
`````

5. Submit a pull request.


### **Future Improvements** ###

While the project is functional and ready for deployment, there are several exciting features and improvements planned for future versions:

**1. Payment Integration**

To enable seamless online transactions, we plan to integrate popular payment gateways such as:

**Stripe**: A widely-used API that facilitates credit card and debit card payments, with support for recurring billing.

**PayPal**: Another popular payment gateway, allowing users to make payments through their PayPal accounts.

**Bank Transfer Integration**: Allowing customers to pay directly through bank transfers or through localized payment solutions depending on the user's region.


**2. Enhanced Order Management System**

To streamline order processing and offer better insights for both customers and admins, the following features will be added:

Order Tracking: Allow customers to track their order status in real time.

Advanced Analytics: Admin dashboard to analyze sales, user behavior, and inventory more effectively.


**3. Customer Reviews and Ratings**

Implement a customer review and rating system for products to help future buyers make informed decisions. Reviews can be integrated with a moderation system to ensure quality content.


### **LICENSE** ###

This project is licensed under the MIT License.


