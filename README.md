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

## License
[MIT © Trashy Armadillos](./LICENSE)




