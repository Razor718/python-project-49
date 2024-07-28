import prompt
from games.calc import brain_calc
from games.even import brain_even
from games.gcd import brain_gcd
from games.prime import brain_prime
from games.progression import brain_progression
def launch_the_game():
    desc_calc = 'What is the result of the expression?'
    desc_even = 'Answer "yes" if the number is even, otherwise answer "no".'
    desc_gcd = 'Find the greatest common divisor of given numbers.'
    desc_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    desc_progression = 'What number is missing in the progression?'
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello,', name + '!')
    match input():
        case 'brain_calc':
            brain_calc()
            print(desc_calc)
        case 'brain_even':
            brain_even()
            print(desc_even)
        case 'brain_gcd':
            brain_gcd()
            print(desc_gcd)
        case 'brain_prime':
            brain_prime()
            print(desc_prime)
        case 'brain_progression':
            brain_progression()
            print(desc_progression)
    return name
launch_the_game()            
