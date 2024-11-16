# AdventOfCode
My Personal Solutions for the Advent of Code event every year in december.

Advent of Code:
https://adventofcode.com/

## Setup

Rename session-cookie-template.txt as session-cookie.txt and put your advent of code session cookie in the file.

## Solve a day

You can create a folder for a specific day and year, download the input for that day and create template python scripts for part 1 and 2.
```bash
python helper/create-day.py <year> <day> [<no-dl>]
```
With year and day replaced by the year and day you want to solve respectively.
no-dl is optional and, if any value is provided, the script will not use the session cookie to download your input.