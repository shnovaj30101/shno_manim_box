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

    def add_chess_to_lattice(self, append_chess_num, board_pos, chess_color = Colors.blue.value, return_animate = False, source_board = None):
        if return_animate:
            if append_chess_num == 0:
                return []

            row_idx, col_idx = board_pos
             
            animate_list = []
            ori_chess_num = len(self.mobject_pos[row_idx][col_idx])
            finish_chess_num = ori_chess_num + append_chess_num


            for i in range(finish_chess_num):
                if i < ori_chess_num:
                    animate_list.append(
                        self.mobject_pos[row_idx][col_idx][i].animate.move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
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
                                            + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle.set_z_index(i)

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle
                            )

                        animate_list.append(FadeIn(chess_circle))
                    else:
                        chess_circle_source = source_board.mobject_pos[row_idx][col_idx].pop(i-finish_chess_num)
                        chess_circle_target = get_chess_circle(
                                    color = chess_circle_source[0].color,
                                    border_color= chess_circle_source[1].color,
                                    radius = min(self.square_h, self.square_w) * 0.5 * 0.5
                                ).move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle_target.set_z_index(i)
                        animate_list.append(
                                ReplacementTransform(chess_circle_source, chess_circle_target)
                        )

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle_target
                            )

            if source_board:
                remain_chess_num = len(source_board.mobject_pos[row_idx][col_idx])

                for i in range(remain_chess_num):
                    animate_list.append(
                        source_board.mobject_pos[row_idx][col_idx][i].animate.move_to(
                                    source_board.line_vgroup.get_center() + UP * 1 * source_board.square_h + LEFT * 1 * source_board.square_w \
                                            + source_board.square_w * col_idx * RIGHT +  source_board.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * source_board.square_w * (remain_chess_num-1) * LEFT + 0.5 * 0.1 * source_board.square_h * (remain_chess_num-1) * UP \
                                            + 0.1 * source_board.square_w * i * RIGHT + 0.1 * source_board.square_h * i * DOWN 
                                )
                    )

            return animate_list

        else:
            if append_chess_num == 0:
                return

            row_idx, col_idx = board_pos

            ori_chess_num = len(self.mobject_pos[row_idx][col_idx])
            finish_chess_num = ori_chess_num + append_chess_num

            for i in range(finish_chess_num):

                if i < ori_chess_num:
                    self.mobject_pos[row_idx][col_idx][i].move_to(
                                self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                        + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                        + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
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
                                            + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
                                            + 0.1 * self.square_w * i * RIGHT + 0.1 * self.square_h * i * DOWN 
                                )
                        chess_circle.set_z_index(i)

                        self.mobject_pos[row_idx][col_idx].append(
                                    chess_circle
                            )

                    else:
                        chess_circle = source_board.mobject_pos[row_idx][col_idx].pop(i-finish_chess_num)
                        chess_circle.move_to(
                                    self.line_vgroup.get_center() + UP * 1 * self.square_h + LEFT * 1 * self.square_w \
                                            + self.square_w * col_idx * RIGHT +  self.square_h * row_idx * DOWN \
                                            + 0.5 * 0.1 * self.square_w * (finish_chess_num-1) * LEFT + 0.5 * 0.1 * self.square_h * (finish_chess_num-1) * UP \
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
        shift_dir = pos - self.line_vgroup.get_center()
        self.line_vgroup.shift(shift_dir)

        chess_vgroup = VGroup()
        for row_idx, col_idx in it.product(range(3), range(3)):
            chess_vgroup.add(*self.mobject_pos[row_idx][col_idx])

        chess_vgroup.shift(shift_dir)

    def board_rotate(self, return_animate = False):
        if return_animate:
            animate_list = []

            animate_list.append(
                Rotate(self.line_vgroup, angle = TAU/4)    
            )

            for row_idx, col_idx in it.product(range(3), range(3)):
                if len(self.mobject_pos[row_idx][col_idx]) == 0:
                    continue

                chess_group = VGroup(*self.mobject_pos[row_idx][col_idx])
                chess_group_destination = chess_group.copy().rotate(
                    angle = TAU/4,
                    about_point = self.line_vgroup.get_center(),
                ).rotate(
                    angle = -TAU/4,
                )
                animate_list.append(
                    Transform(
                        chess_group,
                        chess_group_destination,
                        path_func = utils.paths.path_along_arc(TAU / 4),
                    )
                )
                

            tmp = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
            for row_idx, col_idx in it.product(range(3), range(3)):
                if row_idx == 0 and col_idx == 0:
                    tmp[2][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 1:
                    tmp[1][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 2:
                    tmp[0][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 0:
                    tmp[2][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 1:
                    tmp[1][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 2:
                    tmp[0][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 0:
                    tmp[2][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 1:
                    tmp[1][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 2:
                    tmp[0][2] = self.mobject_pos[row_idx][col_idx]
            for row_idx, col_idx in it.product(range(3), range(3)):
                self.mobject_pos[row_idx][col_idx] = tmp[row_idx][col_idx]

            return animate_list
        else:
            tmp = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
            for row_idx, col_idx in it.product(range(3), range(3)):
                if row_idx == 0 and col_idx == 0:
                    tmp[2][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 1:
                    tmp[1][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 2:
                    tmp[0][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 0:
                    tmp[2][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 1:
                    tmp[1][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 2:
                    tmp[0][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 0:
                    tmp[2][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 1:
                    tmp[1][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 2:
                    tmp[0][2] = self.mobject_pos[row_idx][col_idx]
            for row_idx, col_idx in it.product(range(3), range(3)):
                self.mobject_pos[row_idx][col_idx] = tmp[row_idx][col_idx]

    def chess_left_shift(self, return_animate = False):
        if return_animate:
            animate_list = []

            for row_idx, col_idx in it.product(range(3), range(3)):
                if len(self.mobject_pos[row_idx][col_idx]) == 0:
                    continue

                chess_group = VGroup(*self.mobject_pos[row_idx][col_idx])
                chess_group_destination = chess_group.copy()
                if col_idx == 0:
                    chess_group_destination.shift(2 * self.square_w * RIGHT)
                    animate_list.append(
                        Transform(
                            chess_group,
                            chess_group_destination,
                            path_func = utils.paths.path_along_arc(TAU / 4),
                        )
                    )
                else:
                    chess_group_destination.shift(self.square_w * LEFT)
                    animate_list.append(
                        Transform(
                            chess_group,
                            chess_group_destination,
                        )
                    )

            
            tmp = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
            for row_idx, col_idx in it.product(range(3), range(3)):
                if row_idx == 0 and col_idx == 0:
                    tmp[0][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 1:
                    tmp[0][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 2:
                    tmp[0][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 0:
                    tmp[1][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 1:
                    tmp[1][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 2:
                    tmp[1][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 0:
                    tmp[2][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 1:
                    tmp[2][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 2:
                    tmp[2][1] = self.mobject_pos[row_idx][col_idx]
            for row_idx, col_idx in it.product(range(3), range(3)):
                self.mobject_pos[row_idx][col_idx] = tmp[row_idx][col_idx]

            return animate_list
        else:
            tmp = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ]
            for row_idx, col_idx in it.product(range(3), range(3)):
                if row_idx == 0 and col_idx == 0:
                    tmp[0][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 1:
                    tmp[0][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 0 and col_idx == 2:
                    tmp[0][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 0:
                    tmp[1][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 1:
                    tmp[1][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 1 and col_idx == 2:
                    tmp[1][1] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 0:
                    tmp[2][2] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 1:
                    tmp[2][0] = self.mobject_pos[row_idx][col_idx]
                if row_idx == 2 and col_idx == 2:
                    tmp[2][1] = self.mobject_pos[row_idx][col_idx]
            for row_idx, col_idx in it.product(range(3), range(3)):
                self.mobject_pos[row_idx][col_idx] = tmp[row_idx][col_idx]


class shift_chess_betw_boards(Scene):
    def construct(self):
        s = NineSquare(self, chess_pos = [
            [0, 3, 4],
            [0, 0, 3],
            [2, 0, 0],
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
                    [0, 2, 2],
                    [0, 0, 3],
                    [1, 0, 0],
                ], return_animate = True, source_board = s),
        )
        self.wait()


class board_rotate(Scene):
    def construct(self):
        s = NineSquare(self, chess_pos = [
            [0, 3, 4],
            [0, 0, 3],
            [2, 0, 0],
            ], square_h=1.5, square_w=1.5)
        s.move_to(LEFT*4)
        s.display()

        self.play(
            *s.board_rotate(return_animate=True)
        )
        self.wait()

class chess_left_shift(Scene):
    def construct(self):
        s = NineSquare(self, chess_pos = [
            [0, 3, 4],
            [0, 0, 3],
            [2, 0, 0],
            ], square_h=1.5, square_w=1.5)
        s.move_to(LEFT*4)
        s.display()

        self.play(
            *s.chess_left_shift(return_animate=True)
        )
        self.wait()


