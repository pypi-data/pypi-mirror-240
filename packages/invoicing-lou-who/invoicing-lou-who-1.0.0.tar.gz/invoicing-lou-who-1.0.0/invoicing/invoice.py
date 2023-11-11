import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os


def generate(invoices_path, pdfs_path, image_path, company, product_id,
             product_name, amount_purchased, price_per_unit, total_price):
    """
    This function converts invoice Excel files into PDF invoices.
    :param invoices_path:
    :param pdfs_path:
    :param image_path:
    :param company:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")

    for filepath in filepaths:
        filename = Path(filepath).stem
        invoice_no, date = filename.split("-")

        # Header
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Invoice no. {invoice_no}", ln=1)

        pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

        # Table
        df = pd.read_excel(filepath, sheet_name="Sheet 1")

        # Table Header
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(80, 80, 80)

        for i, col in enumerate(df.columns):
            col_name = col.replace("_", " ").title()
            width = 70 if i == 1 else 30
            line = 1 if i == 4 else 0
            pdf.cell(w=width, h=8, txt=col_name, border=1, ln=line)

        # Table Rows
        pdf.set_font(family="Times", size=10, style="")

        for i, row in df.iterrows():
            pdf.cell(w=30, h=8, txt=str(row[product_id]), border=1)
            pdf.cell(w=70, h=8, txt=row[product_name], border=1)
            pdf.cell(w=30, h=8, txt=str(row[amount_purchased]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[price_per_unit]), border=1)
            pdf.cell(w=30, h=8, txt=str(row[total_price]), border=1, ln=1)

        # Total Sum Message
        total_sum = df[total_price].sum()
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=70, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt="", border=1)
        pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

        # Company Name and Logol
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=25, h=8, txt=f"{company}")
        pdf.image(image_path, w=10)

        if not os.path.exists(pdfs_path):
            os.makedirs(pdfs_path)
        pdf.output(f"{pdfs_path}/{filename}.pdf")

