import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    result = []
    with open(data, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            result.append(line[0])
    return result  
