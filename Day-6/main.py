groups = []
with open('input.txt', 'r') as file:
    groups = [s.strip().splitlines() for s in file.read().split('\n\n')]

def get_all_answers(group):
    question_answers = []
    for person in group:
        person = person.strip()
        for question in person:
            if not question in question_answers:
                question_answers.append(question)
    return question_answers

def sum_answers_anyone(group):
    return len(get_all_answers(group))

def every_person_answered(group, answer):
    for person in group:
        if not answer in person:
            return False
    return True

def sum_answers_everyone(group):
    all_answers = get_all_answers(group)
    sum_valid = 0

    for answer in all_answers:
        if every_person_answered(group, answer):
            sum_valid += 1

    return sum_valid

sum_any = 0
sum_every = 0
for group in groups:
    # Part 1
    sum_any += sum_answers_anyone(group)
    # Part 2
    sum_every += sum_answers_everyone(group)

print('sum anyone:  ', sum_any)
print('sum everyone:', sum_every)