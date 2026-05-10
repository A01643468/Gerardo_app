"""
¿Que personaje de One Piece eres?
Test de personalidad con 20 preguntas.
"""

import tkinter as tk
from tkinter import font as tkfont
from questions import QUESTIONS
from characters import CHARACTERS


class OnePieceQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("¿Que personaje de One Piece eres?")
        self.root.geometry("700x550")
        self.root.configure(bg="#1a1a2e")

        self.current_question = 0
        self.scores = {char: 0 for char in CHARACTERS.keys()}

        self.title_font = tkfont.Font(family="Arial", size=18, weight="bold")
        self.question_font = tkfont.Font(family="Arial", size=13, weight="bold")
        self.option_font = tkfont.Font(family="Arial", size=11)
        self.result_font = tkfont.Font(family="Arial", size=22, weight="bold")

        self.show_welcome()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_welcome(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text="¿QUE PERSONAJE DE ONE PIECE ERES?",
            font=self.title_font,
            bg="#1a1a2e",
            fg="#ffd700",
            wraplength=650,
        ).pack(pady=40)

        tk.Label(
            self.root,
            text=(
                "Responde 20 preguntas sobre tu personalidad\n"
                "y descubre cual de los Mugiwaras (y otros personajes)\n"
                "se parece mas a ti.\n\n"
                "Que comience la aventura!"
            ),
            font=self.option_font,
            bg="#1a1a2e",
            fg="white",
            justify="center",
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="EMPEZAR!",
            font=self.question_font,
            bg="#e94560",
            fg="white",
            activebackground="#c73e54",
            activeforeground="white",
            padx=40,
            pady=15,
            relief="flat",
            cursor="hand2",
            command=self.show_question,
        ).pack(pady=30)

        tk.Label(
            self.root,
            text="Hecho por Gerardo - 2026",
            font=("Arial", 9, "italic"),
            bg="#1a1a2e",
            fg="#aaaaaa",
        ).pack(side="bottom", pady=10)

    def show_question(self):
        self.clear_screen()

        q = QUESTIONS[self.current_question]

        progress_text = f"Pregunta {self.current_question + 1} de {len(QUESTIONS)}"
        tk.Label(
            self.root,
            text=progress_text,
            font=("Arial", 10),
            bg="#1a1a2e",
            fg="#ffd700",
        ).pack(pady=(20, 5))

        progress_frame = tk.Frame(self.root, bg="#16213e", height=8, width=600)
        progress_frame.pack(pady=5)
        progress_frame.pack_propagate(False)
        progress_fill = tk.Frame(
            progress_frame,
            bg="#e94560",
            width=int(600 * (self.current_question + 1) / len(QUESTIONS)),
        )
        progress_fill.pack(side="left", fill="y")

        tk.Label(
            self.root,
            text=q["question"],
            font=self.question_font,
            bg="#1a1a2e",
            fg="white",
            wraplength=620,
            justify="center",
        ).pack(pady=30)

        for option in q["options"]:
            btn = tk.Button(
                self.root,
                text=option["text"],
                font=self.option_font,
                bg="#16213e",
                fg="white",
                activebackground="#0f3460",
                activeforeground="white",
                wraplength=550,
                justify="left",
                padx=20,
                pady=12,
                relief="flat",
                cursor="hand2",
                width=55,
                command=lambda o=option: self.answer(o),
            )
            btn.pack(pady=5)

    def answer(self, option):
        for character, points in option["points"].items():
            self.scores[character] += points

        self.current_question += 1

        if self.current_question < len(QUESTIONS):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_screen()

        winner = max(self.scores, key=self.scores.get)
        char_data = CHARACTERS[winner]

        tk.Label(
            self.root,
            text="Tu personaje es...!",
            font=self.question_font,
            bg="#1a1a2e",
            fg="white",
        ).pack(pady=(40, 10))

        tk.Label(
            self.root,
            text=winner.upper(),
            font=self.result_font,
            bg="#1a1a2e",
            fg="#ffd700",
        ).pack(pady=10)

        tk.Label(
            self.root,
            text=char_data["emoji"],
            font=("Arial", 60),
            bg="#1a1a2e",
        ).pack(pady=10)

        tk.Label(
            self.root,
            text=char_data["description"],
            font=self.option_font,
            bg="#1a1a2e",
            fg="white",
            wraplength=600,
            justify="center",
        ).pack(pady=20, padx=30)

        ranking = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)[:3]
        ranking_text = "Top 3 mas afines:\n"
        for i, (char, score) in enumerate(ranking, 1):
            ranking_text += f"{i}. {char} ({score} pts)\n"

        tk.Label(
            self.root,
            text=ranking_text,
            font=("Arial", 10),
            bg="#1a1a2e",
            fg="#aaaaaa",
            justify="center",
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Volver a jugar",
            font=self.question_font,
            bg="#e94560",
            fg="white",
            activebackground="#c73e54",
            activeforeground="white",
            padx=30,
            pady=10,
            relief="flat",
            cursor="hand2",
            command=self.restart,
        ).pack(pady=10)

    def restart(self):
        self.current_question = 0
        self.scores = {char: 0 for char in CHARACTERS.keys()}
        self.show_welcome()


if __name__ == "__main__":
    root = tk.Tk()
    app = OnePieceQuiz(root)
    root.mainloop()
