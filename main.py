questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": "C"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "answer": "C"
    },
    {
        "question": "What is the hardest natural substance?",
        "options": ["Gold", "Iron", "Diamond", "Silver"],
        "answer": "C"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "Thailand", "South Korea"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["90°C", "100°C", "110°C", "120°C"],
        "answer": "B"
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Brain", "Lungs", "Heart", "Liver"],
        "answer": "C"
    }
]
amount=0
for i in range (0,10):
    print(questions[i].get("question"))
    print(f'A.{questions[i].get("options")[0]}\t B.{questions[i].get("options")[1]}\nC.{questions[i].get("options")[2]}\t\t D.{questions[i].get("options")[3]}')
    answer=input("Enter your answer:").upper()
    if(questions[i].get("answer") == answer):
        print("Correct Answer")
        amount+=100000
        if(i!=9):
            print("You are playing really good.")
            print(f"You have won Rs.{amount} till now.")
        else: 
            print("Congratssssssss...You have won the game")
            print(f"You are a Millioniare now.You have won {amount}")
    else:
        print("Sorry...Its a wrong answer.You lost")
        print(f'The correct answer was {questions[i].get("answer")}')
        break


