import PySimpleGUI as sg
import os
import pandas as pd
import re

#set the theme for the screen/window
sg.theme('TealMono')

#define layout
layout=[[sg.Text('Please fill the feedback form')],
        [sg.Text('Name', size=(25, 1)), sg.InputText()],
        [sg.Text('Question 1', size=(25, 1), justification='left')],
        [sg.Radio('Not Accurate', 'Sleep scale', key='Not Accurate'),
         sg.Radio('Low Accuracy', 'Sleep scale', key='Low Accuracy'),
         sg.Radio('Reasonable Accuracy', 'Sleep scale',key='Reasonable Accuracy'),
         sg.Radio('Good Accuracy', 'Sleep scale', key='Good Accuracy'),
         sg.Radio('Highly Accurate', 'Sleep scale', key='Highly Accurate')],
        [sg.Text('Question 2', size=(25, 1), justification='left')],
        [sg.Radio('Not Accurate', 'Fatigue scale', key='Not Accurate'),
         sg.Radio('Low Accuracy', 'Fatigue scale', key='Low Accuracy'),
         sg.Radio('Reasonable Accuracy', 'Fatigue scale', key='Reasonable Accuracy'),
         sg.Radio('Good Accuracy', 'Fatigue scale', key='Good Accuracy'),
         sg.Radio('Question 3', 'Fatigue scale', key='Highly Accurate')],
        [sg.Text('How accurate was the Stress scale reading ?', size=(25, 1), justification='left')],
        [sg.Radio('Not Accurate', 'Stress scale', key='Not Accurate'),
         sg.Radio('Low Accuracy', 'Stress scale', key='Low Accuracy'),
         sg.Radio('Reasonable Accuracy', 'Stress scale', key='Reasonable Accuracy'),
         sg.Radio('Good Accuracy', 'Stress scale', key='Good Accuracy'),
         sg.Radio('Highly Accurate', 'Stress scale', key='Highly Accurate')],
        [sg.Text('Question 4', size=(25, 1), justification='left')],
        [sg.Radio('Not Accurate', 'Eye tracking', key='Not Accurate'),
         sg.Radio('Low Accuracy', 'Eye tracking', key='Low Accuracy'),
         sg.Radio('Reasonable Accuracy', 'Eye tracking', key='Reasonable Accuracy'),
         sg.Radio('Good Accuracy', 'Eye tracking', key='Good Accuracy'),
         sg.Radio('Highly Accurate', 'Eye tracking', key='Highly Accurate')],
        [sg.Text('Question 5', size=(25, 1), justification='left')],
        [sg.Radio('Not Accurate', 'facial features', key='Not Accurate'),
         sg.Radio('Low Accuracy', 'facial features', key='Low Accuracy'),
         sg.Radio('Reasonable Accuracy', 'facial features', key='Reasonable Accuracy'),
         sg.Radio('Good Accuracy', 'facial features', key='Good Accuracy'),
         sg.Radio('Highly Accurate', 'facial features', key='Highly Accurate')],
        [sg.Text('Comments', size=(25, 1)), sg.InputText()],
        [sg.Button('Submit', font=('Times New Roman',12)),sg.Button('CANCEL', font=('Times New Roman',12))]]

window = sg.Window('XYZ Feedback', layout, finalize=True, size=(700, 500))
# prompt = window['Status'].update
input_key_list = [key for key, value in window.key_dict.items() if isinstance(value, sg.Input)]
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Submit":
        collect_ans = []
        for each_key in values:
            if window[each_key].get() == True:
                output = re.sub(r'\d+', '', each_key)
                collect_ans.append(output)
        if len(collect_ans) != 5:
            sg.popup('XYZ Team', 'Some checkbox are not filled!')
        else:
            if all(map(str.strip, [values[key] for key in input_key_list])):
                break
            else:
                sg.popup('XYZ Team', 'Some inputs missed')
window.close()

# print("values", values)
if values!=None:
    in_list = [["Name", window[0].get()],
               ["Question 1", collect_ans[0]],
               ["Question 2", collect_ans[1]],
               ["Question 3", collect_ans[2]],
               ["Question 4", collect_ans[2]],
               ["Question 5", collect_ans[2]],
               ["Comments", window[1].get()]]

    out_list = pd.DataFrame(in_list)
    pd.set_option('display.max_columns', 500)
    out_list.to_csv(os.path.join(os.getcwd(), 'Output/survey.csv'), index=False, header=False)
