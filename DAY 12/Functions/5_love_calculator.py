def calculate_love_score(name1, name2):
    combined_name = name1 + name2
    combined_name = combined_name.lower()
    
    t = combined_name.count("t")
    r = combined_name.count("r")
    u = combined_name.count("u")
    e = combined_name.count("e")
    first_digit = t + r + u + e
    
    l = combined_name.count("l")
    o = combined_name.count("o")
    v = combined_name.count("v")
    e = combined_name.count("e")
    second_digit = l + o + v + e

    print(str(first_digit)+str(second_digit))    

    
calculate_love_score("Kanye West", "Kim kardashian")