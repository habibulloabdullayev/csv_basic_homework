def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    rows = data.split('\n')
    countries = []
    for row in rows:
        user = row.split(',')
        countries.append(user[0])
    return len(countries)

# Read the csv file
f = open('data.csv')
print(find_number_of_rows(f.read()))