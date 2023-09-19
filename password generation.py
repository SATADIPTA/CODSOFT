import random
import string

def generate_random_password(min_length, max_length, conditions):
    character_sets={
        'uppercase':string.ascii_uppercase,
        'lowercase':string.ascii_lowercase,
        'special':string.punctuation,
        'digit':string.digits,
    }

    selected_characters=[char_set for char_set, include in conditions if include]

    if not selected_characters or min_length <= 0 or max_length < min_length:
        return "Invalid input."

    required_chars=[random.choice(character_sets[char_set]) for char_set in selected_characters]
    remaining_length=random.randint(max(min_length, len(required_chars)), max_length)

    password_chars=required_chars+random.choices(''.join(character_sets[char_set] for char_set in selected_characters), k=remaining_length - len(required_chars))
    random.shuffle(password_chars)

    return ''.join(password_chars)


def main():
    try:
        min_length=int(input("Enter the minimum password length: "))
        max_length=int(input("Enter the maximum password length: "))
        conditions=[
            ('uppercase', input("Include uppercase letters? (yes/no): ").lower() =='yes'),
            ('lowercase', input("Include lowercase letters? (yes/no): ").lower() =='yes'),
            ('special', input("Include special characters? (yes/no): ").lower() =='yes'),
            ('digit', input("Include digits? (yes/no): ").lower() =='yes'),
        ]

        password=generate_random_password(min_length, max_length, conditions)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter valid integers for password length.")

if __name__=="__main__":
    main()
