# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================


import pdfplumber
from CID2Hebrew import replace_cid_tokens_in_list


def readFile(pdf_file):
    print(f"Processing file: {pdf_file}")
    """
    Reads a PDF file-like object and extracts tables from it.
    :param pdf_file: A werkzeug FileStorage object representing the uploaded PDF.
    :return: A list of all extracted tables.
    """
    all_tables = []
    try:
        # Use the `stream` attribute of the FileStorage object for pdfplumber
        with pdfplumber.open(pdf_file.stream) as pdf:
            for page_number, page in enumerate(pdf.pages, start=1):
                tables_on_page = page.extract_tables()
                for table in tables_on_page:
                    new_table = []
                    for row in table:
                        cleaned_row = replace_cid_tokens_in_list(row)
                        cleaned_row.reverse()
                        for i in range(len(cleaned_row)):
                            cell = cleaned_row[i]
                            try:
                                cleaned_row[i] = float(cell)
                                continue
                            except ValueError:
                                pass
                            if cell.__contains__("-") and any(ch.isdigit() for ch in cell):
                                continue
                            cleaned_row[i] = cell[::-1]
                        new_table.append(cleaned_row)
                    all_tables.append(new_table)
    except Exception as e:
        print(f"Error processing PDF file: {str(e)}")
        raise
    print(f"Extracted {len(all_tables)} tables from the PDF.")
    return all_tables
