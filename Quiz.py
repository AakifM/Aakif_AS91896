import tkinter as tk
import tkinter
from dis import Instruction


#MAIN APP CLASS
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extinct Animal Quiz")
        self.root.geometry("700*450")
        self.root.configure( bg= "#e6f2e6")

        #Quia data
        self.questions = [
            {"Question": "Which extinct bird was the largest that lived in New Zealand?",
                "Options": ["Kiwi","Tui","Moa","Kea" ],
                "answer": "Moa"},


            { "Question": "Which giant eagle once hunted the Moa?",
                "Options": ["Golden Eagle","Bald Eagle","Haast’s Eagle","Harpy Eagle"],
                "answer": "Haast’s Eagle"},


            {"Question": "Approximately when did the Haast’s eagle become Extinct?",
                "Options": ["50 years ago","200 years ago","500-600 years ago","2000 years ago"],
                "answer": "500-600 years ago"},


            {"Question": "What was the main resource many large birds in New Zealand went extinct?",
                "Options": ["Volcanos","human hunting","floods","earth quakes"],
                "answer": "Human Hunting" },


            {"Question": "What type of animal was Moa?",
                "Options": ["Mammals","reptiles","flightless birds","Amphibians"],
                "answer": "flightless birds"},

            {"Question": "Which Extinct Owl species lived in New Zealand?",
                "Options": ["Barn Owl","Snowy Owl","Laughing Owl","Forest Owl"],
                "answer": "Laughing Owl"},

            {"Question": "What did Haast’s eagle mainly eat?",
                "Options": ["Fish","insects","Moa","Plants"],
                "answer": "Moa"},


            {"Question": "When did Moa become Extinct?",
                "Options": ["Before humans arrived","After humans arrived","During Ice age","Recently"],
                "answer": "After humans arrived"},

            {"Question": "Which of these animals is extinct in New Zealand?",
                "Options": ["Kiwi","Moa","Tui","Kea"],
                "answer": "Moa"},

            {"Question": "Where did Moa lived",
             "Options": ["Australia", "New Zealand", "Africa", "Asia"],
             "answer": "New Zealand"},
        ]

        self.score = 0
        self.q_index = 0

        #container for pages

        self.container = tk.Frame(root, bg="#e6f2e6")
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        #Initialize all pages

        for F in ("StartPage", "InstructionPage", "QuizPage", "ResultPage"):
            frame = F(self.container, self)
            self.frames[F]= frame
            frame.place(relwidth=1, relheight=1)

            self.show_frame("StartPage")

            def show_frame(self, page):
                frame = self.frames[page]
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
            tk.Button(self,text="start", bg="#2e7d32", fg="white", width=10, command=lambda app.show_frame("QuizPage")).pack(side="right")




root = tk.Tk()
app = QuizApp(root)
root.mainloop()













