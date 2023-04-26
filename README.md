# zeiss_test
zeiss_test

To download and run this code, follow the instructions below:

1. Clone the repository to your local machine by running the following command in your terminal or command prompt: 
git clone https://github.com//.git

2. Switch to the my_new_branch branch by running the following command: git checkout my_new_branch

3. Install the required dependencies by running the following command: 
pip install selenium webdriver_manager

4. Download and install the Chrome web driver for your system from the following link: 
https://chromedriver.chromium.org/downloads

5. Update the ChromeDriverManager().install() line in the code to specify the path to the Chrome web driver executable on your system: 
service = Service('/path/to/chromedriver')

6. Save the changes to the code file.

7. Run the code by running the following command: 
python .py 
Replace with the name of the file that contains the code.

This should open the Zeiss website in a Chrome browser window, accept the cookie popup, click on the "Karriere" link, wait for 7 seconds, and then quit the browser.
