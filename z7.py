import sqlite3
from tkinter import *
from tkinter import messagebox


class my_button:
    def __init__(self, text, font, x, y, width, window, command):
        self.window = window
        self.command = command

        self.button = Button(text=text, font=font, activebackground="blue", activeforeground="white")
        self.button.place(x=x, y=y, width=width)
        self.button.bind('<Button-1>', lambda event: self.click(self.command))


    def click(self, command):
        if command == "enter":
            self.enter()
        elif command == "show":
            self.show()

    def show(self):
        if self.window.entry_password_entry.cget('show') == '':
            self.window.entry_password_entry.config(show='')

    def enter(self):
        print('sjdfgk')
        self.value_login = self.window.entry_login.value.get()
        self.value_pass = self.window.entry_password.value.get()
        self.db = connect_db('simulator_avtoservis.db')
        self.sql = self.db.select_sql("SELECT * from users")
        for row in self.sql:
            self.db_login = row[1]
            self.db_pass = row[2]

            if self.value_login == self.db_login and self.value_pass == self.db_pass:
                self.open = True
                break
            else:
                self.open = False
        self.db.close_db()
        if self.open:
            messagebox.showinfo("Внимание!", 'Доступ разрешен')
            self.window.destroy_main_window()
            self.work_window = my_window('Сервисный центр', '800x800')
            self.work_window.canva_for_work_window()
            self.work_window.widget_for_work_window()
            self.work_window.visible_window()
        else:
            messagebox.showerror("Внимание!", "Неверный логин или пароль")


class my_entry:
    def __init__(self, font, x, y, width, mask):
        self.value = StringVar()
        if mask == True:
            show = "*"
        else:
            show = ""
        self.entry = Entry(textvariable=self.value, font=font, show=show)
        self.entry.place(x=x, y=y, width=width)


class my_label:
    def __init__(self, text, font, bg, x, y):
        self.label = Label(text=text, font=font, bg=bg)
        self.label.place(x=x, y=y)


class connect_db:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connector = sqlite3.connect(self.db_name)
        self.cursor = self.connector.cursor()

    def select_sql(self, sql_txt):
        self.sql_txt = sql_txt
        return self.cursor.execute(self.sql_txt)

    def close_db(self):
        self.connector.commit()
        self.cursor.close()
        self.connector.close()

class My_check_button:
    def __init__(self, text, font, bg, x, y):
        self.check_button= Checkbutton(text=text, font=font, bg=bg, state="disabled", disabledforeground="black")
        self.check_button.place(x=x, y=y)
class my_window:
    def __init__(self, title, size):
        self.window = Tk()
        self.window.geometry(size)
        self.window.resizable(False, False)
        self.window.title(title)
        self.window.configure(bg="Lightblue")
        self.kol_avto= 0
    def widget_for_work_window(self):
        self.label_title=my_label("Сервисное обслуживание автомобиля", "Arial 20 bold", "Lightblue", 150, 10)

        self.step1=My_check_button("Доставить машину в сервис", "Arial 15", "Lightblue", 30, 100)
        self.step2 = My_check_button("Провести полный осмотр", "Arial 15", "Lightblue", 30, 150)
        self.step3 = My_check_button("Помыть машину", "Arial 15", "Lightblue", 30, 200)
        self.step4 = My_check_button("Провести ремонт", "Arial 15", "Lightblue", 30, 250)
        self.step5 = My_check_button("Установить сигнализацию", "Arial 15", "Lightblue", 30, 300)
        self.step6 = My_check_button("Доставить машину в гараж", "Arial 15", "Lightblue", 30, 350)

        self.info= my_label("Чтобы доставить машину" + "\n" + "из гаража в мастерскую и обратно" + "\n" + "воспользуйтесь стрелками на клавиатуре", "Arial 15", "Lightblue", 10, 650)

    def visible_window(self):
        self.window.mainloop()

    def destroy_main_window(self):
        self.window.destroy()

    def widget_for_start_window(self):
        self.label_title = my_label("ВХОД", "Arial 20 bold", "lightblue", 150, 50)
        self.label_login = my_label("Логин:", "Arial 15", "lightblue", 50, 150)
        self.label_password = my_label("Пароль:", "Arial 15", "lightblue", 50, 200)
        self.entry_login = my_entry("Arial 15", 150, 150, 150, False)
        self.entry_password = my_entry("Arial 15", 150, 200, 150, True)
        self.entry_password_entry = self.entry_password.entry
        self.enter_btn = my_button("ВХОД", "Arial 15", 150, 300, 100, self, "enter")
        self.show_btn = my_button("☼", "Arial 12", 310, 200, 35, self, "show")

    def canva_for_work_window(self):
        self.canva= Canvas(width=800, height=800, bg= 'Lightblue')
        self.canva.pack()
        self.work_place= self.canva.create_rectangle(500, 100, 650, 300, width=3, dash=(1,1))
        self.start_place = self.canva.create_rectangle(500, 590, 650, 790, width=3, dash=(1, 1))
        self.txt_master= self.canva.create_text(600, 320, font= "Arial 15", text="мастерская")
        self.txt_garage = self.canva.create_text(600, 570, font="Arial 15", text="гараж")
        self.txt_kol_avto= self.canva.create_text(150, 570, font="Arial 15", text="количество машин:" +str(self.kol_avto))
        self.txt_start= self.canva.create_text(400, 450, font="Arial 20 bold", text="НАЖМИТЕ ДЛЯ НАЧАЛА РАБОТЫ", fill="red", activefill="green")
        self.canva.tag_bind(self.txt_start, '<Button-1>', lambda event, tag=self.txt_start: self.start_work())
    def start_work (self):
        self.canva.delete(self.txt_start)


start_window = my_window("ВХОД", "400x400")
start_window.widget_for_start_window()
start_window.visible_window()
