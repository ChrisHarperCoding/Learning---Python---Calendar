import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel, QPushButton

class CalendarApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Calendar")

        layout = QVBoxLayout()

        self.calendar = QCalendarWidget()
        layout.addWidget(self.calendar)

        self.label = QLabel("")
        layout.addWidget(self.label)

        self.button = QPushButton("Show Selected Date")
        self.button.clicked.connect(self.show_date)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_date(self):
        date = self.calendar.selectedDate()
        self.label.setText(f"Selected date: {date.toString()}")

def main():
    app = QApplication(sys.argv)

    calendar_app = CalendarApp()
    calendar_app.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()