# Web Automation Bot  🤖(Selenium)

### Overview

This is a web automation bot built using Python and Selenium WebDrivers.  
It automatically fills search details and scrapes web pages to find the best hotel deals based on the input provided through code.

### Key Features

- **Web Scraping**: Extracts relevant information from web pages.
- **Auto-filling Forms**: Automatically fills search fields based on predefined inputs.
- **Hotel Deal Finder**: Searches for the best deals on hotels from the scraped data.
  
### Technologies Used

- **Python**: Core programming language for the bot.
- **Selenium WebDriver**: For interacting with web elements and performing actions like filling forms and clicking buttons.

### How It Works

1. **Input**: The bot takes input data (e.g., city, check-in/check-out dates) from the user in the code.
2. **Automation**: Using Selenium, the bot navigates to the target website, fills out the search form, and retrieves the best available hotel deals.
3. **Output**: The bot displays the results based on the user input.

### Installation

To run this project, make sure you have the following installed:

- Python 3.x
- Selenium WebDriver
- WebDriver for your browser (e.g., ChromeDriver for Chrome)

### Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/Aviral-Maheshwari/Se-Bot
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Update the input data in the code for the desired search parameters.
   - Change the CityToGO
   - Change the CheckIn and CheckOut Time
   - Change the no. of adults and kids.
5. Run the bot:
   ```bash
   python run.py
