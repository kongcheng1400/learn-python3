# format print
# 1. internal built-in format
# format(value, format_spec='', /)

format(14, '#b'), format(14, 'b')
# ('0b1110', '1110')
f'{14:#b}', f'{14:b}'
# ('0b1110', '1110')