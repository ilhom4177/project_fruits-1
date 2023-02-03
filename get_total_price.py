def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """
    price = 0
    rows = data.split()
    for row in rows [1:]:

        price+=float(row.split(',')[-1])
    return round(price, 2)
data = open('fruits.csv').read()
print(get_total_price(data))

    