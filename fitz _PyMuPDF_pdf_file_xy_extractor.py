import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF
from PIL import Image, ImageTk

def open_pdf():
    # Ask the user to select a PDF file
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        display_pdf(pdf_path)

def display_pdf(pdf_path):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Select the first page
    page = pdf_document.load_page(0)
    pix = page.get_pixmap()
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    # Convert the PIL image to a format Tkinter can understand
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in the label
    pdf_label.config(image=img_tk)
    pdf_label.image = img_tk  # Keep a reference!
    pdf_label.pack()

def on_canvas_click(event):
    # Update the coordinates label with the X and Y coordinates of the click
    coords_label.config(text=f"X: {event.x}, Y: {event.y}")

# Create the main window
root = tk.Tk()
root.geometry("800x900")

# Create a label to display the PDF
pdf_label = tk.Label(root)
pdf_label.pack()

# Bind the click event
pdf_label.bind("<Button-1>", on_canvas_click)

# Create a label to display the coordinates
coords_label = tk.Label(root, text="X: 0, Y: 0")
coords_label.pack()

# Create a button to open the PDF
open_button = tk.Button(root, text="Open PDF", command=open_pdf)
open_button.pack()

root.mainloop()
