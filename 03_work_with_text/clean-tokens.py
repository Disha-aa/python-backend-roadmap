def clean_tokens(tokens: str) -> str:
      working_tokens = tokens.split()
      if len(working_tokens) <3:
            return tokens
      
      shortest = min(working_tokens, key=len)
      working_tokens.remove(shortest)

      longest = max(working_tokens, key=len)
      working_tokens.remove(longest)
 
      return " ".join(working_tokens)

def main():
      while True:
            user_input = input("Enter a token (or '0' to stop): ")
            if not user_input:
                  print("Error: empty input")
                  continue
            elif user_input == "0":
                  return
            if len(user_input.split()) <3:
                  print("Error: log must consist of at least 3 tokens")
                  continue
            break
      
      result = clean_tokens(user_input)
      print(f"Result after cleaning: {result}")

if __name__ == "__main__":
      main()