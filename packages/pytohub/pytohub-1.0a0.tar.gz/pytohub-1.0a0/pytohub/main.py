import os
import time
import subprocess
import requests
import urllib.request
import tkinter.filedialog as fbox
import tkinter.messagebox as box
from .legohub import listallports, hubconnection
from .menu import main_menu, second_menu, options_menu
from getkey import getkey, keys
import progressbar

pbar = None
conn = None
processes = {}
ports = []
retry = False
hub = None


def clear():
    os.system("cls" if os.name == "nt" else "clear")


class textcolors:
    """ANSI color codes"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    BROWN = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    LIGHT_YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"


def print_text_logo():
    print(
        """ ______   __  __     ______   ______     __  __     __  __     ______    
/\  == \ /\ \_\ \   /\__  _\ /\  __ \   /\ \_\ \   /\ \/\ \   /\  == \   
\ \  _-/ \ \____ \  \/_/\ \/ \ \ \/\ \  \ \  __ \  \ \ \_\ \  \ \  __<   
 \ \_\    \/\_____\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\ 
  \/_/     \/_____/     \/_/   \/_____/   \/_/\/_/   \/_____/   \/_____/                                                                      
"""
    )


class log:
    def fatul(text, exitcode=1):
        print(
            textcolors.RED
            + textcolors.BOLD
            + "[FATUL] "
            + text
            + " ("
            + str(exitcode)
            + ")"
            + textcolors.END
        )
        exit(exitcode)

    def error(text):
        print(textcolors.RED + "[ERROR] " + text + textcolors.END)

    def warning(text):
        print(textcolors.YELLOW + "[WARNING] " + text + textcolors.END)

    def success(text):
        print(textcolors.GREEN + "[SUCCESS] " + text + textcolors.END)

    def successblue(text):
        print(textcolors.BLUE + "[SUCCESS] " + text + textcolors.END)

    def successcyan(text):
        print(textcolors.CYAN + "[SUCCESS] " + text + textcolors.END)

    def log(text):
        print("[INFO] " + text)


def findhub():
    o = 0
    ports = listallports()
    if ports == []:
        log.warning("There is no hubs connected to this computer.")
        print("Start the program on the hub before running PYToHub to list the hub")
        log.fatul("Terminated", exitcode=1)
    elif len(ports) == 1:
        print(
            "There is only one hub connected to this computer do you want to connect it (Y/n)"
        )

    while True:
        clear()
        print("Please select one of your hubs below")
        print("↑↑↑")
        print(ports[o])
        print("↓↓↓")
        print()
        print(f"{o + 1} out of {len(ports)}")
        print()
        print("Navigate using UP/DOWN arrow keys")
        print("Press Q to exit program")
        key = getkey()
        if key == keys.UP:
            if not o == len(ports) - 1:
                o += 1
        elif key == keys.DOWN:
            if not o == 0:
                o -= 1
        elif key == keys.ENTER:
            clear()
            return ports[o]
        elif key == "q":
            exit()
        else:
            pass


def tryconnect(r):
    global hub, retry
    for i in range(11):
        if i == 10:
            log.error("Failed to connect to hub (Maybe you disconnected it?)")
            log.fatul("Terminated", exitcode=1)

        log.log("Connecting...")
        try:
            if retry == False:
                hub = hubconnection(r)

            if hub.send_ping(None) == None:
                log.warning("No data. retrying...")
            else:
                log.success("Connected")
                time.sleep(1)
                log.log("Loading main menu...")
                break
        except Exception as e:
            log.error(f"An error occurred ({e}). Retrying...")


def start_main_menu():
    while True:
        out = main_menu()
        if out[1] == 0:
            log.log("Restarting hub Please wait...")
            hub.send_command("end_conn", [])
            log.success("Command sent")
            log.log(
                "Your hub will restart because if you uploaded data to it changes directorys and glitches the hub"
            )
            exit()
        elif out[1] == 2:
            while True:
                out2 = second_menu("Manage", options=["View mods", "Delete mods"])
                if out2[1] == 1:
                    break
                elif out2[2] == 2:
                    pass
                elif out2[3] == 3:
                    pass
                else:
                    pass
        else:
            pass


def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        widgets = [
            progressbar.Percentage(),
            " ",
            progressbar.ETA(),
            " ",
            textcolors.YELLOW,
            textcolors.BOLD,
            progressbar.Bar(marker="#", left="[", right="]"),
            textcolors.END,
        ]
        pbar = progressbar.ProgressBar(maxval=total_size, widgets=widgets)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None


def download(file, url):
    urllib.request.urlretrieve(url, file, show_progress)


def download_program():
    clear()
    print(
        textcolors.BOLD
        + textcolors.PURPLE
        + "PYToHub is made by @mas6y6 on github\n"
        + textcolors.END
    )
    time.sleep(3)
    print("Loading download menu")
    h = options_menu(
        menuname="Download selection",
        desc="Please pick the lego hub that you are currently using",
        options=[
            "LEGO 45678 Education Spike Prime Hub",
            "LEGO 51515 MINDSTORMS Robot Inventor hub",
        ],
        include_exit=True,
    )
    if h[1] == 0:
        log.log("Requesting where to download...")
        dir = fbox.askdirectory()
        log.log(f"Selected {dir}")
        log.log("Downloading...")
        download(
            f"{dir}/PYToHub.llsp",
            "https://github.com/mas6y6/PyToHub-assets/raw/main/PYToHub.llsp",
        )
        log.success("Downloaded")
    elif h[1] == 1:
        log.log("Requesting where to download...")
        dir = fbox.askdirectory()
        log.log(f"Selected {dir}")
        log.log("Downloading...")
        download(
            f"{dir}/PYToHub.lms",
            "https://github.com/mas6y6/PyToHub-assets/raw/main/PYTohub.lms",
        )
        log.success("Downloaded")
    else:
        log.fatul("Unknown error")


def run():
    global hub
    clear()
    print(
        textcolors.BOLD
        + textcolors.PURPLE
        + "PYToHub is made by @mas6y6 on github\n"
        + textcolors.END
    )
    time.sleep(3)
    while True:
        if not hub == None:
            start_main_menu()
        r = findhub()
        tryconnect(r)
