def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   row = data.split('\n')

   return row[1].split(',')

# Read the csv file
f = open('data.csv')
print(get_first_row(f.read()))