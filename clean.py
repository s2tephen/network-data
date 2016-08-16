"""
Removes duplicates, inverted connections, and self-connections
from network data, effectively making it an undirected graph.

Assumes your file has a header row.

Usage: $ python clean.py input.csv output.csv
"""
import csv, sys

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
  rows = csv.reader(input_file, delimiter=',')
  header = next(rows, None)
  cleaned_rows = []

  for row in rows:
    if row[0] != row[1]:
      row.sort()
      cleaned_rows.append(','.join(row))

  output_file.write(','.join(header) + '\n' + '\n'.join(list(set(cleaned_rows))))