

---

## PDF to Image Converter (pdf2pic.py)

This Python script converts PDF files into individual PNG images using the PyMuPDF library (`fitz`). 

### Code Explanation:

```python
import os
from os.path import exists
import fitz  

def pdf_to_images(pdf_path, output_dir):
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        image = page.get_pixmap()

        img_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        image.save(img_path)
        print(f"Page {page_num + 1} saved as {img_path}")

    pdf_document.close()

path=input("Enter path of pdf :- ")
if exists(path):
    print("File Found.")
    outputpath=input("Enter Output path for images :- ")
    os.mkdir(outputpath)
    inputpath=path
    pdf_to_images(inputpath, outputpath)
    print("Images are Generated and saved in the current Directory subfolder 'Generated_Images' only.")
else:
    print("File Don't Exists")
```

### Overview:

The `pdf2pic.py` script employs the `fitz` library to convert PDFs into PNG images. Here's a breakdown:

### Libraries Used:

- `os`: Handles operating system functionalities.
- `fitz` (PyMuPDF): Manages PDF operations, like loading and extracting pages as images.

### Functionality:

- `pdf_to_images(pdf_path, output_dir)`: Converts PDF pages to PNG images, saving each page as a separate file.
- `path`: User-input path to the PDF for conversion.
- `outputpath`: Directory for storing generated images.
- Validates the existence of the PDF file and creates a new directory for output images.
- Utilizes `pdf_to_images()` to convert the PDF into PNG images and save them in the specified output directory.

### Usage:

Run the script and provide the PDF path when prompted. Ensure PyMuPDF is installed (`pip install PyMuPDF`).

```bash
$ python pdf2pic.py
Enter path of pdf :- /path/to/example.pdf
File Found.
Enter Output path for images :- /path/to/output_folder
Images are Generated and saved in the specified output directory.
```

### Customization:

- Customize file naming, resolution, or error handling within the code.
- Explore additional `fitz` functionalities for advanced PDF operations.
- Adapt the script for specific page ranges or other requirements.

### Notes:

- Refer to inline comments for detailed code explanations.
- Ensure compatibility with PyMuPDF versions and Python environments for seamless execution.
- Validate permissions for file access and directory creation.

---
