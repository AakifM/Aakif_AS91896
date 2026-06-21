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

        #---------------------
        #START PAGE
        #---------------------

        class StartPage(tk.Frame):
            def __init__(self, parent, app):
                super().__init__(parent,bg="e6f2e6")
                tk.Label(self, text="EXTINCT ANIMAL QUIZ")
                font=("Cormorant Garamond",20,"bold")
                bg="e6f2e6".pack(pady=10)

                tk.Button(self, text="Start Quiz", bg="#2e7d32", fg="white", width=20, height=2, command=lambda: app.show_frame(InstructionPage)).pack(pady=10)
                tk.Button(self, text="Help/Rules", bg="#2e7d32", fg="white", width=20, height=2).pack(pady=10)

                tk.Label(self, text="Learn about NZ extinct animals", bg="#e6f2e6").pack(pady=20)

        #---------------------
        #INSTRUCTION PAGE
        #---------------------

        class InstructionPage(tk.Frame):
            def __init__(self, parent,app):
                super().__init__(parent, bg="#e6f2e6")

                tk.Label(self, text="INSTRUCTIONS",
                font=("Cormorant Garamond",18,"bold"),
                bg="#e6f2e6").pack(pady=20)

                instructions=[
                "Read each question carefully",
                "Select the correct answer",
                "Each correct answer= 1 point",
                "Final score shown at the end"
                ]

                for ins in "instructions":
                    tk.Label(self, text="."+ins, bg="#e6f2e6", font=("Arial",12)).pack(anchor="w", padx=150)

                    tk.Button(self,text="Back", bg="#2e7d32", fg="white", width=10, command=lambda:app.show_frame("startPage")).pack(side="left",padx=80,pady=40)
                    tk.Button(self,text="start", bg="#2e7d32", fg="white", width=10, command=lambda:app.show_frame("QuizPage")).pack(side="right", padx=80, pady= 40)

    #-------------------------
    #QUIZ PAGE
    #-------------------------

    class QuizPage(tk.Frame):
        def __init__(self, parent, app):
            super().__init__(parent, bg="#e6f2e6")
            self.app = app

            #Progress bar
            self.progress = ttk.progressbar(self, legth=400, mode='determinate')
            self.progress.pack(pady=20)

            self.score_label= tk.Label(self, text="", bg="e6f2e6")
            self.score_label.pack()

            self.question_label=tk.Label(self,text="", font=("Arial", 14),bg="#e6f2e6")
            self.question_label.pack(pady=20)

            self.selected = tk.StringVar()

            self.options = []
            for i in range(4):
                rb = tk.Radiobutton(self, text="", variable=self.selected, value="", font=("Arial",12), bg= "e6f6e6")
                rb.pack(anchor="w", padx=200)
                self.options.append(rb)

                tk.Button(self, text="next", bg="2e7d32", fg="white", width=15, command=self.next_question).pack(pady=20)

            self.load_question()

            def load_question(self):
                q = self.app.question[self.app.q_index]

                self.question_label.config(text=q["question"])
                self.score_label.config(text=f"Score: {self.app.score} | Question {self.app.q_index + 1}/{len(self.app.questions)}")

                self.selected.set(None)

                for i, option in enumerate(q["options"]):
                    self.options[i].config(text=option, value=option)

            #Upadate progress bar
            progress_value= (self.app.q_index/len(self.app.questions)) *100
            self.progress['value']= progress_value

            def next_question(self):
                selected = self.selected.get()
                correct = self.app.questions[self.app.q_index]["answer"]

                if selected == correct:
                    self.app.score += 1

            if self.selected == 'correct':
                self.app.score+=1

                self.app.q_index+=1

            if self.app.q_index <len(self.app.questions):
                self.load_question()
            else:
                self.progress['value']=100
                self.app.show_frame("ResultPage")
    #---------------------------------
    #RESULT PAGE
    #---------------------------------

    class ResultPage(tk.Frame):
        def __init__ (self, parent, app):
            super().__init__(parent,bg="#e6f2e6")
            self.app=app

            self.title = tk.label(self, text="Quiz Complete",font=("Arial", 18, "bold"),bg="#e6f2e6")
            self.title.pack(pady=20)

            self.score_label = tk.label (self, text="", font=("Arial", 14), bg="#e6f2e6")
            self.score_label.pack(pady=10)

            self.message= tk.Label(self, text="", bg= "#e6f2e6")
            self.message.pack(pady=10)

            tk.Button(self, text="Play Again", bg="#2e7d32", fg="white", width=15, command=app.root.quit).pack(pady=10)

            self.bind("<Visibility>", self.update_result)

        def update_result(self, event):
                score = self.app.score
                total = len(self.app.questions)

                self.score_label.config(text=f"Your Score:{score}/{total}")

                if score == total:
                    msg="Excellent!"
                elif score>total/2:
                    msg=("Great Job!")
                else:
                    msg="Keep Practising"

                self.message.config(text=msg)

        def restart(self):
                self.app.score = 0
                self.app.q_index = 0
                self.app.show_frame("StartPage")

            #------------------------------------
            # RUN PROGRAM
            #-----------------------------------

    class ResultPage(tk.Frame):
        def __init__(self, parent, app):
            super().__init__(parent, bg="#e6f2e6")
            self.app = app

            self.bind("<Visibility>", self.update_result)

        def update_result(self, event):
            score = self.app.score
            total = len(self.app.questions)

            self.score_label.config(text=f"Your Score: {score}/{total}")

            if score == total:
                msg = "Excellent!"
            elif score > total / 2:
                msg = "Great Job!"
            else:
                msg = "Keep Practising"

            self.message.config(text=msg)

root = tk.Tk()
app = QuizApp(root)
root.mainloop()













