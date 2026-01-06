#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import subprocess
import shutil

APP_NAME = "RAMclean"
DROP_CACHE_CMD = "/usr/local/bin/ramclean-dropcache"


def command_exists(cmd):
    return shutil.which(cmd) is not None


def clean_ram():
    if not command_exists("pkexec"):
        messagebox.showerror(
            APP_NAME,
            "pkexec not found.\nInstall polkit to continue."
        )
        return

    try:
        subprocess.run(
            ["pkexec", DROP_CACHE_CMD],
            check=True
        )
        messagebox.showinfo(
            APP_NAME,
            "RAM cache cleaned successfully."
        )
    except subprocess.CalledProcessError:
        messagebox.showerror(
            APP_NAME,
            "Authentication canceled or failed."
        )


def show_processes():
    try:
        proc = subprocess.Popen(
            ["ps", "-eo", "pid,comm,%mem", "--sort=-%mem"],
            stdout=subprocess.PIPE,
            text=True
        )
        lines = proc.stdout.readlines()[:15]
    except Exception as e:
        messagebox.showerror(APP_NAME, str(e))
        return

    win = tk.Toplevel(root)
    win.title("Processes")
    win.geometry("420x300")
    win.configure(bg="#121212")
    win.resizable(False, False)

    text = tk.Text(
        win,
        bg="#1e1e1e",
        fg="#e6e6e6",
        insertbackground="#ffffff",
        relief="flat",
        font=("JetBrains Mono", 10)
    )
    text.pack(expand=True, fill="both", padx=10, pady=10)

    text.insert("1.0", "".join(lines))
    text.config(state="disabled")



root = tk.Tk()
root.title(APP_NAME)
root.geometry("300x170")
root.configure(bg="#121212")
root.resizable(False, False)

frame = tk.Frame(root, bg="#121212")
frame.pack(expand=True)

btn_style = {
    "font": ("JetBrains Mono", 11),
    "bg": "#1e1e1e",
    "fg": "#ffffff",
    "activebackground": "#333333",
    "activeforeground": "#ffffff",
    "relief": "flat",
    "width": 18,
    "height": 1
}

tk.Button(
    frame,
    text="Clean RAM",
    command=clean_ram,
    **btn_style
).pack(pady=(10, 12))

tk.Button(
    frame,
    text="Processes",
    command=show_processes,
    **btn_style
).pack()

root.mainloop()
