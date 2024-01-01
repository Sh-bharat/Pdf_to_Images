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
    

