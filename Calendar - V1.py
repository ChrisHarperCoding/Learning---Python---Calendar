import calendar
from tkinter import *
from tkinter import ttk

class CalendarApp:
    def __init__(self, master):
        self.master = master
        master.title("Calendar")

        self.year = StringVar()
        self.month = StringVar()

        self.init_ui()

    def init_ui(self):
        self.year_label = Label(self.master, text="Year:")
        self.year_label.grid(row=0, column=0, padx=5, pady=5)

        self.year_entry = Entry(self.master, textvariable=self.year)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)

        self.month_label = Label(self.master, text="Month:")
        self.month_label.grid(row=0, column=2, padx=5, pady=5)

        self.month_entry = Entry(self.master, textvariable=self.month)
        self.month_entry.grid(row=0, column=3, padx=5, pady=5)

        self.show_button = Button(self.master, text="Show Calendar", command=self.show_calendar)
        self.show_button.grid(row=0, column=4, padx=5, pady=5)

        self.calendar_frame = ttk.Frame(self.master)
        self.calendar_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

    def show_calendar(self):
        year = int(self.year.get())
        month = int(self.month.get())

        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_str = cal.formatmonth(year, month)

        self.text_widget = Text(self.calendar_frame, wrap=WORD, height=9, width=20)
        self.text_widget.grid(row=1, column=0, padx=10, pady=10)
        self.text_widget.delete(1.0, END)
        self.text_widget.insert(INSERT, month_str)

def main():
    root = Tk()
    calendar_app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()