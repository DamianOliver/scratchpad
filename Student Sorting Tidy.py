import random as rand
from statistics import median

student_list = []
num_students = 10
class_size = 30


class Student:
    def __init__(self, name, ethnicity, english_skill, academic_skill, age):
        self.name = name
        self.ethnicity = ethnicity
        self.english_skill = english_skill
        self.academic_skill = academic_skill
        self.age = age

def generate_ethnicity():
    ethnicity_list = ["Native", "African", "Hispanic", "Asian", "White"]
    return ethnicity_list[rand.randrange(0, len(ethnicity_list))]

def generate_english_skill():
    possible_skills_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    return(possible_skills_list[rand.randrange(0, len(possible_skills_list))])

def generate_acedemic_skill():
    return rand.randrange(7, 9)

def generate_age():
    possible_skills_list = [11, 12, 12, 12, 13, 13, 13, 15, 15]
    return possible_skills_list[rand.randrange(0, len(possible_skills_list))]

def generate_name(ethnicity):
    if ethnicity == "Native":
        names_list = ["Aiyana", "Aponi", "Catori", "Dyani", "Elu", "Enola", "Halona", "Istas", "Kasa", "Kateri", "Kimi", "Lomasi", "Maji", "Mitena", "Na'estse", "Odina", "Orenda", "Pavati", "Sakari",\
            "Adriel", "Ahanu", "Alo", "Anakin", "Calian", "Dakota", "Denali", "Hopi", "Jacy", "Jalen", "Kai", "Kele", "Kosumi", "Mato", "Mika", "Nahele", "Nodin", "Nayati", "Nova", "Nuka", "Takoda"]

    elif ethnicity == "African":
        names_list = ["Abeba", "Aberash", "Ada", "Amara", "Ayaan", "Chidinma", "Cleopatra", "Gugulethu", "Hadiza", "Hibo", "Imani", "Kenya", "Makena", "Masego", "Nala", "Nia", "Ola", \
            "Onika", "Sade", "Taraji", "Zendaya", "Zola", "Zuri", "Aadan", "Abdalla", "Abidemi", "Amari", "Bamidele", "Chima", "Chiumbo", "Diallo", "Faraji", "Femi", "Idir", "Ike", "Imamu", \
            "Jabari", "Kamari", "Kofi"]

    elif ethnicity == "Hispanic":
        names_list = ["Sofia", "Isabella", "Camila", "Valentina", "Valeria", "Mariana", "Luciana", "Daniela", "Gabriela", "Victoria", "Martina", "Lucia", "Ximena", "Sara", "Samantha", \
            "Maria", "Emma", "Catalina", "Julieta", "Mia", "Antonella", "Santiago", "Sebastian", "Matias", "Mateo", "Nicolas", "Alejandro", "Diego", "Samuel", "Benjamin", "Daniel", "Joaquin", \
            "Lucas", "Tomas", "Gabriel", "David", "Emiliano"]

    elif ethnicity == "Asian":
        names_list = ["Aiguo", "Aki", "Akeno", "Chung", "Dae", "Dalip", "Jin", "Feng", "Han", "Hiromi", "Isamu", "Jiang", "Kaede", "Kane", "Keitaro", "Kenshin", "Kiran", "Kwan", \
            "Lee", "Michael", "Munni", "Niran", "Norman", "Peng", "Piyush", "Qiang", "Raiden", "Ronin", "Ryuu", "Sam", "Sanjay", "Sang", "Shin", "Silas", "Takeshi", "Thang", "Tung"]

    elif ethnicity == "White":
        names_list = ["Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Mason", "Ethan", "Olivia", "Emma", "Ava", "Sophia", "Isabella", \
            "Charlotte", "Amelia", "Mia", "Harper", "Evelyn"]

    return names_list[rand.randrange(0, len(names_list))]

def generate_students():
    for i in range(num_students):
        student = Student("Bob", generate_ethnicity(), generate_english_skill(), generate_acedemic_skill(), generate_age())
        student.name = generate_name(student.ethnicity)
        student_list.append(student)
    return student_list

