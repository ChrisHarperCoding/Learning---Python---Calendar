# Import required modules and classes
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel, QPushButton

# Create a custom CalendarApp class that inherits from QWidget
class CalendarApp(QWidget):
    def __init__(self):
        # Call the parent class constructor
        super().__init__()

        # Initialize the user interface
        self.init_ui()

    def init_ui(self):
        # Set the window title
        self.setWindowTitle("Calendar")

        # Create a QVBoxLayout to arrange widgets vertically
        layout = QVBoxLayout()

        # Create a QCalendarWidget and add it to the layout
        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        # Create a QLabel for displaying the selected date and add it to the layout
        self.label = QLabel("")
        layout.addWidget(self.label)

        # Create a QPushButton, connect its 'clicked' signal to the 'show_date' slot, and add it to the layout
        self.button = QPushButton("Show Selected Date")
        self.button.clicked.connect(self.show_date)
        layout.addWidget(self.button)

        # Set the layout for the main QWidget
        self.setLayout(layout)

    # Define the 'show_date' slot that will be called when the button is clicked
    def show_date(self):
        # Get the selected date from the QCalendarWidget
        date = self.calendar.selectedDate()
        # Set the QLabel text to the selected date
        self.label.setText(f"Selected date: {date.toString()}")

# Define the 'main' function to run the application
def main():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a CalendarApp instance and show it
    calendar_app = CalendarApp()
    calendar_app.show()

    # Start the event loop and exit when the application is closed
    sys.exit(app.exec_())

# Run the 'main' function if this script is executed directly
if __name__ == "__main__":
    main()