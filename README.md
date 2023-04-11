# DjangoApp
API and UI made using the Django with DRF that allows to create Customers with fields: `name`, `VAT identification number`, `creation date`, `address`(fields: `street`, `house number`, `apartment number`, `city`, `postal code`). Every customer has one address and all fields except `creation date` are editable.

Customers can be added, edited and deleted without authentication via the `UI`, with authentication privileges via the `API` and with superuser credentials via the `django admin panel`.

## Live preview
You may check my application at: `http://djangoapp.joaorz.atthost24.pl/` Available addresses are in the section below, the api is available only after logging in with the username `guest` with the password `admin123#` 

## Available addresses:
1. Admin panel(not available in live preview):
    - `/admin` - administration panel.
2. API(available only for authenticated users):
    - `/api`- API
3. UI:
    - `/` - displays collapsed customer addition form and list of customers
    - `/<customer_uuid>/edit` - displays customer edition form
    - `/<customer_uuid>/delete` - displays customer deletion confirmation

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