def print_students(student_list):
    for i in range(len(student_list)):
        for a in range(len(student_list[i])):
            print("Name: {:<10} Ethnicity: {:<10} English Skill: {:<5} Academic Skill: {:<5} Age: {:<5}".format(student_list[i][a].name, student_list[i][a].ethnicity, student_list[i][a].english_skill, student_list[i][a].academic_skill, student_list[i][a].age))
        num_native, num_african, num_hispanic, num_asian, num_white = identify_present_ethnicities(student_list[i])
        age_list = create_student_age_list(student_list[i])
        median_age = median(age_list)
        num_11, num_12, num_13, num_14, num_15 = identify_present_ages(student_list[i])
        print()
        print("There are {} Native students. There are {} African students. There are {} Hispanic students. There are {} Asian students. There are {} White students.".format(num_native, num_african, num_hispanic, num_asian, num_white))
        print("The median age in the class is {}. There are {} eleven years olds, {} twelve year olds, {} thirteen year olds, {} fourteen year olds, and {} fifteen year olds.".format(median_age, num_11, num_12, num_13, num_14, num_15))
        print("-----------------------------------------------------------------------------------------")

def reverse_list(l):
    new_l = []
    for i in range(len(l)):
        new_l.append(l[len(l) - i - 1])
    return new_l

def sort_class_size(student_list):
    updated_student_list = [[]]
    current_class = 0
    for i in range(len(student_list)):
        if int(i / class_size) > current_class:
            updated_student_list.append([])
            current_class += 1
        updated_student_list[current_class].append(student_list[i])
    return updated_student_list

def identify_majority(group, attribute):
    if attribute == "academic_skill":
        grade_7 = 0
        grade_8 = 0
        for i in range(len(group)):
            if group[i].academic_skill == 7:
                grade_7 += 1
            elif group[i].academic_skill == 8:
                grade_8 += 1
        if grade_7 > grade_8:
            return 7
        elif grade_8 > grade_7:
            return 8
        else:
            return 7
    elif attribute == "english_skill":
        skill_1 = 0
        skill_4 = 0
        for i in range(len(group)):
            if group[i].english_skill == 1 or group[i].english_skill == 2:
                skill_1 += 1
            else:
                skill_4 += 1
        if skill_1 > skill_4:
            return 1
        else:
            return 4

def create_student_age_list(group):
    age_list = []
    for student in group:
        age_list.append(student.age)
    return age_list


def sort_class_academic_skill(student_list):
    trade_value = 0
    should_break = False
    for a in range(len(student_list)):
        if identify_majority(student_list[a], "academic_skill") == 7:
            trade_value = 8
        else:
            trade_value = 7
        for i in range(len(student_list[a])):
            student = student_list[a][i]
            if student.academic_skill == trade_value:
                for x in range(len(student_list) - a):
                    if should_break:
                        should_break = False
                        break
                    for y in range(len(student_list[x])):
                        if a + 1 + x >= len(student_list):
                            break
                        second_student = student_list[x + 1 + a][y]
                        if second_student.academic_skill != trade_value:
                            student_list[a][i] = second_student
                            student_list[x + 1 + a][y] = student
                            should_break = True
                            break

    return student_list

def sort_class_english_skill(student_list):
    trade_value_1 = 0
    trade_value_2 = 0
    should_break = False
    for a in range(len(student_list)):
        if identify_majority(student_list[a], "english_skill") == 1:
            trade_value_1 = 3
            trade_value_2 = 4
        else:
            trade_value_1 = 1
            trade_value_2 = 2
        for i in range(len(student_list[a])):
            student = student_list[a][i]
            if student.english_skill == trade_value_1 or student.english_skill == trade_value_2:
                for x in range(len(student_list) - a):
                    if should_break:
                        should_break = False
                        break
                    if a + 1 + x >= len(student_list):
                            break
                    for y in range(len(student_list[x + 1 + a])):
                        second_student = student_list[x + 1 + a][y]
                        if second_student.english_skill != trade_value_1 and second_student.english_skill != trade_value_2:
                            if second_student.academic_skill == student.academic_skill:
                                student_list[a][i] = second_student
                                student_list[x + 1 + a][y] = student
                                should_break = True
                                break

    return student_list

