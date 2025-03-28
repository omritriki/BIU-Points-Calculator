# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================
# Description:
# This file contains the function to calculate the GPA (Grade Point Average) based on extracted tables.
# Inputs:
#   - tables: A list of tables extracted from the PDF, where each table contains course data.
# Outputs:
#   - The calculated GPA as a float.
# ===================================================================================================

def calculateGPA(tables):
    sum = 0  # Total weighted grades
    points = 0  # Total credit points

    for table in tables:
        table.sort(key=lambda x: x[0])  # Sort the table by the first column (course ID)
        for i in range(len(table)):
            if isinstance(table[i][4], float):  # Check if the grade is a float
                grade = table[i][4]
                curr_points = table[i][3]

                # Handle duplicate course rows (e.g., retakes or partial grades)
                if i != len(table) - 1 and table[i + 1][0] == table[i][0]:
                    curr_points += table[i + 1][3]
                if i != 0 and table[i - 1][0] == table[i][0]:
                    curr_points += table[i - 1][3]

                # Accumulate weighted grades and credit points
                sum += (grade * curr_points)
                points += curr_points

    return sum / points  # Return the calculated GPA
