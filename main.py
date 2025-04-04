# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================
# Description:
#   This script processes a PDF grade sheet to calculate engineering points, Judaism points, and GPA.
# Inputs:
#   - file: A file-like object representing the uploaded PDF.
#   - degree: The selected degree (string).
#   - year: The starting year of the degree (string).
# Outputs:
#   - A formatted string summarizing the calculated points and GPA.
# ===================================================================================================

# Import necessary modules
import logging
from calculator import read_file, calculate_points, calculate_gpa, points_dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_degree_options_and_years():
    logging.info("Fetching degree options and starting years.")
    degree_options = list(points_dict.points.keys())
    starting_years = {degree: list(points_dict.points[degree].keys()) for degree in degree_options}
    return degree_options, starting_years

def main(file, degree, year):
    logging.info(f"Processing file for degree: {degree}, year: {year}")
    try:
        # Process the uploaded file to extract tables
        logging.info("Reading file content.")
        table = read_file.readFile(file)  # Extract data from the PDF
        logging.info(f"Extracted table: {table}")

        # Calculate engineering and Judaism points
        logging.info("Calculating points.")
        engPoints, judPoints = calculate_points.countPoints(table)
        logging.info(f"Engineering points: {engPoints}, Judaism points: {judPoints}")

        # Calculate total points and GPA
        logging.info("Calculating GPA and total points.")
        total_points = points_dict.points[degree][year] * 2
        max_binary_points = points_dict.points[degree][year] * 0.2
        average = calculate_gpa.calculateGPA(table)
        logging.info(f"Total points: {total_points}, Max binary points: {max_binary_points}, Average: {average}")

        # Prepare the result summary
        result = (
            f"Engineering points: {engPoints:.2f}<span class='small-text'> (out of {total_points:.2f} points)</span><br>"
            f"Maximum binary points: {max_binary_points:.2f}<br>"
            f"Judaism points: {judPoints}<span class='small-text'> (out of 20 points)</span><br>"
            f"Average: {average:.2f}"
        )
        logging.info("Result prepared successfully.")
        return result
    except Exception as e:
        logging.error(f"Error in main function: {str(e)}")
        raise


if __name__ == '__main__':
    main()
