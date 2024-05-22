from func import *
from button import *

init()

root = Tk()

path = StringVar()

root.title('PyPDF')
root.minsize(height=500, width=700)

Label(root, text='PDF Tools', fg='red', font=(
    'Arial', 16)).grid(row=0, columnspan=2)

listbox = Listbox(root, height=20, width=115)
listbox.grid(row=1, columnspan=2)
show(listbox)

Label(root, text='Enter path of PDF:', font=('Arial', 12)).grid(row=2, column=0)
Entry(root, width=80, textvariable=path).grid(row=2, column=1)

button_input = Frame(root)
Button(button_input, text="Add", command=lambda: add(
    listbox, path)).pack(side=LEFT, padx=2)
Button(button_input, text="Delete", command=lambda: delete(
    listbox)).pack(side=LEFT, padx=2)
Button(button_input, text="Delete all",
       command=lambda: deleteAll(listbox)).pack(side=LEFT, padx=2)
Button(button_input, text="Exit", command=root.quit).pack(side=LEFT, padx=2)
button_input.grid(row=5, column=1)

button_output = Frame(root)
Button(button_output, text="Extract text",
       command=lambda: extract_text_all_file(paths)).pack(side=LEFT, padx=2)
Button(button_output, text="Extract images",
       command=lambda: extract_images_all_file(paths)).pack(side=LEFT, padx=2)
Button(button_output, text="Merge all files", command=lambda: merge_pdfs(
    paths)).pack(side=LEFT, padx=2)
button_output.grid(row=6, column=1)
root.mainloop()
