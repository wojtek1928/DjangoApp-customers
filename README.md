# DjangoApp
API and UI made using the Django with DRF that allows to create Customers with fields: `name`, `VAT identification number`, `creation date`, `address`(fields: `street`, `house number`, `apartment number`, `city`, `postal code`). Every customer has one address and all fields except `creation date` are editable.

The customers can be added, edited and deleted without authentication via `UI` and with superuser's credentials via `django administrator panel` and `API`.

## Environment set up 
1. Setup virtual environment for on your computer(Windows example: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
2. Activate your virtual environment.
3. Pull this repository.
4. Run command `pip install -r requirements.txt`
5. Set your console in folder with pulled repository.
6. Apply migration with command `python manage.py migrate`
7. Create superuser with command `python manage.py createsuperuser`
8. Run django server with command: `python manage.py runserver`
9. You can go to website via link in console or by typing `127.0.0.1:8000` in your browser.

With any problems contact with author by github or by mail `wojtek1928@gmail.com`.

## Available addresses:
1. Admin panel(available  only for superuser):
    - `127.0.0.1:8000/admin` - administration panel.
2. API(available  only for superuser):
    - `127.0.0.1:8000`- API
3. UI:
    - `127.0.0.1:8000` - displays collapsed customer addition form and list of customers
    - `127.0.0.1:8000/<customer_uuid>/edit` - displays customer edition form
    - `127.0.0.1:8000/<customer_uuid>/delete` - displays customer deletion confirmation
