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

from read_file import readFile
from calculate_gpa import calculateGPA
from points_dict import points
from count_points import countPoints

def main(file, degree, year):
    # Process the uploaded file to extract tables
    table = readFile(file)  # Extract data from the PDF
    engPoints, judPoints = countPoints(table)  # Calculate engineering and Judaism points

    # Calculate total points and GPA
    total_points = points[degree][year] * 2
    max_binary_points = points[degree][year] * 0.2
    average = calculateGPA(table)

    # Prepare the result summary with <span> tags for smaller text
    result = (
        f"Engineering points: {engPoints:.2f}<span class='small-text'> (out of {total_points:.2f} points)</span><br>"
        f"Maximum binary points: {max_binary_points:.2f}<br>"
        f"Judaism points: {judPoints}<span class='small-text'> (out of 20 points)</span><br>"
        f"Average: {average:.2f}"
    )
    return result


if __name__ == '__main__':
    main()
