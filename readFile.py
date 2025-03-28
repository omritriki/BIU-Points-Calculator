# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================
# Description:
#   This script reads a PDF file, verifies if it is a gradesheet, extracts tables from it, and processes the data.
# Inputs:
#   - pdf_file: A werkzeug FileStorage object representing the uploaded PDF.
# Outputs:
#   - A list of all extracted and processed tables.
# ===================================================================================================

import pdfplumber
from CID2Hebrew import replace_cid_tokens_in_list

def is_gradesheet(pdf):
    expected_header = ['ןויצ', 'ז״נ', 'ש״ש', 'דוק', 'סרוק אשונה םש']
    for page in pdf.pages:
        tables = page.extract_tables()
        if tables:
            # Assume the header is in the first row of the first table
            header_text = replace_cid_tokens_in_list(tables[0][0])
            if expected_header == header_text:
                return True
    return False


def readFile(pdf_file):
    all_tables = []

    try:
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_file.stream) as pdf:
            # Verify if the file is a gradesheet
            if not is_gradesheet(pdf):
                raise ValueError("The uploaded file is not a valid gradesheet.")

            # Extract tables from each page
            for page in pdf.pages:
                tables_on_page = page.extract_tables()
                for table in tables_on_page:
                    new_table = []
                    for row in table:
                        # Process each row in the table
                        cleaned_row = replace_cid_tokens_in_list(row)  # Replace CID tokens
                        cleaned_row.reverse()  # Reverse the row for proper order
                        for i in range(len(cleaned_row)):
                            cell = cleaned_row[i]
                            try:
                                # Attempt to convert the cell to a float
                                cleaned_row[i] = float(cell)
                                continue
                            except ValueError:
                                pass
                            # Handle cells with dashes and digits
                            if "-" in cell and any(ch.isdigit() for ch in cell):
                                continue
                            # Reverse the text in the cell
                            cleaned_row[i] = cell[::-1]
                        new_table.append(cleaned_row)  # Add the processed row to the new table
                    all_tables.append(new_table)  # Add the processed table to the list of all tables
    except Exception as e:
        # Handle any errors that occur during processing
        print(f"Error processing PDF file: {str(e)}")
        raise

    # Log the number of extracted tables
    print(f"Extracted {len(all_tables)} tables from the PDF.")
    return all_tables
