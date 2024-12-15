def calculate_love_score(name1,name2):
    total1 = 0
    total2 = 0
    name3 = name1 + name2
    for letter in name3:
        if letter == 't':
            total1 += 1 
        elif letter == 'u':
            total1 += 2 
        elif letter == 'e':
            total1 += 2 
    for letter in name3:
      if letter == "l":
        total2 += 1
      elif letter == "e":
        total2 += 2
    print(f"Love Score = {total1}{total2}")


calculate_love_score('angela yu','jack bauer')