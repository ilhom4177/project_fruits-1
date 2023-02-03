def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    rows = data.split()
    price = float(rows[1].split(',')[1])
    for row in rows [1:]:
        fruit = row.split(',')
        if price > float(fruit[-1]):
            price = float(fruit[-1])
            name = fruit[1]
    return name
data = open('fruits.csv').read()
print(get_cheapest_fruit_id(data)) 