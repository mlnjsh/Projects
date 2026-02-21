"""
Claude Code Status Words — Fun Animated Scene
Shows the whimsical gerund words Claude Code uses while processing,
with a rotating Claude logo in the center and words placed in clear zones.
"""

from manim import *
import numpy as np

# ============================================================
# COLOR PALETTE — Claude Code Terminal Vibes
# ============================================================
BG_COLOR = "#0D1117"
CLAUDE_ORANGE = "#E8804C"
CLAUDE_TAN = "#D4A574"
NEON_GREEN = "#39FF14"
NEON_CYAN = "#00FFFF"
NEON_PURPLE = "#BF40FF"
NEON_PINK = "#FF6EC7"
NEON_YELLOW = "#FFE633"
NEON_BLUE = "#4FC3F7"
SOFT_WHITE = "#E6EDF3"
DIM_GRAY = "#484F58"
GOLD = "#FFD700"

CAT_CODE = NEON_CYAN
CAT_BUGS = "#FF6B6B"
CAT_FILES = NEON_GREEN
CAT_DESIGN = NEON_PURPLE
CAT_BUILDS = NEON_YELLOW
CAT_HELLO = NEON_PINK

# ============================================================
# DATA
# ============================================================
CATEGORIES = [
    {"label": "code",   "icon": "</>", "color": CAT_CODE,   "words": ["Crafting", "Forging", "Weaving"]},
    {"label": "bugs",   "icon": "B",   "color": CAT_BUGS,   "words": ["Investigating", "Sleuthing", "Untangling"]},
    {"label": "files",  "icon": "F",   "color": CAT_FILES,  "words": ["Rummaging", "Scouring", "Unearthing"]},
    {"label": "design", "icon": "D",   "color": CAT_DESIGN, "words": ["Sketching", "Sculpting", "Painting"]},
    {"label": "builds", "icon": "B",   "color": CAT_BUILDS, "words": ["Assembling", "Brewing", "Conjuring"]},
    {"label": "hello",  "icon": "H",   "color": CAT_HELLO,  "words": ["Waving", "Beaming", "Greeting"]},
]

BONUS_WORDS = [
    "Illuminating", "Orchestrating", "Polishing",
    "Pondering", "Harmonizing",
]

# Fixed positions for each category's 3 words — spread around the logo
# Format: (x, y) for each word. Carefully hand-placed to avoid overlaps.
WORD_POSITIONS = [
    # code (top-left)
    [(-5.2, 2.8), (-5.2, 2.2), (-5.2, 1.6)],
    # bugs (top-right)
    [(3.8, 2.8), (3.8, 2.2), (3.8, 1.6)],
    # files (mid-left)
    [(-5.2, 0.2), (-5.2, -0.4), (-5.2, -1.0)],
    # design (mid-right)
    [(3.8, 0.2), (3.8, -0.4), (3.8, -1.0)],
    # builds (bottom-left)
    [(-5.2, -2.0), (-5.2, -2.6), (-5.2, -3.2)],
    # hello (bottom-right)
    [(3.8, -2.0), (3.8, -2.6), (3.8, -3.2)],
]

BONUS_POSITIONS = [
    (-1.8, 3.2), (1.8, 3.2), (-1.8, -3.2), (1.8, -3.2), (0, -3.5),
]


