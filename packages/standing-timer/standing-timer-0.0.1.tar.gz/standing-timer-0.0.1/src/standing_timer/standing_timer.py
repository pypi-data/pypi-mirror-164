#!/usr/bin/env python

import PySimpleGUI as sg
import time
from datetime import datetime
from tinydb import TinyDB, Query
from config import write_auth_config, has_auth_token, config


def time_as_int():
    return int(round(time.time() * 100))


def today():
    return datetime.now().strftime("%Y-%m-%d")


def main():
    sg.theme("Black")

    layout = [
        [sg.Text("")],
        [
            sg.Text(
                "",
                size=(6, 2),
                font=("Helvetica", 20),
                justification="center",
                key="text",
            )
        ],
        [
            sg.Button("Stand Up", key="-RUN-PAUSE-", button_color=("white", "#001480")),
            sg.Button("Reset", button_color=("white", "#007339"), key="-RESET-"),
            sg.Exit(button_color=("white", "firebrick4"), key="Exit"),
        ],
    ]

    window = sg.Window(
        "Standing Timer",
        layout,
        no_titlebar=True,
        auto_size_buttons=False,
        keep_on_top=True,
        grab_anywhere=True,
        element_padding=(0, 0),
        finalize=True,
        element_justification="c",
    )

    current_time, paused_time, paused = 0, 0, True
    start_time = None
    segments = []
    last_start_time = None

    while True:
        if not paused:
            event, values = window.read(timeout=10)
            current_time = time_as_int() - start_time
        else:
            event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "-RESET-":
            paused_time = start_time = time_as_int()
            current_time = 0
            segments = []
            paused = True
            window["-RUN-PAUSE-"].update("Stand Up" if paused else "Sit Down")
        elif event == "-RUN-PAUSE-":
            paused = not paused
            if paused:
                paused_time = time_as_int()
                segments.append(time_as_int() - last_start_time)
            else:
                start_time = (
                    time_as_int()
                    if not start_time
                    else start_time + time_as_int() - paused_time
                )
                last_start_time = time_as_int()
            # Change button's text
            window["-RUN-PAUSE-"].update("Stand Up" if paused else "Sit Down")
        # --------- Display timer in window --------
        window["text"].update(
            "{:02d}:{:02d}".format(
                (current_time // 100) // 60,
                (current_time // 100) % 60,
                current_time % 100,
            )
        )

    if not paused:
        segments.append(time_as_int() - last_start_time)

    db = TinyDB("standing-timer.json")

    Search = Query()
    prev_query = db.search(Search.date == today())

    if len(prev_query):
        prev = prev_query[0]
        print(prev)
        db.update(
            {
                "standing_time": prev["standing_time"] + current_time,
                "segments": prev["segments"] + segments,
            },
            Search.date == today(),
        )
    else:
        db.insert(
            {"date": today(), "standing_time": current_time, "segments": segments}
        )

    window.close()


if __name__ == "__main__":
    token = ""

    if not has_auth_token():
        while token.strip() == "":
            token = input("Please enter your auth token:")

    server_url = input(
        "Please enter your custom server url if applicable (default StandingTimer prod):"
    )

    write_auth_config(token, server_url)

    main()
