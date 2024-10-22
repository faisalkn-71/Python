from school import School
from person import Student, Teacher
from subject import Subject 
from classroom import classroom

school = School("CSUST", "Changsha, Hunan, China")

eight = classroom("Eight")
nine = classroom("Nine")
ten = classroom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

rafi = Student("Rafi", eight)
zisan = Student("Zisan", nine)
shekhor = Student("Shekhor", ten)
sunny = Student("Sunny", ten)


school.student_admission(rafi)
school.student_admission(zisan)
school.student_admission(shekhor)
school.student_admission(sunny)


abul = Teacher("Abul Khan")
babul = Teacher("Babul Khan")
khabul = Teacher("Khabul Khan")


bangla = Subject("Bangla", abul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", khabul)
biology = Subject("Biology", khabul)


eight.add_subject(bangla)
eight.add_subject(physics)
eight.add_subject(chemistry)
nine.add_subject(physics)
nine.add_subject(chemistry)
nine.add_subject(biology)
ten.add_subject(bangla)
ten.add_subject(physics)
ten.add_subject(chemistry)
ten.add_subject(biology)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()


print(school)