import tkinter as tk
from tkinter import messagebox
import random

class IntelligentTeacher:
    def __init__(self, root):
        self.root = root
        self.root.title("My teacher")

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root, font=("Helvetica", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack(pady=10)

        self.answer = None
        self.company = None
        self.solution = None
        self.trail = None
        self.topics = None

        self.generate_question()

    def generate_question(self):
        subjects = ["mathematics", "science", "business", "psychology", "technology"]
        selected_subject = random.choice(subjects)

        if selected_subject == "mathematics":
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            self.solution = num1 + num2
            self.question_label.config(text=f"What is the sum of {num1} and {num2}?")
            self.answer = self.solution

        elif selected_subject == "science":
            elements = ["hydrogen", "oxygen", "carbon", "nitrogen", "chlorine"]
            self.solution = random.choice(elements)
            self.question_label.config(text=f"What is the chemical symbol for {self.solution}?")
            if self.solution == "hydrogen":
                self.answer = "H"
            elif self.solution == 'oxygen':
                self.answer = "O"
            elif self.solution == "carbon":
                self.answer = "C"
            elif self.solution == "nitrogen":
                self.answer = "N"
            elif self.solution == "chlorine":
                self.answer = "Cl"

        elif selected_subject == "business":
            self.company = ["Tesla", "Amazon", "Meta", "Microsoft", "OpenAI", "Twitter", "SpaceX"]
            self.solution = random.choice(self.company)
            self.question_label.config(text=f"Who is the founder of {self.solution}?")
            if self.solution == "Tesla" or self.solution == "SpaceX":
                self.answer = "Elon Musk"
            elif self.solution == "Amazon":
                self.answer = "Jeff Bezos"
            elif self.solution == "Meta":
                self.answer = "Mark Zack"
            elif self.solution == "Microsoft":
                self.answer = "Bill Gates"
            elif self.solution == "OpenAI":
                self.answer = "Sam Altman"
            else:
                self.answer = "Jack Dorsey"

        elif selected_subject == "psychology":
            self.topics = ['Motivation', 'stress management', "rehabilitation"]
            self.solution = random.choice(self.topics)
            self.question_label.config(text=f"Which topic deals with {self.solution} ?")
        elif selected_subject == "technology":
            self.trail = ['machine intelligence', 'cloud storage', 'websites and web application', """automation
             of device""", "software design and development"]
            self.solution = random.choice(self.trail)
            self.question_label.config(text=f"Which branch of computer science involves {self.solution} ?")
            if self.solution == "machine intelligence":
                self.answer = 'Artificial intelligence' or 'AI'
            elif self.solution == 'cloud storage':
                self.answer = 'cloud computing'
            elif self.solution == "websites and web application":
                self.answer = "web development"
            elif self.solution == "automation of device":
                self.answer = "internet of things" or "iot"
            elif self.solution == "software design and development":
                self.answer = "software engineering" or "software development"


    def check_answer(self):
        user_answer = self.answer_entry.get()

        if user_answer.lower() == str(self.answer).lower():
            messagebox.showinfo("Correct", "Great job! Your answer is correct.")
        else:
            messagebox.showerror("Incorrect", "Oops! Your answer is incorrect. Try again.")

        self.generate_question()
        self.answer_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = IntelligentTeacher(root)
    root.mainloop()
