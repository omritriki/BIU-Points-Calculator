def calculateGPA(tables):
    sum = 0
    points = 0
    for table in tables:
        table.sort(key=lambda x: x[0])
        for i in range(len(table)):
            if isinstance(table[i][4], float):
                grade = table[i][4]
                curr_points = table[i][3]
                if i != len(table) - 1:
                    if table[i + 1][0] == table[i][0]:
                        curr_points += table[i + 1][3]
                if i != 0:
                    if table[i - 1][0] == table[i][0]:
                        curr_points += table[i - 1][3]
                sum += (grade * curr_points)
                points += curr_points

    return sum / points
