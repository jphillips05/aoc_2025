import os
from dotenv import load_dotenv
import requests

load_dotenv()

here = os.path.dirname(os.path.abspath(__file__))


class DataFile:
    def __init__(self, year: str, day: str):
        self.create_directory(year)

        cookie = {"session": os.environ["AOC_SESSION"]}
        req = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookie
        )

        with open(os.path.join(here, f"./data/{year}/{day}.txt"), "w") as f:
            f.write(req.text)

    # create dir if not exists
    def create_directory(self, year: str):
        if not os.path.exists(os.path.join(here, f"./data/{year}")):
            os.makedirs(os.path.join(here, f"./data/{year}"))
