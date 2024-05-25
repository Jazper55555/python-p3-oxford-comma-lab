# oxford_comma(['Luca', 'Andrea', 'Stew'])

def oxford_comma(items):
    if len(items) == 1:
        return ''.join(items)
    elif len(items) == 2:
        return ' and '.join(items)
    elif len(items) >= 3:
        items.insert(-1, f'and {items[-1]}')
        items.pop()
        string = ', '.join(items)
        return string
    pass
