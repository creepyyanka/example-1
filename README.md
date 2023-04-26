# zeiss_test
This repository contains a Python script that uses the Selenium library to automate browsing on the website https://www.zeiss.de/. To run the script, follow the steps below:

1) Clone the repository to your local machine or download and extract the zip file.
2) Navigate to the directory where the repository is located using your command prompt or terminal.
3) Create a virtual environment by running the following command:
'python -m venv env'
4) Activate the virtual environment by running the following command:
For Windows
'.\env\Scripts\activate'

For Linux or macOS
'source env/bin/activate'

5) Install the required libraries using the following command:
'pip install -r requirements.txt'

6) Run the Python script using the following command:
'python zeiss_selenium.py'

7) The script will launch the Chrome browser and navigate to https://www.zeiss.de/. 
It will then accept cookies and click on the "Karriere" link to navigate to the careers page of the website.

8) After waiting for 7 seconds, the browser will be closed automatically.
Note: The code has been tested with Python 3.8.10 and may not work with other versions of Python.
