import requests, json

def GetCourseName(courseNameURL):
    r = requests.get(courseNameURL)

    courseNameJson = json.loads(r.content)
    return courseNameJson['coursename']

def GetCourseType(typeNameURL):
    r = requests.get(typeNameURL)

    typeNameJson = json.loads(r.content)
    return typeNameJson['shortcode']

def PrintCourse(courseURL):
    r = requests.get(courseURL)

    if r.status_code != 200:
        print("course: course not found.")
    else:
        courseJson = json.loads(r.content)
        degreeTypeURL = courseJson['_links']['degreetype']['href']
        courseNameURL = courseJson['_links']['coursename']['href']

        degreeType = GetCourseType(degreeTypeURL)
        courseName = GetCourseName(courseNameURL)

        print("course: {0} {1}".format(degreeType, courseName))

r = requests.get('http://5.67.108.54:8080/student/')

studentListJson = json.loads(r.content)

for student in studentListJson['_embedded']['student']:
    print("name: {0}".format(student['name']))
    print("address: {0}".format(student['address']))
    print("dob: {0}".format(student['dob']))
    PrintCourse(student['_links']['course']['href'])
    print("\n")