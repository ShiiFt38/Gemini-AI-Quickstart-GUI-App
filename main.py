import os
import sys
import PIL.Image
from dotenv import load_dotenv
import google.generativeai as genai
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# App setup
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
app = QApplication([])
widget = QWidget()
widget.setWindowTitle("Vision AI Model")
widget.setFixedSize(700, 600)

# App objects
txtbox_prompt = QLineEdit()
btn_generate = QPushButton("Generate")
txt_imageHolder = QLabel("Upload Image...")
btn_image = QPushButton("Select Image")
txt_response = QLabel("1. Upload an Image\n2. Enter a prompt\n 3. Click 'Generate' to see results")
scroll_response = QScrollArea()

# App Layout
main_layout = QVBoxLayout()

main_top_row = QHBoxLayout()
col_one_row_one = QVBoxLayout()
col_two_row_one = QVBoxLayout()
main_top_row.addLayout(col_one_row_one, 55)
main_top_row.addLayout(col_two_row_one, 35)

main_second_row = QHBoxLayout()

main_layout.addLayout(main_top_row, 30)
main_layout.addLayout(main_second_row, 70)
widget.setLayout(main_layout)

# App Design
txt_response.setWordWrap(True)
scroll_response.setWidget(txt_response)
scroll_response.setWidgetResizable(True)

col_one_row_one.addWidget(txtbox_prompt, alignment=Qt.AlignCenter)
col_one_row_one.addWidget(btn_generate, alignment=Qt.AlignCenter)
col_two_row_one.addWidget(txt_imageHolder, alignment=Qt.AlignCenter)
col_two_row_one.addWidget(btn_image, alignment=Qt.AlignCenter)

main_second_row.addWidget(scroll_response)

buttonStyles = (
        "* { margin: 30px; " +
        "font: bold 12px ;"
        "border-radius: 45px ;"
        "width: 180px ;" +
        "height: 30px; " +
        "background-color: grey ;" +
        "color: white; }" +
        "*:hover { background-color: white; color: black }")
txt_response.setStyleSheet("font: 20px black; display: flex; text-align: center;")
txtbox_prompt.setStyleSheet("height: 30px; width: 300px")
btn_generate.setStyleSheet(buttonStyles)
btn_image.setStyleSheet(buttonStyles)

# App Functionality
selected_image = ""

def generate_response():
    global selected_image_path
    if not selected_image_path:
        txt_response.setText("Please select an image first.")
        return

    prompt = txtbox_prompt.text()
    if not prompt:
        txt_response.setText("Please enter a prompt.")
        return

    try:
        image = PIL.Image.open(selected_image_path)
        response = model.generate_content([prompt, image])
        txt_response.setText(response.text)
    except Exception as e:
        txt_response.setText(f"An error occurred: {str(e)}")

def select_image():
    global selected_image_path
    file_dialog = QFileDialog()
    image_path, _ = file_dialog.getOpenFileName(widget, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

    if image_path:
        selected_image_path = image_path
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        txt_imageHolder.setPixmap(scaled_pixmap)
        txt_imageHolder.setAlignment(Qt.AlignCenter)

btn_generate.clicked.connect(generate_response)
btn_image.clicked.connect(select_image)

# App Initialisation
widget.show()
app.exec_()
