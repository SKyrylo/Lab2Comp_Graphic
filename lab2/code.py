from PIL import Image, ImageDraw

with open('DS9.txt', 'r') as file:
    lines = file.readlines()

list = []

for line in lines:
    a, b = map(int, line.strip().split())
    list.append((a, b))
polotno = Image.new("RGB", (960, 540), "white")
draw = ImageDraw.Draw(polotno)

point_size = 3

for a, b in list:
    draw.ellipse(
        [(a - point_size, b - point_size), (a + point_size, b + point_size)],
        fill=(0,0,255),
        outline=(0,0,255),
    )

polotno.save("Результат.png")
polotno.show()
file.close()