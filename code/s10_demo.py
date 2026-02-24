import re

text = "Call me at 617-555-1234. Or at 617-555-5678. dfasdfsfasdfsfdsf my phone is 617-555-1234. dfasdfsfasdfsfdsf my phone is 617-555-5678."

results = re.findall(r"\d{3}-\d{3}-\d{4}", text)
for phone in results:
    print(phone)
