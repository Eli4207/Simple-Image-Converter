import os.path
from tkinter import filedialog
import ttkbootstrap as ttk
from PIL import Image

filepaths = []

def add_file():
    allowed_filetypes = ("PNG files", "*.png"),("JPEG files", "*.jpg"),("GIF files", "*.gif"),("TIFF files", "*.tif"),("WEBP files", "*.webp"),("All files", "*.*")
    file = filedialog.askopenfilename(initialdir=os.path.abspath(__file__), title="Select a File", filetypes=(allowed_filetypes))
    if not file == "":
        filepaths.append(file)
    update_files()

def update_files():
    files = ""
    for i in range(0, len(filepaths)):
        files += "\n" + str(i + 1) + ". " + filepaths[i]
    flabel.configure(text="Selected files: " + files)

def convert_file():
    if len(filepaths) == 0:
        wlabel.configure(text="Please add files to convert!")
    elif r.get() == "":
        wlabel.configure(text="Please specify an image format!")
    else:
        for i in range(0, len(filepaths)):
            img = Image.open(filepaths[i])
            rgb_img = img.convert("RGB")
            rgb_img.save(os.path.basename(filepaths[i]).split('.')[0] + r.get())
        wlabel.configure(text="Images successfully converted!")
        filepaths.clear()


root = ttk.Window(themename="litera")
root.title("SPM")
root.resizable(width=False, height=False)
r = ttk.StringVar()

hlabel = ttk.Label(root, text="Simple Image Converter", font=('Arial', 20))
hlabel.grid(column=0, row=0)

b1 = ttk.Button(root, text="Search file", width=30, command=add_file)
b1.grid(column=0, row=1)

flabel = ttk.Label(root, text="Selected files: ", font=('Arial', 12))
flabel.grid(column=0, row=2)

clabel = ttk.Label(root, text="Convert to: ", font=('Arial', 12))
clabel.grid(column=0, row=3)

cbox = ttk.Combobox(root, textvariable=r)
cbox['state'] = 'readonly'
cbox['values'] = ['.png', '.jpg', '.gif', '.tif', '.webp']
cbox.grid(column=1, row=3)

b2 = ttk.Button(root, text="Convert", width=30, command=convert_file)
b2.grid(column=0, row=4)

wlabel = ttk.Label(root, text=" ", font=('Arial', 12))
wlabel.grid(column=1, row=4)

root.mainloop()