def max_activities(activities):
    activities.sort(key=lambda x: x[1])  
    selected_activities = [activities[0]]  
    previous_finish = activities[0][1] 

    for activity in activities[1:]:
        start, finish = activity
        if start >= previous_finish: 
            selected_activities.append(activity)
            previous_finish = finish

    return selected_activities

def main():
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    selected_activities = max_activities(activities)
    print(selected_activities)

if __name__ == "__main__":
    main()
