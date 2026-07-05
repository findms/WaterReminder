A lightweight, cross-platform Python script that runs quietly in the background and slides an animated character onto your screen every hour to remind you to hydrate.

Features
Zero Dependencies: Uses Python's built-in tkinter library. No pip install required.

Non-Intrusive: The window has no borders, stays on top, and features a transparent background.

Smart Timer: The 1-hour countdown only begins after you click the "Drank!" button, preventing multiple popups if you are away from your desk.

Prerequisites
Python 3.x installed on your system.

Setup Instructions
Create a folder for the project.

Save the Python script as reminder.py in this folder.

Place your animated GIF in the same folder and name it character.gif.

Note on Transparency: > * Windows: The script makes the color "white" transparent. Ensure your GIF has a solid white background for the floating effect to work.

macOS: Uses native system transparency. A GIF with an inherently transparent background works best.

How to Run
Open your terminal or command prompt, navigate to your project folder, and run the following command:

python reminder.py (Windows)
python3 reminder.py (MacOS)
