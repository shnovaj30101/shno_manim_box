from manim import *
from manim.utils.color import Colors
from nine_square import NineSquare


class question_19(Scene):
    def construct(self):

        # number_plane = NumberPlane()

        # self.add(number_plane)

        title = Tex("Problem 19.").scale(2).move_to(UP*3+RIGHT*3)

        s5 = NineSquare(self, chess_pos = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ], square_h=1.2, square_w=1.2, chess_color = Colors.red.value)
        s5.move_to(RIGHT*3)
        t5 = Tex("None").next_to(s5.line_vgroup, DOWN * 2)
        self.play(
            s5.display(),
            FadeIn(t5),
            FadeIn(title),
        )


        s1 = NineSquare(self, chess_pos = [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
            ], square_h=0.6, square_w=0.6)
        s1.move_to(LEFT*5 + UP * 2.25)
        t1 = Tex("E").next_to(s1.line_vgroup, DOWN * 2)
        self.play(
            s1.display(),
            FadeIn(t1),
        )

        s2 = NineSquare(self, chess_pos = [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
            ], square_h=0.6, square_w=0.6, chess_color = Colors.red.value)
        s2.move_to(LEFT*1.5 + UP * 2.25)
        t2 = Tex("E").next_to(s2.line_vgroup, DOWN * 2)
        self.play(
            s2.display(),
            FadeIn(t2),
        )

        s3 = NineSquare(self, chess_pos = [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
            ], square_h=0.6, square_w=0.6, chess_color = Colors.green.value)
        s3.move_to(LEFT*1.5 + DOWN * 1)
        t3 = Tex("E").next_to(s3.line_vgroup, DOWN * 2)
        self.play(
            s3.display(),
            FadeIn(t3),
        )

        s4 = NineSquare(self, chess_pos = [
            [0, 1, 1],
            [0, 0, 1],
            [0, 0, 0],
            ], square_h=0.6, square_w=0.6, chess_color = Colors.yellow.value)
        s4.move_to(LEFT*5 + DOWN * 1)
        t4 = Tex("E").next_to(s4.line_vgroup, DOWN * 2)
        self.play(
            s4.display(),
            FadeIn(t4),
        )

        self.wait(0.5)

        t2_1 = Tex("L").next_to(s2.line_vgroup, DOWN * 2)
        self.play(
            *s2.board_rotate(return_animate=True),
            ReplacementTransform(t2, t2_1),
        )
        self.wait(0.5)

        t3_1 = Tex("L").next_to(s3.line_vgroup, DOWN * 2)
        self.play(
            *s3.board_rotate(return_animate=True),
            ReplacementTransform(t3, t3_1),
        )
        self.wait(0.5)

        t3_2 = Tex("L@L").next_to(s3.line_vgroup, DOWN * 2)
        self.play(
            *s3.board_rotate(return_animate=True),
            ReplacementTransform(t3_1, t3_2),
        )
        self.wait(0.5)

        t4_1 = Tex("L").next_to(s4.line_vgroup, DOWN * 2)
        self.play(
            *s4.board_rotate(return_animate=True),
            ReplacementTransform(t4, t4_1),
        )
        self.wait(0.5)

        t4_2 = Tex("L@L").next_to(s4.line_vgroup, DOWN * 2)
        self.play(
            *s4.board_rotate(return_animate=True),
            ReplacementTransform(t4_1, t4_2),
        )
        self.wait(0.5)

        t4_3 = Tex("L@L@L").next_to(s4.line_vgroup, DOWN * 2)
        self.play(
            *s4.board_rotate(return_animate=True),
            ReplacementTransform(t4_2, t4_3),
        )
        self.wait(0.5)

        t5_1 = Tex("E").next_to(s5.line_vgroup, DOWN * 2)
        self.play(
            *s5.add_chess_to_board(chess_pos = [
                    [0, 1, 1],
                    [0, 0, 1],
                    [0, 0, 0],
                ], return_animate = True, source_board = s1),
            ReplacementTransform(t5, t5_1),
        )
        self.wait(0.2)

        t5_2 = Tex("E+L").next_to(s5.line_vgroup, DOWN * 2)
        self.play(
            *s5.add_chess_to_board(chess_pos = [
                    [1, 1, 0],
                    [1, 0, 0],
                    [0, 0, 0],
                ], return_animate = True, source_board = s2),
            ReplacementTransform(t5_1, t5_2),
        )
        self.wait(0.2)

        t5_3 = Tex("E+L+(L@L)").next_to(s5.line_vgroup, DOWN * 2)
        self.play(
            *s5.add_chess_to_board(chess_pos = [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                ], return_animate = True, source_board = s3),
            ReplacementTransform(t5_2, t5_3),
        )
        self.wait(0.2)

        t5_4 = Tex("E+L+(L@L)+(L@L@L)").next_to(s5.line_vgroup, DOWN * 2)
        self.play(
            *s5.add_chess_to_board(chess_pos = [
                    [0, 0, 0],
                    [0, 0, 1],
                    [0, 1, 1],
                ], return_animate = True, source_board = s4),
            ReplacementTransform(t5_3, t5_4),
        )
        self.wait(0.2)

        self.wait(2)
