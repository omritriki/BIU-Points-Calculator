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

import logging
from calculator import read_file, calculate_points, calculate_gpa, points_dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_degree_options_and_years():
    degree_options = list(points_dict.points.keys())
    starting_years = {degree: list(points_dict.points[degree].keys()) for degree in degree_options}
    return degree_options, starting_years


def main(file_content, degree, year):
    try:
        table = read_file.readFile(file_content)
                
        # Calculate engineering and Judaism points
        try:
            engPoints, judPoints = calculate_points.countPoints(table)
        except Exception as calc_error:
            logging.error(f"Error in points calculation: {str(calc_error)}")
            logging.error(f"Text sample at error: {table[max(0, calc_error.__traceback__.tb_lineno-20):calc_error.__traceback__.tb_lineno+20]}")
            raise

        # Calculate total points and GPA
        total_points = points_dict.points[degree][year] * 2
        max_binary_points = points_dict.points[degree][year] * 0.2
        average = calculate_gpa.calculateGPA(table)

        result = (
            f"Engineering points: {engPoints:.2f}<span class='small-text'> (out of {total_points:.2f} points)</span><br>"
            f"Maximum binary points: {max_binary_points:.2f}<br>"
            f"Judaism points: {judPoints}<span class='small-text'> (out of 20 points)</span><br>"
            f"Average: {average:.2f}"
        )
        
        return result

    except Exception as e:
        logging.error(f"Error processing PDF file: {str(e)}")
        raise


if __name__ == '__main__':
    main()
