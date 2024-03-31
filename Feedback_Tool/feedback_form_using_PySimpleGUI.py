import PySimpleGUI as psg

#set the theme for the screen/window
psg.theme('TealMono')

#define layout
layout=[[psg.Text('Choose your Bread',size=(20, 1), font='Lucida',justification='left')],
        [psg.Radio('Whole Wheat','rd_bread', key ='Whole Wheat'), psg.Radio('Multigrain','rd_bread', key='Multigrain'),
         psg.Radio('Normal','rd_bread', key='Normal'),psg.Radio('Stuffed','rd_bread', key='Stuffed'),psg.Radio('Healthy seeds','rd_bread', key='Healthy seeds')],
        [psg.Text('Choose your Toppings',size=(20, 1), font='Lucida',justification='left')],
        [psg.Checkbox('Pepperoni',key='Pepperoni'), psg.Checkbox('Mushroom',key='Mushroom'),
         psg.Checkbox('Corn',key='Corn'),psg.Checkbox('Cherry Tomatoes',key='Cherry Tomatoes'),psg.Checkbox('Olives',key='Olives')],
        [psg.Text('Choose your Sauces',size=(20, 1), font='Lucida',justification='left')],
        [psg.Checkbox('Onion',key='Onion Sauce'), psg.Checkbox('Paprika',key='Paprika'),
         psg.Checkbox('Schezwan',key='Schezwan'),psg.Checkbox('Tandoori',key='Tandoori')],
        [psg.Button('SAVE', font=('Times New Roman',12)),psg.Button('CANCEL', font=('Times New Roman',12))]]

#Define Window
win =psg.Window('Make your Pizza',layout)

#Read  values entered by user
e,v=win.read()

#close first window
win.close()

#access all the values and if selected add them to a string
strx=""
for val in v:
    if win[val].get() == True:
        strx = strx + " " + val + ","

#display string in a popup
psg.popup('Custom Pizza',      
            'Your chosen pizza will be made with', strx[0:len(strx)-1]) 
