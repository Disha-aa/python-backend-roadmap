def toggle_case(text: str) -> str:
    result = []
    for char in text:
        x = ord(char)
        if ord("a") <= x <= ord("z"):
            result.append(chr(x-(ord("a")-ord("A"))))
        elif ord("A") <= x <= ord("Z"):
            result.append(chr(x+(ord("z")-ord("Z"))))
        else:
            result.append(chr(x))
            
    return "".join(result)

def main():
    user_input = input()

    if not user_input:
        print("Error: empty input")
        return
    
    result = toggle_case(user_input)
    print(result)

if "__main__" == __name__:
    main()