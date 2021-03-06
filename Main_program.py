from tkinter import *  # Library building an GUI with tkinter
from PIL import ImageTk, Image  # Library to process the images made by the camera
from picamera import PiCamera  # Library for using the Camera of the Pi
import cv2 # Library for the scanner
from pyzbar import pyzbar  # Library for the scanner

camera = PiCamera()  # creating an object to use the Camera
path = "QRC.png"  # here you can specify where the image of the scan will be saved.


def picture_and_scan():  # Function to take a picture of the QR code and analyze it
    global link, typ, rect, poly
    camera.capture(path)  # camera is taking a picture

    image = cv2.imread(path)  # Seacing for QR-Code on the taken picture
    barcodes = pyzbar.decode(image)

    for barcode in barcodes:  # Extracting the information from the QR code and assigning it to the variables
        link = barcode.data
        typ = barcode.type
        rect = barcode.rect
        poly = barcode.polygon
    try:  # Checking whether information could be extracted from the captured image

        if link != "":
            print("something found")  # control-command for the shell
        else:
            pass
    except:  # This part is executed when no information is found
        print("\n!!Kein Code zum scannen gefunden!!")
        link = 0
        typ = 0
        rect = 0
        poly = 0


def show_qrc():  # Function for a button to display the information found in the scan
    global link, typ, rect, poly
    img = Image.open(path)  # creating a variable with the scan image

    img = img.resize((550, 420))  # scaling the image
    img = ImageTk.PhotoImage(img)  # adapt the image for the GUI

    picture_label.config(image=img)  # creating a label for the image
    picture_label.image = img
    info_Label.configure(text=str(link) + "\n" + str(typ) + "\n" + str(rect) + "\n" + str(poly))


# All below: Definition of the GUI-Window
window = Tk()
window.geometry("1200x800+200+200")
window.configure(bg="grey")
window.title("Barcode-Scanner")

picture_label = Label(window)
picture_label.place(x=200, y=50, width=500, height=420)

btn_scan = Button(window, text="scan", command=picture_and_scan)
btn_scan.config(height=2, width=10)
btn_scan.place(x=20, y=20)

btn_show_code = Button(window, text="show QRC", command=show_qrc)
btn_show_code.config(height=2, width=10)
btn_show_code.place(x=20, y=100)

btn_infos = Button(window, text="show QRC", command=show_qrc)
btn_infos.config(height=2, width=10)
btn_infos.place(x=20, y=100)

info_Label = Label(window, text="Informationen des QR-Codes \n werden hier angezeigt")
info_Label.place(x=800, y=50, width=400, height=200)

window.mainloop()  # loop for the GUI
