from manim import *
from manim.utils.color import Colors
import itertools as it

def get_chess_circle(radius, color=average_color(Colors.black.value, Colors.blue.value), border_color=Colors.blue.value):
    vgroup = VGroup()
    circle = Circle(radius=radius, color=color, fill_opacity=1)
    border = Circle(radius=radius, color=border_color)
    vgroup.add(circle)
    vgroup.add(border)

    return vgroup

class NineSquare:
    def __init__(self, 
            scene,
            chess_pos = None,
            chess_color = Colors.blue.value,
            square_h=1,
            square_w=1
            ):

        self.scene = scene
        self.square_h = square_h
        self.square_w = square_w

        if chess_pos is None:
            chess_pos = [
                    [0,0,0],
                    [0,0,0],
                    [0,0,0],
                    ]

        self.line_vgroup = VGroup()
        self.mobject_pos = [
                [[], [], []],
                [[], [], []],
                [[], [], []],
                ]

        v_line_list = []
        v_line_list.extend(
                [
                    Line(1.5*square_w*LEFT + 1.5*square_h*DOWN, 1.5*square_w*LEFT + 1.5*square_h*UP),
                    Line(0.5*square_w*LEFT + 1.5*square_h*DOWN, 0.5*square_w*LEFT + 1.5*square_h*UP),
                    Line(0.5*square_w*RIGHT + 1.5*square_h*DOWN, 0.5*square_w*RIGHT + 1.5*square_h*UP),
                    Line(1.5*square_w*RIGHT + 1.5*square_h*DOWN, 1.5*square_w*RIGHT + 1.5*square_h*UP),
                    ]
                )
        h_line_list = []
        h_line_list.extend(
                [
                    Line(1.5*square_h*UP + 1.5*square_w*LEFT, 1.5*square_h*UP+ 1.5*square_w*RIGHT),
                    Line(0.5*square_h*UP + 1.5*square_w*LEFT, 0.5*square_h*UP+ 1.5*square_w*RIGHT),
                    Line(0.5*square_h*DOWN + 1.5*square_w*LEFT, 0.5*square_h*DOWN+ 1.5*square_w*RIGHT),
                    Line(1.5*square_h*DOWN + 1.5*square_w*LEFT, 1.5*square_h*DOWN+ 1.5*square_w*RIGHT),
                    ]
                )

        for line in v_line_list:
            self.line_vgroup.add(line)

        for line in h_line_list:
            self.line_vgroup.add(line)

        self.add_chess_to_board(chess_pos, chess_color = chess_color, return_animate = False)

    def add_chess_to_board(self, chess_pos, chess_color = Colors.blue.value, return_animate = False, source_board=None):
        if return_animate:
            animate_list = []
            for row_idx, col_idx in it.product(range(3), range(3)):
                if chess_pos[row_idx][col_idx] == 0:
                    continue

                animate_list.extend(
                    self.add_chess_to_lattice(chess_pos[row_idx][col_idx], (row_idx, col_idx), chess_color, return_animate, source_board)
                )

            return animate_list

        else:
            for row_idx, col_idx in it.product(range(3), range(3)):
                if chess_pos[row_idx][col_idx] == 0:
                    continue

                self.add_chess_to_lattice(chess_pos[row_idx][col_idx], (row_idx, col_idx), chess_color, return_animate, source_board)

    def add_chess_to_lattice(self, chess_num, board_pos, chess_color = Colors.blue.value, return_animate = False, source_board = None):
        if return_animate:
            if chess_num == 0:
                return []

            row_idx, col_idx = board_pos
             
            animate_list = []
            chess_num += len(self.mobject_pos[row_idx][col_idx])

            for i in range(chess_num):
                if i < len(self.mobject_pos[row_idx][col_idx]):
                    animate_list.append(
                        self.mobject_pos[row_idx][col_idx][i].animate.move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                    )

                else:
                    if source_board is None:
                        chess_circle = get_chess_circle(
                                    color = average_color(Colors.black.value, chess_color),
                                    border_color= chess_color,
                                    radius = min(self.square_h, self.square_w) * 0.5 * 0.5
                                ).move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle.set_z_index(i)

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle
                            )

                        animate_list.append(FadeIn(chess_circle))
                    else:
                        chess_circle_source = source_board.mobject_pos[row_idx][col_idx].pop(i-chess_num)
                        chess_circle_target = get_chess_circle(
                                    color = chess_circle_source[0].color,
                                    border_color= chess_circle_source[1].color,
                                    radius = min(self.square_h, self.square_w) * 0.5 * 0.5
                                ).move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle_target.set_z_index(100)
                        animate_list.append(
                                ReplacementTransform(chess_circle_source, chess_circle_target)
                        )

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle_target
                            )

            return animate_list

        else:
            if chess_num == 0:
                return 

            row_idx, col_idx = board_pos

            chess_num += len(self.mobject_pos[row_idx][col_idx])

            for i in range(chess_num):

                if i < len(self.mobject_pos[row_idx][col_idx]):
                    self.mobject_pos[row_idx][col_idx][i].move_to(
                                self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                        + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                        + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                        + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                            )

                else:
                    if source_board is None:
                        chess_circle = get_chess_circle(
                                    color = average_color(Colors.black.value, chess_color),
                                    border_color= chess_color,
                                    radius = min(self.square_h, self.square_w) * 0.5 * 0.5
                                ).move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle.set_z_index(i)

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle
                            )

                    else:
                        chess_circle = source_board.mobject_pos[row_idx][col_idx].pop(i-chess_num)
                        chess_circle.move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle
                            )


    def display(self):
        self.scene.play(FadeIn(self.line_vgroup))

        chess_vgroup = VGroup()
        for row_idx, col_idx in it.product(range(3), range(3)):
            chess_vgroup.add(*self.mobject_pos[row_idx][col_idx])

        self.scene.play(FadeIn(chess_vgroup))

    def move_to(self, pos):
        self.line_vgroup.move_to(pos)

        chess_vgroup = VGroup()
        for row_idx, col_idx in it.product(range(3), range(3)):
            chess_vgroup.add(*self.mobject_pos[row_idx][col_idx])

        chess_vgroup.move_to(pos)

    def pos_rotate(self):
        pass

    def animate_rotate(self):
        pass

class nine_square_problem(Scene):
    def construct(self):
        s = NineSquare(self, chess_pos = [
            [0, 1, 2],
            [0, 0, 3],
            [1, 0, 0],
            ], square_h=1.5, square_w=1.5)
        s.move_to(LEFT*4)
        s.display()

        t = NineSquare(self, chess_pos = [
            [0, 2, 1],
            [0, 0, 1],
            [2, 0, 0],
            ], square_h=1.5, square_w=1.5, chess_color = Colors.red.value)
        t.move_to(RIGHT*4)
        t.display()

        self.play(
            *t.add_chess_to_board(chess_pos = [
                    [0, 1, 1],
                    [0, 0, 2],
                    [1, 0, 0],
                ], return_animate = True, source_board = s),
        )
        self.wait()

        # a = [
            # [[], [], []],
            # [[], [], []],
            # [[], [], []],
        # ]
        # for row_idx, col_idx in it.product(range(3), range(3)):
            # for obj in t.mobject_pos[row_idx][col_idx]:
                # a[row_idx][col_idx].append(obj.z_index)

        # print(a)


