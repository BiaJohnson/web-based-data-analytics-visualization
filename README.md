# Property Finance Dashboard

## Overview

The Property Finance Dashboard is a Django web application that allows users to upload a CSV file containing property data. The application processes the data to display a table and various charts that provide insights into property pricing, rental income, expenses, and net income.

## Features

- **CSV File Upload**: Easily upload a CSV file with property details.
- **Data Processing**: Automatically calculates and displays:
  - Price
  - Rent
  - EMI 
  - Tax
  - Monthly Expenses
  - Net Expenses
  - Net Income
- **Data Visualization**: View graphical representations of key financial metrics through interactive charts.

## Getting Started

### Prerequisites
- Python 3.10
- Django 3.2
- Pandas
- Tailwind

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/BiaJohnson/web-based-data-analytics-visualization
   cd property-finance-dashboard


2. Create a virtual environment:
   pip install virtualenv # On Windows

3. Run database migrations:
   python manage.py makemigrations
   python manage.py sqlmigrate myapp 0001
   python manage.py migrate
   python manage.py shell

4. Start virtual environemnt:
   cd env/scripts  # go to scripts folder to activate env
   activate
   python manage.py runserver

5- Open your browser and go to http://127.0.0.1:8000/.

## Usage

1. Navigate to the upload page.
2. Select and upload your CSV file.
3. View the generated table and charts displaying your property data.

### CSV File Format:

Your CSV file should contain the following columns:

- Price
- Rent
- EMI
- Tax
- Monthly Expenses
- Net Expenses
- Net Income

Ensure that the data is properly formatted for accurate calculations.
