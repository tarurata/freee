import argparse
import json
from datetime import datetime, timedelta

from freee import Freee


def authorize_freee_client(freee: Freee) -> None:
    jsonized_tokens = freee.read_tokens()
    freee.set_tokens(jsonized_tokens)
    freee.run_refresh_token()


def load_invoice_template() -> dict:
    with open("invoice_template.json") as f:
        invoice_template = json.load(f)
    return invoice_template


def prepare_invoice(hours, month) -> dict:
    invoice_template = load_invoice_template()
    invoice_template["issue_date"] = datetime.now().strftime("%Y-%m-%d")
    invoice_template["booking_date"] = datetime.now().strftime("%Y-%m-%d")
    invoice_template["invoice_contents"][0]["qty"] = hours  # Worked hours
    month_after_next_month = datetime.strptime(f"{month}-01", "%Y-%m-%d") + timedelta(days=62)
    due_date = month_after_next_month.replace(day=10)
    due_date_formatted = due_date.strftime("%Y-%m-%d")
    invoice_template["due_date"] = due_date_formatted
    return invoice_template


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-ho", "--hours", type=float, required=True, help="Worked hours, either float or int")
    current_month = datetime.now().strftime("%Y-%m")
    parser.add_argument("-m", "--month", type=str, required=True, default=current_month, help="Worked month. yyyy-mm")
    args = parser.parse_args()

    freee = Freee()
    authorize_freee_client(freee)
    invoice_template = prepare_invoice(args.hours, args.month)
    response = freee.create_invoices(invoice_template)
    print(response)


if __name__ == "__main__":
    main()
