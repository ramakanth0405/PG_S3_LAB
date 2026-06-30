raw_text_file_lines = [
    "10:00:01 INFO - Gateway connection established,",
    "10:00:05 CRITICAL - Temperature sensor disconnected!",
    "10:00:12 INFO - System memory status normal",
    "10:00:22 CRITICAL - Voltage dropped below 11V!"
]


critical_errors = []

# Loop through the text file line by line 
for line in raw_text_file_lines:
    if "CRITICAL" in line:
        cleaned_line = line.strip()
        critical_errors.append(cleaned_line)

print("Parsed Critical Incidents: ")
print(critical_errors)