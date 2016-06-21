# WorkHours - Johnathon Kwisses (Kwistech)
from tkinter import *
from webbrowser import open_new
from WorkHours.files.functions import *


class App:

    def __init__(self, conn, root):
        self.conn = conn
        self.root = root

        self.interface(self.root)

    def interface(self, root):
        main_label = Label(root, text="Enter work hours below:")
        main_label.grid(row=0, column=0, columnspan=3, pady=5)

        time_label = Label(root, text="Time:")
        time_label.grid(row=1, column=0)

        to_label = Label(root, text="to")
        to_label.grid(row=1, column=2)

        total_hrs_label = Label(root, text="Hours:")
        total_hrs_label.grid(row=2, column=0)

        copyright_label = Label(root, text="© 2016 Kwistech")
        copyright_label.grid(row=3, column=0, columnspan=2, pady=5, sticky="S")

        time_entry1 = Entry(root, width=6, justify="center")
        time_entry1.grid(row=1, column=1)

        time_entry2 = Entry(root, width=6, justify="center")
        time_entry2.grid(row=1, column=3)

        hour_entry = Entry(root, width=6, justify="center")
        hour_entry.grid(row=2, column=1)

        open_button = Button(root, text="Open",
                             command=lambda: self.open())
        open_button.grid(row=2, column=3, pady=5)

        user_info = [time_entry1, time_entry2, hour_entry]

        submit_button = Button(root, text="Submit",
                               command=lambda: self.set_info(user_info))
        submit_button.grid(row=3, column=3, padx=5)

    @staticmethod
    def open():
        open_new("http://sqliteonline.com/")

    def set_info(self, user_info):
        user_info_str = [x.get() for x in user_info]
        times = "{} - {}".format(user_info_str[0], user_info_str[1])
        hours = user_info_str[2]
        num_entries = select_all_len(self.conn)
        insert_row(self.conn, num_entries, times, hours)

        for entry in user_info:
            entry.delete(first=0, last=139)  # Deletes text in Entry widgets.


def main():
    conn = create_conn()
    create_table(conn)

    root = Tk()
    root.title("Work Hours")

    App(conn, root)

    root.mainloop()

if __name__ == "__main__":
    main()
