# BangazonAPI
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

API exposes Consumer-side, and Company-side resources for Bangazon, LLC.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)   
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Installation
1. ```git clone <repo address>``` into a local directory of your choosing.
2. ```cd Bangazon-API/BangazonAPI/migrations```
3. Delete all migration files EXCEPT __init__.py
4. Delete contents of database (db.sqlite3)
5. ```cd ../```
6. ```python manage.py makemigrations```
7. ```python manage.py migrate```
8. ```python manaage.py createsuperuser```
9. ```python manage.py runserver```
10. login to api with superuser info

## Usage
1. In fixtures directory, fillerdata.json file can be edited to test different data. From the web browser, data can also be added to each table from the API interface.


## Contribute
1. Fork it!
2. Create your feature branch: 
```git checkout -b <new-feature-branch-name-here>```
3. Commit your changes: 
```git commit -m 'Add some feature'```
4. Push to the branch: 
```git push origin <new-feature-branch-name-here-too>```
5. Submit a pull request :D

Small note: If editing the Readme, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## Credits
Project Manager:
  - Gilberto Diaz

API Build Contributors:
  - Jessica Younker
  - Helana Nosrat
  - Max Baldridge
  - Angela Lee
  - Justin Short

# Modern Bangazon API Client Application

## Authentication

You will learn how to use the built-in authentication and authorization modules in Django and DRF to create users and handle authenticating requests. You will learn how to use the Token Authentication system rather than the Session Authentication.

## Requirements

We need to build a mobile-response, single page application for use on mobile devices. This project will eventually be used as the prototype for an Ionic application. You are not responsible for that migration.

### Story

**As a** Bangazon customer

**In order** to sell, or buy, a product at any time

**I want** to be able to access the Bangazon site on my phone

### Scenarios

**Given** a customer wants to buy or sell a product

**When** the customer opens the Bangazon mobile app

**Then** the customer should be shown the last 20 products added to the platform

**And** have an affordance to perform a product search

**And** have an affordance to authenticate

---

**Given** a customer is viewing a product list

**When** the customer performs a gesture on a product link

**Then** the customer should be presented with the product details

**And** an affordance for adding the product to their shopping cart

---

**Given** a customer is on any view

**When** the customer performs a gesture on the affordance to authenticate

**Then** the customer should be presented with the log in view

---

**Given** a customer is authenticated

**When** the customer performs a gesture on the affordance to add a product to the shopping cart

**Then** the customer should see that the item was successfully added by an affordance in the navigation area which shows the number of items in their cart

---

**Given** a customer wants to view their shopping cart

**When** the customer performs a gesture on the cart affordance in the navigation area

**Then** the customer should be presented with a list of items in their cart

**And** the total price of the items in their cart

**And** an affordance to select a payment type

**And** an affordance to complete the order

## License
[MIT © Trashy Armadillos](./LICENSE)




