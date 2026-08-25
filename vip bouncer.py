# challenge 4


beachClub = [16, 21, 18, 14, 30, 17]
downtownClub = [21, 20 ,19, 15]
def bouncer_bot(age_list):
    total_money = 0
    people_admitted = 0
    rejected_ages = []
    for age in age_list:
        if age >= 18:
            total_money += 10
            people_admitted += 1
        else:
            rejected_ages.append(age)
    print(total_money)
    print(people_admitted)
    print(rejected_ages)
bouncer_bot(beachClub)
bouncer_bot(downtownClub)