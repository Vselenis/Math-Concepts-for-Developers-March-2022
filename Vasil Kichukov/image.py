from color import Color

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, col):
        self.pixels[y][x] = col

    @staticmethod
    def to_byte(k):
        return round(max(min(k * 255, 255), 0))

    def write_ppm(self, img_file):
        img_file.write(f"P3 {self.width} {self.height}\n255\n")
        for row in self.pixels:
            for color in row:
                img_file.write(f'{Image.to_byte(color.x)} {Image.to_byte(color.y)} {Image.to_byte(color.z)} ')

            img_file.write('\n')





def TestImage():
    WIDTH = 3
    HIGTH = 2

    img = Image(WIDTH, HIGTH)
    red = Color(x=1, y=0, z=0)
    green = Color(x=0, y=1, z=0)
    blue = Color(x=0, y=0, z=1)

    img.set_pixel(0, 0, red)
    img.set_pixel(1, 0, green)
    img.set_pixel(2, 0, blue)

    img.set_pixel(0, 1, red + green)
    img.set_pixel(2, 1, red * 0.001)
    img.set_pixel(1, 1, red + blue + green)

    with open('test_image.ppm', "w") as img_file:
        img.write_ppm(img_file)


if __name__ == "__main__":
    TestImage()

