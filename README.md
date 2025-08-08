
# Barcode by Python

This project contains Python scripts to generate Code128 barcodes for products, including a GUI application and possibly console or helper scripts.

## Project Structure


BARCODE BY PYTHON/
├── .vscode/                      # VSCode settings (optional)
├── barcodes/                     # Generated barcode images (auto-created)
├── build/                        # PyInstaller build files (auto-created)
├── dist/                         # PyInstaller executables (auto-created)
├── venv/                         # Python virtual environment
├── main.py                       # Main GUI application script
├── products.csv                  # Product log file (auto-created)
├── README.md                    # This file
├── requirements.txt              # Python dependencies
├── vendor\_barcode.py             # Additional barcode-related script
├── vendor\_barcode\_app.py         # Additional barcode-related script


## Requirements

- Python 3.6+  
- Dependencies listed in `requirements.txt`. To install them, run:
pip install -r requirements.txt


The main packages used include:
* `python-barcode`
* `Pillow`
* `tkinter` (usually bundled with Python)

## Running the Applications

### GUI Application (`vendor_barcode.py`)

Run this to launch the graphical barcode generator:

```bash
python vendor_barcode.py
```

* Enter **Product Name** and **Product Code** in the input fields
* Click **Generate Barcode** to create and save the barcode
* Barcodes saved in `barcodes/` folder
* Product details appended to `products.csv`
* Barcode preview shown in the GUI

---

## Running Executables (`.exe` files)

After packaging with PyInstaller, your executables will appear in the `dist/` folder.

### To run the GUI executable:

* Double-click the executable inside `dist/` (likely named `vendor_barcode_app.py.exe` or similar)
* The GUI app will launch without needing Python installed

## Packaging with PyInstaller

To create standalone `.exe` files, run from the project root:

pyinstaller --onefile --windowed --add-data "barcode/fonts/DejaVuSans.ttf;barcode/fonts" vendor_barcode_app.py


* Adjust the font path if needed
* For console scripts, remove `--windowed` flag

## Notes

* The `barcodes/` folder and `products.csv` are created automatically if they don't exist
* Use the `resource_path()` function in your scripts to correctly locate resource files, especially after packaging

## License
Open source and free to use.

## Contact
Feel free to open issues or pull requests for questions or contributions.





Thanks for sharing your folder structure! Based on what I see, here’s a tailored **README.md** that fits your project setup exactly, assuming:

* Your main GUI app script is `main.py`
* You have two other scripts: `vendor_barcode.py` and `vendor_barcode_app.py` (maybe console and GUI or helpers)
* `products.csv` is your CSV log file
* You have folders like `barcodes/` for output, `build/` and `dist/` for PyInstaller outputs, and `venv/` for your virtual environment
* You also have `requirements.txt` for dependencies

---

Here’s your custom README.md content for that structure:

```markdown
# Barcode by Python

This project contains Python scripts to generate Code128 barcodes for products, including a GUI application and possibly console or helper scripts.

---

## Project Structure

```

BARCODE BY PYTHON/
├── .vscode/                      # VSCode settings (optional)
├── barcodes/                     # Generated barcode images (auto-created)
├── build/                        # PyInstaller build files (auto-created)
├── dist/                         # PyInstaller executables (auto-created)
├── venv/                         # Python virtual environment
├── main.py                       # Main GUI application script
├── products.csv                  # Product log file (auto-created)
├── README.md                    # This file
├── requirements.txt              # Python dependencies
├── vendor\_barcode.py             # Additional barcode-related script
├── vendor\_barcode\_app.py         # Additional barcode-related script

````

---

## Requirements

- Python 3.6+  
- Dependencies listed in `requirements.txt`. To install them, run:

```bash
pip install -r requirements.txt
````

The main packages used include:

* `python-barcode`
* `Pillow`
* `tkinter` (usually bundled with Python)

---

## Running the Applications

### GUI Application (`main.py`)

Run this to launch the graphical barcode generator:

```bash
python main.py
```

* Enter **Product Name** and **Product Code** in the input fields
* Click **Generate Barcode** to create and save the barcode
* Barcodes saved in `barcodes/` folder
* Product details appended to `products.csv`
* Barcode preview shown in the GUI

---

### Other Scripts

You may have other scripts (`vendor_barcode.py`, `vendor_barcode_app.py`) that serve helper or console functions.
Check their headers or comments for usage instructions.

---

## Running Executables (`.exe` files)

After packaging with PyInstaller, your executables will appear in the `dist/` folder.

### To run the GUI executable:

* Double-click the executable inside `dist/` (likely named `main.exe` or similar)
* The GUI app will launch without needing Python installed

---

## Packaging with PyInstaller

To create standalone `.exe` files, run from the project root:

```bash
pyinstaller --onefile --windowed --add-data "barcode/fonts/DejaVuSans.ttf;barcode/fonts" main.py
```

* Adjust the font path if needed
* For console scripts, remove `--windowed` flag

---

## Notes

* The `barcodes/` folder and `products.csv` are created automatically if they don't exist
* Use the `resource_path()` function in your scripts to correctly locate resource files, especially after packaging

---

## License

Open source and free to use.

---

## Contact

Feel free to open issues or pull requests for questions or contributions.
