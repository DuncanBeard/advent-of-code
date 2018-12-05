with open('input.txt') as f:
    match_found = False
    for line in f:
        for index in range(len(line)):
            search_string = line[:index] + line[index+1:]
            seen = {}
            with open('input.txt') as f_inner:
                for inner_line in f_inner:
                    inner_string = inner_line[:index] + inner_line[index+1:]
                    if inner_string == search_string:
                        if inner_string in seen.keys():
                            print (inner_string)
                            match_found = True
                            break
                        else:
                            seen[inner_string] = 1
            if match_found:
                break
        if match_found:
            break