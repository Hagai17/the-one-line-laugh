"""Write one funny line to /output/entry.txt.

The line is a single line of at most 200 characters, on any subject, with a
real surprise at the end.
"""

import os

LINE = (
    "I've had a gym bag packed by the door since January; it is now the "
    "fittest thing I own."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
