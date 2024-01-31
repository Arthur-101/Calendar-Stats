from customtkinter import *
import tkinter as tk
from tkinter import ttk
import calendar
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

        #######   MAIN FRAME   #######
        self.main_frame = CTkFrame(self.root, border_width=0, corner_radius=0, fg_color='#242424')
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        ##### Frame to show calender  #####
        self.calendar_frame = CTkFrame(self.main_frame, border_width=5, corner_radius=0, border_color='#007200')
        self.calendar_frame.place(relx=0.05, rely=0.07, relwidth=0.4, relheight=0.4)
        
        # # Create the previous and next buttons
        self.previous_month_button = CTkButton(self.calendar_frame, text="<<<", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_previous_month)
        self.previous_month_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_month_button = CTkButton(self.calendar_frame, text=">>>", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_next_month)
        self.next_month_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)
        
        self.show_calendar(self.year, self.month)
        
        self.time_frame = CTkFrame(self.main_frame, border_width=0, corner_radius=0, fg_color='#242424')
        self.time_frame.place(relx=0.48, rely=0.07, relwidth=0.38, relheight=0.2)
        
        ####  Time and Day label  ####
        self.timelabel = CTkLabel(self.time_frame, font=('calibri',60,'bold'))
        self.timelabel.place(relx=0.01,rely=0.02, )
        self.am_pm_label = CTkLabel(self.time_frame, font=('calibri',120,'bold'))
        self.am_pm_label.place(relx=0.625,rely=0.01, )
        self.daylabel = CTkLabel(self.time_frame, font=('calibri', 30, 'bold'))
        self.daylabel.place(relx=0.345, rely=0.45, )
        
        self.update_daytime()
        
        
        ####  Progress Bar Frame  ####
        self.progress_frame = CTkFrame(self.main_frame, border_width=0, corner_radius=0, fg_color='#242424')
        self.progress_frame.place(relx=0.21, rely=0.6, relwidth=0.62, relheight=0.2)
        
        self.progressbars_list = [self.day_in_week_progress, self.day_in_month_progress, self.day_in_year_progress,
                             self.year_in_decade_progress, self.year_in_century_progress]
        
        self.current_progressbar_index = 2
        
        self.current_progressbar()
        
        self.lower_progress_button = CTkButton(self.main_frame, text="↓", font=('calibri', 30, 'bold'),
                fg_color='#38b000', hover_color='#008000', command = self.change_progressbar_lower)
        self.lower_progress_button.place(relx=0.1, rely=0.63, relwidth=0.06, relheight=0.07)

        self.upper_progress_button = CTkButton(self.main_frame, text="↑", font=('calibri', 30, 'bold'),
                fg_color='#38b000', hover_color='#008000', command = self.change_progressbar_upper)
        self.upper_progress_button.place(relx=0.84, rely=0.63, relwidth=0.06, relheight=0.07)
        
        

    ##  Update Time and Date
    def update_daytime(self):
        current_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]  ## Truncating microsecond to milisecond
        self.timelabel.configure(text=current_time)
        am_pm = datetime.now().strftime('%p')
        self.am_pm_label.configure(text=am_pm)
        current_day = datetime.now().strftime('%A')
        self.daylabel.configure(text=current_day)
        self.timelabel.after(1, self.update_daytime)  # Update every 1 milliseconds
    
    
    ##  Show Calendar
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
        self.previous_month_button = CTkButton(self.calendar_frame, text="<<<", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_previous_month)
        self.previous_month_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_month_button = CTkButton(self.calendar_frame, text=">>>", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_next_month)
        self.next_month_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)

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
        self.previous_month_button = CTkButton(self.calendar_frame, text="<<<", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_previous_month)
        self.previous_month_button.place(relx=0.05, rely=0.05, relwidth=0.15, relheight=0.1)

        self.next_month_button = CTkButton(self.calendar_frame, text=">>>", font=('calibri', 20, 'bold'),
                    fg_color='#38b000', hover_color='#008000', command=self.show_next_month)
        self.next_month_button.place(relx=0.8, rely=0.05, relwidth=0.15, relheight=0.1)


    ##  Days In WEEK
    def day_in_week_progress(self):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        # Create a Progressbar widget
        self.progress_bar = CTkProgressBar(self.progress_frame, orientation='horizontal',  variable=self.progress_var,
            mode='determinate', corner_radius=1, border_width=3, border_color='#007200', progress_color='#38b000')
        self.progress_bar.place(relx=0.02, rely=0.1, relwidth=0.84, relheight=0.4)
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('Calibri', 30, 'bold'),)
        self.progress_num.place(relx=0.865, rely=0.16)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Week", font=('Fira Code', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_day_in_week_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_day_in_week_progress(self, progress_bar, progress_var, progress_num):
        # Get the current date
        current_date = datetime.now()
        # today's day number in the week (0 = Monday, 6 = Sunday)
        week_day_number = current_date.weekday() + 1
        
        total_days = 7

        # percentage of the month that has passed
        progress_percentage = (week_day_number / total_days) * 100
        progress_value = progress_percentage/100
        
        # progress_bar['value'] = progress_value

        var = progress_var.get()
        if var < progress_value:
            progress_var.set(var + 0.001)
            progress_num.configure(text = f"{progress_var.get()*100:.2f} %")
            self.root.after(1, self.update_day_in_week_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_value:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


    ##  Days In MONTHS
    def day_in_month_progress(self):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        # Create a Progressbar widget
        self.progress_bar = CTkProgressBar(self.progress_frame, orientation='horizontal',  variable=self.progress_var,
            mode='determinate', corner_radius=1, border_width=3, border_color='#007200', progress_color='#38b000')
        self.progress_bar.place(relx=0.02, rely=0.1, relwidth=0.84, relheight=0.4)
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('Calibri', 30, 'bold'),)
        self.progress_num.place(relx=0.865, rely=0.16)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Month", font=('Fira Code', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_day_in_month_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_day_in_month_progress(self, progress_bar, progress_var, progress_num):
        # Get the current date
        current_date = datetime.now()
        # Get the day of the month
        current_day = current_date.timetuple().tm_mday
        
        # Get the last day of the month
        last_day_of_month = calendar.monthrange(current_date.year, current_date.month)[1]
        total_days = last_day_of_month

        # percentage of the month that has passed
        progress_percentage = (current_day / total_days) * 100
        progress_value = progress_percentage/100
        
        # progress_bar['value'] = progress_value

        var = progress_var.get()
        if var < progress_value:
            progress_var.set(var + 0.01)
            progress_num.configure(text = f"{progress_var.get()*100:.2f} %")
            self.root.after(10, self.update_day_in_month_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_value:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


    ##  Days In YEARS
    def day_in_year_progress(self,):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        # Create a Progressbar widget        
        self.progress_bar = CTkProgressBar(self.progress_frame, orientation='horizontal',  variable=self.progress_var,
            mode='determinate', corner_radius=1, border_width=3, border_color='#007200', progress_color='#38b000')
        self.progress_bar.place(relx=0.02, rely=0.1, relwidth=0.84, relheight=0.4)
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('Calibri', 30, 'bold'),)
        self.progress_num.place(relx=0.865, rely=0.16)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Year", font=('Fira COde', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_day_in_year_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_day_in_year_progress(self, progress_bar, progress_var, progress_num):
        # Get the current date
        current_date = datetime.now()
        # Get the day of the year
        current_day = current_date.timetuple().tm_yday
        
        # Get the current year
        current_year = datetime.now().year
        # Get the last day of the year
        last_day_of_year = datetime(current_year, 12, 31).date()
        # Total number of days in the year
        total_days = last_day_of_year.timetuple().tm_yday

        # percentage of the year that has passed
        progress_percentage = (current_day / total_days) * 100
        progress_value = progress_percentage/100
        
        # progress_bar['value'] = progress_value

        var = progress_var.get()
        if var < progress_value:
            progress_var.set(var + 0.001)
            progress_num.configure(text = f"{progress_var.get()*100:.2f} %")
            self.root.after(1, self.update_day_in_year_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_value:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


    ##  Years IN DECADE
    def year_in_decade_progress(self,):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        # Create a Progressbar widget        
        self.progress_bar = CTkProgressBar(self.progress_frame, orientation='horizontal',  variable=self.progress_var,
            mode='determinate', corner_radius=1, border_width=3, border_color='#007200', progress_color='#38b000')
        self.progress_bar.place(relx=0.02, rely=0.1, relwidth=0.84, relheight=0.4)
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('Calibri', 30, 'bold'),)
        self.progress_num.place(relx=0.865, rely=0.16)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Decade", font=('Fira COde', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_year_in_decade_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_year_in_decade_progress(self, progress_bar, progress_var, progress_num):
        # Get the current year
        current_year = datetime.now().year
        
        # start year of the current decade
        start_year_of_decade = (current_year // 10) * 10
        
        # Total number of years in a decade
        total_years = 10

        # percentage of the year that has passed
        progress_percentage = ((current_year - start_year_of_decade) / total_years) * 100
        progress_value = progress_percentage/100
        
        # progress_bar['value'] = progress_value

        var = progress_var.get()
        if var < progress_value:
            progress_var.set(var + 0.001)
            progress_num.configure(text = f"{progress_var.get()*100:.2f} %")
            self.root.after(1, self.update_year_in_decade_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_value:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


    ##  Years IN CENTURY
    def year_in_century_progress(self,):
        # Create a progress variable
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        # Create a Progressbar widget        
        self.progress_bar = CTkProgressBar(self.progress_frame, orientation='horizontal',  variable=self.progress_var,
            mode='determinate', corner_radius=1, border_width=3, border_color='#007200', progress_color='#38b000')
        self.progress_bar.place(relx=0.02, rely=0.1, relwidth=0.84, relheight=0.4)
        self.progress_bar.set(0)
        self.progress_bar.start()
        
        self.progress_num = CTkLabel(self.progress_frame, text="0 %", font=('Calibri', 30, 'bold'),)
        self.progress_num.place(relx=0.865, rely=0.16)
        
        self.progress_name = CTkLabel(self.progress_frame, text="Century", font=('Fira COde', 30, 'bold'))
        self.progress_name.place(relx=0.46, rely=0.6)
        
        self.update_year_in_century_progress(self.progress_bar, self.progress_var, self.progress_num)

    def update_year_in_century_progress(self, progress_bar, progress_var, progress_num):
        # Get the current year
        current_year = datetime.now().year
        
        # start year of the current century
        start_year_of_century = (current_year // 100) * 100
        
        # Total number of years in a century
        total_years = 100

        # percentage of the year that has passed
        progress_percentage = ((current_year - start_year_of_century) / total_years) * 100
        progress_value = progress_percentage/100
        
        # progress_bar['value'] = progress_value

        var = progress_var.get()
        if var < progress_value:
            progress_var.set(var + 0.001)
            progress_num.configure(text = f"{progress_var.get()*100:.2f} %")
            self.root.after(1, self.update_year_in_century_progress, progress_bar, progress_var, progress_num)

        # Stop the progress bar when the progress reaches or exceeds 100%
        if progress_var.get() >= progress_value:
            progress_num.configure(text = f"{progress_percentage:.2f} %")
            progress_bar.stop()


    ##  Other Functions
    def current_progressbar(self,):
        self.progressbars_list[self.current_progressbar_index]()


    ##  Change ProgressBar Buttons
    def change_progressbar_lower(self,):
        # self.progress_bar.stop()
        self.current_progressbar_index = self.current_progressbar_index - 1
        
        if self.current_progressbar_index == 0:
            self.lower_progress_button.configure(state=DISABLED)
        else:
            self.upper_progress_button.configure(state=NORMAL)
        
        for widget in self.progress_frame.winfo_children():
            widget.destroy()
        
        self.current_progressbar()
    
    def change_progressbar_upper(self,):
        # self.progress_bar.stop()
        self.current_progressbar_index = self.current_progressbar_index + 1
        
        if self.current_progressbar_index == len(self.progressbars_list) - 1:
            self.upper_progress_button.configure(state=DISABLED)
        else:
            self.lower_progress_button.configure(state=NORMAL)
        
        for widget in self.progress_frame.winfo_children():
            widget.destroy()
        
        self.current_progressbar()
        
        



if __name__ == "__main__":
    root = CTk()
    main_win = calender_win(root)
    root.mainloop()

