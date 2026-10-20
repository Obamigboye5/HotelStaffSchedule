import pandas as pd
from datetime import datetime
import calendar

# Staff names
staff = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Frank", "Grace", "Henry", "Isabella", "Jack"
]

# Year and month
year = 2026
month = 11

# Shift pattern
shifts = ["Morning", "Evening", "Night", "Off"]

# Get number of days in November
num_days = calendar.monthrange(year, month)[1]

# Create schedule
schedule = {}

for day in range(1, num_days + 1):
    day_schedule = []
    for i, employee in enumerate(staff):
        shift = shifts[(day + i) % len(shifts)]
        day_schedule.append(shift)
    schedule[f"Nov-{day:02d}"] = day_schedule

# Create DataFrame
df = pd.DataFrame(schedule, index=staff)

# Save to Excel
output_file = "Hotel_Staff_Schedule_November.xlsx"
df.to_excel(output_file)

print(f"Schedule saved to {output_file}")
print(df.head())