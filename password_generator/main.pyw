#!/usr/bin/pythonw
"""A GUI password generator and manager."""
from os.path import exists

import encryptor as encryptor
import password as password
import subprocess
import tkinter as tk
from tkinter import scrolledtext

file_path = 'generated_passwords.txt'

def passwd_generate():
    """Generate the password."""
    passwd = password.Password()
    generated_passwd = passwd.generate()
    passwd_display['text'] = f'{web_entry.get()}: {generated_passwd}'


def update_scrollbox():
    """Update the scrollbox with the file's content."""
    with open(file_path, 'r') as file:
        scrollbox.replace(1.0, tk.END, file.read())


def save_to_file():
    """Saves the password to generated_passwords.txt"""
    with open(file_path, 'a') as file:
        passwd_to_save = passwd_display.cget('text')
        file.write(f'{passwd_to_save}\n')

    with open(file_path, 'r') as file:
        unsorted_passwords = [line for line in file]
    sorted_passwords_lst = sorted(unsorted_passwords)
    sorted_passwords = ''.join(item for item in sorted_passwords_lst)

    with open(file_path, 'w') as file:
        file.write(sorted_passwords)
    update_scrollbox()


def edit_file():
    subprocess.call(
        args = ['C:/Windows/notepad.exe', file_path],
        shell = False
    )


if __name__ == '__main__':
    if not exists(file_path):
        with open(file_path, 'w'):
            pass
        encryptor.encrypt(file_path)

    encryptor.decrypt(file_path)

    root = tk.Tk()
    root.title('Password Generator')
    root.geometry('240x320')
    root.minsize(240, 320)
    root.maxsize(240, 540)

    web_frame = tk.Frame()
    web_entry_label = tk.Label(
        web_frame,
        text = 'Website'
    )
    web_entry = tk.Entry(web_frame)
    passwd_display = tk.Label(
        web_frame,
        text = ''
    )
    gen_save_frame = tk.Frame()
    generate_button = tk.Button(
        gen_save_frame,
        text = 'Generate',
        command = passwd_generate
    )
    save_button = tk.Button(
        gen_save_frame,
        text = 'Save',
        command = save_to_file
    )
    scroll_frame = tk.Frame()
    edit_button = tk.Button(
        scroll_frame,
        text = 'Edit',
        command = edit_file
    )
    refresh_button = tk.Button(
        scroll_frame,
        text = 'Refresh',
        command = update_scrollbox
    )
    scrollbox = scrolledtext.ScrolledText()
    update_scrollbox()

    web_frame.pack()
    web_entry_label.pack(pady = 5)
    web_entry.pack(pady = 5)
    passwd_display.pack(pady = 5)

    gen_save_frame.pack()
    generate_button.pack(
        side = tk.LEFT,
        pady=5,
        padx=10
    )
    save_button.pack(
        side = tk.LEFT,
        pady = 5,
        padx = 10
    )
    scroll_frame.pack(side = tk.BOTTOM)
    edit_button.pack(
        side = tk.LEFT,
        pady = 5,
        padx = 10
    )
    refresh_button.pack(
        side = tk.LEFT,
        pady = 5,
        padx = 10
    )
    scrollbox.pack(
        side = tk.BOTTOM,
        pady = 5,
        padx =5
    )

    root.mainloop()
    encryptor.encrypt(file_path)
