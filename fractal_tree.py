
from manim import *
from collections import deque
from math import cos, sin
import numpy as np
import random

def vec_rot(vec, degree):
    theta = np.deg2rad(degree)
    rot = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    return np.dot(rot, vec)

def get_angle(vec1, vec2):
    return np.arctan2(vec2[1], vec2[0]) - np.arctan2(vec1[1], vec1[0])

class tree(Scene):
    def construct(self):

        square_queue = deque()
        ori_edge = 1.6
        ori_pos = DOWN * 3 + LEFT * ori_edge / 2
        layer_count = 1
        render_num = 10

        # def update_path(path):
            # previous_path = path.copy()
            # previous_path.add_points_as_corners([dot.get_center()])
            # path.become(previous_path)

        square_queue.append([ori_pos, ori_pos + ori_edge / 2 * RIGHT + ori_edge / 2 * UP, 1])
        color_list = [BLUE_C, TEAL_C, GREEN_C, YELLOW_C, GOLD_C, RED_C]

        for i in range(render_num):
            draw_item_list = []
            while len(square_queue) > 0 and square_queue[0][2] == layer_count:
                now_item = square_queue.popleft()
                draw_item_list.append(now_item)
                ver_edge = vec_rot((now_item[1] - now_item[0])[0:2], 45) * 2**0.5
                ver_edge = np.append(ver_edge, 0.0)
                hor_edge = vec_rot((now_item[1] - now_item[0])[0:2], -45) * 2**0.5
                hor_edge = np.append(hor_edge, 0.0)

                if layer_count + 1 <= render_num:
                    square_queue.append([
                        now_item[0] + ver_edge,
                        now_item[0] + ver_edge * 1.5,
                        layer_count + 1,
                        ])
                    square_queue.append([
                        now_item[1] + ver_edge,
                        now_item[1] + ver_edge + hor_edge / 2,
                        layer_count + 1,
                        ])

            layer_count += 1
            square_create_list = []

            for now_item in draw_item_list:
                s = Square(side_length=np.linalg.norm(now_item[1]-now_item[0]) * 2**0.5)
                s.move_to(now_item[1])
                s.rotate(get_angle(UP+RIGHT, now_item[1]-now_item[0]))
                s.set_color(random.choice(color_list))
                square_create_list.append(Create(s))

            self.play(*square_create_list)

            # for idx, now_item in enumerate(draw_item_list):
                # path = VMobject()
                # dot = Dot()
                # dot.move_to(now_item[0])
                # path.set_points_as_corners([dot.get_center(), dot.get_center()])
                # path.add_updater(update_path)
                # ver_edge = vec_rot((now_item[1] - now_item[0])[0:2], 45) * 2**0.5
                # ver_edge = np.append(ver_edge, 0.0)
                # hor_edge = vec_rot((now_item[1] - now_item[0])[0:2], -45) * 2**0.5
                # hor_edge = np.append(hor_edge, 0.0)
                # self.add(path, dot)
                # self.play(dot.animate.shift( hor_edge ))
                # self.play(dot.animate.shift( ver_edge ))
                # self.play(dot.animate.shift( -hor_edge ))
                # self.play(dot.animate.shift( -ver_edge ))