class ClaudeCodeWords(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ═══════════════════════════════════════
        # INTRO — Terminal boot sequence
        # ═══════════════════════════════════════
        cursor = Text("|", font_size=36, color=NEON_GREEN)

        boot_lines = [
            "> claude --version",
            "Claude Code v1.0.45",
            "> claude",
            "Initializing...",
        ]

        current_y = 1.5
        shown_texts = []

        for line in boot_lines:
            col = NEON_GREEN if line.startswith(">") else DIM_GRAY
            t = Text(line, font_size=22, color=col, font="Consolas")
            t.move_to(UP * current_y)
            t.align_to(LEFT * 4.5, LEFT)
            shown_texts.append(t)

            self.play(FadeIn(t, shift=RIGHT * 0.3), run_time=0.25)
            if line == "Initializing...":
                cursor.next_to(t, RIGHT, buff=0.1)
                for _ in range(3):
                    self.play(FadeIn(cursor, run_time=0.12))
                    self.play(FadeOut(cursor, run_time=0.12))
            current_y -= 0.55

        self.wait(0.2)
        self.play(*[FadeOut(t, shift=UP * 0.5) for t in shown_texts], run_time=0.4)

        # ═══════════════════════════════════════
        # TITLE CARD
        # ═══════════════════════════════════════
        title = Text(
            "What does Claude Code say",
            font_size=44, color=SOFT_WHITE, weight=BOLD,
        )
        title2 = Text(
            "while it's thinking?",
            font_size=44, color=CLAUDE_ORANGE, weight=BOLD,
        )
        title_group = VGroup(title, title2).arrange(DOWN, buff=0.2)

        sparkles = VGroup()
        for pos in [UL * 2.2, UR * 2.2 + RIGHT * 0.5, DL * 1.5 + LEFT, DR * 1.8]:
            s = Text("*", font_size=18, color=GOLD)
            s.move_to(title_group.get_center() + pos)
            sparkles.add(s)

        self.play(
            FadeIn(title, shift=UP * 0.3),
            FadeIn(title2, shift=DOWN * 0.3),
            LaggedStart(*[FadeIn(s, scale=0) for s in sparkles], lag_ratio=0.15),
            run_time=0.8,
        )
        self.wait(0.8)
        self.play(
            FadeOut(title_group, shift=UP * 1),
            FadeOut(sparkles),
            run_time=0.5,
        )

        # ═══════════════════════════════════════
        # CENTER LOGO
        # ═══════════════════════════════════════
        logo_circle = Circle(
            radius=0.6, color=CLAUDE_ORANGE,
            stroke_width=5, fill_opacity=0.1,
            fill_color=CLAUDE_ORANGE,
        )
        logo_inner = Text(
            "C", font_size=40, color=CLAUDE_ORANGE, weight=BOLD,
        )
        logo_text = Text(
            "claude", font_size=14, color=DIM_GRAY, font="Consolas",
        )
        logo_text.next_to(logo_circle, DOWN, buff=0.2)
        logo_group = VGroup(logo_circle, logo_inner, logo_text)

        # Subtle orbit rings
        orbit_ring = Circle(
            radius=2.5, color=DIM_GRAY,
            stroke_width=0.6, stroke_opacity=0.2,
        )
        orbit_ring2 = Circle(
            radius=1.5, color=DIM_GRAY,
            stroke_width=0.4, stroke_opacity=0.15,
        )

        self.play(
            DrawBorderThenFill(logo_circle),
            FadeIn(logo_inner, scale=0.5),
            FadeIn(logo_text, shift=UP * 0.1),
            Create(orbit_ring),
            Create(orbit_ring2),
            run_time=0.8,
        )

        self.play(
            Rotate(logo_inner, angle=TAU, about_point=logo_inner.get_center()),
            run_time=1.2,
            rate_func=smooth,
        )

        # ═══════════════════════════════════════
        # CATEGORY PARADE — words placed in fixed zones
        # ═══════════════════════════════════════
        all_word_mobs = []
        all_cat_labels = []

        for cat_idx, cat in enumerate(CATEGORIES):
            positions = WORD_POSITIONS[cat_idx]

            # Category label at top of its zone
            is_left = cat_idx % 2 == 0
            label_x = positions[0][0]
            label_y = positions[0][1] + 0.5

            cat_label = Text(
                f'{cat["icon"]} {cat["label"]}',
                font_size=16, color=cat["color"], weight=BOLD,
            )
            cat_label.move_to([label_x + 0.8, label_y, 0])

            cat_underline = Line(
                cat_label.get_left() + DOWN * 0.1 + LEFT * 0.1,
                cat_label.get_right() + DOWN * 0.1 + RIGHT * 0.1,
                color=cat["color"], stroke_width=2, stroke_opacity=0.6,
            )

            # Prompt at bottom
            prompt = Text(
                f'> ask about {cat["label"]}...',
                font_size=16, color=DIM_GRAY, font="Consolas",
            )
            prompt.to_edge(DOWN, buff=0.4)

            self.play(
                FadeIn(cat_label, shift=DOWN * 0.15),
                Create(cat_underline),
                FadeIn(prompt, shift=UP * 0.15),
                run_time=0.3,
            )

            all_cat_labels.append(VGroup(cat_label, cat_underline))

            # Animate each word
            word_mobs_this_cat = []
            for w_idx, word in enumerate(cat["words"]):
                tx, ty = positions[w_idx]

                # Small dot + word
                dot = Dot(color=cat["color"], radius=0.04, fill_opacity=0.8)
                word_text = Text(
                    word, font_size=20, color=cat["color"], weight=BOLD,
                )
                word_row = VGroup(dot, word_text).arrange(RIGHT, buff=0.12)
                word_row.move_to([tx + 0.8, ty, 0])

                # Fly in from center
                word_row.save_state()
                word_row.move_to(ORIGIN).scale(0.1).set_opacity(0)

                self.play(
                    word_row.animate.restore(),
                    logo_circle.animate.set_stroke(color=cat["color"]),
                    run_time=0.35,
                    rate_func=rush_from,
                )

                # Quick pulse
                self.play(
                    word_text.animate.scale(1.1),
                    run_time=0.1,
                    rate_func=there_and_back,
                )

                word_mobs_this_cat.append(word_row)

            all_word_mobs.extend(word_mobs_this_cat)

            self.wait(0.3)

            # Reset logo color
            self.play(
                logo_circle.animate.set_stroke(color=CLAUDE_ORANGE),
                run_time=0.15,
            )

            # Fade prompt only (keep words and category label)
            self.play(FadeOut(prompt), run_time=0.2)

        # ═══════════════════════════════════════
        # BONUS WORDS
        # ═══════════════════════════════════════
        bonus_label = Text(
            "and many more...",
            font_size=18, color=GOLD, weight=BOLD,
        )
        bonus_label.to_edge(UP, buff=0.3)
        self.play(FadeIn(bonus_label, shift=DOWN * 0.15), run_time=0.3)

        bonus_mob_list = []
        for i, bw in enumerate(BONUS_WORDS):
            bx, by = BONUS_POSITIONS[i]
            bt = Text(bw, font_size=16, color=CLAUDE_TAN, weight=BOLD)
            bt.move_to([bx, by, 0])
            bt.save_state()
            bt.move_to(ORIGIN).scale(0.1).set_opacity(0)
            bonus_mob_list.append(bt)

        self.play(
            LaggedStart(
                *[bt.animate.restore() for bt in bonus_mob_list],
                lag_ratio=0.1,
            ),
            run_time=0.8,
        )

        self.wait(0.5)

        # ═══════════════════════════════════════
        # GRAND FINALE — gentle swirl
        # ═══════════════════════════════════════
        everything = VGroup(*all_word_mobs, *bonus_mob_list)
        self.play(
            Rotate(everything, angle=PI / 6, about_point=ORIGIN),
            logo_inner.animate.scale(1.2),
            run_time=1.2,
            rate_func=smooth,
        )

        # ═══════════════════════════════════════
        # CLOSING CARD
        # ═══════════════════════════════════════
        fade_list = [FadeOut(m) for m in all_word_mobs + bonus_mob_list]
        fade_list.extend([FadeOut(m) for m in all_cat_labels])
        fade_list.extend([
            FadeOut(bonus_label),
            FadeOut(orbit_ring),
            FadeOut(orbit_ring2),
        ])
        self.play(*fade_list, run_time=0.8)

        closing = Text(
            "Every word is generated fresh",
            font_size=32, color=SOFT_WHITE, weight=BOLD,
        )
        closing2 = Text(
            "-- no two sessions are alike --",
            font_size=24, color=CLAUDE_ORANGE,
        )
        closing_group = VGroup(closing, closing2).arrange(DOWN, buff=0.15)
        closing_group.next_to(logo_group, DOWN, buff=0.6)

        fun_fact = Text(
            'The words match what you ask about!',
            font_size=16, color=DIM_GRAY, font="Consolas",
        )
        fun_fact.next_to(closing_group, DOWN, buff=0.4)

        self.play(FadeIn(closing, shift=UP * 0.2), run_time=0.4)
        self.play(FadeIn(closing2, shift=UP * 0.15), run_time=0.3)
        self.play(FadeIn(fun_fact, shift=UP * 0.15), run_time=0.3)

        # Final logo pulse
        self.play(
            logo_circle.animate.set_stroke(width=8),
            logo_inner.animate.scale(1.15),
            run_time=0.25,
            rate_func=there_and_back,
        )

        self.wait(2.0)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=0.8,
        )
