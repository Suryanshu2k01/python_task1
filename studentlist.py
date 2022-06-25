def numbers(students):
    list = []
    for i in range(len(students)):
        for j in range(len(students[i])):
            list.append(students[i][j])
            
            num = {}
            for elements in list:
                num = {elements:list.count(elements) for elements in list}
                return num

def popular(num):
    popular_course = max(num, key = num.get)
    return popular_course

students = [['math', 'phy', 'chem', 'cs'], ['math', 'phy'], ['math', 'chem'], ['history', 'eco']]    
n = numbers(students)
print(n)
p = popular(n)
print("The course done by most students is:", p)


