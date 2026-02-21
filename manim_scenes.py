"""
Manim Animation Scenes for "Vectors: The Language of Data"
Author: Dr Milan Joshi
Theme: Blueprint Noir — cinematic, minimal, architectural

Each Scene class produces one animation for embedding into Beamer slides
via the animate LaTeX package (PNG frame sequences).
"""

from manim import *
import numpy as np

# ============================================================
# GLOBAL COLOR PALETTE — "Blueprint Noir"
# ============================================================
BG_COLOR = "#0B0B1A"
VECTOR_A_COLOR = "#4FC3F7"    # Electric Blue
VECTOR_B_COLOR = "#FF8A65"    # Warm Orange
RESULTANT_COLOR = "#66BB6A"   # Vibrant Green
PROJECTION_COLOR = "#AB47BC"  # Soft Purple
LABEL_COLOR = "#B0BEC5"       # Neutral Gray
ACCENT_COLOR = "#FFD54F"      # Gold
GRID_COLOR = "#1A1A3A"        # Blueprint grid lines
GRID_COLOR_BRIGHT = "#252550" # Brighter grid for visibility
TEXT_COLOR = "#EEEEFF"        # Clean white
TABLE_HEADER_COLOR = "#4FC3F7"
TABLE_ROW_COLOR = "#EEEEFF"
HIGHLIGHT_COLOR = "#FFD54F"   # Gold highlight

# ============================================================
# REUSABLE HELPER FUNCTIONS
# ============================================================

def create_blueprint_grid(x_range=(-7, 7), y_range=(-4, 4), step=1):
    """Create a subtle blueprint-style background grid."""
    lines = VGroup()
    for x in np.arange(x_range[0], x_range[1] + step, step):
        lines.add(Line(
            start=[x, y_range[0], 0],
            end=[x, y_range[1], 0],
            stroke_width=0.5,
            stroke_color=GRID_COLOR,
            stroke_opacity=0.4
        ))
    for y in np.arange(y_range[0], y_range[1] + step, step):
        lines.add(Line(
            start=[x_range[0], y, 0],
            end=[x_range[1], y, 0],
            stroke_width=0.5,
            stroke_color=GRID_COLOR,
            stroke_opacity=0.4
        ))
    return lines


def create_glowing_dot(position, color=ACCENT_COLOR, radius=0.07):
    """Create a dot with a subtle glow effect."""
    glow = Dot(position, color=color, radius=radius * 3, fill_opacity=0.15)
    dot = Dot(position, color=color, radius=radius)
    return VGroup(glow, dot)


# ============================================================
# SCENE 1: DataToVector (v4 — FASTER TIMING)
#
# Target: ~15s at 60fps = ~900 frames
# Playback at 60fps in PDF = snappy
# ============================================================

