import tkinter
from tkinter import filedialog
import PIL
from PIL import ImageOps
import pathlib
import os

def show_image(inputPhoto):
    #img = cv2.imread(inputPhoto, cv2.IMREAD_COLOR)
    #cv2.imshow("uwu", img)
    return True

def imgSplitting():
    global inputDialog
    inputDialog = filedialog.askopenfilename(title="Select input file", filetypes=(("All files", "*.*"), ("png files", "*.png"),("jpg files", "*.jpg")))

    image_file = inputDialog
    sourceDir = pathlib.Path(image_file).parent.resolve()
    ext = os.path.basename(image_file).split('/')[-1].split(".")[0]
    print("Full path to image: " + str(image_file))
    print("File directory: " + str(sourceDir))
    print("Name of the file: " + str(ext))

    folderPath = str(sourceDir) + "/" + str(ext)

    print("Checking for folder to save the images to...")
    try:
        print("Image folder found!")
        os.listdir(folderPath)
    except:
        print("No image folder found, so created one!")
        os.mkdir(folderPath)   

    img = PIL.Image.open(image_file)
    wRes, hRes = img.size
    print(str(wRes) + "x " + str(hRes) + "y")

    borders = [(0, 0, wRes / 2, hRes / 2), (wRes / 2, 0, wRes, hRes / 2), (0, hRes / 2, wRes / 2, hRes), (wRes / 2, hRes / 2, wRes, hRes)]

    i = 0
    while(i < 4):
        path = folderPath + "/" + str(ext) + "_" + str(i) + ".png"
        print("Saved image path: " + str(path))
        cropped = img.crop(borders[i])
        #cropped.show()
        cropped.save(path, "PNG")
        i+=1

def window():
    # Main GUI config
    window = tkinter.Tk()
    window.title('Instagram IMG Splitter')
    window.geometry("300x50")
    tkinter.Label(window, text= "Instagram IMG Splitter").pack()
    photoButton = tkinter.Button(window, text="Select file", command=imgSplitting).pack()
    window.mainloop()

window()