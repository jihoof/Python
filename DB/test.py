# import
from DB_module import *
from rich.console import Console
from rich.table import Table

# settings
db = client["school"]
students = db["students"]
console = Console()


# function
def find_grade(grade):
    return list(students.find({"grade": grade}))


def print_grade_table(grade, data):
    table = Table(
        title=f"Students with Grade {grade}",
        title_style="bold magenta",
        header_style="bold cyan",
        border_style="bright_blue"
    )

    # 컬럼 구조 — 학생 데이터 구조에 맞게 컬럼을 원하는대로 더 추가 가능
    table.add_column("Name", justify="left")
    table.add_column("Age", justify="center")
    table.add_column("Major", justify="left")
    table.add_column("Grade", justify="center")

    if not data:
        table.add_row("-", "-", "-", f"{grade} (No Data)")
    else:
        for s in data:
            table.add_row(
                str(s.get("name", "-")),
                str(s.get("age", "-")),
                str(s.get("major", "-")),
                str(s.get("grade", "-"))
            )

    console.print(table)
    console.print("\n")  # 줄 간격


# main
grades = ["A", "B", "C", "D", "E", "F"]

for g in grades:
    result = find_grade(g)
    print_grade_table(g, result)















