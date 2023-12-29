import readline
import os
from openai import OpenAI
from Evan import Magic_spell

normal_font = '\033[0m'
red = '\033[1;31;40m'
bond = '\033[1;97m'

os.system("cls" if os.name == "nt" else "clear")


print(""" \033[1;31;40m\  \ \033[1;97m    ______
  \033[1;31;40m\  \ \033[1;97m  |        \      /     /\      |\   |
   \033[1;31;40m\  \ \033[1;97m |______   \    /     /  \     | \  |
   \033[1;31;40m/  / \033[1;97m |          \  /     /____\    |  \ |
  \033[1;31;40m/  / \033[1;97m  |______     \/     /      \   |   \| \033[1;31;40mBy TheEthicalGuy\033[1;97m
 \033[1;31;40m/  / \033[1;97m  
    """)

while True:
    try:
        API_KEY = input("\033[1;31;40mEnter your chatGPT API>>\033[0m " )
        break
    except KeyboardInterrupt:
        print("Please try again")
    
client = OpenAI(api_key=API_KEY)

evan_soul = Magic_spell


def get_response(evan_soul, previous_questions_and_answers, new_message):
    try:
        #bring evan to life
        messages = [
            { "role": "system", "content": evan_soul },
        ]
        # add the previous questions and answers
        for question, answer in previous_questions_and_answers:
            messages.append({ "role": "user", "content": question })
            messages.append({ "role": "assistant", "content": answer })
        # add the new question
        messages.append({ "role": "user", "content": new_message })

        evan_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return evan_response.choices[0].message.content
    except Exception as error:
        if 'Error code: 401' in str(error):
            print("Invalid Authentication or Incorrect API")
        elif 'Error code: 429' in str(error):
            print("You exceeded your current quota, please check your plan and billing details")
        elif 'Error code: 503' in str(error):
            print("The engine is currently overloaded, please try again later")

def main():
    os.system("cls" if os.name == "nt" else "clear")
    print(""" \033[1;31;40m\  \ \033[1;97m    ______
  \033[1;31;40m\  \ \033[1;97m  |        \      /     /\      |\   |
   \033[1;31;40m\  \ \033[1;97m |______   \    /     /  \     | \  |
   \033[1;31;40m/  / \033[1;97m |          \  /     /____\    |  \ |
  \033[1;31;40m/  / \033[1;97m  |______     \/     /      \   |   \| \033[1;31;40mv1.2\033[1;97m
 \033[1;31;40m/  / \033[1;97m  
    """)
    print("Hey buddy, I'm Evan and I'm here to be your assistant")
    print("feel free to ask me anything related to the art of hacking")
    print("and let's start to rule them all")
    print(" ")
    # keep track of previous questions and answers
    previous_questions_and_answers = []
    try:
        while True:
            # ask the user for their question
            new_message = input('\033[1;31;40m>>\033[0m ')
            if new_message == 'exit':
                print("\033[1;31;40mbye :)\033[0m")
                break

            response = get_response(evan_soul, previous_questions_and_answers, new_message)

            # add the new question and answer to the list of previous questions and answers
            previous_questions_and_answers.append((new_message, response))

            # print the response
            if response is None:
                print("\033[1;31;40mbye :)\033[0m")
                break
            print(response)
    except KeyboardInterrupt:
        print("\033[1;31;40mbye :)\033[0m")



if __name__ == "__main__":
    main()

