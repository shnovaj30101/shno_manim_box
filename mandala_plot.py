from manim import *
import numpy as np
import math
import random

from itertools import cycle

ALL_COLORS = [RED, BLUE, GREEN, TEAL, YELLOW, PURPLE, MAROON, PINK, GOLD]

repeat_num = 6
petal_order = 3
petal_length = 3
circle_order = 4

def get_astral():
    bezier_plot = Bezier([ORIGIN, RIGHT , RIGHT + UP * 0.3])
    bezier_plot2 = Bezier([ORIGIN, RIGHT, RIGHT + DOWN * 0.3])
    bezier_plot3 = Bezier([ORIGIN + 3*RIGHT, RIGHT, RIGHT + UP * 0.3])
    bezier_plot4 = Bezier([ORIGIN + 3*RIGHT, RIGHT, RIGHT + DOWN * 0.3])
    astral_group = VGroup(bezier_plot, bezier_plot2, bezier_plot3, bezier_plot4)
    return astral_group


class Bezier(ParametricFunction):
    def __init__(self, points, **kwargs):
        super().__init__(bezier(points),**kwargs)

def ploar_to_cartesian(radius, angle):
    return RIGHT * math.cos(angle) * radius + UP * math.sin(angle) * radius

class RandomMandala(Scene):
    def construct(self):

        center_point = ORIGIN

        petal_points = [
            center_point,
        ]
        petal_points_2 = [
            center_point,
        ]
        petal_points_3 = [
            center_point,
        ]

        for i in range(petal_order-1):
            petal_points.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_2.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_3.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
        # petal_points_2[-1] = petal_points[-1]
        # petal_points_3[-1] = petal_points[-1]
        petal_points.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_2.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_3.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))

        petal_bezier_plot = Bezier(petal_points)
        petal_bezier_plot_2 = Bezier(petal_points_2)
        petal_bezier_plot_3 = Bezier(petal_points_3)

        petal_group = VGroup(petal_bezier_plot, petal_bezier_plot_2, petal_bezier_plot_3)

        for i in range(repeat_num):
            new_group = petal_group.copy().rotate(i * TAU/repeat_num, about_point=center_point)
            self.add(new_group)

        # circle_points = [
        #     RIGHT * (petal_length + 0.5)
        # ]
        # circle_points_2 = [
        #     RIGHT * (petal_length + 0.5)
        # ]
        # circle_points_3 = [
        #     RIGHT * (petal_length + 0.5)
        # ]

        # for i in range(circle_order-2):
        #     circle_points.append(ploar_to_cartesian(
        #             random.uniform(petal_length - 0.5, petal_length + 0.5),
        #             TAU / repeat_num / (circle_order-1) * (i+1)
        #             ))
        #     circle_points_2.append(ploar_to_cartesian(
        #             random.uniform(petal_length - 0.5, petal_length + 0.5),
        #             TAU / repeat_num / (circle_order-1) * (i+1)
        #             ))
        #     circle_points_3.append(ploar_to_cartesian(
        #             random.uniform(petal_length - 0.5, petal_length + 0.5),
        #             TAU / repeat_num / (circle_order-1) * (i+1)
        #             ))

        # circle_points.append(ploar_to_cartesian(
        #         petal_length + 0.5,
        #         TAU / repeat_num
        #         ))
        # circle_points_2.append(ploar_to_cartesian(
        #         petal_length + 0.5,
        #         TAU / repeat_num
        #         ))
        # circle_points_3.append(ploar_to_cartesian(
        #         petal_length + 0.5,
        #         TAU / repeat_num
        #         ))

        # circle_bezier_plot = Bezier(circle_points)
        # circle_bezier_plot_2 = Bezier(circle_points_2)
        # circle_bezier_plot_3 = Bezier(circle_points_3)

        # circle_group = VGroup(circle_bezier_plot, circle_bezier_plot_2, circle_bezier_plot_3)

        # for i in range(repeat_num):
        #     new_group = circle_group.copy().rotate(i * TAU/repeat_num, about_point=center_point)
        #     self.add(new_group)

class RandomMandala2(Scene):
    def construct(self):
        center_point = ORIGIN

        petal_points = [
            center_point,
        ]
        petal_points_2 = [
            center_point,
        ]
        petal_points_3 = [
            center_point,
        ]

        for i in range(petal_order-1):
            petal_points.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_2.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_3.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
        # petal_points_2[-1] = petal_points[-1]
        # petal_points_3[-1] = petal_points[-1]
        petal_points.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_2.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_3.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))

        petal_bezier_plot = Bezier(petal_points)
        petal_bezier_plot_2 = Bezier(petal_points_2)
        petal_bezier_plot_3 = Bezier(petal_points_3)

        petal_group = VGroup(petal_bezier_plot, petal_bezier_plot_2, petal_bezier_plot_3)

        for i in range(repeat_num):
            new_group = petal_group.copy().rotate(i * TAU/repeat_num).shift(-ploar_to_cartesian(
                petal_length * 0.5,
                0.5 * TAU / repeat_num
                ))
            self.add(new_group)


