import sys
from pathlib import Path
from handlers import *

def main():
    try:
        file_path = Path(sys.argv[1]).absolute()
        read_level = str(Path(sys.argv[2])).upper()
        logs = load_logs(file_path)
        log_levels = [key for key,value in count_logs_by_level(logs)] 

        display_log_counts(count_logs_by_level(logs))
        
        if read_level in log_levels:
            print()
            filtered_logs = filter_logs_by_level(logs, read_level) 
            print(f'Деталі логів для рівня \'{colorize(read_level)}\':')
            for log in filtered_logs:
                string = " ".join([
                    log['date'].strftime('%Y-%m-%d'),
                    log['time'].strftime('%H:%M:%S'),
                    '-', log['message']
                ])
                print(string)
        else:
            raise ValueError(f'Invalid input: {read_level} is missing from the log level list')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()