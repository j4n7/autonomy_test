import sqlite3
import csv

# NUMBER OF SITUATIONS
n_sit = 12

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
items = cur.execute(
    """SELECT subject_id, situation_n, item_n, score, latency
       FROM questionnaire_item
       ORDER BY 1, 2, 3""")
ord_items = [row for row in items]

subject = cur.execute(
    """SELECT id, code, age, sex, civil_status, last_studies,
              occupation, home_city, home_country,
              current_city, postal_code, current_country,
              completed, total_time,
              pre_score, ano_score, het_score,
              soc_score, sov_score
       FROM questionnaire_subject
       WHERE code LIKE '%villegas%'
       ORDER BY 1""")

'''Make a row with all the items of a subject'''
inline_rows = []
new_row = []
row_id = None
for i, row in enumerate(ord_items):
    current_id = row[0]
    if current_id == row_id:
        row = list(row)
        del row[0]
        new_row += row
    elif current_id != row_id:
        row_id = current_id
        inline_rows.append(new_row)
        new_row = []
        new_row += list(row)
    if i + 1 == len(ord_items):
        inline_rows.append(new_row)
del inline_rows[0]

'''Delete situation and item number'''
items_rows = []
items_row = []
n = 0
short_row = []
for row in inline_rows:
    items_row.append(row[0])
    for v in row[1:]:
        short_row.append(v)
        n += 1
        if n == 4:
            items_row.extend([short_row[2], short_row[3]])
            n = 0
            short_row = []
    items_rows.append(items_row)
    items_row = []

'''
for i, v in enumerate(items_rows):
    print(inline_rows[i])
    print('Processed')
    print(v)
    print('')
'''

'''Create the final row with the subject and item data'''
data = []
for n in subject:
    for m in items_rows:
        if n[0] == m[0]:
            data.append(list(n) + m[1:])

'''Append "NA" when an empty string is found'''
for row in data:
    for i, v in enumerate(row):
        if v == '':
            row[i] = 'NA'

headers = ['id', 'code', 'age', 'sex', 'civil_status', 'last_studies',
           'occupation', 'home_city', 'home_country',
           'current_city', 'postal_code', 'current_country',
           'completed', 'total_time',
           'pre_score', 'ano_score', 'het_score',
           'soc_score', 'sov_score']

for v in range(n_sit):
    for n in range(5):
        headers.extend([str(v + 1) + '_' + str(n + 1) + 's',
                        str(v + 1) + '_' + str(n + 1) + 'l'])

with open('ordered_db.csv', 'w', newline='') as csv_f:
    writer = csv.writer(csv_f)
    writer.writerow(headers)
    writer.writerows(data)
