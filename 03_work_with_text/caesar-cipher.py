def caesar_cipher(text: str, shift: int, encode: bool) -> str:
      caesar_text = []
      if not encode:
            shift = -shift
      for char in text:
            num = ord(char)
            if ord('A') <= num <= ord('Z'):
                  new_char = chr((num-ord('A') + shift) % 26 + ord('A'))
                  caesar_text.append(new_char)
            elif ord('a') <= num <= ord('z'):
                  new_char = chr((num-ord('a') + shift) % 26 + ord('a'))
                  caesar_text.append(new_char)
            else:
                  new_char = chr(num)
                  caesar_text.append(new_char)

      return "".join(caesar_text)

def main():
      while True:
            user_input = input("Enter a text (or '0' to stop): ")
            if user_input == "0":
                  return

            try:
                  user_shift = int(input("Enter a shift: "))
                  if user_shift <= 0:
                        print("Error: valid value")
                        continue
            except ValueError:
                  print("Error: enter a integer")
                  continue

            is_encode = input("Encode or decode? ").lower()
            if is_encode == "encode":
                  is_encode = True
            elif is_encode == "decode":
                  is_encode = False
            else:
                  print("Error: empty input")
                  continue
            
            if not user_input or not user_shift:
                  print("Error: empty input")
                  continue
            break
            
      encode_result = caesar_cipher(user_input, user_shift, is_encode)

      print(f"Source text: {user_input}")
      print(f"Encode: {encode_result}")

if __name__ == "__main__":
      main()