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

import io
import pdfplumber
import logging
from calculator import cid_to_hebrew

logging.getLogger("pdfplumber").setLevel(logging.ERROR)

def is_gradesheet(pdf):
    # Define both possible headers (with different quotation marks)
    expected_headers = [
        ['ןויצ', 'ז״נ', 'ש״ש', 'דוק', 'סרוק אשונה םש'],  # Using Hebrew Punctuation Gershayim (U+05F4)
        ['ןויצ', 'ז"נ', 'ש"ש', 'דוק', 'סרוק אשונה םש']   # Using Regular Quotation Mark (U+0022)
    ]
    
    for page in pdf.pages:
        tables = page.extract_tables()
        if tables:
            # Assume the header is in the first row of the first table
            header_text = cid_to_hebrew.convert_cid_list_to_hebrew(tables[0][0])
            logging.debug(f"Extracted header: {header_text}")
            
            # Check if the header matches any of the expected formats
            if header_text in expected_headers:
                return True
                
    raise ValueError(f"Unexpected header: {header_text}, expected one of: {expected_headers}")


def readFile(file_content):
    joined_table = []  # Initialize a single table to hold all rows

    try:
        # Convert bytes to file-like object
        pdf_file = io.BytesIO(file_content)
        
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_file) as pdf:
            # Verify if the file is a gradesheet
            if not is_gradesheet(pdf):
                raise ValueError("The uploaded file is not a valid gradesheet")

            # Extract tables from each page
            for page in pdf.pages:
                tables_on_page = page.extract_tables()
                for table in tables_on_page:
                    for row in table:
                        # Process each row in the table
                        cleaned_row = cid_to_hebrew.convert_cid_list_to_hebrew(row)  # Replace CID tokens
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
                        joined_table.append(cleaned_row)  # Add the processed row to the joined table
    except Exception as e:
        # Handle any errors that occur during processing
        logging.error(f"Error processing PDF file: {str(e)}")
        raise

    return joined_table
