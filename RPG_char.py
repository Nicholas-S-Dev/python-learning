full_dot = '●'
empty_dot = '○'

def create_character(name, strenght, intelligence, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'

    if len(name) > 10:
        return 'The character name is too long'
    
    if " " in name:
        return 'The character name should not contain spaces'
    
    stat = [strenght, intelligence, charisma]

    # Single loop for all stat checks
    for stat_value in stat:
        if not isinstance(stat_value, int):
            return 'All stats should be integers'
        if stat_value < 1:
            return 'All stats should be no less than 1'
        if stat_value > 4:
            return 'All stats should be no more than 4'

    # Check the total points
    if sum(stat) != 7:
        return 'The character should start with 7 points'
        
    str_line = "STR " + full_dot * strenght + empty_dot * (10 - strenght)
    int_line = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)

    return name + '\n' + str_line + '\n' + int_line + '\n' + cha_line

result = create_character("Strong John", 4, 2, 1)
print(result)
