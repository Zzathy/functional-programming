import math

def translasi(x, y, tx, ty):
    result_x = x + tx
    result_y = y + ty
    return result_x, result_y

def dilatasi(x, y, sx, sy):
    result_x = x * sx
    result_y = y * sy
    return result_x, result_y

def dirotasi(x, y, corner):
    corner_rad = math.radians(corner)
    result_x = x * math.cos(corner_rad) - y * math.sin(corner_rad)
    result_y = x * math.sin(corner_rad) + y * math.cos(corner_rad)
    return result_x, result_y

coordinat = (3, 5)

tx, ty = 2, -1
afterTranslasi = translasi(*coordinat, tx, ty)
print("Setelah translasi:", afterTranslasi)

sx, sy = 2, -1
afterDilatasi = dilatasi(*coordinat, sx, sy)
print("Setelah dilatasi:", afterDilatasi)

corner_rotation = 30
afterDirotasi = dirotasi(*coordinat, corner_rotation)
print("Setelah rotasi:", afterDirotasi)