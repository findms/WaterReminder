import tkinter as tk
import platform
import time

class WaterReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Reminder")

        # 1. Window setup: no borders, always on top
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        # 2. Transparency Setup
        # IMPORTANT: For Windows, your GIF's background must be exactly this color to become invisible.
        self.os_name = platform.system()
        self.bg_color = "white" 

        if self.os_name == "Windows":
            self.root.attributes("-transparentcolor", self.bg_color)
        elif self.os_name == "Darwin": 
            self.root.attributes("-transparent", True)
            self.bg_color = "systemTransparent"

        self.root.config(bg=self.bg_color)

        # 3. Load the GIF frames
        self.frames = []
        self.scale_factor = 2 # Change to 1 for original size, 3 for one-third size, etc.
        
        try:
            i = 0
            while True:
                # Load each frame of the GIF
                frame = tk.PhotoImage(file="character.gif", format=f"gif -index {i}")
                
                # Shrink the frame if it's too big
                if self.scale_factor > 1:
                    frame = frame.subsample(self.scale_factor, self.scale_factor)
                    
                self.frames.append(frame)
                i += 1
        except tk.TclError:
            pass # Reached the end of the GIF frames

        if not self.frames:
            print("Error: Could not load 'character.gif'. Please ensure it exists in the folder.")
            self.width, self.height = 150, 150
            self.image_label = tk.Label(root, text="💧 GIF Missing", bg="lightblue", width=15, height=5)
        else:
            self.width = self.frames[0].width()
            self.height = self.frames[0].height()
            self.current_frame = 0
            self.image_label = tk.Label(root, bg=self.bg_color)
            
            # Start the GIF animation loop
            self.animate_gif()

        self.image_label.pack()

        # 4. Add the specific "Drank" button
        # The character only leaves when THIS is clicked.
        self.button = tk.Button(root, text="Drank!", command=self.slide_out, cursor="hand2", font=("Arial", 12, "bold"))
        self.button.pack(pady=5)
        
        # Add button height to total height so it fits on screen
        self.total_height = self.height + 40 

        # 5. Calculate screen positions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        
        # Bottom right corner positioning
        self.y_pos = self.screen_height - self.total_height - 80 
        self.start_x = self.screen_width 
        self.target_x = self.screen_width - self.width - 20 

        self.current_x = self.start_x

        # 6. Initialize off-screen
        self.root.geometry(f"{self.width}x{self.total_height}+{self.start_x}+{self.y_pos}")

        self.reminder_interval = 3600000 # 1 hour
        print(f"[{time.strftime('%H:%M:%S')}] Reminder running. First popup in 5 seconds...")
        
        # Initial test popup after 5 seconds
        self.root.after(5000, self.slide_in)

    def animate_gif(self):
        """Loops through the loaded GIF frames to create the animation."""
        if self.frames:
            self.image_label.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(100, self.animate_gif) # Changes frame every 100 milliseconds

    def slide_in(self):
        """Moves the window from right to left."""
        if self.current_x > self.target_x:
            self.current_x -= 15 
            self.root.geometry(f"{self.width}x{self.total_height}+{self.current_x}+{self.y_pos}")
            self.root.after(15, self.slide_in)

    def slide_out(self):
        """Moves the window back out to the right."""
        if self.current_x < self.start_x:
            self.current_x += 15 
            self.root.geometry(f"{self.width}x{self.total_height}+{self.current_x}+{self.y_pos}")
            self.root.after(15, self.slide_out)
        else:
            print(f"[{time.strftime('%H:%M:%S')}] Hydrated! See you in an hour.")
            self.root.after(self.reminder_interval, self.slide_in)

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterReminderApp(root)
    root.mainloop()