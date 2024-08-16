import tkinter as tk
from tkinter import ttk
from typing import List
import csv
import os


class GradeCalculatorGUI(tk.Tk):


    def __init__(self) -> None:
        super().__init__()
        self.title("Grade Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        self.configure(bg='#f7f7f7')

        title_label = ttk.Label(self, text="Grade Calculator", font=('Helvetica', 16, 'bold'), background='#f7f7f7')
        title_label.pack(pady=20)

        self.attempts_label = ttk.Label(self, text="Number of Attempts (1-4):", background='#f7f7f7')
        self.attempts_label.pack(pady=10)
        self.attempts_entry = ttk.Entry(self)
        self.attempts_entry.pack(pady=5)

        self.names_label = ttk.Label(self, text="Student Name:", background='#f7f7f7')
        self.names_label.pack(pady=10)
        self.names_entry = ttk.Entry(self)
        self.names_entry.pack(pady=5)

        self.scores_frame = ttk.Frame(self)
        self.scores_frame.pack(pady=10)

        self.submit_button = ttk.Button(self, text="Submit", command=self.handle_submit)
        self.submit_button.pack(pady=15)

        self.message_label = ttk.Label(self, text="", background='#f0f0f0', foreground='red',
                                       font=('Helvetica', 12), wraplength=350)
        self.message_label.pack(pady=10)

        self.result_label = ttk.Label(self, text="", background='#f0f0f0', font=('Helvetica', 12, 'bold'))
        self.result_label.pack(pady=10)

        self.attempts_entry.bind("<FocusIn>", self.clear_message)
        self.names_entry.bind("<FocusIn>", self.clear_message)

    def handle_submit(self):

        self.message_label.config(text="")

        attempts_input = self.attempts_entry.get()

        if not attempts_input.isdigit() or not (1 <= int(attempts_input) <= 4):
            self.message_label.config(text="You must enter a numerical value (1-4) for the number of attempts.",
                                      foreground='red')
            return

        attempts = int(attempts_input)
        student_name = self.names_entry.get().strip()

        self.message_label.config(text="")

        self.create_score_entries(attempts)

    def create_score_entries(self, attempts: int):

        for widget in self.scores_frame.winfo_children():
            widget.destroy()

        for i in range(attempts):
            score_label = ttk.Label(self.scores_frame, text=f"Score {i + 1}:")
            score_label.grid(row=i, column=0, padx=5, pady=5, sticky='w')
            score_entry = ttk.Entry(self.scores_frame, width=10)
            score_entry.grid(row=i, column=1, padx=5, pady=5)

        submit_scores_button = ttk.Button(self.scores_frame, text="Submit Scores", command=self.submit_scores)
        submit_scores_button.grid(row=attempts, columnspan=2, pady=10)

    def get_scores(self, attempts: int) -> List[int]:

        scores = []
        for i in range(attempts):
            score_entry = self.scores_frame.grid_slaves(row=i, column=1)[0]
            score = score_entry.get()
            if score.isdigit():
                score = int(score)
                if 0 <= score <= 100:
                    scores.append(score)
                else:
                    self.message_label.config(text="Scores must be between 0 and 100.", foreground='red')
                    return []
            else:
                self.message_label.config(text="Please enter valid numerical scores.", foreground='red')
                return []
        return scores

    def calculate_grade(self, score: int) -> str:

            if score >= 90:
                return "A"
            elif score >= 80:
                return "B"
            elif score >= 70:
                return "C"
            elif score >= 60:
                return "D"
            else:
                return "F"

    def submit_scores(self):

        self.message_label.config(text="")

        attempts_input = self.attempts_entry.get()
        if attempts_input.isdigit():
            attempts = int(attempts_input)
            scores = self.get_scores(attempts)
            student_name = self.names_entry.get().strip()

            if scores:
                highest_score = max(scores)

                letter_grade = self.calculate_grade(highest_score)

                scores_with_zeros = scores + [0] * (4 - attempts)
                scores_with_zeros.append(highest_score)

                self.save_to_csv(student_name, scores, letter_grade)

                self.message_label.config(text="Scores submitted successfully!", foreground='green')
                self.result_label.config(text=f"Letter Grade: {letter_grade}")

                self.clear_inputs()
        else:
            self.message_label.config(text="Please enter a valid number of attempts.", foreground='red')

    def save_to_csv(self, student_name: str, scores: List[int], letter_grade: str):

        filename = "grades.csv"

        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["Name", "Score 1", "Score 2", "Score 3", "Score 4", "Final", "Letter Grade"])

            highest_score = max(scores)

            scores_with_zeros = scores + [0] * (4 - len(scores))

            writer.writerow([student_name] + scores_with_zeros + [highest_score, letter_grade])

    def clear_inputs(self):

        self.names_entry.delete(0, tk.END)
        for widget in self.scores_frame.winfo_children():
            widget.destroy()
        self.attempts_entry.delete(0, tk.END)
        self.attempts_entry.focus_set()

    def clear_message(self, event=None):
        self.message_label.config(text="")
        self.result_label.config(text="")


if __name__ == "__main__":
    app = GradeCalculatorGUI()
    app.mainloop()