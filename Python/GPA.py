def get_grade_point(grade):
    """
    Convert letter grade to grade points (4.0 scale)
    """
    grade_scale = {
        'A+': 4.0, 'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'D-': 0.7,
        'F': 0.0
    }
    return grade_scale.get(grade.upper(), 0.0)


def get_letter_grade(gpa):
    """
    Convert GPA to letter grade
    """
    if gpa >= 3.85:
        return 'A+'
    elif gpa >= 3.7:
        return 'A'
    elif gpa >= 3.3:
        return 'A-'
    elif gpa >= 3.0:
        return 'B+'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 2.3:
        return 'B-'
    elif gpa >= 2.0:
        return 'C+'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.3:
        return 'C-'
    elif gpa >= 1.0:
        return 'D+'
    elif gpa >= 0.7:
        return 'D'
    elif gpa >= 0.0:
        return 'D-'
    else:
        return 'F'


def calculate_course_points(grade, credit_hours):
    """
    Calculate quality points for a single course
    Quality Points = Grade Points × Credit Hours
    """
    grade_point = get_grade_point(grade)
    course_points = grade_point * credit_hours
    return course_points


def calculate_gpa(courses):
    """
    Calculate overall GPA
    GPA = Total Quality Points / Total Credit Hours
    """
    total_points = 0
    total_credits = 0
    
    for course in courses:
        grade = course['grade']
        credit_hours = course['credit_hours']
        course_points = calculate_course_points(grade, credit_hours)
        total_points += course_points
        total_credits += credit_hours
    
    if total_credits == 0:
        return 0.0
    
    gpa = total_points / total_credits
    return gpa


def display_course_details(course, course_number):
    """
    Display individual course details with points and grade letter
    """
    name = course['name']
    grade = course['grade']
    credit_hours = course['credit_hours']
    course_points = calculate_course_points(grade, credit_hours)
    grade_point = get_grade_point(grade)
    
    print(f"\nCourse {course_number}:")
    print(f"  Name: {name}")
    print(f"  Grade: {grade}")
    print(f"  Credit Hours: {credit_hours}")
    print(f"  Grade Point: {grade_point:.2f}")
    print(f"  Course Points: {course_points:.2f}")


def main():
    """
    Main function to run the GPA calculator
    """
    print("=" * 50)
    print("         GPA CALCULATOR")
    print("=" * 50)
    
    # Get number of courses
    while True:
        try:
            num_courses = int(input("\nEnter the number of courses: "))
            if num_courses <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    courses = []
    
    # Input course details
    for i in range(num_courses):
        print(f"\n--- Course {i + 1} ---")
        
        course_name = input("Enter course name: ")
        
        while True:
            grade = input("Enter grade (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F): ").upper()
            if get_grade_point(grade) >= 0 or grade == 'F':
                break
            print("Invalid grade. Please try again.")
        
        while True:
            try:
                credit_hours = float(input("Enter credit hours: "))
                if credit_hours <= 0:
                    print("Credit hours must be positive.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        courses.append({
            'name': course_name,
            'grade': grade,
            'credit_hours': credit_hours
        })
    
    # Display results
    print("\n" + "=" * 50)
    print("         COURSE DETAILS")
    print("=" * 50)
    
    for i, course in enumerate(courses, 1):
        display_course_details(course, i)
    
    # Calculate and display total GPA
    total_gpa = calculate_gpa(courses)
    total_credits = sum(course['credit_hours'] for course in courses)
    total_points = sum(calculate_course_points(course['grade'], course['credit_hours']) 
                      for course in courses)
    overall_letter_grade = get_letter_grade(total_gpa)
    
    print("\n" + "=" * 50)
    print("         OVERALL GPA")
    print("=" * 50)
    print(f"Total Credit Hours: {total_credits:.2f}")
    print(f"Total Quality Points: {total_points:.2f}")
    print(f"GPA: {total_gpa:.2f}")
    print(f"Letter Grade: {overall_letter_grade}")
    print("=" * 50)


if __name__ == "__main__":
    main()