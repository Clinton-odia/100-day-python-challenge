from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game = False
while not game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift= int(input("Type the shift number:\n"))
  def caesar(direction):
    if direction == "encode":
      def encrypt(original_text,shift_amount):
        cipher_text = ""
        for letter in original_text:
          if letter not in alphabet:
            cipher_text += letter
          else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

        print(f"Here is the encoded result: {cipher_text}")
      encrypt(original_text=text,shift_amount=shift)
    elif direction == "decode":
      def decrypt(original_text,shift_amount):
        decipher_text = ""
        for letter in original_text:
          if letter not in alphabet:
            decipher_text += letter
          else:
            original_position = alphabet.index(letter) - shift_amount
            original_position %= len(alphabet)
            decipher_text += alphabet[original_position]
          
        print(f"Here is the decoded result: {decipher_text}")
      decrypt(original_text=text,shift_amount=shift)
    else:
      print("we don't understand what you mean!")
  caesar(direction=direction)
  game_over = input("Do you want to continue: Type 'Y' for yes & 'N' for No: ").lower()
  if game_over == 'n':
    game = True
    print("Thank you for your time")