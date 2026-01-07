import json
from pathlib import Path

from dotenv import load_dotenv

from chains import get_extraction_chain
from utils import extract_text_from_pdf

load_dotenv(override=True)

invoices_folder_path = str(Path(__file__).parent / "data")


def main():
    print(f"Hello from invoiceautomation!")


if __name__ == "__main__":
    main()
    chain = get_extraction_chain()
    all_invoices = {}
    for file in Path(invoices_folder_path).glob("*.pdf"):
        invoice_text = extract_text_from_pdf(str(file))
        try:
            response = chain.invoke({"invoice_text": invoice_text})

            print("--- Extracted Data ---")
            print(f"Company: {response.company_name}")
            print(f"Total:   {response.total_amount}")
            print(f"InvoiceID:   {response.invoice_number}")
            print(f"TaxAmount:   {response.tax_amount}")
            print(f"CompanyAddress:   {response.company_address}")
            all_invoices[str(file.name)] = response.model_dump()
        except Exception as e:
            print(f"Error during extraction {e}")

    with open("results.json", "w") as file:
        json.dump(all_invoices, file, indent=4)
