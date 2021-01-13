"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices, melon_flesh_color, melon_rind_color, melon_average_weight


def print_melon(name, seedless, price,flesh_color, rind_color, weight):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print( f'''{name.upper()}
            seedless: {seedless}
            price: {price}
            flesh_color: {flesh_color}
            weight: {weight}
            rind_color: {rind_color}''')

    
for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i], melon_flesh_color[i], melon_rind_color[i], melon_average_weight[i] )
