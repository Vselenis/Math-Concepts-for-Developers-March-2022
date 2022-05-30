from image import Image
from ray import Ray
from point import Point
from color import Color


class Engine:
    MAX_DEPTH = 5
    MIN_DISPLACE = 0.0002

    def render(self, scene):
        width = scene.width
        height = scene.height
        aspect_ratio = width / height
        x_min = -1.0
        x_max = +1.0
        # we calculate pixel in every x move
        x_move = (x_max - x_min) / (width - 1)
        y_min = -1.0 / aspect_ratio
        y_max = +1.0 / aspect_ratio
        # we calculate pixel in every y move
        y_move = (y_max - y_min) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for ys in range(height):
            y = y_min + ys * y_move
            for xs in range(width):
                x = x_min + xs * x_move
                ray = Ray(camera, Point(x, y) - camera)
                pixels.set_pixel(xs, ys, self.ray_trace(ray, scene))
        return pixels

    def ray_trace(self, ray, scene, depth=0):
        color = Color(0, 0, 0)
        self.find_nearest(ray, scene)
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.direction * dist_hit
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        if depth < self.MAX_DEPTH:
            new_ray_origin = hit_pos + hit_normal * self.MIN_DISPLACE #MIN_DISPLACE is delta from the formula
            new_ray_direction = ray.direction - 2 * ray.direction.dot_product(hit_normal) * hit_normal
            new_ray = Ray(new_ray_origin, new_ray_direction)
            #Attenuate the reflected ray by the reflection coefficient
            color += (self.ray_trace(new_ray, scene, depth+1) * obj_hit.material.reflection)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None
        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj

        return (dist_min, obj_hit)

    # pretty complex function - direct implementation of the requirements.
    def color_at(self, obj_hit, hit_pos, normal, scene):
        material = obj_hit.material
        obj_color = material.color_at(hit_pos)
        to_cam = scene.camera - hit_pos
        specular_k = 50
        color = material.ambient * Color.from_hex("#000000")
        # Light calculations
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            # Diffuse shading (Lambert)
            color += obj_color * material.diffuse \
                     * max(normal.dot_product(to_light.direction), 0)  # max prevent negative values
            # Specular shading (Blinn-Phong)
            half_vector = (to_light.direction + to_cam).normalize()
            color += (light.color * material.specular \
                      * max(normal.dot_product(half_vector), 0) ** specular_k)

        return color
