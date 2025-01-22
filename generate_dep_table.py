#!/usr/bin/env python3

from gather_metadata import gather_metadata
from tabulate import tabulate

deps = gather_metadata()

table = [['Project', 'Creators']]
for project in deps:
    table.append([
        f"[{project['name']}]({project['url']})",
        ', '.join([f"[{member['name']}]({member['url']})" for member in project['members']])
    ])

print(tabulate(table, headers="firstrow", tablefmt="github"))