def identify_present_ethnicities(group):
    num_native = 0
    num_african = 0
    num_hispanic = 0
    num_asian = 0
    num_white = 0
    for i in range(len(group)):
        if group[i].ethnicity == "Native":
            num_native += 1
        elif group[i].ethnicity == "African":
            num_african += 1
        elif group[i].ethnicity == "Hispanic":
            num_hispanic += 1
        elif group[i].ethnicity == "Asian":
            num_asian += 1
        else:
            num_white += 1
    return num_native, num_african, num_hispanic, num_asian, num_white

def identify_present_ages(group):
    num_11 = 0
    num_12 = 0
    num_13 = 0
    num_14 = 0
    num_15 = 0
    for i in range(len(group)):
        if group[i].age == 11:
            num_11 += 1
        elif group[i].age == 12:
            num_12 += 1
        elif group[i].age == 13:
            num_13 += 1
        elif group[i].age == 14:
            num_14 += 1
        else:
            num_15 += 1
    return num_11, num_12, num_13, num_14, num_15

def compare_lists(list_1, list_2):
    for a in range(len(list_2)):
        for i in range(len(list_2[a])):
            student_1 = list_1[a][i]
            student_2 = list_2[a][i]
            if student_1.age != student_2.age:
                return True
    return False

def copy_list(list_1):
    list_2 = []
    for a in range(len(list_1)):
        list_2.append([])
        for i in range(len(list_1)):
            list_2[a].append(list_1[a][i])
    return list_2


