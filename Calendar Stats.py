from customtkinter import *
import tkinter as tk
from tkinter import ttk
import calendar
# import datetime
from datetime import datetime


class calender_win:
    def __init__(self, root):
        self.root = root
        set_appearance_mode('DARK')
        self.root.wm_state("zoomed")
        window_width = root.winfo_screenwidth()
        window_height = root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        self.root.title('Calendar')
        
        self.year = datetime.now().year
        self.month = datetime.now().month

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
        
        ####  Time and Day label  ####
        self.timelabel = CTkLabel(self.time_frame, font=('calibri',60,'bold'))
        self.timelabel.place(relx=0.01,rely=0.02, )
        self.am_pm_label = CTkLabel(self.time_frame, font=('calibri',120,'bold'))
        self.am_pm_label.place(relx=0.625,rely=0.01, )
        self.daylabel = CTkLabel(self.time_frame, font=('calibri', 30, 'bold'))
        self.daylabel.place(relx=0.39, rely=0.45, )
        
        self.update_daytime()
        
        self.progress_frame = CTkFrame(self.root, border_width=1, corner_radius=0, fg_color='#242424')
        self.progress_frame.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.2)
        
        self.day_in_year_progress()
        
        

    def update_daytime(self):
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]  ## Truncating microsecond to milisecond
        self.timelabel.configure(text=current_time)
        am_pm = datetime.now().strftime('%p')
        self.am_pm_label.configure(text=am_pm)
        current_day = datetime.now().strftime('%A')
        self.daylabel.configure(text=current_day)
        self.timelabel.after(1, self.update_daytime)  # Update every 1 milliseconds
    
    def show_calendar(self, year, month):
        # Get the current year and month
        # year = datetime.now().year
        # month = datetime.now().month
        today = datetime.now().day

        # Create a calendar for the specified year and month
        cal = calendar.monthcalendar(year, month)
        
        # Get the current day
        today = datetime.today().date()


        # Create a label to display the calendar
        self.calendar_label = CTkLabel(self.calendar_frame, text=calendar.month_name[month] + " " + str(year), font=('Fira Code', 20, 'bold'))
        self.calendar_label.place(relx=0.38, rely=0.07,)

        # Create labels for the days of the week
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day_name in enumerate(days):
            self.day_label = CTkLabel(self.calendar_frame, text=day_name, font=('Fira Code', 17, 'bold'))
            self.day_label.place(relx=0.1 + i * 0.13, rely=0.2,)

        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                if day != 0:
                    date_str = str(day)  # Convert date to string
                    if datetime(year, month, day).date() == datetime.today().date():
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

    def day_in_year_progress(self,):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        # Create a style for the progress bar
        # self.style = ttk.Style()
        # self.style.theme_use('default')
        # self.style.configure("TProgressbar",
        #                 thickness=30,  # You can adjust the thickness of the progress bar
        #                 troughcolor="#ffc8dd",  # Background color
        #                 troughrelief="flat",  # Relief style for the background
        #                 troughborderwidth=2,  # Border width for the background
        #                 barcolor="#a2d2ff",  # Foreground color
        #                 barrelief="flat",  # Relief style for the foreground
        #                 barborderwidth=5)  # Border width for the foreground
        # Create a Progressbar widget
        self.progress_bar = ttk.Progressbar(self.progress_frame, orient="horizontal", variable=self.progress_var, length=300, mode="determinate",
            maximum=100,) # style='TProgressbar')

        self.progress_bar.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.4)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('calibri', 30, 'bold'), bg_color='#e6e6e6', text_color='black')
        self.progress_num.place(relx=0.8, rely=0.15)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Year", font=('calibri', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_day_in_year_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_day_in_year_progress(self, progress_bar, progress_var, progress_num):
        # Get the current date
        current_date = datetime.now()
        # Get the day of the year
        current_day = current_date.timetuple().tm_yday
        
        # Get the current year
        current_year = datetime.now().year
        # Create a date object for the last day of the year
        last_day_of_year = datetime(current_year, 12, 31).date()
        # Get the day of the year for the last day (which is also the total number of days in the year)
        total_days = last_day_of_year.timetuple().tm_yday

        # Calculate the percentage of the year that has passed
        progress_percentage = (current_day / total_days) * 100
        # progress_percentage = 51.00
        
        progress_bar['value'] = progress_percentage

        var = progress_var.get()
        if var < progress_percentage:
            progress_var.set(var + 0.01)
            progress_num.configure(text = f"{progress_var.get():.2f} %")
            self.root.after(1, self.update_day_in_year_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_percentage:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


if __name__ == "__main__":
    root = CTk()
    main_win = calender_win(root)
    root.mainloop()

