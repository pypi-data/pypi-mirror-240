if __name__ == '__main__':
    from tkwinico import Winico
    import tkinter as tk

    Window = tk.Tk()

    Ico = Winico(Window)


    def CallBack(Message, X, Y):
        if Message == "WM_RBUTTONDOWNessage":
            Menu = tk.Menu(tearoff=False)
            Menu.add_command(label="Quit", command=Window.quit)
            Menu.tk_popup(X, Y)


    Ico.tray_add(Ico.icon("application"), callback=CallBack, callback_args=["%message", "%x", "%y"])

    Window.mainloop()