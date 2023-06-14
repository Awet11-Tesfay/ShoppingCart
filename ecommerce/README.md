# Django eCommerce Website

This is a Django-based eCommerce website project that allows users to browse and purchase products online. It provides features such as user authentication, product catalog, shopping cart functionality, and order management.

## Features

- User Registration and Authentication: Users can sign up, log in, and log out of the website. Authentication is used to protect certain functionalities and ensure secure access.

- Product Catalog: The website displays a catalog of products with details such as name, description, price, and images. Users can browse and search for products based on different criteria.

- Shopping Cart: Users can add products to their shopping cart and manage the quantities. The cart retains the selected products even if the user navigates away from the page.

- Checkout and Payment: The website provides a checkout process where users can review their cart, enter shipping details, and make payments securely using a supported payment gateway.

- Order Management: Admin users have access to an order management system to view and process customer orders. They can update order statuses, generate invoices, and track the fulfillment process.

## Technologies Used

- Python: The primary programming language for backend development.
- Django: A high-level Python web framework used for rapid development and ease of implementation.
- HTML, CSS, and JavaScript: Used for frontend development and creating a visually appealing user interface.
- Bootstrap: Employed as a frontend framework to ensure a responsive and mobile-friendly design.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Awet11-Tesfay/ShoppingCart.git

2. Create a virtual environment and activate it:

    ```bash
    python -m venv env
    source env/bin/activate

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

4. Run database migrations:
    ```bash
    python manage.py migrate

5. Start the development server:
    ```bash
    python manage.py runserver

6. Open your browser and visit http://localhost:8000 to access the website.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Submit a pull request with a detailed description of your changes.

## Acknowledgements

Special thanks to the alx software engineering cohort #7 students and our Mentors for their valuable contributions and support.