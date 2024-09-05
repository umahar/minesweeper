def annotate(minefield):
    # Handle empty board case
    if not minefield:
        return []

    row_length = len(minefield[0])

    # Check for uniform row lengths and valid characters
    for row in minefield:
        if len(row) != row_length:
            raise ValueError("The board is invalid with current input.")
        if any(c not in (" ", "*") for c in row):
            raise ValueError("The board is invalid with current input.")

    result = []
    row_no = 0

    for row in minefield:
        new_row = []
        for index, item in enumerate(row):
            if item == " ":
                count = no_of_mines(minefield, row, index, row_no)
                # Replace 0 with space
                if count == 0:
                    new_row.append(" ")
                else:
                    new_row.append(str(count))
            else:
                new_row.append(item)
        result.append("".join(new_row))
        row_no += 1

    return result


def no_of_mines(minefield, row, index, row_no):
    total_count = 0
    count_h = count_horizontal(row, index)

    # Skip vertical and diagonal checks for single-row boards
    if len(minefield) > 1:
        count_v = count_vertical(index, row_no, minefield)
        count_d = count_diagonal(minefield, row_no, index)
        total_count = count_h + count_v + count_d
    else:
        total_count = count_h

    return total_count


def count_horizontal(row, index):
    count = 0
    # Check on right only
    if index == 0:
        if index + 1 < len(row) and row[index + 1] == "*":
            count += 1

    # Check on left only
    elif index == len(row) - 1:
        if index - 1 >= 0 and row[index - 1] == "*":
            count += 1
    # Check both
    else:
        if index + 1 < len(row) and row[index + 1] == "*":
            count += 1
        if index - 1 >= 0 and row[index - 1] == "*":
            count += 1
    return count


def count_vertical(index, row_no, minefield):
    count = 0
    # Check below only
    if row_no == 0:
        if len(minefield) > 1:
            value = minefield[row_no + 1]
            if value[index] == "*":
                count += 1

    # Check above only
    elif row_no == len(minefield) - 1:
        if len(minefield) > 1:
            value = minefield[row_no - 1]
            if value[index] == "*":
                count += 1
    # Check both
    else:
        if (minefield[row_no + 1])[index] == "*":
            count += 1
        if (minefield[row_no - 1])[index] == "*":
            count += 1
    return count


def count_diagonal(minefield, row_no, index):
    count = 0
    rows = len(minefield)
    cols = len(minefield[0])

    # Top-left diagonal
    if row_no > 0 and index > 0:
        if minefield[row_no - 1][index - 1] == "*":
            count += 1

    # Top-right diagonal
    if row_no > 0 and index < cols - 1:
        if minefield[row_no - 1][index + 1] == "*":
            count += 1

    # Bottom-left diagonal
    if row_no < rows - 1 and index > 0:
        if minefield[row_no + 1][index - 1] == "*":
            count += 1

    # Bottom-right diagonal
    if row_no < rows - 1 and index < cols - 1:
        if minefield[row_no + 1][index + 1] == "*":
            count += 1

    return count


# Test cases
print(annotate([]))  # Should return []
print(annotate([" * * "]))  # Should return ["1*2*1"]
print(annotate(["*   *"]))  # Should return ["*1 1*"]
print(annotate([" ", "*", " ", "*", " "]))  # Should return ["1", "*", "2", "*", "1"]
print(annotate(["*", " ", " ", " ", "*"]))  # Should return ["*", "1", " ", "1", "*"]
