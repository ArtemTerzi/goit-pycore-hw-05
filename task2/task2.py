from typing import Generator, Union
import re

def generator_numbers(text: str) -> Generator[Union[int,float], None, None]:
    pattern = r"-?\d+(\.\d+)?"
    for match in re.finditer(pattern, text):
        yield (float(match.group()) if '.' in match.group() else int(match.group()) )

def sum_profit(text: str, func: Generator): return sum(x for x in func(text))

if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, \
        доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    gen = generator_numbers(text)
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")