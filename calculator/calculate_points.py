# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================
# Description:
# This file contains functions to identify course types and calculate total engineering and Judaism points.
# Inputs:
#   - tables: A list of tables extracted from the PDF, where each table contains course data.
# Outputs:
#   - engPoints: Total engineering points as a float.
#   - judPoints: Total Judaism points as a float.
# ===================================================================================================

def identifyCourses(row):
    # Check if the course ID starts with specific prefixes
    if isinstance(row[1], str) and row[1].startswith("83"):
        return 1  # Engineering course
    elif isinstance(row[1], str) and (
            row[1].startswith("01") or row[1].startswith("02") or row[1].startswith("03") or row[1].startswith("13")):
        return 2  # Judaism course
    return -1  # Other course


def countPoints(table):
    engPoints = 0.0  
    judPoints = 0.0  

    for row in table:
        switch = identifyCourses(row)  # Identify the course type
        if switch == -1:
            continue  # Skip rows that are not relevant
        if switch == 1:  # Engineering course
            try:    
                engPoints += row[3]
            except (TypeError, ValueError):
                pass  # Ignore invalid data
        if switch == 2:  # Judaism course
            try:
                judPoints += row[3]
            except (TypeError, ValueError):
                pass  # Ignore invalid data
    return engPoints, judPoints  # Return the calculated points

