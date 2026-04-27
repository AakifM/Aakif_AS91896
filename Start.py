import tkinter as tk
from tkinter import ttk


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Extinct Animal Quiz")
        self.root.geometry("700*450")
        self.root.configure( bg= "#e6f2e6")