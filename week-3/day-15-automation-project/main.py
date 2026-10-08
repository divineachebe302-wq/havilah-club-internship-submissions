

# Day 15 - Python Automation Project
# Project: Report Generator
# Reads students.csv and writes a text summary of the scores.

import os
import csv  # Needed to read CSV files


# --- Configuration ---
# Build paths from the location of this file, so the program works
# no matter which folder the terminal is in.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_PATH = os.path.join(BASE_DIR, "data")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "output")
INPUT_FILE = "students.csv"
REPORT_FILE = "report.txt"


# --- Core Functions ---

def read_scores(file_path):
    """Read the CSV file and return a list of (name, score) tuples."""
    scores = []

    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # An empty file has no header, and a file without these columns can't be read
        if reader.fieldnames is None or "name" not in reader.fieldnames or "score" not in reader.fieldnames:
            raise ValueError("The CSV must have 'name' and 'score' columns.")

        for row in reader:
            name = (row["name"] or "").strip()
            raw_score = (row["score"] or "").strip()

            # Skip blank or non-numeric scores instead of crashing
            try:
                score = float(raw_score)
            except ValueError:
                print(f"Skipping row with invalid score: {row}")
                continue

            scores.append((name, score))

    return scores


def calculate_stats(scores):
    """Work out the count, average, highest, and lowest score."""
    values = [score for _, score in scores]

    return {
        "count": len(values),
        "average": sum(values) / len(values),
        "highest": max(values),
        "lowest": min(values),
    }


def write_report(stats, report_file):
    """Write the summary to a text file."""
    lines = [
        "Student Score Report",
        "====================",
        f"Number of records: {stats['count']}",
        f"Average score: {stats['average']:.2f}",
        f"Highest score: {stats['highest']}",
        f"Lowest score: {stats['lowest']}",
    ]

    with open(report_file, "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")


def process(input_path, output_path):
    """Run the full report: read the data, calculate the stats, and save the report."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Could not find the input file: {input_path}")

    scores = read_scores(input_path)

    if not scores:
        raise ValueError("No valid score records were found in the file.")

    stats = calculate_stats(scores)

    # Create the output folder if it doesn't exist yet
    os.makedirs(output_path, exist_ok=True)
    report_file = os.path.join(output_path, REPORT_FILE)
    write_report(stats, report_file)

    return report_file


# --- Main ---

def main():
    input_file = os.path.join(INPUT_PATH, INPUT_FILE)

    try:
        report_file = process(input_file, OUTPUT_PATH)
        print(f"Report saved to {report_file}")
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()