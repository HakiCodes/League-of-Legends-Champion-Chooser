def choose_value():
    values = ["Ahri", "Syndra", "Akali"]
    scores = [0, 0, 0]

    # Ask the user about the threat
    threat = input("Does the enemy team have threat onto you? (Yes/No) ")
    if threat.lower() == "yes":
        scores[0] += 2
        scores[2] += 3 
    elif threat.lower() == "no":
        scores[0] += 2
        scores[1] += 3
        scores[2] += 1
    print(scores)

    # Ask the user about the range
    long_range = input("Is the opponent long-ranged? (Yes/No) ")
    if long_range.lower() == "yes":
        scores[0] += 2
        scores[1] += 3
        scores[2] += 1
    elif long_range.lower() == "no":
        scores[0] += 1
        scores[1] += 2
        scores[2] += 1
    print(scores)
    # Ask the user about their team's AP
    ap = input("Does your team have a lot of AP? ('Yes'/'A Little'/'No') ")
    if ap.lower() == "yes":
        scores[0] -= 2
        scores[1] -= 3
        scores[2] += 1
    elif ap.lower() == "no":
        scores[0] += 2
        scores[1] += 3
        scores[2] += 1
    else:
        scores[0] += 2
        scores[1] += 3
        scores[2] += 1 
    print(scores)

    # Find the value with the highest score
    highest_score = max(scores)
    if highest_score == 0:
        return "No value was selected"
    elif scores.count(highest_score) > 1:
        return "Both " + values[scores.index(highest_score)] + " and " + values[scores.index(highest_score, scores.index(highest_score)+1)] + " are good choices this game."
    else:
        return values[scores.index(highest_score)]

    # Test the function
print(choose_value())  # Output: "Ahri" or "Akali"
