from color import Color
from point import Point
from vector import Vector
from scene import Scene
from sphere import Sphere
from engine import Engine
from light import Light
from material import Material, Surface



def main():
    WIDTH = 960
    HEIGHT = 540
    camera = Vector(0, -0.38, -1.4)
    objects = [Sphere(
        Point(0, 10000.5, 1),
        10000.0,
        Surface(
            color1=Color.from_hex("#420500"),
            color2=Color.from_hex("#e6b87d"),
            ambient=0.2,
            reflection=0.2,
        ),
    ), Sphere(Point(-1, -0.05, 1.5), 0.5, Material(Color.from_hex("FF0000"))),
        Sphere(Point(1, -0.05, 1.5), 0.5, Material(Color.from_hex("00FF00"))),
        Sphere(Point(0, -0.1, 1), 0.2, Material(Color.from_hex("FFFF00")))]
    lights = [Light(Point(-0.5, -10.5, 0), Color.from_hex("#E6E6E6"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = Engine()
    image = engine.render(scene)

    with open('ray_tracing_world.ppm', "w") as img_file:
        image.write_ppm(img_file)


if __name__ == "__main__":
    main()

