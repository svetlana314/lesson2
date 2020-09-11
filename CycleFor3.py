def main():
    school = [
    {'school_class': '4a', 'scores': [3, 4, 5, 5, 2]},
    {'school_class': '5b', 'scores': [2, 4, 4, 5, 2, 5, 5, 3]},
    {'school_class': '3a', 'scores': [4, 5, 5, 5, 3, 2, 5]},
    {'school_class': '4c', 'scores': [3, 4, 5, 5, 4, 4, 2, 2]}
    ]

    scores_sum_school = 0
    students_number = 0

    for every_class in school:
        #print(every_class['school_class'], sum(every_class['scores'])/len(every_class['scores']))
        scores_sum_class = 0
        for score in every_class['scores']:
            scores_sum_class += score
        print(f"Average score in class {every_class['school_class']} is {scores_sum_class/len(every_class['scores'])}.")
        scores_sum_school += scores_sum_class
        students_number += len(every_class['scores'])

    print(f"Average score in school is {scores_sum_school/students_number}.")    

if __name__ == "__main__":
    main()