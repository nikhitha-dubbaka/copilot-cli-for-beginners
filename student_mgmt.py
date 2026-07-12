#!/usr/bin/env python3
"""Student Management System with JSON persistence.

Features:
- Add students
- View all students
- Search by name
- Update a student's marks
- Delete a student
- Save data to students.json
- Load data from students.json on start

Run interactively: python student_mgmt.py
Run demo: python student_mgmt.py --demo
"""
import json
import argparse
import os
import sys
from typing import List, Dict, Optional

DATA_FILE = "students.json"


def load_students(filename: str = DATA_FILE) -> List[Dict]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"Warning: could not read {filename}, starting with empty data")
        return []


def save_students(students: List[Dict], filename: str = DATA_FILE) -> None:
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(students, f, indent=2)
    except IOError as e:
        print(f"Error saving data: {e}")


def next_id(students: List[Dict]) -> int:
    if not students:
        return 1
    return max(s.get('id', 0) for s in students) + 1


def add_student(students: List[Dict], name: str, marks: float) -> Dict:
    student = {'id': next_id(students), 'name': name, 'marks': marks}
    students.append(student)
    save_students(students)
    print(f"Added: {student}")
    return student


def view_students(students: List[Dict]) -> None:
    if not students:
        print("No students found.")
        return
    print("Students:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")


def search_students(students: List[Dict], query: str) -> List[Dict]:
    q = query.lower()
    results = [s for s in students if q in s['name'].lower()]
    if results:
        for s in results:
            print(f"Found: ID {s['id']} - {s['name']} (Marks: {s['marks']})")
    else:
        print("No matching students.")
    return results


def find_student_by_id(students: List[Dict], student_id: int) -> Optional[Dict]:
    for s in students:
        if s.get('id') == student_id:
            return s
    return None


def update_marks(students: List[Dict], student_id: int, new_marks: float) -> bool:
    s = find_student_by_id(students, student_id)
    if not s:
        print("Student not found.")
        return False
    s['marks'] = new_marks
    save_students(students)
    print(f"Updated: ID {s['id']} now has marks {s['marks']}")
    return True


def delete_student(students: List[Dict], student_id: int) -> bool:
    s = find_student_by_id(students, student_id)
    if not s:
        print("Student not found.")
        return False
    students.remove(s)
    save_students(students)
    print(f"Deleted student ID {student_id}")
    return True


def interactive():
    students = load_students()
    while True:
        print("\nStudent Management")
        print("1) Add student")
        print("2) View all students")
        print("3) Search by name")
        print("4) Update student's marks")
        print("5) Delete student")
        print("6) Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            name = input("Name: ").strip()
            marks_str = input("Marks: ").strip()
            try:
                marks = float(marks_str)
            except ValueError:
                print("Invalid marks. Use a number.")
                continue
            add_student(students, name, marks)
        elif choice == '2':
            students = load_students()
            view_students(students)
        elif choice == '3':
            q = input("Search name: ").strip()
            students = load_students()
            search_students(students, q)
        elif choice == '4':
            id_str = input("Student ID to update: ").strip()
            try:
                sid = int(id_str)
            except ValueError:
                print("Invalid ID")
                continue
            marks_str = input("New marks: ").strip()
            try:
                new_marks = float(marks_str)
            except ValueError:
                print("Invalid marks")
                continue
            students = load_students()
            update_marks(students, sid, new_marks)
        elif choice == '5':
            id_str = input("Student ID to delete: ").strip()
            try:
                sid = int(id_str)
            except ValueError:
                print("Invalid ID")
                continue
            students = load_students()
            delete_student(students, sid)
        elif choice == '6' or choice.lower() in ('exit', 'quit'):
            print("Goodbye")
            break
        else:
            print("Unknown choice")


def demo_sequence():
    # Remove existing file for clean demo
    if os.path.exists(DATA_FILE):
        try:
            os.remove(DATA_FILE)
        except OSError:
            pass
    students = load_students()
    print("Demo: adding students")
    add_student(students, "Alice", 85.0)
    add_student(students, "Bob", 92.5)
    add_student(students, "Charlie", 78.0)
    print("\nDemo: view all")
    view_students(load_students())
    print("\nDemo: search 'bo'")
    search_students(load_students(), 'bo')
    print("\nDemo: update Bob's marks (ID 2 -> 95)")
    update_marks(load_students(), 2, 95.0)
    print("\nDemo: view all after update")
    view_students(load_students())
    print("\nDemo: delete Alice (ID 1)")
    delete_student(load_students(), 1)
    print("\nDemo: final list")
    view_students(load_students())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Student Management System')
    parser.add_argument('--demo', action='store_true', help='run demo sequence')
    args = parser.parse_args()
    if args.demo:
        demo_sequence()
    else:
        try:
            interactive()
        except (KeyboardInterrupt, EOFError):
            print('\nExiting')
            sys.exit(0)
