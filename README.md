
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

