import pdfplumber
import CID2Hebrew


def readFile(pdf_path):
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            tables_on_page = page.extract_tables()
            for table in tables_on_page:
                new_table = []
                for row in table:
                    cleaned_row = CID2Hebrew.replace_cid_tokens_in_list(row)
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
    return all_tables
