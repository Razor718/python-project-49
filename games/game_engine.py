from brain_games.scripts import brain_main
from games import calc, even, gcd, prime, progression
def launch_the_game():
    desc_calc = 'What is the result of the expression?'
    desc_even = 'Answer "yes" if the number is even, otherwise answer "no".'
    desc_gcd = 'Find the greatest common divisor of given numbers.'
    desc_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    desc_progression = 'What number is missing in the progression?'
    brain_main.brain_main()
    print('Please, select the game!')
    userscore = 0
    winscore = 3
    match input():
        case 'brain_calc':
            print(desc_calc)
            while userscore < winscore:
                calc.brain_calc()
                if calc.c == calc.answer:
                    print('Correct!')
                    userscore += 1
                else:
                    print(f'''
                    Question: {calc.a} {calc.str_operator} {calc.b}
                    {calc.answer} is wrong answer ;(.
                    Correct answer was {calc.c}.
                    Let's try again, {brain_main.name}!''')
                    break
                if userscore == 3:
                    print(f'Congratulations, {brain_main.name}!')
        case 'brain_even':
            print(desc_even)
            while userscore < winscore:
                even.brain_even()
                if even.random_number % 2 == 0 and even.answer != 'yes':
                    print(f'''{even.answer} is wrong answer ;(.
                    Correct answer was yes.
                    Let's try again, {brain_main.name}!''')
                    break
                elif even.random_number % 2 != 0 and even.answer != 'no':
                    print(f'''{even.answer} is wrong answer ;(.
                    Correct answer was no.
                    Let's try again, {brain_main.name}!''')
                    break
                else:
                    print('Correct!')
                    userscore += 1
                if userscore == 3:
                    print(f'Congratulations, {brain_main.name}!')
        case 'brain_gcd':
            print(desc_gcd)
            while userscore < winscore:
                gcd.brain_gcd()
                if gcd.answer == gcd.result:
                    print('Correct!')
                    userscore += 1
                else:
                    print(f'''{gcd.answer} is wrong answer ;(.
                    Correct answer was {gcd.result}.
                    Let's try again, {brain_main.name}!''')
                    break
                if userscore == 3:
                    print(f"Congratulations, {brain_main.name}!")
        case 'brain_prime':
            print(desc_prime)
            while userscore < winscore:
                prime.brain_prime()
                if prime.is_prime and prime.answer == 'yes':
                    print('Correct!')
                    userscore += 1
                elif not prime.is_prime and prime.answer == 'no':
                    print('Correct!')
                    userscore += 1
                else:
                    print(
                    f'''Question: {prime.random_number}
                    Your answer: {prime.answer}
                    {prime.answer} is wrong asnwer;(.
                    Correct asnwer was {'yes' if prime.is_prime else 'no'}
                    Let's try again, {brain_main.name}!''')
                    break
                if userscore == 3:
                    print(f'Congratulations, {brain_main.name}!')
        case 'brain_progression':
            print(desc_progression)
            while userscore < winscore:
                progression.brain_progression()
                if progression.answer == progression.random_index:
                    print('Correct!')
                    userscore += 1
                else:
                    print(
                    f'''Question: {progression.str_result}
                    Your answer: {progression.answer}
                    {progression.answer} is wrong answer ;(.
                    Correct answer was {progression.random_index}
                    Let's try again, {brain_main.name}!''')
                    break
                if userscore == 3:
                    print(f'Congratulations, {brain_main.name}!')
def main():
    launch_the_game()

if __name__ == '__main__':
    main()      
