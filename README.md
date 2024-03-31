# Freee Invoice Automation

## What is this?
This repository contains a Python script for automating invoice management tasks within Freee, a popular Japanese invoice management software. The script allows users to generate an invoice through the Freee API, leveraging a predefined invoice template and automating the token refresh process for authentication.

## How to Use
To use this script, you need to have Python installed on your system along with the necessary dependencies managed by Poetry. Follow the steps below to get started:

1. **Install Dependencies**: Ensure you have Poetry installed. If not, install it following the instructions on the [official Poetry website](https://python-poetry.org/docs/). Then, navigate to the project directory and run `poetry install` to install the required dependencies.
2. **Configure API Credentials**: Copy `.env.example` to `.env` and fill it with your Freee API credentials. Here's a brief explanation of each field:
   - `grant_type`: Specifies the OAuth grant type (typically `authorization_code` or `refresh_token`).
   - `client_id`: Your application's Client ID from Freee.
   - `client_secret`: Your application's Client Secret from Freee.
   - `code`: The authorization code obtained from Freee (used once to get a refresh token).
   - `redirect_uri`: The URI Freee redirects to after authorization.
   - `refresh_token`: Used to obtain new access tokens without reauthorization.
  
3. **Prepare invoice_template.json**: You can download existing invoice data in json format using Free API.
4. **Run the Script**: The script can be executed with the following command:
    ```
    poetry run python <script_name>.py --hours <HOURS> --month <YYYY-MM>
    ```
   Replace `<script_name>` with the name of the script file, `<HOURS>` with the number of hours worked, and `<YYYY-MM>` with the month for which the invoice is being prepared.

## Requirements
- Python 3.7+
- Poetry for dependency management

## Features
- Automated invoice creation based on a predefined template.
- Dynamic calculation of invoice issue and due dates.
- Automatic handling of API authentication tokens.

## Notes
- This script assumes you have an active Freee account and API access.
- You may need to modify the `Freee` class and `invoice_template.json` based on your specific Freee account setup and invoice requirements.

For detailed API documentation and more advanced features, refer to the [official Freee API documentation](https://developer.freee.co.jp/docs/accounting).


