def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    rows = data.split()
    price = float(rows[1].split(',')[1])
    for row in rows [1:]:
        fruit = row.split(',')
        if price > float(fruit[-1]):
            price = float(fruit[-1])
            name = fruit[0]
    return name
data = open('fruits.csv').read()
print(get_cheapest_fruit(data)) 