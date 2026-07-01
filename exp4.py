from datetime import datetime

now = datetime.now()
formatted_time = now.strftime("%a %b %d : %Y, %I:%M %p IST")
print(formatted_time)
