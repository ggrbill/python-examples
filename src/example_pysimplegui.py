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
        if event == 'OK':
            # Open a Popup window to send a good message
            sg.Popup(f'Hello my dear friend {values[0]}!', title='Hello World!')
        elif event == 'Cancel':
            # Open a Popup window to send a message and close window
            sg.Popup(f'Good bye my friend!', title='Bye')
            break
        else:
            break
    # Close window
    window.close()

if __name__ == '__main__':
    main()