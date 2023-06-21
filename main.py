from PIL import Image, ImageTk
import tkinter as tk

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400


def draw_indian_flag():
    # Create the main window
    window = tk.Tk()
    window.title("Indian Flag")

    # Create a canvas for drawing
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Draw the saffron rectangle
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT / 3, fill="#FF9933")

    # Draw the white rectangle
    canvas.create_rectangle(0, CANVAS_HEIGHT / 3, CANVAS_WIDTH, CANVAS_HEIGHT * 2 / 3, fill="white")

    # Draw the green rectangle
    canvas.create_rectangle(0, CANVAS_HEIGHT * 2 / 3, CANVAS_WIDTH, CANVAS_HEIGHT, fill="#138808")

    # Load and display the Ashoka Chakra image
    chakra_image = Image.open(r"C:\Users\Admin\Desktop\download.png")
    chakra_image = chakra_image.resize(
        (int(CANVAS_HEIGHT / 3), int(CANVAS_HEIGHT / 3)))  # Adjust the size of the chakra image
    chakra_photo = ImageTk.PhotoImage(chakra_image)
    canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, image=chakra_photo)

    # Run the main window loop
    window.mainloop()


if __name__ == '__main__':
    draw_indian_flag()
