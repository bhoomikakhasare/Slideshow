from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# list of image path
image_paths = [
    r"C:\Users\hp\OneDrive\Pictures\flowert.jpg",
    r"C:\Users\hp\OneDrive\Pictures\roma1.jpg",
    r"C:\Users\hp\OneDrive\Pictures\roma4.jpg",
    r"C:\Users\hp\OneDrive\Pictures\roma9.jpg",
    r"C:\Users\hp\OneDrive\Pictures\roma5.jpg"
]

# resize the images to 1080x1080
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)

def update_image():
    photo_image = next(slideshow)
    label.config(image=photo_image)
    root.after(3000, update_image)   # change image every 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Play slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()