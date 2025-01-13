# Tableau E-commerce Dashboard Project

This project showcases a Tableau dashboard that visualizes product data from a simulated e-commerce store, fetched using the Fake Store API. The dashboard includes various analyses like product distribution, price distribution, and product count by category.

## Files in this Repository

- **`dataAuto.py`**: A Python script that fetches and processes data from the Fake Store API.
- **`_E-commerce Product Analysis: Distribution and Pricing_.twbx`**: The Tableau Packaged Workbook containing the interactive dashboard.

## How to Use

1. **Clone the repository** or download the files.
2. **Run the Python script** `dataAuto.py` to fetch the product data.
3. **Open the Tableau workbook** (`_E-commerce Product Analysis: Distribution and Pricing_.twbx`) using Tableau Desktop or Tableau Public to explore the dashboard.

## Dashboard Features

- Product Distribution by Category
- Average Price by Product Category
- Total Price by Product Category
- Price Distribution by Product Category
- Product Count by Category

## Installation Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/your-repository.git
cd your-repository
```
### 2. Install Dependencies
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```
### 3. Configure Dropbox
Create a Dropbox app and generate an access token.
Replace the placeholder token in fetchapi.py with your Dropbox access token.

### 4. Set Up Cron Job
To automate the script to run every 15 minutes, do the following:

Open the crontab editor:
```bash
crontab -e
```
Add the following line to execute the script every 15 minutes:
bash
```bash
*/15 * * * * /usr/bin/python3 /path/to/your/fetchapi.py
```
This will ensure that the script is executed at regular intervals, updating the products.csv file with fresh data.

### 5. Open the Tableau Workbook
Open the E-commerce_Dashboard.twbx file in Tableau Desktop or Tableau Public.
Ensure Tableau is connected to the live products.csv file stored in Dropbox.

## Technologies Used

- **Tableau**: For creating interactive dashboards and visualizations.
- **Fake Store API**: Provides simulated e-commerce data.
- **Python**: Used to fetch and preprocess data from the API.
- **Dropbox**: Used to store and share the live data file.
- **Cron**: Automates the execution of the Python script every 15 minutes.
  
## How It Works

The Python script fetchapi.py fetches the latest product data from the Fake Store API.
The data is saved in a CSV file (products.csv), which is stored in Dropbox.
Tableau connects to this CSV file to create dynamic visualizations that update whenever new data is fetched.
The Cron job ensures that the Python script runs every 15 minutes, keeping the data fresh.

## Conclusion

This project demonstrates the integration of Tableau with external data sources (Fake Store API and Dropbox), allowing for real-time data visualization with automated updates. The use of a cron job to schedule the execution of the Python script ensures that the data is updated automatically without manual intervention.
