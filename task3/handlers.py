from collections import defaultdict
from colorama import Fore, Style
from datetime import datetime as dt
from tabulate import tabulate

def parse_log_line(line: str) -> dict:
        try:
            data=line.split()
            gold_data = {
                'date': dt.strptime(data[0], "%Y-%m-%d").date(),
                'time': dt.strptime(data[1], "%H:%M:%S").time(),
                'level': data[2],
                'message': " ".join(data[3:])
            }
            return gold_data
        except Exception as e:
            print(e)
            return {}

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file: return [parse_log_line(line) for line in file]
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def filter_logs_by_level(logs: list, level: str) -> list: return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    count_logs = defaultdict(int)
    for log in logs: count_logs[log['level']] += 1
    return count_logs.items()

def display_log_counts(counts: dict):
    data = [(colorize(key), value) for key, value in counts]

    print(tabulate(data, headers=["Рівень логування", "Кількість"], tablefmt="grid"))

def colorize(text:str) -> str:
    colors = {
        "ERROR": Fore.RED,
        "WARNING": Fore.YELLOW,
        "INFO": Fore.GREEN,
        "DEBUG": Fore.BLUE
    }
    return colors.get(text, "") + text + Style.RESET_ALL
