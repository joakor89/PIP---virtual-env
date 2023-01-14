import random


def choose_options():
  options = ('rock', 'paper', 'scissor')
  user_option = input('rock, paper or scissor => ')
  user_option = user_option.lower()

  if not user_option in options:
    print('It is a valid option')
    # continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Draw!')
  elif user_option == 'rock':
    if computer_option == 'scissor':
      print('rock win on scissor')
      print('user won!')
      user_wins += 1
    else:
      print('Paper won rock')
      print('computer won!')
      computer_wins += 1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper won rock')
      print('user won!')
      user_wins += 1
    else:
      print('scissor won paper')
      print('computer won!')
      computer_wins += 1
  elif user_option == 'scissor':
    if computer_option == 'paper':
      print('scissor won paper!')
      print('user won!')
      user_wins += 1
    else:
      print('rock won scissor')
      print('computer won!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    if computer_wins == 2:
      print('The winner is computer')
      break

    if user_wins == 2:
      print('The winner is user')
      break

run_game()