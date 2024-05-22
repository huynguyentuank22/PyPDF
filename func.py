from pypdf import PdfReader
from pypdf import PdfWriter
import os 

def init():
    try:
        os.makedirs(r'output')
        os.makedirs(r'output\text')
        os.makedirs(r'output\images')
    except FileExistsError:
        for folder_name in os.listdir(r"output\images"):
            folder_path = os.path.join(r"output\images", folder_name)
            if os.path.isdir(folder_path):
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        os.unlink(file_path) # Xoa file
                os.rmdir(folder_path)  # Xoa thu muc
            
        for folder_name in os.listdir(r"output\text"):
            folder_path = os.path.join(r"output\text", folder_name)
            if os.path.isdir(folder_path):
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        os.unlink(file_path) # Xoa file
                os.rmdir(folder_path)  # Xoa thu muc  

def extract_text_all_file(pdf_paths):
    for path in pdf_paths:
        pdf_name = os.path.basename(path).split('.')[0]
        try:
            os.makedirs(r'output\text\\' + pdf_name)
        except FileExistsError:
            for file_name in os.listdir(r'output\text\\' + pdf_name):
                file_path = os.path.join(r'output\text\\' + pdf_name, file_name)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
        extract_text(path, pdf_name)

def extract_images_all_file(pdf_paths):
    for path in pdf_paths:
        pdf_name = os.path.basename(path).split('.')[0]
        try:
            os.makedirs(r'output\images\\' + pdf_name)
        except FileExistsError:
            for file_name in os.listdir(r'output\images\\' + pdf_name):
                file_path = os.path.join(r'output\images\\' + pdf_name, file_name)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
        extract_images(path, pdf_name)

def extract_text(pdf_path, file_name):
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    for i in range(num_pages):
        page = reader.pages[i]
        with open(r'output\text\\' + file_name + '\\page_' + str(i+1) + '.txt', 'w', encoding='utf-8') as f:
            f.write(page.extract_text())
    f.close()

def extract_images(pdf_path, file_name):
    reader = PdfReader(pdf_path)
    num_pages = len(reader.pages)

    count = 0
    for page in reader.pages:
        for img in page.images:
            with open(r'output\images\\' + file_name + '\\img_' + str(count) + '.png', 'wb') as f:
                f.write(img.data)
            count = count + 1
    f.close()

def merge_pdfs(pdf_paths):
    merge = PdfWriter()
    for path in pdf_paths:
        merge.append(path)
    merge.write(r'output\merged.pdf')
