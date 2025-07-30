import json
import re

with open('data/knowledge_base.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data:
    definition = entry['definition']
    if len(definition) < 50:
        print(f"Short definition found: {entry['term']}")
    if not re.match(r'^[A-Z].*\.$', definition):
        print(f"Potential punctuation/capitalization issue: {entry['term']}")
