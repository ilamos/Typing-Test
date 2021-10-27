# Imports, Tkiner for UI, random for choosing words
import tkinter as GUI
from tkinter import messagebox
from tkinter import messagebox
from tkinter.constants import END, LEFT, RIGHT
from math import floor
import time
import random
word_library = [
    "close",
    "sex",
    "obstacle",
    "relinquish",
    "photography",
    "past",
    "responsible",
    "descent",
    "list",
    "cathedral",
    "dollar",
    "spray",
    "laundry",
    "cancer",
    "implicit",
    "helmet",
    "eternal",
    "index",
    "picture",
    "decoration",
    "communist",
    "percent",
    "result",
    "mechanism",
    "depart",
    "thesis",
    "indulge",
    "hell",
    "asset",
    "player",
    "volume",
    "scan",
    "middle",
    "wrong",
    "estimate",
    "master",
    "session",
    "shrink",
    "deprive",
    "baby",
    "shout",
    "canvas",
    "swarm",
    "astonishing",
    "flesh",
    "include",
    "foreigner",
]
class typing_test():
    class char():
        def __init__(self, char, right):
            self.right = right
            self.str = char

        def get_tag(self):
            if self.right:
                return "right"
            else:
                return "wrong" 

    class app_data():
        def __init__(self, words):
            print("Initializing application data.")
            self.text_array = []
            for i in range(words):
                self.text_array.append(random.choice(word_library))
            self.typing_text = " ".join(self.text_array)
            self.typing_textvar = GUI.StringVar()
            self.typing_textvar.set(self.typing_text)
            self.typing_writevar = GUI.StringVar()
            self.typing_chararr = []
            self.typing_index = 0
            self.typing_mistakes = 0
            self.word_amount = words
            self.start_time = None

    def replace_char(self, cur_string, new_char, index):
        return cur_string[:index] + new_char + cur_string[index + 1:]

    def update_text(self):
        print("Updating text")
        if self.appdata.typing_index > len(self.appdata.typing_text) - 1:
            return
        self.writing_text.configure(state="normal")
        self.writing_text.delete("1.0", END)
        for cur_char in self.appdata.typing_chararr:
            self.writing_text.insert("end", cur_char.str, cur_char.get_tag())
        self.writing_text.see("end")
        self.writing_text.configure(state="disabled")
        cur_text = self.appdata.typing_text
        cur_text = "> " + cur_text[self.appdata.typing_index:self.appdata.typing_index + 20]
        self.appdata.typing_textvar.set(cur_text)
        if self.appdata.typing_index == 1:
            self.appdata.start_time = time.time()

    def on_backspace(self, event):
        print("Backspace pressed")
        self.appdata.typing_chararr = self.appdata.typing_chararr[:-1]
        self.appdata.typing_index = max(self.appdata.typing_index - 1, 0)
        self.update_text()

    def check_text_end(self):
        if self.appdata.typing_index == len(self.appdata.typing_text):
            seconds = time.time() - self.appdata.start_time
            wpm = floor(len(self.appdata.text_array) / (seconds / 60))
            print("-- TEST END --")
            print("Time taken: " + str(seconds))
            print("WPM: " + str(wpm))
            print("Words: " + str(self.appdata.word_amount))
            messagebox.showinfo("Test ended", """Typing test ended.  \n
             Mistakes: """ + str(self.appdata.typing_mistakes) + """\n
             WPM: """ + str(wpm))
            self.app_window.destroy()

    def on_type(self, *args):
        current_writing = self.appdata.typing_writevar.get()
        current_textleft = self.appdata.typing_text
        print("Letter written: " + current_writing)
        self.writing_text.configure(state="normal")
        if current_textleft[self.appdata.typing_index].capitalize() == current_writing.capitalize():
            self.appdata.typing_chararr.append(self.char(current_writing, True))
        else:
            self.appdata.typing_chararr.append(self.char(current_writing, False))
            self.appdata.typing_mistakes += 1
        self.appdata.typing_writevar.set("")
        self.writing_text.configure(state="disabled")
        self.appdata.typing_index += 1
        self.update_text()
        self.check_text_end()

    def init_elements(self):
        print("Initializing window elements.")
        self.typing_label = GUI.Label(textvariable=self.appdata.typing_textvar).pack()
        self.writing_text = GUI.Text(height=1, width=20, wrap="none", padx=20, background="gray")
        self.writing_text.tag_configure("right", foreground="green", background="white")
        self.writing_text.tag_configure("wrong", foreground="red", background="black", underline=True)
        self.writing_text.configure(state="disabled")
        self.writing_text.pack()
        self.text_entry = GUI.Entry(textvariable=self.appdata.typing_writevar, width=10).pack()
        self.app_window.bind("<BackSpace>", self.on_backspace)
        self.appdata.typing_writevar.trace_add("write", callback=self.on_type)
        

    def init_window(self):
        print("Initializing app window.")
        self.app_window = GUI.Tk()
        self.app_window.geometry("400x110")
        self.app_window.resizable(False, False)
        self.app_window.title("Typing test")

    def __init__(self, words):
        print("Initializing application.")
        self.init_window()
        self.appdata = self.app_data(words)
        self.init_elements()
        self.update_text()
        print("Starting app loop.")
        self.app_window.mainloop()
        

def __main__():
    app = typing_test(20)

__main__()