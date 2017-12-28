s = "abcd"
s1 = "abcd"
print(type(s))
print(type(s1))


current_time = "18:29:01"
hours = int(current_time[:2])
minutes = int(current_time[3:5])
seconds = int(current_time[6:8])
print(type(hours))
total_seconds = hours*3600 + minutes*60+seconds
print(total_seconds)
time_lst = current_time.split(":")
print(time_lst[0])


s = "github"
print(s[:3])

print(s[3:])
print(s[-3:])
