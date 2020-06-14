import PySimpleGUI as sg

def main():
    # All the stuff inside your window
    layout = [ [sg.Text('Type Your Name:'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]
    # Create the Window
    window = sg.Window('PySimpleGui Example', layout)
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        if event in ('Cancel', None):
            break
        elif event in ('OK'):
            # Open a Popup window to send a good message
            sg.Popup(f'Hello my dear friend {values[0]}!', title='Hello World!')
        else:
            break
    # Closing the window
    window.close()

if __name__ == '__main__':
    main()