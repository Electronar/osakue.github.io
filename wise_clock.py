import tkinter as tk
import time

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("WISE Pop-Clock")
        
        # Create a frame for the clock
        self.frame = tk.Frame(root, bg="black", bd=10, relief="raised")
        self.frame.pack(padx=10, pady=10)

        # Create label for the clock
        self.clock_label = tk.Label(self.frame, font=("Helvetica", 60), fg="white", bg="black")
        self.clock_label.pack()

        self.color_index = 0
        self.colors = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A1']
        
        self.update_clock()
    
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)

        # Change color every 5 seconds
        if int(time.strftime("%S")) % 5 == 0:
            self.clock_label.config(fg=self.colors[self.color_index])
            self.color_index = (self.color_index + 1) % len(self.colors)  # Cycle through colors

        # Double size every hour at the start of the hour (HH:00:00)
        if int(time.strftime("%M")) == 0 and int(time.strftime("%S")) == 0:
            self.root.attributes('-topmost', True)  # Make window topmost
            self.clock_label.config(font=("Helvetica", 120))  # Double size
            self.root.after(10000, lambda: self.reset_size())  # Return to original size after 10 seconds

        # Update the clock every second
        self.root.after(1000, self.update_clock)

    def reset_size(self):
        self.clock_label.config(font=("Helvetica", 60))  # Return to original size
        self.root.attributes('-topmost', False)  # Remove topmost attribute

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
