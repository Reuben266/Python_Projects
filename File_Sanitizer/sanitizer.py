import re

find_ip = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
words_to_redact = ["failed", "Failed", "token", "Token"]

try:
  with open("sample_log.txt", "r") as file, open("cleaned_log.txt", "w") as output:
    count = 0
    for lines in file:
      for words in words_to_redact:
        if words in lines:
          count += 1
        line = lines.replace(words, "[REDACTED]")
        lines = re.sub(find_ip, "[REDACTED_IP]", line)
      output.write(lines)
  print(f"{count} REDACTED words")
except FileNotFoundError:
  print("File was not created")
