import requests
from PyQt5.QtWidgets import (
    QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QLabel, QWidget, QHBoxLayout
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CalculatorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Interactive Calculator with API")
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background-color: #2C3E50;")

        # Central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Title Label
        self.title_label = QLabel("🧮 Calculator (API-based)")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setStyleSheet("color: #ECF0F1; margin: 10px;")
        self.layout.addWidget(self.title_label)

        # Input fields
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText("Enter first number")
        self.input1.setStyleSheet(self._input_style())
        self.layout.addWidget(self.input1)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText("Enter second number")
        self.input2.setStyleSheet(self._input_style())
        self.layout.addWidget(self.input2)

        # Result label
        self.result_label = QLabel("Result: ")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(QFont("Arial", 14))
        self.result_label.setStyleSheet("color: #F39C12; margin: 10px;")
        self.layout.addWidget(self.result_label)

        # Buttons for operations
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.add_button("+", self.perform_addition, "#27AE60")
        self.add_button("-", self.perform_subtraction, "#C0392B")
        self.add_button("*", self.perform_multiplication, "#8E44AD")
        self.add_button("/", self.perform_division, "#3498DB")

    def _input_style(self):
        """Style for input fields."""
        return """
            QLineEdit {
                background-color: #ECF0F1;
                border: 2px solid #95A5A6;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #3498DB;
            }
        """

    def add_button(self, symbol, callback, color):
        """Add a button with a specific symbol, callback, and color."""
        button = QPushButton(symbol)
        button.setFont(QFont("Arial", 14, QFont.Bold))
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: #1ABC9C;
            }}
        """)
        button.clicked.connect(callback)
        self.button_layout.addWidget(button)

    def get_inputs(self):
        """Get inputs and validate them."""
        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            return num1, num2
        except ValueError:
            self.result_label.setText("⚠️ Error: Enter valid numbers.")
            raise

    def perform_addition(self):
        """Send addition request to the API."""
        try:
            num1, num2 = self.get_inputs()
            response = requests.post("http://127.0.0.1:5000/api/add", json={"num1": num1, "num2": num2})
            self.result_label.setText(f"Result: {response.json()['result']}")
        except Exception as e:
            self.result_label.setText(f"⚠️ Error: {str(e)}")

    def perform_subtraction(self):
        """Send subtraction request to the API."""
        try:
            num1, num2 = self.get_inputs()
            response = requests.post("http://127.0.0.1:5000/api/subtract", json={"num1": num1, "num2": num2})
            self.result_label.setText(f"Result: {response.json()['result']}")
        except Exception as e:
            self.result_label.setText(f"⚠️ Error: {str(e)}")

    def perform_multiplication(self):
        """Send multiplication request to the API."""
        try:
            num1, num2 = self.get_inputs()
            response = requests.post("http://127.0.0.1:5000/api/multiply", json={"num1": num1, "num2": num2})
            self.result_label.setText(f"Result: {response.json()['result']}")
        except Exception as e:
            self.result_label.setText(f"⚠️ Error: {str(e)}")

    def perform_division(self):
        """Send division request to the API."""
        try:
            num1, num2 = self.get_inputs()
            response = requests.post("http://127.0.0.1:5000/api/divide", json={"num1": num1, "num2": num2})
            if response.status_code == 400:
                self.result_label.setText(f"⚠️ Error: {response.json()['error']}")
            else:
                self.result_label.setText(f"Result: {response.json()['result']}")
        except Exception as e:
            self.result_label.setText(f"⚠️ Error: {str(e)}")
