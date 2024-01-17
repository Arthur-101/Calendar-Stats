from customtkinter import *
import calendar
import datetime
# from time import strftime


class calender_win:
    def __init__(self, root):
        self.root = root
        set_appearance_mode('DARK')
        self.root.wm_state("zoomed")
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        self.root.title('Calendar')
        
        self.year = datetime.datetime.now().year
        self.month = datetime.datetime.now().month
        


        ##### Frame to show calender  #####
        self.calendar_frame = CTkFrame(self.root, border_width=5, corner_radius=0, )
        self.calendar_frame.place(relx=0.05, rely=0.07, relwidth=0.4, relheight=0.4)
        
        # # Create the previous and next buttons
        self.previous_button = CTkButton(self.calendar_frame, text="<<<", command=self.show_previous_month)
        self.previous_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_button = CTkButton(self.calendar_frame, text=">>>", command=self.show_next_month)
        self.next_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)
        
        self.show_calendar(self.year, self.month)
        
        self.time_frame = CTkFrame(self.root, border_width=0, corner_radius=0, fg_color='#242424')
        self.time_frame.place(relx=0.48, rely=0.07, relwidth=0.38, relheight=0.2)
        
        self.timelabel = CTkLabel(self.time_frame, font=('calibri',60,'bold'))
        self.timelabel.place(relx=0.01,rely=0.02, )
        self.am_pm_label = CTkLabel(self.time_frame, font=('calibri',120,'bold'))
        self.am_pm_label.place(relx=0.625,rely=0.01, )
        self.daylabel = CTkLabel(self.time_frame, font=('calibri', 30, 'bold'))
        self.daylabel.place(relx=0.39, rely=0.45, )
        
        self.update_daytime()
        

    def update_daytime(self):
        # current_time = strftime('%H:%M:%S %p')
        current_time = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]  ## Truncating microsecond to milisecond
        self.timelabel.configure(text=current_time)
        am_pm = datetime.datetime.now().strftime('%p')
        self.am_pm_label.configure(text=am_pm)
        current_day = datetime.datetime.now().strftime('%A')
        self.daylabel.configure(text=current_day)
        self.timelabel.after(1, self.update_daytime)  # Update every 1000 milliseconds (1 second)
    
    def show_calendar(self, year, month):
        # Get the current year and month
        # year = datetime.datetime.now().year
        # month = datetime.datetime.now().month
        today = datetime.datetime.now().day  # Use a different variable name here

        # Create a calendar for the specified year and month
        cal = calendar.monthcalendar(year, month)
        
        # Get the current day
        today = datetime.date.today()


        # Create a label to display the calendar
        self.calendar_label = CTkLabel(self.calendar_frame, text=calendar.month_name[month] + " " + str(year), font=('Fira Code', 20, 'bold'))
        self.calendar_label.place(relx=0.38, rely=0.07,)

        # Create labels for the days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day_name in enumerate(days):  # Use a different variable name here
            self.day_label = CTkLabel(self.calendar_frame, text=day_name, font=('Fira Code', 17, 'bold'))
            self.day_label.place(relx=0.1 + i * 0.13, rely=0.2,)

        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                if day != 0:
                    date_str = str(day)  # Convert date to string
                    if datetime.date(year, month, day) == today:
                        self.day_label = CTkLabel(self.calendar_frame, text=date_str, text_color='#ff0000', font=('Fira Code', 17, 'bold'))
                    else:
                        self.day_label = CTkLabel(self.calendar_frame, text=date_str, font=('Fira Code', 17,))
                    self.day_label.place(relx=0.1 + col * 0.13, rely=0.3 + row * 0.11,)

    def show_previous_month(self):
        # nonlocal year, month
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        try:
            for child in self.calendar_frame.winfo_children():
                child.destroy()
        except:
            pass
        self.show_calendar(self.year, self.month)
        
        # # Create the previous and next buttons
        self.previous_button = CTkButton(self.calendar_frame, text="<<<", command=self.show_previous_month)
        self.previous_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_button = CTkButton(self.calendar_frame, text=">>>", command=self.show_next_month)
        self.next_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)

    def show_next_month(self):
        # nonlocal year, month
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        try:
            for child in self.calendar_frame.winfo_children():
                child.destroy()
        except:
            pass
        self.show_calendar(self.year, self.month)
        
        # # Create the previous and next buttons
        self.previous_button = CTkButton(self.calendar_frame, text="<<<", command=self.show_previous_month)
        self.previous_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_button = CTkButton(self.calendar_frame, text=">>>", command=self.show_next_month)
        self.next_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)


if __name__ == "__main__":
    root = CTk()
    main_win = calender_win(root)
    root.mainloop()

