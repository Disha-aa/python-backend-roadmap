def scramble(user_input: str) -> str:
    if len(user_input) == 3:
          return user_input[::-1]
    
    if len(user_input) %2 != 0:
          last_char = user_input[-1]
          working_str = user_input[:-1]
    else:
          working_str = user_input
          last_char = ""

    result = list(working_str)

    i = 0
    while i + 2 < len(working_str):
            result[i], result[i+2] = result[i+2], result[i]
            i += 1
            print(result)
    return "".join(result) + last_char

def main():
    user_input = input("Enter a word: ")
    if len(user_input.split()) > 1:
          print("Error: enter one word")
          return
    elif not user_input:
          print("Error: empty input")
          return

    result = scramble(user_input)
    print(result)

if __name__ == "__main__":
      main()