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

from readFile import readFile
from GPA import calculateGPA
from pointsDict import points
from countPoints import countPoints

def main(file, degree, year):
    # Process the uploaded file to extract tables
    tables = readFile(file)  # Extract data from the PDF
    engPoints, judPoints = countPoints(tables)  # Calculate engineering and Judaism points

    # Calculate total points and GPA
    total_points = points[degree][year] * 2
    max_binary_points = points[degree][year] * 0.2
    average = calculateGPA(tables)  

    # Prepare the result summary
    result = (
        f"Engineering points: {engPoints} (out of {total_points} points)\n"
        f"Maximum binary points: {max_binary_points:.2f}\n"
        f"Judaism points: {judPoints} (out of 20 points)\n"
        f"Average: {average:.2f}"
    )
    return result


if __name__ == '__main__':
    main()
