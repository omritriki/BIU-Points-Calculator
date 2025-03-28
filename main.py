# ===================================================================================================
#                                       BIU N.K.Z Calculator
#                                            Omri Triki
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================


from readFile import readFile
from GPA import calculateGPA
from pointsDict import points
from countPoints import countPoints


def main(file, degree, year):
    print(f"Degree: {degree}")
    print(f"Year: {year}")
    print(f"File type: {type(file)}")
    print(f"File name: {file.filename}")

    # Process the uploaded file directly
    tables = readFile(file)  # Pass the file-like object to readFile
    engPoints, judPoints = countPoints(tables)
    print(f"Engineering points: {engPoints}")

    total_points = points[degree][year] * 2
    print(f"Total points: {total_points}")
    max_binary_points = points[degree][year] * 0.2
    print(f"Max binary points: {max_binary_points}")
    average = calculateGPA(tables)
    print(f"Engineering points: {engPoints}")

    # Prepare the result
    result = (
        f"Engineering points: {engPoints} (out of {total_points} points)\n"
        f"Maximum binary points: {max_binary_points:.2f}\n"
        f"Judaism points: {judPoints} (out of 20 points)\n"
        f"Average: {average:.2f}"
    )
    return result


if __name__ == '__main__':
    main()
