import tkinter as tk
from tkinter import ttk


# --------------------------
# MAIN APP
# --------------------------

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extinct Animal Quiz")
        self.root.geometry("700x450")
        self.root.configure(bg="#e6f2e6")

        # Quiz Data
        self.questions = [
            {"Question": "Which extinct bird was the largest that lived in New Zealand?",
             "Options": ["Kiwi", "Tui", "Moa", "Kea"],
             "Answer": "Moa"},

            {"Question": "Which giant eagle once hunted the Moa?",
             "Options": ["Golden Eagle", "Bald Eagle", "Haast’s Eagle", "Harpy Eagle"],
             "Answer": "Haast’s Eagle"},

            {"Question": "Approximately when did the Haast’s Eagle become extinct?",
             "Options": ["50 years ago", "200 years ago", "500-600 years ago", "2000 years ago"],
             "Answer": "500-600 years ago"},

            {"Question": "What was the main reason many large birds in New Zealand went extinct?",
             "Options": ["Volcanoes", "Human hunting", "Floods", "Earthquakes"],
             "Answer": "Human hunting"},

            {"Question": "What type of animal was Moa?",
             "Options": ["Mammals", "Reptiles", "Flightless birds", "Amphibians"],
             "Answer": "Flightless birds"},

            {"Question": "Which extinct owl species lived in New Zealand?",
             "Options": ["Barn Owl", "Snowy Owl", "Laughing Owl", "Forest Owl"],
             "Answer": "Laughing Owl"},

            {"Question": "What did Haast’s Eagle mainly eat?",
             "Options": ["Fish", "Insects", "Moa", "Plants"],
             "Answer": "Moa"},

            {"Question": "When did Moa become extinct?",
             "Options": ["Before humans arrived", "After humans arrived", "During Ice Age", "Recently"],
             "Answer": "After humans arrived"},

            {"Question": "Which of these animals is extinct in New Zealand?",
             "Options": ["Kiwi", "Moa", "Tui", "Kea"],
             "Answer": "Moa"},

            {"Question": "Where did Moa live?",
             "Options": ["Australia", "New Zealand", "Africa", "Asia"],
             "Answer": "New Zealand"}
        ]

        self.score = 0
        self.q_index = 0

        container = tk.Frame(root, bg="#e6f2e6")
        container.pack(fill="both", expand=True)

        self.frames = {}

        for Page in (StartPage, InstructionPage, QuizPage, ResultPage):
            frame = Page(container, self)
            self.frames[Page.__name__] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]

        if page_name == "QuizPage":
            frame.load_question()

        if page_name == "ResultPage":
            frame.update_result()

        frame.tkraise()

# --------------------------
# START PAGE
# --------------------------

class StartPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#e6f2e6")

        tk.Label(
            self,
            text="EXTINCT ANIMAL QUIZ",
                    font=("Arial", 22, "bold"),
                    bg="#e6f2e6"
        ).pack(pady=50)

        tk.Button(
            self,
            text="Start Quiz",
            width=20,
            bg="#2e7d32",
            fg="white",
            command=lambda: app.show_frame("InstructionPage")
        ).pack(pady=10)

        tk.Label(
            self,
            text="Learn about New Zealand's extinct animals!",
            bg="#e6f2e6",
            font=("Arial", 12)
        ).pack(pady=20)

# --------------------------
# INSTRUCTION PAGE
# --------------------------

class InstructionPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#e6f2e6")

        tk.Label(
            self,
            text="Instructions",
            font=("Arial", 18, "bold"),
            bg="#e6f2e6"
        ).pack(pady=20)

        instructions = [
            "Read each question carefully",
            "Choose one answer",
            "Each correct answer earns 1 point",
            "Your final score is shown at the end"
        ]

        for ins in instructions:
            tk.Label(
                self,
                text="• " + ins,
                bg="#e6f2e6",
                font=("Arial", 12)
            ).pack(anchor="w", padx=120)

            tk.Button(
                self,
                text="Back",
                width=12,
                command=lambda: app.show_frame("StartPage")
            ).pack(side="left", padx=80, pady=50)

            tk.Button(
                self,
                text="Begin",
                width=12,
                command=lambda: app.show_frame("QuizPage")
            ).pack(side="right", padx=80, pady=50)

#-------------------------
#QUIZ PAGE
#-------------------------

class QuizPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#e6f2e6")

        self.app = app

        self.progress = ttk.Progressbar(
            self,
            length=400,
            mode="determinate"
        )
        self.progress.pack(pady=15)

        self.score_label = tk.Label(
            self,
            text="",
            bg="#e6f2e6"
        )
        self.score_label.pack()

        self.question_label = tk.Label(
            self,
            text="",
            font=("Arial", 14, "bold"),
            bg="#e6f2e6",
            wraplength=600
        )
        self.question_label.pack(pady=20)

        self.selected = tk.StringVar()

        self.options = []

        for i in range(4):
            rb = tk.Radiobutton(
                self,
                text="",
                variable=self.selected,
                value="",
                font=("Arial", 12),
                bg="#e6f2e6"
            )
            rb.pack(anchor="w", padx=180)
            self.options.append(rb)

        tk.Button(
            self,
            text="Next",
            width=15,
            bg="#2e7d32",
            fg="white",
            command=self.next_question
        ).pack(pady=20)

    def load_question(self):
        q = self.app.questions[self.app.q_index]

        self.question_label.config(text=q["Question"])

        self.score_label.config(
            text=f"Score: {self.app.score} | Question {self.app.q_index + 1}/{len(self.app.questions)}"
        )

        self.selected.set("")

        for i, option in enumerate(q["Options"]):
            self.options[i].config(
                text=option,
                value=option
            )

        self.progress["value"] = (
            self.app.q_index / len(self.app.questions)
        ) * 100

    def next_question(self):
        selected = self.selected.get()

        if selected == self.app.questions[self.app.q_index]["Answer"]:
            self.app.score += 1

        self.app.q_index += 1

        if self.app.q_index < len(self.app.questions):
            self.load_question()
        else:
            self.progress["value"] = 100
            self.app.show_frame("ResultPage")


# --------------------------
# RESULT PAGE
# --------------------------

class ResultPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#e6f2e6")

        self.app = app

        tk.Label(
            self,
            text="Quiz Complete!",
            font=("Arial", 20, "bold"),
            bg="#e6f2e6"
        ).pack(pady=20)

        self.score_label = tk.Label(
            self,
            text="",
            font=("Arial", 16),
            bg="#e6f2e6"
        )
        self.score_label.pack(pady=10)

        self.message = tk.Label(
            self,
            text="",
            font=("Arial", 14),
            bg="#e6f2e6"
        )
        self.message.pack(pady=10)

        tk.Button(
            self,
            text="Play Again",
            width=15,
            bg="#2e7d32",
            fg="white",
            command=self.restart
        ).pack(pady=20)

    def update_result(self):
        score = self.app.score
        total = len(self.app.questions)

        self.score_label.config(
            text=f"Your Score: {score}/{total}"
        )

        if score == total:
            msg = "Excellent!"
        elif score >= total / 2:
            msg = "Great Job!"
        else:
            msg = "Keep Practising!"

        self.message.config(text=msg)

    def restart(self):
        self.app.score = 0
        self.app.q_index = 0
        self.app.show_frame("StartPage")

# --------------------------
# RUN PROGRAM
# --------------------------

root = tk.Tk()
app = QuizApp(root)
root.mainloop()












