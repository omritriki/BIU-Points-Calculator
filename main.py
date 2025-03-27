# ===================================================================================================
#                               The Official BIU N.K.Z Calculator
#                           Beny Boshoer, Yuval Disatnik, Omri Triki
#                                         THE MASTERMINDS
#                                       Bar Ilan University
#                                               2025
# ===================================================================================================


import readFile
import GPA


def identifyCourses(row):
    # If row[1] starts with '83', it's an Engineering course
    if isinstance(row[1], str) and row[1].startswith("83"):
        return 1
    # If row[1] starts with '01,02,03', it's a Judaism course
    elif isinstance(row[1], str) and (
            row[1].startswith("01") or row[1].startswith("02") or row[1].startswith("03") or row[1].startswith("13")):
        return 2
    return -1


def countPoints(tables):
    engPoints = 0.0
    binPoints = 0.0
    judPoints = 0.0
    for table in tables:
        for row in table:
            switch = identifyCourses(row)
            if switch == -1:
                continue
            if switch == 1:
                try:
                    engPoints += row[3]
                    if row[4] == "עובר":
                        binPoints += row[3]
                except (TypeError, ValueError):
                    pass
            if switch == 2:
                try:
                    judPoints += row[3]
                except (TypeError, ValueError):
                    pass
    return engPoints, binPoints, judPoints


def main():
    path = "/Users/omritriki/VSCodeProjects /Nakaz/Omri_Triki_Gradesheet.pdf"
    tables = readFile.readFile(path)

    engPoints, binPoints, judPoints = countPoints(tables)
    print("Engineering points:", engPoints)
    print("Binary Engineering points:", binPoints)
    print("Judaism points:", judPoints)

    average = GPA.calculateGPA(tables)
    print("Average:", f"{average:.2f}")


if __name__ == '__main__':
    main()
