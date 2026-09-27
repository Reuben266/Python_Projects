try:
  with open("Bugrepots.txt", "r") as file, open("cleaned_reports.txt", "w") as cleaned_reports:
    count = 0
    sensitive_words = ["Warning", "Skipping", "null"]
    for line in file:
      for word in sensitive_words:
        if word in line:
          lines  = line.replace(word, "[Redacted]")
          cleaned_reports.write(lines)
except FileNotFoundError:
  print("file not found")