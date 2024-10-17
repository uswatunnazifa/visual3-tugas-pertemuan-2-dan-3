import PySimpleGUI as sg

sg.theme_text_color('#292d32')
texts = [
    [sg.Text("SELAMAT DATANG DI KELAS 5O",font=("Arial",25,"italic","bold","underline"))],
    [sg.Text("NPM : 2210010717")],
    [sg.Text("Nama : Uswatun")],
    [sg.Text("Kelas : TI O Reguler Banjarmasin")],
    [sg.Text("Matkul : Visual 3")]
]

window = sg.Window(title='Latihan Pertama', layout=texts, size=(600, 300), font=('Georgia', 20))
window()
window.close()