"""
DETECT CHANGE
=============

This module detect all the change in a selected directory.

And execute a program chosen on saved changes. (Python, Ruby, C++)
"""

import time
import os
import subprocess
import sys
import pathlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pyfiglet import Figlet
from _purcent import Loader as __Loader
from _colors import Colors
from _menu import menu


os.system('cls' if os.name == 'nt' else 'clear')
f = Figlet(font='banner3-D', width=80)
print(f.renderText('Change'))
print(f.renderText('Detect'))
global language
language = menu(["python", "ruby", "c++"], "Choose the language you want to use:")
if language == "python":
    CMD = ["py", "python"]
elif language == "ruby":
    CMD = ["ruby", "ruby"]
elif language == "c++":
    CMD = input(f"{Colors.BOLD}Enter the compiler you want to use: {Colors.GREEN}( g++ | clang++ | ...) {Colors.END}")
    OPTION = input(f"{Colors.Bold}Enter compilation options you want to use: {Colors.GREEN}(None){Colors.END}").split(" ")
    if OPTION in ["none", "", " "]:
        OPTION = [""]
    OUTPUT_ATTRIBUTE = input(f"{Colors.BOLD}Enter the output attribute you want to use: {Colors.GREEN}(-o){Colors.END}")
    if OUTPUT_ATTRIBUTE in ["", " "]:
        OUTPUT_ATTRIBUTE = "-o"
    OUTPUT_FILE = input(f"{Colors.BOLD}Enter the output file you want to use: {Colors.GREEN}(out.exe){Colors.END}").lower()
    if OUTPUT_FILE in ["", " "]:
        OUTPUT_FILE = "out.exe"
else:
    print(f"❌ {Colors.BOLD}{Colors.RED}Wrong language{Colors.END}")
    sys.exit()

# Automatic detection of the root directory
BASE_DIR = pathlib.Path(__file__).parent.absolute().cwd()

FILE = input(f"{Colors.BOLD}Enter the file you want to watch the base directory\n|-> {BASE_DIR}... \n{Colors.END}")
THE_FILE = os.path.join(BASE_DIR, f'{FILE}')
# Check if the file's path is valid
if not os.path.isfile(THE_FILE) or THE_FILE == " " or THE_FILE == "":
    print(f"❌ {Colors.BOLD}{Colors.RED}File not found{Colors.END}")
    sys.exit()

if language in ["c++", "cpp"]:
    COMMAND_LIST = [CMD]
    COMMAND_LIST.extend(iter(OPTION))
    COMMAND_LIST.append(THE_FILE)
    COMMAND_LIST.append(OUTPUT_ATTRIBUTE)
    COMMAND_LIST.append(OUTPUT_FILE)


def __language_output():
    h = __Loader()
    h.run()
    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    if language in ["ruby", "rb"]:
        __ruby_output()
    elif language in ["python", "py", "python3"]:
        __python_output()
    elif language in ["c++", "cpp"]:
        __cpp_output()

def __cpp_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('C++'))
    print(f"{THE_FILE}")

def __python_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('Python'))
    print(f"{THE_FILE}")


def __ruby_output():
    custom_fig = Figlet(font='banner3-D')
    print(custom_fig.renderText('Ruby'))
    print(f"{THE_FILE}")

__language_output()

class _Watcher:
    DIRECTORY_TO_WATCH = BASE_DIR

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = _Handler()
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception:
            self.observer.stop()
            print ("Exiting program...")

        self.observer.join()


class _Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"{Colors.GREEN}{Colors.BOLD}+{Colors.END} {Colors.BOLD}Received created event - {event.src_path}.{Colors.END}")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if event.src_path == THE_FILE:
                print("O U T P U T")
                print("═══════════════════════════════════════════════════════════")
                if language != "c++":
                    now = time.perf_counter()
                    cm = ''
                    cm = CMD[0] if os.name == 'nt' else CMD[1]
                    subprocess.call([cm, f'{THE_FILE}'])
                    end = time.perf_counter()
                else:
                    now = time.perf_counter()
                    subprocess.call(COMMAND_LIST)
                    end = time.perf_counter()
                    print(f"{Colors.GREEN}{Colors.BOLD}COMPLILATON COMPLETED{Colors.END}")
                print("═══════════════════════════════════════════════════════════")
                print(f"{Colors.PURPLE}{Colors.BOLD}{end - now}s{Colors.END}")
                # get the time of execution

                print(" ")
                print("---")
                print(f"✅ {Colors.GREEN}{Colors.BOLD}Listening for changes...{Colors.END}")
            elif event.src_path == f'{BASE_DIR}\detectchange.py':
                print(f"❗{Colors.RED}{Colors.BOLD}RESTART THE PROGRAM FOR APPLY CHANGES{Colors.END}❗")
            else:
                print(f"{Colors.GREEN}{Colors.BOLD}+{Colors.END} Received modified event - {event.src_path}.")
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print(f"{Colors.RED}{Colors.BOLD}-{Colors.END} Received deleted event - {event.src_path}.")


def activate() -> None:
    """
    Detect change in the Root directory and execute the program chosen.
    ```python
    from changedetector import detectchange
    detectchange.activate()
    ```
    """
    w = _Watcher()
    print(" ")
    print("👀 Watching...")
    print(" ")
    w.run()

if __name__ == '__main__':
    activate()
    sys.exit()
