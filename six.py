"""
Write a function which is given an exam mark,
and it returns a string — the grade for that mark —
according to this scheme:

Mark    Grade

>= 90   Great
[80-90) Good
[70-80) OK
[60-70) Fair
[50-60) Needs Help
<50     Failing

The square and round brackets denote closed and open intervals.
A closed interval includes the number, and open interval excludes it.
So 49.99999 gets grade Failing, but 50 gets grade Needs Help. Assume:

grade_list = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


Test your function by printing the mark and the grade for all the elements in this list.
"""
def mark_to_grade(num):
    if num >= 90:
        return("Great")
    elif num >= 80 and num < 90:
        return "Good"
    elif num >= 70 and num<80:
        return "OK"
    elif num>=60 and num<70:
        return "Fair"
    elif num >= 50 and num<60:
        return "Needs Help"
    elif num<50:
        return "Failing"
grade_list = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in grade_list:
    print(mark_to_grade(i))