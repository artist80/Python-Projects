#!/usr/bin/env python3

import os
import datetime

class ExpenseTracker:
	def __init__(self, filename="expense.txt"):
		self.filename = filename

	def add_expense(self, category, amount, description=""):
		timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		entry = f"{timestamp} | {category} | {amount} | {description}\n"

		with open(self.filename, "a") as file:
			file.write(entry)

		print("Expense added successfully.")

	def view_expenses(self):
		try:
			with open(self.filename, "r") as file:
				expenses = file.readlines()
				if not expenses:
					print("No expenses recorded.")
				else:
					print("Expenses History:")
					for expense in expenses:
						print(expense, end="")
		except FileNotFoundError:
			print("No expenses recorded yet.")

# Example usage
expense_tracker = ExpenseTracker()

while True:
	print("\nExpense Tracker Menu:")
	print("1. Add Expense")
	print("2. View Expense")
	print("3. Exit")

	choice = input("Enter your choice (1/2/3): ")

	if choice == "1":
		category = input("Enter expense category: ")
		amount = float(input("Enter expense amount: "))
		description = input("Enter expense description (optional): ")
		expense_tracker.add_expense(category, amount, description)
	elif choice == "2":
		expense_tracker.view_expenses()
	elif choice == "3":
		print("Exiting Expense Tracker. GoodBye!")
		break
	else:
		print("Invalid choice. Please Enter 1, 2, or 3.")