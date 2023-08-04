#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    row = data.split('\n')
    return row[0].split(',')
    
# Read the csv file
f = open('data.csv')
print(get_column_names(f.read()))