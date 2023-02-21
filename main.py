import datetime

today = datetime.datetime.today()

print(f"-- TODAY: {today} --")

with open("log.txt", "a") as file:
  file.write(f"{today}/n")
  
print("-- LOG UPDATED SUCCESSFULLY --")
