def linear_interpolation(x, x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Os pontos x1 e x2 não podem ser iguais para a interpolação linear.")

    y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return y


x1, y1 = 2, 3
x2, y2 = 5, 8
x_interpolate = 3
result = linear_interpolation(x_interpolate, x1, y1, x2, y2)
print(f"A interpolação linear de {x_interpolate} entre ({x1}, {y1}) e ({x2}, {y2}) é {result}")

