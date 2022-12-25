point = (1, 1)
#point = (0, 3)
#point = (3, 0)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = x

def where_is(point):
    match point:
        case Point(0, 0):
            print('Origin')
        case Point(0, y):
            print(f'Y={y}')
        case Point(x, 0):
            print(f'X={x}')
        case Point():
            print('something else')
        case _:
            print('not a point')