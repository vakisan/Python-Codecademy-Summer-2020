def grade_converter(gpa):
  if(gpa>=4.0):
    return "A";
  elif(gpa>=3.0):
    return "B";
  elif(gpa>=2.0):
    return "C";
  elif(gpa>=1.0):
    return "D";
  elif(gpa>=0.0):
    return "F";
  
grade = grade_converter(4.0);
print(grade);
grade = grade_converter(3.4);
print(grade);
grade = grade_converter(2.5);
print(grade);
grade = grade_converter(1.4);
print(grade);
grade = grade_converter(0.5);
print(grade);