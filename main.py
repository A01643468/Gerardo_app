"""
ONE PIECE PERSONALITY QUIZ
Diseno moderno con CustomTkinter.
"""

import customtkinter as ctk
from questions import QUESTIONS
from characters import CHARACTERS

# Configuracion global de tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Paleta de colores personalizada
COLOR_BG = "#0a0e27"
COLOR_CARD = "#1a1f3a"
COLOR_ACCENT = "#ff6b35"
COLOR_ACCENT_HOVER = "#e55a2b"
COLOR_GOLD = "#ffd700"
COLOR_OPTION = "#252b4a"
COLOR_OPTION_HOVER = "#323a63"
COLOR_TEXT = "#ffffff"
COLOR_TEXT_DIM = "#8b92b8"
COLOR_PROGRESS_BG = "#252b4a"
COLOR_PROGRESS_FILL = "#ff6b35"


class OnePieceQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("One Piece Personality Quiz")
        self.geometry("900x700")
        self.minsize(800, 650)
        self.configure(fg_color=COLOR_BG)

        # Estado
        self.current_question = 0
        self.scores = {char: 0 for char in CHARACTERS.keys()}

        # Container principal
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True, padx=40, pady=30)

        self.show_welcome()

    def clear(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # ======================== PANTALLA DE BIENVENIDA ========================
    def show_welcome(self):
        self.clear()

        # Frame central con efecto de tarjeta
        card = ctk.CTkFrame(
            self.container,
            fg_color=COLOR_CARD,
            corner_radius=20,
            border_width=2,
            border_color=COLOR_ACCENT,
        )
        card.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.85)

        # Icono pirata grande
        ctk.CTkLabel(
            card,
            text="⚓",
            font=ctk.CTkFont(family="Segoe UI Emoji", size=80),
            text_color=COLOR_GOLD,
        ).pack(pady=(40, 10))

        # Titulo
        ctk.CTkLabel(
            card,
            text="ONE PIECE",
            font=ctk.CTkFont(family="Arial Black", size=42, weight="bold"),
            text_color=COLOR_GOLD,
        ).pack(pady=(0, 0))

        ctk.CTkLabel(
            card,
            text="PERSONALITY QUIZ",
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
            text_color=COLOR_TEXT,
        ).pack(pady=(0, 5))

        # Linea decorativa
        line = ctk.CTkFrame(card, fg_color=COLOR_ACCENT, height=3, width=200)
        line.pack(pady=15)

        # Descripcion
        ctk.CTkLabel(
            card,
            text=(
                "Descubre cual de los personajes de One Piece\n"
                "se parece mas a tu personalidad"
            ),
            font=ctk.CTkFont(family="Arial", size=14),
            text_color=COLOR_TEXT_DIM,
            justify="center",
        ).pack(pady=(5, 5))

        # Info badges
        badges_frame = ctk.CTkFrame(card, fg_color="transparent")
        badges_frame.pack(pady=20)

        for icon, text in [("📋", "20 Preguntas"), ("👥", "10 Personajes"), ("⏱️", "5 minutos")]:
            badge = ctk.CTkFrame(badges_frame, fg_color=COLOR_OPTION, corner_radius=15)
            badge.pack(side="left", padx=10, ipadx=15, ipady=8)
            ctk.CTkLabel(
                badge,
                text=f"{icon}  {text}",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=COLOR_TEXT,
            ).pack()

        # Boton EMPEZAR (grande y llamativo)
        ctk.CTkButton(
            card,
            text="COMENZAR AVENTURA  →",
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            fg_color=COLOR_ACCENT,
            hover_color=COLOR_ACCENT_HOVER,
            text_color=COLOR_TEXT,
            corner_radius=30,
            width=280,
            height=55,
            command=self.start_quiz,
        ).pack(pady=(25, 20))

        # Footer
        ctk.CTkLabel(
            card,
            text="◆ Hecho por Gerardo · 2026 ◆",
            font=ctk.CTkFont(family="Arial", size=10, slant="italic"),
            text_color=COLOR_TEXT_DIM,
        ).pack(side="bottom", pady=15)

    def start_quiz(self):
        self.current_question = 0
        self.scores = {char: 0 for char in CHARACTERS.keys()}
        self.show_question()

    # ======================== PANTALLA DE PREGUNTA ========================
    def show_question(self):
        self.clear()

        q = QUESTIONS[self.current_question]
        progress = (self.current_question + 1) / len(QUESTIONS)

        # Header con progreso
        header = ctk.CTkFrame(self.container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 20))

        ctk.CTkLabel(
            header,
            text=f"PREGUNTA {self.current_question + 1} / {len(QUESTIONS)}",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            text_color=COLOR_GOLD,
        ).pack(anchor="w")

        # Barra de progreso moderna
        progress_bar = ctk.CTkProgressBar(
            header,
            height=8,
            corner_radius=4,
            fg_color=COLOR_PROGRESS_BG,
            progress_color=COLOR_ACCENT,
        )
        progress_bar.pack(fill="x", pady=(8, 0))
        progress_bar.set(progress)

        # Card de la pregunta
        question_card = ctk.CTkFrame(
            self.container,
            fg_color=COLOR_CARD,
            corner_radius=20,
        )
        question_card.pack(fill="both", expand=True)

        # Numero grande de la pregunta
        ctk.CTkLabel(
            question_card,
            text=f"Q{self.current_question + 1}",
            font=ctk.CTkFont(family="Arial Black", size=60, weight="bold"),
            text_color=COLOR_ACCENT,
        ).pack(pady=(25, 0))

        # Pregunta
        question_text = q["question"]
        # Limpiar el numero del inicio (ej "1. ")
        if ". " in question_text[:4]:
            question_text = question_text.split(". ", 1)[1]

        ctk.CTkLabel(
            question_card,
            text=question_text,
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color=COLOR_TEXT,
            wraplength=700,
            justify="center",
        ).pack(pady=(5, 25), padx=40)

        # Opciones en grid 2x2
        options_grid = ctk.CTkFrame(question_card, fg_color="transparent")
        options_grid.pack(fill="both", expand=True, padx=40, pady=(0, 30))

        options_grid.grid_columnconfigure(0, weight=1)
        options_grid.grid_columnconfigure(1, weight=1)
        options_grid.grid_rowconfigure(0, weight=1)
        options_grid.grid_rowconfigure(1, weight=1)

        letters = ["A", "B", "C", "D"]
        for i, option in enumerate(q["options"]):
            row, col = divmod(i, 2)
            self._create_option_card(
                options_grid,
                letter=letters[i],
                text=option["text"],
                option=option,
                row=row,
                col=col,
            )

    def _create_option_card(self, parent, letter, text, option, row, col):
        """Crea una tarjeta clickeable para cada opcion."""
        card = ctk.CTkFrame(
            parent,
            fg_color=COLOR_OPTION,
            corner_radius=15,
            cursor="hand2",
        )
        card.grid(row=row, column=col, padx=8, pady=8, sticky="nsew")

        # Hover effect
        def on_enter(e):
            card.configure(fg_color=COLOR_OPTION_HOVER, border_width=2, border_color=COLOR_ACCENT)

        def on_leave(e):
            card.configure(fg_color=COLOR_OPTION, border_width=0)

        def on_click(e):
            self.answer(option)

        card.bind("<Enter>", on_enter)
        card.bind("<Leave>", on_leave)
        card.bind("<Button-1>", on_click)

        # Letra grande
        letter_label = ctk.CTkLabel(
            card,
            text=letter,
            font=ctk.CTkFont(family="Arial Black", size=32, weight="bold"),
            text_color=COLOR_ACCENT,
        )
        letter_label.pack(pady=(15, 5))
        letter_label.bind("<Enter>", on_enter)
        letter_label.bind("<Leave>", on_leave)
        letter_label.bind("<Button-1>", on_click)

        # Texto de la opcion
        text_label = ctk.CTkLabel(
            card,
            text=text,
            font=ctk.CTkFont(family="Arial", size=13),
            text_color=COLOR_TEXT,
            wraplength=280,
            justify="center",
        )
        text_label.pack(pady=(0, 15), padx=15)
        text_label.bind("<Enter>", on_enter)
        text_label.bind("<Leave>", on_leave)
        text_label.bind("<Button-1>", on_click)

    def answer(self, option):
        for character, points in option["points"].items():
            self.scores[character] += points

        self.current_question += 1

        if self.current_question < len(QUESTIONS):
            self.show_question()
        else:
            self.show_result()

    # ======================== PANTALLA DE RESULTADO ========================
    def show_result(self):
        self.clear()

        winner = max(self.scores, key=self.scores.get)
        char_data = CHARACTERS[winner]

        # Calculos para barras de afinidad
        max_score = max(self.scores.values())
        ranking = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)

        # Header
        header = ctk.CTkFrame(self.container, fg_color="transparent")
        header.pack(fill="x", pady=(0, 15))

        ctk.CTkLabel(
            header,
            text="✦  RESULTADO  ✦",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            text_color=COLOR_GOLD,
        ).pack()

        # Card principal con el resultado
        result_card = ctk.CTkFrame(
            self.container,
            fg_color=COLOR_CARD,
            corner_radius=20,
            border_width=2,
            border_color=COLOR_ACCENT,
        )
        result_card.pack(fill="both", expand=True)

        # Subtitulo
        ctk.CTkLabel(
            result_card,
            text="TU PERSONAJE ES",
            font=ctk.CTkFont(family="Arial", size=13, weight="bold"),
            text_color=COLOR_TEXT_DIM,
        ).pack(pady=(25, 0))

        # Nombre del personaje (HUGE)
        ctk.CTkLabel(
            result_card,
            text=winner.upper(),
            font=ctk.CTkFont(family="Arial Black", size=56, weight="bold"),
            text_color=COLOR_GOLD,
        ).pack(pady=(0, 10))

        # Linea decorativa
        line = ctk.CTkFrame(result_card, fg_color=COLOR_ACCENT, height=3, width=150)
        line.pack(pady=(0, 15))

        # Descripcion
        ctk.CTkLabel(
            result_card,
            text=char_data["description"],
            font=ctk.CTkFont(family="Arial", size=13),
            text_color=COLOR_TEXT,
            wraplength=700,
            justify="center",
        ).pack(pady=(0, 25), padx=50)

        # Seccion de afinidad
        affinity_label = ctk.CTkLabel(
            result_card,
            text="◆  TOP 5 AFINIDAD  ◆",
            font=ctk.CTkFont(family="Arial", size=11, weight="bold"),
            text_color=COLOR_GOLD,
        )
        affinity_label.pack(pady=(0, 10))

        # Barras de afinidad para top 5
        affinity_frame = ctk.CTkFrame(result_card, fg_color="transparent")
        affinity_frame.pack(fill="x", padx=80, pady=(0, 20))

        for i, (char, score) in enumerate(ranking[:5]):
            row = ctk.CTkFrame(affinity_frame, fg_color="transparent")
            row.pack(fill="x", pady=3)

            # Nombre
            ctk.CTkLabel(
                row,
                text=char,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=COLOR_TEXT,
                width=80,
                anchor="w",
            ).pack(side="left")

            # Barra
            percentage = score / max_score if max_score > 0 else 0
            bar = ctk.CTkProgressBar(
                row,
                height=12,
                corner_radius=6,
                fg_color=COLOR_PROGRESS_BG,
                progress_color=COLOR_ACCENT if i == 0 else COLOR_OPTION_HOVER,
            )
            bar.pack(side="left", fill="x", expand=True, padx=10)
            bar.set(percentage)

            # Puntaje
            ctk.CTkLabel(
                row,
                text=f"{score} pts",
                font=ctk.CTkFont(size=10),
                text_color=COLOR_TEXT_DIM,
                width=50,
                anchor="e",
            ).pack(side="left")

        # Botones de accion
        buttons_frame = ctk.CTkFrame(result_card, fg_color="transparent")
        buttons_frame.pack(pady=(0, 25))

        ctk.CTkButton(
            buttons_frame,
            text="↻  Volver a jugar",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            fg_color=COLOR_ACCENT,
            hover_color=COLOR_ACCENT_HOVER,
            corner_radius=25,
            width=180,
            height=45,
            command=self.start_quiz,
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            buttons_frame,
            text="🏠  Inicio",
            font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
            fg_color=COLOR_OPTION,
            hover_color=COLOR_OPTION_HOVER,
            corner_radius=25,
            width=180,
            height=45,
            command=self.show_welcome,
        ).pack(side="left", padx=8)


if __name__ == "__main__":
    app = OnePieceQuizApp()
    app.mainloop()
