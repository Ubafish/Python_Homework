import os
import csv

csvpath = "PyBank/Resources/budget_data.csv"

total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_changes = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_profit_loss += int(first_row[1])
    prev_profit_loss = int(first_row[1])

    rows = list(csvreader)

    for i in range(len(rows)):

        total_months += 1

        total_profit_loss += int(rows[i][1])

        profit_loss_change = int(rows[i][1]) - prev_profit_loss
        prev_profit_loss = int(rows[i][1])

        profit_loss_changes.append(profit_loss_change)

    average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

    greatest_increase = max(profit_loss_changes)
    greatest_increase_date = str(rows[profit_loss_changes.index(greatest_increase) + 1][0])

    greatest_decrease = min(profit_loss_changes)
    greatest_decrease_date = str(rows[profit_loss_changes.index(greatest_decrease) + 1][0])

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_folder = "PyBank/analysis"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, "financial_analysis.txt")

with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")