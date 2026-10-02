# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.


import csv

INPUT_FILE = "students.csv"
OUTPUT_FILE = "top_students_sorted.csv"
PASS_MARK = 90


# Exercise 1: Create the dataset 
def create_dataset(path):
    rows = [
        ["name", "score", "department", "age"],
        ["  Alice Johnson ", "85", "Computer Science", "20"],
        ["bob smith", "72", "Engineering", "22"],
        [" CHIOMA OKAFOR", "91", "Computer Science", "21"],
        ["David Eze ", "58", "Business", "23"],
        ["Emeka Nwosu", "67", "Engineering", "20"],
        ["  fatima bello", "94", "Medicine", "22"],
        ["Grace Adeyemi ", "45", "Business", "24"],
        ["HASSAN YUSUF", "78", "Computer Science", "21"],
        ["Ifeoma Obi", "88", "Medicine", "20"],
        ["  John Doe", "62", "Engineering", "23"],
        ["Kemi Balogun ", "74", "Business", "22"],
        ["LUCY AMADI", "99", "Computer Science", "21"],
        ["Musa Ibrahim", "53", "Engineering", "24"],
        ["  Ngozi Eze", "81", "Medicine", "20"],
        ["Obinna Kalu ", "69", "Business", "23"],
        ["PATRICK OKON", "90", "Computer Science", "22"],
        ["Queen Ojo", "76", "Medicine", "21"],
        ["  Rita Umeh", "49", "Engineering", "24"],
        ["Samuel Ade ", "83", "Business", "20"],
        ["TOLA AKINS", "95", "Computer Science", "22"],
        ["Uche Nnamdi", "71", "Engineering", "21"],
    ]
    with open(path, "w", newline="", encoding="utf-8") as file:
        csv.writer(file).writerows(rows)


# Exercise 2: Read the dataset into a list of dictionaries
def read_dataset(path):
    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


# Exercise 3: Clean text fields and convert score/age to numbers
def clean_data(rows):
    cleaned = []
    for row in rows:
        cleaned.append({
            "name": row["name"].strip().title(),
            "score": float(row["score"]),
            "department": row["department"].strip().title(),
            "age": int(row["age"]),
        })
    return cleaned


# Exercise 4: Summary of the numeric column (score)
def summarise(rows, column="score"):
    values = [row[column] for row in rows]
    return {
        "total_records": len(values),
        "minimum": min(values),
        "maximum": max(values),
        "average": sum(values) / len(values),
    }


# Exercise 5: Filter records that satisfy a condition
def filter_records(rows, min_score):
    return [row for row in rows if row["score"] >= min_score]


# Exercise 6: Sort and save results with csv.DictWriter
def save_results(rows, path):
    sorted_rows = sorted(rows, key=lambda r: r["score"], reverse=True)
    fieldnames = ["name", "score", "department", "age"]
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)
    return sorted_rows


# Exercise 7: main() organises the whole data-processing workflow
def main():
    create_dataset(INPUT_FILE)
    print(f"Created dataset: {INPUT_FILE}")

    raw_rows = read_dataset(INPUT_FILE)
    print(f"Read {len(raw_rows)} records\n")

    students = clean_data(raw_rows)

    summary = summarise(students)
    print("=== Data Summary (score) ===")
    print(f"Total records: {summary['total_records']}")
    print(f"Minimum score: {summary['minimum']}")
    print(f"Maximum score: {summary['maximum']}")
    print(f"Average score: {summary['average']:.2f}\n")

    passed = filter_records(students, PASS_MARK)
    print(f"=== Students with score >= {PASS_MARK} ({len(passed)} found) ===")
    for s in passed:
        print(f"{s['name']:<18} {s['score']:>5.1f}  {s['department']}")

    sorted_rows = save_results(passed, OUTPUT_FILE)
    print(f"\nSaved {len(sorted_rows)} sorted records to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()