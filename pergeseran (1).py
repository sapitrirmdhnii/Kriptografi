#!/usr/bin/python3
import tkinter as tk
import string

abjad = string.ascii_lowercase*2

class NewprojectApp:
    def __init__(self, master=None):
        # Build UI
        self.master = master
        self.master.title("Aplikasi Caesar Cipher")
        self.master.geometry("400x300")
        self.master.configure(bg="#E6E6E6")

        frame1 = tk.Frame(master, bg="#E6E6E6")
        frame1.pack(pady=20)

        label1 = tk.Label(frame1, text="Ketik Plaintext atau Chipertextnya:", bg="#E6E6E6")
        label1.pack()

        entry1 = tk.Entry(frame1, width=40)
        entry1.pack()

        label2 = tk.Label(frame1, text="Jumlah Pergeseran:", bg="#E6E6E6")
        label2.pack()

        entry2 = tk.Entry(frame1, width=40)
        entry2.pack()

        frame2 = tk.Frame(master, bg="#E6E6E6")
        frame2.pack(pady=10)

        button1 = tk.Button(frame2, text="Enkripsi", command=self.enkripsi, bg="#4CAF50", fg="white")
        button1.pack(side="left")

        button2 = tk.Button(frame2, text="Dekripsi", command=self.dekripsi, bg="#F44336", fg="white")
        button2.pack(side="right")

        frame3 = tk.Frame(master, bg="#E6E6E6")
        frame3.pack(pady=20)

        label3 = tk.Label(frame3, text="Hasil", bg="#E6E6E6")
        label3.pack()

        entry3 = tk.Entry(frame3, width=40)
        entry3.pack()

        self.entry1 = entry1
        self.entry2 = entry2
        self.entry3 = entry3

    def enkripsi(self):
        pesan = self.entry1.get()
        key = int(self.entry2.get())
        cipher = ''
        for i in pesan:
            if i in abjad:
                k = abjad.find(i.lower())
                k = (k + key) % 52
                cipher = cipher + abjad[k]
        self.entry3.delete(0, tk.END)
        self.entry3.insert(0, cipher)

    def dekripsi(self):
        cipher = self.entry1.get()
        key = int(self.entry2.get())
        pesan = ''
        for i in cipher:
            if i in abjad:
                k = abjad.find(i)
                k = (k - key) % 52
                pesan = pesan + abjad[k]
        self.entry3.delete(0, tk.END)
        self.entry3.insert(0, pesan)

if __name__ == "__main__":
    root = tk.Tk()
    app = NewprojectApp(root)
    root.mainloop()  # Ubah ini agar jendela berjalan dengan mainloop() pada root
