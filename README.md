# Barcode scanner with Python GUI
This is a project to scan QR-Codes with the camera of the Raspberry Pi. The Information of the QR-Code will then be displayed on a GUI.<br><br>
![This is a test QR-Code you can scan](/Screenshots/qrcode.jpeg)
# Hardware
All you need is is listed below:<br>
-Raspberry Pi Model 3 (or newer)<br>
-Raspberry Pi Camera V2<br>
I recommend to build a camera tripod for the Pi-Cam (For example with a 3D printer). This way you don't have to hold the camera during the recording. This prevents the captured image from becoming blurred and this way a faulty readout.<br>
When you connect the camera to the Pi, make sure the cable is facing the right direction. Otherwise you will not get a picture.

# Software
First, you have to enable the camera port on the Raspberry Pi. There are a lot of tutorials out there so I will not go into detail about this step. Next, we have to install the required tools and libaries for my code. You can simply copy and paste the following lines of code. Then execute them. There should be no errors: <br>

sudo apt-get update<br>
sudo apt-get install python3 python3-pip libzbar0<br>
sudo pip3 install opencv-python pyzbar imutils<br>
sudo apt-get install libcblas-dev libhdf5-dev libhdf5-serial-dev libatlas-base-dev lib<br>
jasper-dev libqtgui4 libqt4-test<br>

If you are using an older versions of Python, please delete them. These will cause problems later when displaying the image in the GUI if they are not deleted.
Your Pi is now ready for the first scan.

# How the program works
When you run the code, the GUI will open. You will have two buttons. One to take a picture of the code and another to display the information of the code. These are then shown in the label. The taken image of the QR-Code will also be displayed. 

# Possible upgrades of the project
-create another button so that you can open the link of a QR code directly<br>
-get a better camera: Until now, it is only possible to read QR codes. This is because the Raspberry Pi Camera V2 is still not good enough to take clear pictures of a barcode. The lines are simply too blurry to be read by the program. The libraries used are capable of reading barcodes. You can change the path to a downloaded image of a barcode. You will see that then the information can be read. 

# Sources
Since this is a school project I looked up how to set up such scanner. Below you will find the link I used:<br>
-https://tutorials-raspberrypi.de/raspberry-pi-barcode-scanner-qr-mit-kamera-selber-bauen/


