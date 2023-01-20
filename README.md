# My SWE599 Project
This project was built for "SWE599 PROJECT" course.
Please refer to the report for detailed explanations.

## Installation Guide:

1. Install `Git`, `Python 3.11.0` and `pgAdmin 4`, if your system does not have these already. You may prefer to open the folders inside `Visual Studio Code` and use the command prompt inside of it for easier installation and development processes, details of which is shared in the next steps.

2. Clone this repository to your computer by running the command `git clone https://github.com/SametTasti/swe599.git` in your command prompt. Please note that you should ideally run this command in the folder you want the project to be installed to, with a command prompt whose directory is the installation folder itself.

3. Navigate to the root directory of the cloned repository in your command prompt by running the command `cd swe599`.

4. Next, you may activate the environment with the command `myenv\Scripts\activate` which should provide an easy way to run the project to most users. You may also create a new environment with `python -m venv env_ismi`, where `env_ismi` must be replaced with an environment name of your choice. If you create a new environment, you must install requirements, explained in the `step 6` of this installation guide.

5. Now, change your directory to the project directory with the command `cd makamproject`.

6. Install the required packages from the requirements.txt file by running `pip install -r requirements.txt`. This step is required if you want to use another environment for development or general usage. The cautious user may run this command regardless. The environment provided with the repository already includes required technologies and can be used by itself.

7. Create a new `PostgreSQL` database within the `pgAdmin` for the web application and update the `settings.py` file's `DATABASES` dictionary with the database credentials of your choice. Please refer to the database credentials part included within this project's settings file `settings.py` to setup the database. This step is highly configurable and if the user wants to use the database as is, the user should then create a database named `newtest` as can be seen in the settings file's database dictionary and then continue with the next step provided. Please refer to Django's database documentation to learn how to integrate a new database to the application. The database MUST BE of PostgreSQL kind, otherwise the application will not work. Also, by default, the `newtest` database must be located inside the default server called `PostgreSQL 15` which comes by default when you install `pgAdmin 4`.

8. Run the migrations using the commands `python manage.py makemigrations` and `python manage.py migrate`. This will create the required tables in your machine and these can be displayed in the `pgAdmin` under `newtest` database (if default database configurations are used for the installation). `manage.py` is located in the project root folder (which we had navigated to in the `step 5`).

9. Create an admin for the web application by running the command `python manage.py createsuperuser` and following the instructions inside the command prompt. Please note that you can also login to the web application with your admin account.

10. After making sure you have migrated the models to the database successfully, run the commands `python manage.py import_makam_data` and `python manage.py import_usul_data` once to initialize the models with the required data. These are custom commands which read data from the text files which contain `makams` and `usuls` and create objects which populate the database. The text files are located in the project root, where `manage.py` is located.

10. Run the local server by running `python manage.py runserver` and use the webapp by navigating to `http://127.0.0.1:8000/` in your browser.