def sort_class_ethnicity(student_list):
    should_break = False
    for part in range(4):
        if part == 2:
            print_students(student_list)
            student_list = reverse_list(student_list)
        for a in range(len(student_list)):
            for i in range(len(student_list[a])):
                num_native, num_african, num_hispanic, num_asian, num_white = identify_present_ethnicities(student_list[a])

                trade_for_value = []
                trade_value = []
                if part == 0 or part == 3:
                    if num_native > 4:
                        trade_value.append("Native")
                    else:
                        trade_value.append("Placeholder")
                    if num_african > 4:
                        trade_value.append("African")
                    else:
                        trade_value.append("Placeholder")
                    if num_hispanic > 4:
                        trade_value.append("Hispanic")
                    else:
                        trade_value.append("Placeholder")
                    if num_asian > 4:
                        trade_value.append("Asian")
                    else:
                        trade_value.append("Placeholder")
                    if num_white > 4:
                        trade_value.append("White")
                    else:
                        trade_value.append("Placeholder")

                    if num_native < 4:
                        trade_for_value.append("Native")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_african < 4:
                        trade_for_value.append("African")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_hispanic < 4:
                        trade_for_value.append("Hispanic")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_asian < 4:
                        trade_for_value.append("Asian")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_white < 4:
                        trade_for_value.append("White")
                    else:
                        trade_for_value.append("Placeholder")

                elif part == 1 or part == 3:
                    trade_value = []
                    trade_for_value = []
                    if num_native > 8:
                        trade_value.append("Native")
                    else:
                        trade_value.append("Placeholder")
                    if num_african > 8:
                        trade_value.append("African")
                    else:
                        trade_value.append("Placeholder")
                    if num_hispanic > 8:
                        trade_value.append("Hispanic")
                    else:
                        trade_value.append("Placeholder")
                    if num_asian > 8:
                        trade_value.append("Asian")
                    else:
                        trade_value.append("Placeholder")
                    if num_white > 8:
                        trade_value.append("White")
                    else:
                        trade_value.append("Placeholder")

                    if num_native < 8:
                        trade_for_value.append("Native")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_african < 8:
                        trade_for_value.append("African")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_hispanic < 8:
                        trade_for_value.append("Hispanic")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_asian < 8:
                        trade_for_value.append("Asian")
                    else:
                        trade_for_value.append("Placeholder")
                    if num_white < 8:
                        trade_for_value.append("White")
                    else:
                        trade_for_value.append("Placeholder")

                elif part == 2:
                    not_allowed_list_2 = []
                    if num_native_2 >= 8:
                        not_allowed_list_2.append("Native")
                    else:
                        not_allowed_list_2.append("Placeholder")
                    if num_african_2 >= 8:
                        not_allowed_list_2.append("African")
                    else:
                        not_allowed_list_2.append("Placeholder")
                    if num_hispanic_2 >= 8:
                        not_allowed_list_2.append("Hispanic")
                    else:
                        not_allowed_list_2.append("Placeholder")
                    if num_asian_2 >= 8:
                        not_allowed_list_2.append("Asian")
                    else:
                        not_allowed_list_2.append("Placeholder")
                    if num_white_2 >= 8:
                        not_allowed_list_2.append("White")
                    else:
                        not_allowed_list_2.append("Placeholder")

                student = student_list[a][i]
                if student.ethnicity in trade_value:
                    if part != 2 or not student.ethnicity in not_allowed_list_2:
                        for x in range(len(student_list) - a):
                            if should_break:
                                should_break = False
                                break
                            if a + 1 + x >= len(student_list):
                                    break
                            not_allowed_list = []
                            num_native_2, num_african_2, num_hispanic_2, num_asian_2, num_white_2 = identify_present_ethnicities(student_list[a + x + 1])
                            if num_native_2 <= 4:
                                not_allowed_list.append("Native")
                            else:
                                not_allowed_list.append("Placeholder")
                            if num_african_2 <= 4:
                                not_allowed_list.append("African")
                            else:
                                not_allowed_list.append("Placeholder")
                            if num_hispanic_2 <= 4:
                                not_allowed_list.append("Hispanic")
                            else:
                                not_allowed_list.append("Placeholder")
                            if num_asian_2 <= 4:
                                not_allowed_list.append("Asian")
                            else:
                                not_allowed_list.append("Placeholder")
                            if num_white_2 <= 4:
                                not_allowed_list.append("White")
                            else:
                                not_allowed_list.append("Placeholder")

                            for y in range(len(student_list[x + 1 + a])):
                                second_student = student_list[x + 1 + a][y]
                                if second_student.ethnicity in trade_for_value:
                                    if second_student.ethnicity not in not_allowed_list:
                                        if second_student.academic_skill == student.academic_skill:
                                            if second_student.english_skill == 1 or second_student.english_skill == 2:
                                                second_english = 1
                                            else:
                                                second_english = 4
                                            if student.english_skill == 3 or student.english_skill == 4:
                                                first_english = 1
                                            else:
                                                first_english = 4
                                            if first_english == second_english:
                                                    student_list[a][i] = second_student
                                                    student_list[x + 1 + a][y] = student

                                        should_break = True
                                    break
    student_list = reverse_list(student_list)
    return student_list

