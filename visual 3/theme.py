import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010584")],
                           [sg.Text("Nama   : Yusuf Kamal Pasya")],
                           [sg.Text("Kelas  : 5P Reguler Banjarmasin")],
                           [sg.Text("Matkul :Pemrograman Visual 3")]],
                           size=(400,200))
window()
window.close()
