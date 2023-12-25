# Online Zoo Shop: Manage Products and Orders with Django
![image_2023-12-25_03-17-34](https://github.com/matveykaa/OnlineStore/assets/101522923/07b24f0c-a69b-49da-b368-f0e3f90141e5)

![image_2023-12-25_03-18-57](https://github.com/matveykaa/OnlineStore/assets/101522923/899c7789-622e-4d2b-9117-0a44dacb1751)

The app provides a custom dashboard to manage products and orders. Users can like a product, add it to the cart, proceed to checkout, leave comments to products and send review to shop admins. Order processing is supported, but the payment is handled using a fake pay system.

[Preview](#app-preview)

## Features

There are two types of users in this app: regular users and managers.

### Available to the Users:

- **Cart**: Users can manage items in their cart.
- **Edit Personal Information**: Users can update their personal details.
- **Orders**: Users can view their order history.
- **Favorites**: Users can like and save their favorite products.
- **Reset Password**: Users can reset their password using their registered email.
- **Leave comments**: Users can comment what they like of products.
- **Send review**: Users can send reviews to admin email.

### Available to the Managers:

Managers can access all the features available to regular users, along with additional capabilities, through the custom dashboard accessible at [http://localhost:8000/accounts/login/manager](http://localhost:8000/accounts/login/manager).

- **Add Product**: Managers can add new products to the shop.
- **Edit and Delete Product**: Managers can modify or remove existing products.
- **Add New Category**: Managers have the ability to create new categories for products.
- **Access to Orders**: Managers can view and manage all orders and order items.

## Technologies Used

- Python 3
- Django
- Bootstrap
- Postgres
- Redis
- Celery

## How to Run the Application

1. Clone or download the project to your local machine.
2. Change directory to the "onlineStore" folder.
3. Ensure that you have Python 3, pip, Docker and virtualenv installed on your machine.
4. Create a virtual environment using the following command:
   - For Mac and Linux: `python3 -m venv venv`
   - For Windows: `python -m venv venv`
5. Activate the virtual environment:
   - For Mac and Linux: `source venv/bin/activate`
   - For Windows: `venv\scripts\activate`
6. Up docker-compose: `docker-compose up --build`
7. Migrate the database by executing: `python manage.py migrate`
8. Start the server: `python manage.py runserver`
9. You should now be able to access the application by visiting: [http://localhost:8000/](http://localhost:8000/)

## Manager Dashboard Access

To access the custom dashboard for managers, please use the following credentials:

- Email: manager@example.com
- Password: managerpass1234

## License

released under the [MIT License](LICENSE).

## App Preview
![Screencast-from-25 12 2023-04_37_15](https://github.com/matveykaa/OnlineStore/assets/101522923/11769fde-623a-4a10-a20a-cfd11f16f7f2)