class DataToVector(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── Background grid (sparse for performance) ──
        bg_grid = create_blueprint_grid(x_range=(-8, 8), y_range=(-5, 5), step=2)
        bg_grid.set_opacity(0.12)
        self.add(bg_grid)

        # ═══════════════════════════════════════
        # BEAT 1 — Title Card (~2.5s)
        # ═══════════════════════════════════════
        title = Text("What is a Vector?", font_size=48, color=TEXT_COLOR, weight=BOLD)
        subtitle = Text(
            "A numerical representation of data",
            font_size=24, color=LABEL_COLOR,
        )
        subtitle.next_to(title, DOWN, buff=0.4)

        left_line = Line(
            title.get_left() + LEFT * 0.5, title.get_left() + LEFT * 2.5,
            color=VECTOR_A_COLOR, stroke_width=2, stroke_opacity=0.6,
        )
        right_line = Line(
            title.get_right() + RIGHT * 0.5, title.get_right() + RIGHT * 2.5,
            color=VECTOR_A_COLOR, stroke_width=2, stroke_opacity=0.6,
        )

        scan_line = Line(LEFT * 8, RIGHT * 8, color=VECTOR_A_COLOR,
                         stroke_width=1.5, stroke_opacity=0.3)
        scan_line.move_to(UP * 4)

        self.play(
            scan_line.animate.move_to(DOWN * 4),
            FadeIn(title, shift=UP * 0.3),
            Create(left_line), Create(right_line),
            run_time=0.8,
        )
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.4)
        self.wait(0.8)

        self.play(
            FadeOut(title), FadeOut(subtitle),
            FadeOut(left_line), FadeOut(right_line),
            FadeOut(scan_line),
            run_time=0.5,
        )

        # ═══════════════════════════════════════
        # BEAT 2 — Patient Data Table
        # ═══════════════════════════════════════
        section_label = Text("MEDICAL DATASET", font_size=14,
                             color=VECTOR_A_COLOR, weight=BOLD)
        section_label.to_edge(UP, buff=0.35).shift(LEFT * 3)
        underline = Line(
            section_label.get_left() + DOWN * 0.15,
            section_label.get_right() + DOWN * 0.15,
            color=VECTOR_A_COLOR, stroke_width=1.5, stroke_opacity=0.5,
        )

        self.play(
            FadeIn(section_label, shift=DOWN * 0.1),
            Create(underline),
            run_time=0.4,
        )

        header_texts = ["Patient", "Age", "BP"]
        header = VGroup(*[
            Text(t, font_size=18, color=TABLE_HEADER_COLOR, weight=BOLD)
            for t in header_texts
        ])
        header.arrange(RIGHT, buff=1.0)
        header.next_to(section_label, DOWN, buff=0.5)

        h_sep = Line(
            header.get_left() + LEFT * 0.4 + DOWN * 0.18,
            header.get_right() + RIGHT * 0.4 + DOWN * 0.18,
            color=VECTOR_A_COLOR, stroke_width=1, stroke_opacity=0.4,
        )

        rows_data = [
            ("Patient 1", "58", "122"),
            ("Patient 2", "71", "110"),
            ("Patient 3", "48", "110"),
            ("Patient 4", "34", "123"),
            ("Patient 5", "62", "152"),
        ]

        data_rows = VGroup()
        for name, age, bp in rows_data:
            cells = VGroup(
                Text(name, font_size=16, color=TABLE_ROW_COLOR),
                Text(age, font_size=16, color=TABLE_ROW_COLOR),
                Text(bp, font_size=16, color=TABLE_ROW_COLOR),
            )
            cells.arrange(RIGHT, buff=1.0)
            for cell, hcell in zip(cells, header):
                cell.move_to([hcell.get_x(), cell.get_y(), 0])
            data_rows.add(cells)

        data_rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        data_rows.next_to(h_sep, DOWN, buff=0.25)

        self.play(FadeIn(header, shift=DOWN * 0.15), Create(h_sep), run_time=0.4)
        self.play(
            LaggedStart(*[FadeIn(row, shift=DOWN * 0.1) for row in data_rows],
                         lag_ratio=0.12),
            run_time=0.8,
        )
        self.wait(0.5)

        # ═══════════════════════════════════════
        # BEAT 3 — Highlight Patient 1
        # ═══════════════════════════════════════
        highlight_rect = SurroundingRectangle(
            data_rows[0], color=HIGHLIGHT_COLOR,
            stroke_width=2.5, corner_radius=0.08, buff=0.1,
        )
        glow_rect = SurroundingRectangle(
            data_rows[0], color=HIGHLIGHT_COLOR,
            stroke_width=0, fill_color=HIGHLIGHT_COLOR,
            fill_opacity=0.06, corner_radius=0.08, buff=0.1,
        )
        self.play(Create(highlight_rect), FadeIn(glow_rect), run_time=0.4)
        self.play(
            highlight_rect.animate.set_stroke(opacity=0.3),
            glow_rect.animate.set_opacity(0.12),
            rate_func=there_and_back, run_time=0.5,
        )
        self.wait(0.3)

        # ═══════════════════════════════════════
        # BEAT 4 — Extract into Column Vector
        # ═══════════════════════════════════════
        extract_arrow = MathTex(r"\Longrightarrow", font_size=32, color=ACCENT_COLOR)
        extract_arrow.next_to(data_rows[0], RIGHT, buff=0.6)

        col_vector = Tex(
            r"$\vec{p}_1 = \begin{bmatrix} 58 \\ 122 \end{bmatrix}$",
            font_size=34, color=ACCENT_COLOR,
        )
        col_vector.next_to(extract_arrow, RIGHT, buff=0.5)

        age_label = Text("Age", font_size=12, color=VECTOR_A_COLOR)
        bp_label = Text("BP", font_size=12, color=VECTOR_B_COLOR)
        age_label.next_to(col_vector, RIGHT, buff=0.3).shift(UP * 0.15)
        bp_label.next_to(col_vector, RIGHT, buff=0.3).shift(DOWN * 0.15)

        age_arrow = Arrow(
            age_label.get_left(), col_vector.get_right() + RIGHT * 0.02 + UP * 0.15,
            color=VECTOR_A_COLOR, stroke_width=1.5, buff=0.05,
            max_tip_length_to_length_ratio=0.3,
        )
        bp_arrow = Arrow(
            bp_label.get_left(), col_vector.get_right() + RIGHT * 0.02 + DOWN * 0.15,
            color=VECTOR_B_COLOR, stroke_width=1.5, buff=0.05,
            max_tip_length_to_length_ratio=0.3,
        )

        self.play(FadeIn(extract_arrow, shift=RIGHT * 0.2), run_time=0.3)
        self.play(FadeIn(col_vector, shift=RIGHT * 0.2), run_time=0.5)
        self.play(
            FadeIn(age_label, shift=LEFT * 0.1), FadeIn(bp_label, shift=LEFT * 0.1),
            GrowArrow(age_arrow), GrowArrow(bp_arrow),
            run_time=0.4,
        )
        self.wait(0.5)

        # ═══════════════════════════════════════
        # BEAT 5 — Transition: shrink table, bring in plot
        # ═══════════════════════════════════════
        table_group = VGroup(
            section_label, underline, header, h_sep, data_rows,
            highlight_rect, glow_rect,
            extract_arrow, col_vector, age_label, bp_label, age_arrow, bp_arrow,
        )

        divider = Line(
            UP * 3.5, DOWN * 3.5,
            color=VECTOR_A_COLOR, stroke_width=0.8, stroke_opacity=0.3,
        )
        divider.move_to(LEFT * 0.8)

        self.play(
            table_group.animate.scale(0.62).to_edge(LEFT, buff=0.3).shift(DOWN * 0.1),
            FadeIn(divider),
            run_time=0.8,
        )

        # ═══════════════════════════════════════
        # BEAT 6 — Coordinate Plane
        # ═══════════════════════════════════════
        plot_title = Text("VECTOR SPACE", font_size=14,
                          color=VECTOR_A_COLOR, weight=BOLD)
        plot_title.move_to(RIGHT * 3.5 + UP * 3.2)
        plot_underline = Line(
            plot_title.get_left() + DOWN * 0.15,
            plot_title.get_right() + DOWN * 0.15,
            color=VECTOR_A_COLOR, stroke_width=1.5, stroke_opacity=0.5,
        )

        axes = Axes(
            x_range=[0, 80, 20], y_range=[0, 170, 20],
            x_length=5.0, y_length=4.5,
            axis_config={
                "color": LABEL_COLOR, "stroke_width": 1.5,
                "include_ticks": True, "tick_size": 0.04,
                "include_numbers": True, "font_size": 14,
                "numbers_to_exclude": [],
            },
            tips=True,
        )
        axes.move_to(RIGHT * 3.5 + DOWN * 0.1)

        x_label = Text("Age", font_size=16, color=LABEL_COLOR)
        x_label.next_to(axes.x_axis, DOWN, buff=0.25)
        y_label = Text("BP", font_size=16, color=LABEL_COLOR)
        y_label.next_to(axes.y_axis, LEFT, buff=0.25)

        # Subtle solid grid
        plot_grid = VGroup()
        for x_val in range(20, 81, 20):
            plot_grid.add(Line(
                axes.c2p(x_val, 0), axes.c2p(x_val, 170),
                color=GRID_COLOR_BRIGHT, stroke_width=0.4,
                stroke_opacity=0.2,
            ))
        for y_val in range(20, 171, 20):
            plot_grid.add(Line(
                axes.c2p(0, y_val), axes.c2p(80, y_val),
                color=GRID_COLOR_BRIGHT, stroke_width=0.4,
                stroke_opacity=0.2,
            ))

        self.play(
            FadeIn(plot_title, shift=DOWN * 0.1),
            Create(plot_underline),
            FadeIn(plot_grid),
            Create(axes, lag_ratio=0.02),
            FadeIn(x_label), FadeIn(y_label),
            run_time=0.8,
        )
        self.wait(0.3)

        # ═══════════════════════════════════════
        # BEAT 7-11 — Plot each patient as a vector arrow
        # ═══════════════════════════════════════
        origin_pt = axes.c2p(0, 0)

        def plot_patient(age, bp, color, label_tex, label_dir, font_size=16,
                         stroke_width=3, run_time_arrow=0.6, run_time_label=0.3,
                         wait_after=0.2):
            pt = axes.c2p(age, bp)
            arr = Arrow(
                start=origin_pt, end=pt,
                color=color, stroke_width=stroke_width, buff=0,
                max_tip_length_to_length_ratio=0.1,
            )
            glow = create_glowing_dot(pt, color)
            lab = Tex(label_tex, font_size=font_size, color=color)
            lab.next_to(pt, label_dir, buff=0.15)

            self.play(GrowArrow(arr), run_time=run_time_arrow)
            self.play(
                FadeIn(glow, scale=2),
                FadeIn(lab, shift=label_dir * 0.1),
                run_time=run_time_label,
            )
            self.wait(wait_after)

        # Patient 1 — Blue — UP (flagship)
        plot_patient(58, 122, VECTOR_A_COLOR,
                     r"$\vec{p}_1 = \begin{bmatrix} 58 \\ 122 \end{bmatrix}$",
                     UP, font_size=18, stroke_width=3.5,
                     run_time_arrow=0.7, run_time_label=0.4, wait_after=0.3)

        # Patient 2 — Orange — DOWN+RIGHT
        plot_patient(71, 110, VECTOR_B_COLOR,
                     r"$\vec{p}_2 = \begin{bmatrix} 71 \\ 110 \end{bmatrix}$",
                     DOWN + RIGHT, run_time_arrow=0.5, wait_after=0.2)

        # Patient 3 — Green — LEFT
        plot_patient(48, 110, RESULTANT_COLOR,
                     r"$\vec{p}_3 = \begin{bmatrix} 48 \\ 110 \end{bmatrix}$",
                     LEFT, run_time_arrow=0.5, wait_after=0.2)

        # Patient 4 — Purple — UP+LEFT
        plot_patient(34, 123, PROJECTION_COLOR,
                     r"$\begin{bmatrix} 34 \\ 123 \end{bmatrix}$",
                     UP + LEFT, font_size=14, stroke_width=2.5,
                     run_time_arrow=0.4, run_time_label=0.3, wait_after=0.15)

        # Patient 5 — Gray — RIGHT
        plot_patient(62, 152, LABEL_COLOR,
                     r"$\begin{bmatrix} 62 \\ 152 \end{bmatrix}$",
                     RIGHT, font_size=14, stroke_width=2.5,
                     run_time_arrow=0.4, run_time_label=0.3, wait_after=0.15)

        self.wait(0.3)

        # ═══════════════════════════════════════
        # BEAT 12 — Closing message
        # ═══════════════════════════════════════
        dim_rect = Rectangle(
            width=14, height=1.4,
            fill_color=BG_COLOR, fill_opacity=0.88,
            stroke_width=0,
        )
        dim_rect.to_edge(DOWN, buff=0)

        msg_main = Text(
            "Every data point is a vector",
            font_size=30, color=ACCENT_COLOR, weight=BOLD,
        )
        msg_sub = Text(
            "Each row in your dataset maps to an arrow in vector space",
            font_size=16, color=LABEL_COLOR,
        )
        msg_group = VGroup(msg_main, msg_sub).arrange(DOWN, buff=0.15)
        msg_group.to_edge(DOWN, buff=0.3)

        self.play(
            FadeIn(dim_rect),
            FadeIn(msg_main, shift=UP * 0.2),
            run_time=0.5,
        )
        self.play(FadeIn(msg_sub, shift=UP * 0.1), run_time=0.3)
        self.wait(1.5)

        # Final fade
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=0.8)
