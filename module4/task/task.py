import math

def transformation(func):
    def wrapper(x, y, gradien, tx, ty, sx, sy):
        x, y = x + tx, y + ty
        
        radian_corner = math.radians(60)
        x, y = x * math.cos(radian_corner) - y * math.sin(radian_corner), \
               x * math.sin(radian_corner) + y * math.cos(radian_corner)
        
        x, y = x * sx, y * sy
        
        result = func(x, y, gradien, tx, ty, sx, sy)
        return result
    return wrapper

@transformation
def line_equation_calculation(x, y, gradien, tx, ty, sx, sy):
    C = y - gradien * x
    return f"Y = {gradien:.2f}x + {C:.2f}"

x, y, gradien = map(int, input("Input (NIM) x, y, dan gradien (pisahkan dengan spasi): ").split())
tx, ty = map(float, input("Input tx dan ty untuk translasi (pisahkan dengan spasi): ").split())
sx, sy = map(float, input("Input sx dan sy untuk perbesaran skala (pisahkan dengan spasi): ").split())

result_transformation = line_equation_calculation(x, y, gradien, tx, ty, sx, sy)

print(f"\nPersamaan garis melalui titik ({x},{y}) dan bergradien {gradien}:")
print(f"Y = {gradien:.2f}x + {-gradien * x + y:.2f}")
print("\nPersamaan garis baru setelah transformasi:")
print(result_transformation)