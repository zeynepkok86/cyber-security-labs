from PIL import Image

width, height = 300, 200
img = Image.new("RGB", (width, height), "white")

for y in range(height):
    for x in range(width):
        if (x // 50 + y // 50) % 2 == 0:
            img.putpixel((x, y), (30, 30, 30))

img.save("original.bmp")
print("original.bmp created")