class RandomMandala3(Scene):
    def construct(self):

        center_point = ORIGIN

        petal_points = [
            center_point,
        ]
        petal_points_2 = [
            center_point,
        ]
        petal_points_3 = [
            center_point,
        ]

        for i in range(petal_order-1):
            petal_points.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_2.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_3.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
        # petal_points_2[-1] = petal_points[-1]
        # petal_points_3[-1] = petal_points[-1]
        petal_points.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_2.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_3.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))

        petal_bezier_plot = Bezier(petal_points)
        petal_bezier_plot_2 = Bezier(petal_points_2)
        petal_bezier_plot_3 = Bezier(petal_points_3)
        print(petal_points)
        print(petal_points_2)
        print(petal_points_3)

        petal_group = VGroup(petal_bezier_plot, petal_bezier_plot_2, petal_bezier_plot_3)

        for i in range(repeat_num):
            new_group = petal_group.copy().rotate(i * TAU/repeat_num, about_point=center_point)
            self.add(new_group)

        c = Circle(radius=petal_length * 9/8, color=WHITE).move_to(center_point)
        self.add(c)
        c2 = Circle(radius=petal_length * 13/8, color=WHITE).move_to(center_point)
        self.add(c2)

        astral = get_astral()
        astral.shift(RIGHT * petal_length * 0.8)

        for i in range(repeat_num):
            new_astral = astral.copy().rotate(i * TAU/repeat_num, about_point=center_point)
            self.add(new_astral)


class astral(Scene):
    def construct(self):
        bezier_plot = Bezier([ORIGIN, RIGHT , RIGHT + UP * 0.3])
        bezier_plot2 = Bezier([ORIGIN, RIGHT, RIGHT + DOWN * 0.3])
        bezier_plot3 = Bezier([ORIGIN + 3*RIGHT, RIGHT, RIGHT + UP * 0.3])
        bezier_plot4 = Bezier([ORIGIN + 3*RIGHT, RIGHT, RIGHT + DOWN * 0.3])
        astral_group = VGroup(bezier_plot, bezier_plot2, bezier_plot3, bezier_plot4)

        self.add(astral_group)

def gen_random_mandala_circle(circle_length, circle_order, circle_wave, circle_angle):
    petal_points = [
        ploar_to_cartesian(
            circle_length/1.2,
            (0.5 + 0.1) * TAU / repeat_num
            )
    ]

    for i in range(circle_order-2):
        petal_points.append(
            ploar_to_cartesian(
                circle_length * random.uniform(1*(1+circle_wave)/2, 1*circle_wave),
                0.5 * TAU / repeat_num * (circle_order-2-i) / (circle_order-1)
                )
        )
    petal_points.append(
        ploar_to_cartesian(
            circle_length * circle_wave,
            0
            )
    )
    petal_bezier_plot = Bezier(petal_points)
    petal_bezier_plot_2 = Bezier(list(map(lambda p: p*(RIGHT+DOWN), petal_points)))
    group = VGroup(petal_bezier_plot, petal_bezier_plot_2)
    output_group = VGroup()
    for i in range(repeat_num):
        new_group = group.copy().rotate(i * TAU/repeat_num + circle_angle, about_point=ORIGIN)
        output_group.add(new_group)

    return output_group

class RandomMandalaCircle(Scene):
    def construct(self):

        circle_wave = 1.5
        ori_circle_length = 2
        # for i in range(5):
        #     if i % 2 == 0:
        #         self.add(gen_random_mandala_circle(ori_circle_length/(circle_wave**i), 5, circle_wave, 0))
        #     else:
        #         self.add(gen_random_mandala_circle(ori_circle_length/(circle_wave**i), 5, circle_wave, TAU/repeat_num/2))

        # for i in range(5):
                # self.add(gen_random_mandala_circle(ori_circle_length/(circle_wave**i), 5, circle_wave, TAU/repeat_num/3 * i))

        c = gen_random_mandala_circle(ori_circle_length, 5, circle_wave, 0)

        c_repeat_num = 3
        for i in range(c_repeat_num):
            new_c = c.copy().rotate(i * TAU/repeat_num/c_repeat_num, about_point=ORIGIN)
            self.add(new_c)

class RandomMandala4(Scene):
    def construct(self):
        center_point = ORIGIN

        petal_points = [
            center_point,
        ]
        petal_points_2 = [
            center_point,
        ]
        petal_points_3 = [
            center_point,
        ]

        for i in range(petal_order-1):
            petal_points.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_2.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
            petal_points_3.append(ploar_to_cartesian(
                random.uniform(i * petal_length/petal_order, (i+1) * petal_length/petal_order),
                random.uniform(-TAU/repeat_num, 2 * TAU / repeat_num)
                )
            )
        # petal_points_2[-1] = petal_points[-1]
        # petal_points_3[-1] = petal_points[-1]
        petal_points.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_2.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))
        petal_points_3.append(ploar_to_cartesian(
                petal_length,
                0.5 * TAU / repeat_num
                ))

        petal_bezier_plot = Bezier(petal_points)
        petal_bezier_plot_2 = Bezier(petal_points_2)
        petal_bezier_plot_3 = Bezier(petal_points_3)

        # petal_group = VGroup(petal_bezier_plot, petal_bezier_plot_2, petal_bezier_plot_3)
        petal_group = VGroup(petal_bezier_plot, petal_bezier_plot_2)

        for i in range(repeat_num):
            new_group = petal_group.copy().rotate(i * TAU/repeat_num).shift(-ploar_to_cartesian(
                petal_length * 0.5,
                0.5 * TAU / repeat_num
                ))
            self.add(new_group)

        circle_wave = 1.5
        ori_circle_length = 2
        c = gen_random_mandala_circle(ori_circle_length, 5, circle_wave, 0)

        c_repeat_num = 3
        for i in range(c_repeat_num):
            new_c = c.copy().rotate(i * TAU/repeat_num/c_repeat_num, about_point=ORIGIN)
            self.add(new_c)
