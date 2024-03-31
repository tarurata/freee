# Freee Invoice Automation

## What is this?
This repository contains a Python script for automating invoice management tasks within Freee, a popular Japanese invoice management software. The script allows users to generate an invoice through the Freee API, leveraging a predefined invoice template and automating the token refresh process for authentication.

## How to Use
To use this script, you need to have Python installed on your system along with the necessary dependencies managed by Poetry. Follow the steps below to get started:

1. **Install Dependencies**: Ensure you have Poetry installed. If not, install it following the instructions on the [official Poetry website](https://python-poetry.org/docs/). Then, navigate to the project directory and run `poetry install` to install the required dependencies.
2. **Configure**: Before running the script, ensure you have an `invoice_template.json` file in the project directory and a valid setup for the `Freee` class to handle authentication with the Freee API.
3. **Run the Script**: The script can be executed with the following command:
    ```
    poetry run python <script_name>.py --hours <HOURS> --month <YYYY-MM>
    ```
   Replace `<script_name>` with the name of the script file, `<HOURS>` with the number of hours worked, and `<YYYY-MM>` with the month for which the invoice is being prepared.

## Requirements
- Python 3.x
- Poetry for dependency management

## Features
- Automated invoice creation based on a predefined template.
- Dynamic calculation of invoice issue and due dates.
- Automatic handling of API authentication tokens.

## Notes
- This script assumes you have an active Freee account and API access.
- You may need to modify the `Freee` class and `invoice_template.json` based on your specific Freee account setup and invoice requirements.

For detailed API documentation and more advanced features, refer to the [official Freee API documentation](https://developer.freee.co.jp/docs/accounting).
