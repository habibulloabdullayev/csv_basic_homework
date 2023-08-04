def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    rows = data.split('\n')
    countries = []
    for row in rows:
        user = row.split(',')
        countries.append(user[0])
    return countries
    
# Read the csv file
f = open('data.csv')
print(get_first_column(f.read()))