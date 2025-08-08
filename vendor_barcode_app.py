import os
import csv
import barcode
from barcode.writer import ImageWriter
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# When creating ImageWriter:
writer = ImageWriter()
writer.font_path = resource_path("barcode/fonts/DejaVuSans.ttf")
# ---------- Setup ----------
if not os.path.exists("barcodes"):
    os.makedirs("barcodes")

CSV_FILE = "products.csv"
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Product Code", "Barcode File"])

# ---------- Barcode Generator ----------
def generate_barcode(product_name, product_code):
    try:
        BarcodeClass = barcode.get_barcode_class('code128')
        code = BarcodeClass(product_code, writer=ImageWriter())

        options = {
            "module_width": 0.5,
            "module_height": 25,
            "font_size": 10,   # minimal but > 0 to avoid error
            "dpi": 300,
            "quiet_zone": 6
        }

        filename = os.path.join("barcodes", f"{product_name}_barcode")
        barcode_path = code.save(filename, options)

        # Add product info text below barcode
        add_text_to_barcode(barcode_path, product_name, product_code)

        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([product_name, product_code, barcode_path])

        return barcode_path

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate barcode: {e}")
        return None

# ---------- Add Text to Barcode ----------
def add_text_to_barcode(image_path, name, code):
    img = Image.open(image_path)
    width, height = img.size

    new_height = height + 50
    new_img = Image.new("RGB", (width, new_height), "white")
    new_img.paste(img, (0, 0))

    draw = ImageDraw.Draw(new_img)
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except:
        font = ImageFont.load_default()

    text = f"{name} | {code}"
    text_width = draw.textlength(text, font=font)
    text_x = (width - text_width) // 2
    text_y = height + 10

    draw.text((text_x, text_y), text, fill="black", font=font)

    new_img.save(image_path)

# ---------- GUI Actions ----------
def on_generate():
    name = entry_name.get().strip()
    code = entry_code.get().strip()

    if not name or not code:
        messagebox.showwarning("Input Error", "Please enter both product name and code.")
        return

    path = generate_barcode(name, code)
    if path:
        messagebox.showinfo("Success", f"Barcode saved: {path}")
        show_barcode_image(path)

def show_barcode_image(path):
    img = Image.open(path)
    img = img.resize((300, 180))
    img_tk = ImageTk.PhotoImage(img)
    label_image.config(image=img_tk)
    label_image.image = img_tk

# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Vendor Barcode Generator")
root.geometry("420x500")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Vendor Barcode Generator", font=("Arial", 18, "bold"), bg="#333", fg="white", pady=10)
title_label.pack(fill="x")

try:
    logo_img = Image.open("logo.png")
    logo_img = logo_img.resize((120, 120))
    logo_tk = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_tk, bg="#f0f0f0")
    logo_label.image = logo_tk
    logo_label.pack(pady=5)
except:
    tk.Label(root, text="[Your Logo Here]", font=("Arial", 12, "italic"), bg="#f0f0f0").pack(pady=5)

tk.Label(root, text="Product Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_name = tk.Entry(root, width=35, font=("Arial", 11))
entry_name.pack()

tk.Label(root, text="Product Code:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
entry_code = tk.Entry(root, width=35, font=("Arial", 11))
entry_code.pack()

tk.Button(root, text="Generate Barcode", command=on_generate, bg="#007acc", fg="white", font=("Arial", 12), width=20).pack(pady=15)

label_image = tk.Label(root, bg="#f0f0f0")
label_image.pack(pady=10)

footer = tk.Label(root, text="© 2025 Vendor Tools", font=("Arial", 9), bg="#f0f0f0", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
