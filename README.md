# My SWE599 Project
This project was built for "SWE599 PROJECT" course.
Please refer to the report for detailed explanations.

## Installation Guide:

1. Install `Git` and `pgAdmin 4`, if your system does not have these already.

2. Clone the repository by running the command `git clone https://github.com/SametTasti/swe599.git` in your command prompt.

3. Navigate to the root directory of the cloned repository in your command prompt by running the command `cd swe599`.

4. Create a new environment with the command `python -m venv YOUR_ENV_NAME`, where `YOUR_ENV_NAME` must be replaced with an environment name of your choice.

5. Activate your environment with the command `YOUR_ENV_NAME\Scripts\activate` and then change your directory to the project directory with the command `cd makamproject`.

6. Install the required packages from the `requirements.txt` file by running `pip install -r requirements.txt`.

7. Create a new `PostgreSQL` database within the `pgAdmin` for the web application and update the `settings.py` file's `DATABASES` dictionary with your newly created database credentials. 

8. Run the migrations using the commands `python manage.py makemigrations` and `python manage.py migrate`.

9. Create an admin account for the web application by running the command `python manage.py createsuperuser` and following the instructions inside the command prompt. Please note that you can also login to the web application with your admin account.

10. After making sure you have migrated the models to the database successfully, run the commands `python manage.py import_makam_data` and `python manage.py import_usul_data` once to initialize the models with the required data. These are custom commands which read data from the text files which contain `makams` and `usuls` and create objects which populate the database. The text files are located in the project root, where `manage.py` is located.

10. Run the local server by running `python manage.py runserver` and use the webapp by navigating to `http://127.0.0.1:8000/` in your browser. You may use the system now!
