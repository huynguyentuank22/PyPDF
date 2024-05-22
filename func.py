from pypdf import PdfReader
from pypdf import PdfWriter
import os 

def init():
    try:
        os.makedirs(r'output')
        os.makedirs(r'output\text')
        os.makedirs(r'output\images')
    except FileExistsError:
        for filename in os.listdir(r"output\images"):
            file_path = os.path.join(r"output\images", filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Xóa tệp
        for filename in os.listdir(r"output\text"):
            file_path = os.path.join(r"output\text", filename)
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Xóa tệp

def extract_text_all_file(pdf_paths):
    for path in pdf_paths:
        extract_text(path)
def extract_images_all_file(pdf_paths):
    for path in pdf_paths:
        extract_images(path)

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    for i in range(num_pages):
        page = reader.pages[i]
        with open(r'output\text\page_' + str(i+1) + '.txt', 'w', encoding='utf-8') as f:
            f.write(page.extract_text())
    f.close()

def extract_images(pdf_path):
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    count = 0
    for page in reader.pages:
        for img in page.images:
            with open(r'output\images\img_' + str(count) + '.png', 'wb') as f:
                f.write(img.data)
            count = count + 1
    f.close()

def merge_pdfs(pdf_paths):
    merge = PdfWriter()
    for path in pdf_paths:
        merge.append(path)
    merge.write(r'output\merged.pdf')