def sort_class_age(student_list):
    should_break = False
    previous_list = [[Student("placeholder", "placeholder", "palceholder", "placeholder", 99)]]
    iterations = 0
    while compare_lists(student_list, previous_list):
        iterations += 1
        previous_list = copy_list(student_list)
        for a in range(len(student_list)):
            for i in range(len(student_list[a])):
                age_list = create_student_age_list(student_list[a])
                class_median = median(age_list)
                student = student_list[a][i]
                for x in range(len(student_list) - a):
                    if should_break:
                        should_break = False
                        break
                    if a + 1 + x >= len(student_list):
                            break
                    for y in range(len(student_list[x + 1 + a])):
                        second_student = student_list[x + 1 + a][y]
                        if abs(class_median - student.age) > abs(class_median - second_student.age):
                            if second_student.academic_skill == student.academic_skill:
                                if second_student.english_skill == 1 or second_student.english_skill == 2:
                                    second_english = 1
                                else:
                                    second_english = 4
                                if student.english_skill == 3 or student.english_skill == 4:
                                    first_english = 4
                                else:
                                    first_english = 1
                                if first_english == second_english:
                                    num_native_2, num_african_2, num_hispanic_2, num_asian_2, num_white_2 = identify_present_ethnicities(student_list[a + x + 1])
                                    not_allowed_list = []
                                    if num_native_2 <= 4:
                                        not_allowed_list.append("Native")
                                    else:
                                        not_allowed_list.append("Placeholder")
                                    if num_african_2 <= 4:
                                        not_allowed_list.append("African")
                                    else:
                                        not_allowed_list.append("Placeholder")
                                    if num_hispanic_2 <= 4:
                                        not_allowed_list.append("Hispanic")
                                    else:
                                        not_allowed_list.append("Placeholder")
                                    if num_asian_2 <= 4:
                                        not_allowed_list.append("Asian")
                                    else:
                                        not_allowed_list.append("Placeholder")
                                    if num_white_2 <= 4:
                                        not_allowed_list.append("White")
                                    else:
                                        not_allowed_list.append("Placeholder")

                                    not_allowed_list_2 = []
                                    num_native_2, num_african_2, num_hispanic_2, num_asian_2, num_white_2 = identify_present_ethnicities(student_list[a])
                                    if num_native_2 >= 8:
                                        not_allowed_list_2.append("Native")
                                    else:
                                        not_allowed_list_2.append("Placeholder")
                                    if num_african_2 >= 8:
                                        not_allowed_list_2.append("African")
                                    else:
                                        not_allowed_list_2.append("Placeholder")
                                    if num_hispanic_2 >= 8:
                                        not_allowed_list_2.append("Hispanic")
                                    else:
                                        not_allowed_list_2.append("Placeholder")
                                    if num_asian_2 >= 8:
                                        not_allowed_list_2.append("Asian")
                                    else:
                                        not_allowed_list_2.append("Placeholder")
                                    if num_white_2 >= 8:
                                        not_allowed_list_2.append("White")
                                    else:
                                        not_allowed_list_2.append("Placeholder")
                                        if student.ethnicity not in not_allowed_list or not_allowed_list_2:
                                            student_list[a][i] = second_student
                                            student_list[x + 1 + a][y] = student
                                            should_break = True
                                            break
    return student_list

def check_underflow(l):
    num_native_2, num_african_2, num_hispanic_2, num_asian_2, num_white_2 = identify_present_ethnicities(l)
    if num_native_2 < 4:
        return True

    if num_african_2 < 4:
        return True
        
    if num_hispanic_2 < 4:
        return True

    if num_asian_2 < 4:
        return True
    if num_white_2 < 4:
        return True
        
    return False


print("How many students would you like to generate? A multiple of 30 would be ideal.")
num_students = int(input())
student_list = generate_students()
for student in student_list:
    print("Name: {:<10} Ethnicity: {:<10} English Skill: {:<5} Academic Skill: {:<5} Age: {:<5}".format(student.name, student.ethnicity, student.english_skill, student.academic_skill, student.age))

print()
pause = input("Students will next be split into classes. Press Enter to continue.")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()
student_list = sort_class_size(student_list)
print_students(student_list)

print()
pause = input("Students will next be split by grade, or academic skill. Press Enter to continue.")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()
student_list = sort_class_academic_skill(student_list)
print_students(student_list)

print()
pause = input("Students will next be split by English skill. Press Enter to continue.")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()
student_list = sort_class_english_skill(student_list)
print_students(student_list)

print()
pause = input("Students will now be sorted by ethnicity. Press Enter to continue.")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()
student_list = sort_class_ethnicity(student_list)
print_students(student_list)

print()
pause = input("Students will now be sorted by age. Press Enter to continue.")
print("-----------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------")
print()
student_list = sort_class_age(student_list)
print_students(student_list)