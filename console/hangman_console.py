"""
============================================
🇮🇳 Hangman – I ❤ My India (Console Edition)
============================================

🧑‍💻 Author: Arun vk  
🎯 Description:
This is a console-based Hangman game written in Python 
to celebrate and test your knowledge of Indian cities.

Players must guess the name of a randomly chosen city,
one letter at a time — with only 7 lives to spare!

📅 Year: 2025  
🛠️ Tools: Python (random, string)

"""
       
import random 
# from words import words
import string

words = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", "Indore", "Bhopal", "Patna", "Ludhiana", "Agra", "Nashik", "Vadodara", "Faridabad", "Meerut", "Rajkot", "Varanasi", "Srinagar", "Amritsar", "Allahabad", "Ranchi", "Coimbatore", "Jodhpur", "Chandigarh", "Guwahati", "Gwalior", "Vijayawada", "Raipur", "Kozhikode", "Thiruvananthapuram", "Madurai", "Jamshedpur", "Aurangabad", "Hubli", "Mysuru", "Tiruchirappalli", "Udaipur", "Noida", "Ghaziabad", "Howrah", "Salem", "Bareilly", "Aligarh", "Moradabad", "Jalandhar", "Kolhapur", "Bilaspur", "Dehradun", "Jabalpur", "Dhanbad", "Nellore", "Tirupati", "Warangal", "Puducherry", "Shimla", "Siliguri", "Thane", "Asansol", "Ajmer", "Panaji", "Gandhinagar", "Bhavnagar", "Solapur", "Bikaner", "Mangalore", "Erode", "Rourkela", "Haridwar", "Thrissur", "Nanded", "Jamnagar", "Cuttack", "Ujjain", "Imphal", "Aizawl", "Itanagar", "Shillong", "Tezpur", "Port Blair", "Agartala", "Darjeeling", "Kota", "Rewa", "Satna", "Sagar", "Durgapur", "Bhagalpur", "Begusarai", "Gaya", "Muzaffarpur", "Siwan", "Katihar", "Saharsa", "Arrah"
        ]

def get_valid_word(words):
    print("Guess the name of the popular cities in india :- ")
    word = random.choice(words)   # Randomly chooses something from the list 
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)   # Letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()   # What the user has guessed

    lives = 7

    # getting user input 
    while len(word_letters) > 0 and lives > 0:
        # Letters used 
        # " ".join(['a', 'b', 'cd']) --> 'a b cd'
        print(f"You have {lives} lives left and you have used these letters : ", " ".join(used_letters))

        # What current word is (i.e., W _ O R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word : ", " ".join(word_list))
        


        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")  

            else:
                lives = lives - 1   # Takes away a live if wrong
                print("Letter is not in word.")


        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")

    # Gets here when len(word_letters) == 0 Or lives == 0
    if lives == 0:
        print(f"You Died, Sorry. The Word was {word}")
    else:
        print(f"Yap! You guessed the {word}!!!")


if __name__ == '__main__':
    hangman()