"""
Using a fake robot as the receiver of messages.
"""

# DONE: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# DONE: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

import mqtt_remote_method_calls as com
import time
import tkinter
from tkinter import ttk


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)

    time.sleep(1)  # Time to allow the MQTT setup.

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=3, column=1)
    forward_button['command'] = lambda: (forward(left_speed_entry, right_speed_entry, mqtt_client))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=4, column=0)
    left_button['command'] = lambda: print("Left button")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=4, column=1)
    stop_button['command'] = lambda: (stop(mqtt_client))


    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=4, column=2)
    right_button['command'] = lambda: print("Right button")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=5, column=1)
    back_button['command'] = lambda: (back(left_speed_entry, right_speed_entry, mqtt_client))


    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=6, column=0)
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=7, column=0)
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=6, column=2)
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=7, column=2)
    e_button['command'] = lambda: exit()

    root.mainloop()


def forward(entry1, entry2, mqtt_client):
    print()
    l = entry1.get()
    r = entry2.get()
    mqtt_client.send_message("forward", [l, r])

def back(entry1, entry2, mqtt_client):
    print()
    l = entry1.get() * -1
    r = entry2.get() * -1
    mqtt_client.send_message("back", [l, r])

def stop(mqtt_client):
    mqtt_client.send_message("stop")




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()