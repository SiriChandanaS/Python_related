import tkinter as tk
from tkinter import messagebox

class TimerWidget:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Widget")
        self.time_remaining = 0

        # Label for displaying the timer
        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
        self.timer_label.pack(pady=20)

        # Entry for setting timer
        self.entry_label = tk.Label(root, text="Set timer (in seconds):")
        self.entry_label.pack()

        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        # Buttons
        self.start_button = tk.Button(root, text="Start", command=self.start_timer, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, bg="red", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, bg="yellow", fg="black")
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.running = False  # Control for the timer running state

    def start_timer(self):
        try:
            if not self.running:
                self.time_remaining = int(self.time_entry.get())
                self.running = True
                self.update_timer()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def reset_timer(self):
        self.time_remaining = 0
        self.running = False
        self.timer_label.config(text="00:00:00")

    def stop_timer(self):
        self.running = False

    def update_timer(self):
        if self.time_remaining > 0 and self.running:
            minutes, seconds = divmod(self.time_remaining, 60)
            hours, minutes = divmod(minutes, 60)
            self.timer_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)  # Call this function again after 1 second
        elif self.time_remaining == 0 and self.running:
            self.running = False
            messagebox.showinfo("Time's up", "The timer has finished!")

# Create and run the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    timer = TimerWidget(root)
    root.mainloop()
