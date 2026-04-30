import tkinter as tk
from tkinter import ttk

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

        self.container = tk.frame(root, bg="#e6f2e6")












