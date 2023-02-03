import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    names = []
    rows =data.split()
    for row in rows [1:]:
        names.append(row.split(',')[0])
    return names
data = open('fruits.csv').read()
print(get_frutis_name(data))
