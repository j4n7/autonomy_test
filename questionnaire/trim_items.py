import csv
import test_items as ti


print(ti.situations)

merged = []

for key, value in ti.situations.items():
    for n in range(12):
        if key == n:
            merged.append(value[:45])
            for item in ti.items[key]:
                merged.append(item[:45])
                merged.append('')

print(merged)


with open('trimmed_items.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in merged:
        writer.writerow([row])
