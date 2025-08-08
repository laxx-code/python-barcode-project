import os
import csv
import barcode
from barcode.writer import ImageWriter

# Ensure 'barcodes' folder exists
if not os.path.exists("barcodes"):
    os.makedirs("barcodes")

# CSV file to store product details
CSV_FILE = "products.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Product Code", "Barcode File"])

def generate_barcode(product_name, product_code):
    # Get the barcode class for Code 128
    BarcodeClass = barcode.get_barcode_class('code128')
    
    # Create barcode object
    code = BarcodeClass(product_code, writer=ImageWriter())
    
    # Custom size & quality options
    options = {
        "module_width": 0.5,   # bar width in mm
        "module_height": 25,   # bar height in mm
        "font_size": 14,       # size of text below barcode
        "dpi": 400,            # print quality (higher = sharper)
        "text_distance": 1,    # gap between barcode and text
        "quiet_zone": 6        # margin around barcode
    }
    

    # Save barcode in 'barcodes' folder
    filename = os.path.join("barcodes", f"{product_name}_barcode")
    barcode_path = code.save(filename)
    
    # Save product details in CSV
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([product_name, product_code, barcode_path])
    
    print(f"✅ Barcode generated for '{product_name}' and saved as: {barcode_path}")

def main():
    print("=== Vendor Barcode Generator ===")
    
    while True:
        product_name = input("Enter product name (or 'exit' to quit): ").strip()
        if product_name.lower() == "exit":
            print("Exiting program...")
            break
        
        product_code = input("Enter product code: ").strip()
        
        if not product_code:
            print("❌ Product code cannot be empty.")
            continue
        
        generate_barcode(product_name, product_code)

if __name__ == "__main__":
    main()
