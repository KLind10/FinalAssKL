# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# part 1 : scorers & report

scorer_name0 = 'Ruud Gullit'
scorer_name1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorer0 = f'Ruud Gullit {goal_0}'
scorer1 = f'Marco van Basten {goal_1}'

scorers = scorer0+','+" "+scorer1
print(scorers)
report = scorer_name0+" "+'scored in the'+" "+str(goal_0)+'nd minute' '\n' +scorer_name1+" "+'scored in the'+" "+str(goal_1)+'th minute'
print(report)

# part 2 : player

player = 'Ronald Koeman'

first_name = player[:player.find(' ')] 
print(first_name)

last_name_len = len(player[(player.find(' ')+1):])
print(last_name_len)

name_short = first_name[0]+'.'+player[player.find(' '):]
print(name_short)

chant = ((first_name+'!'+' ')*len(first_name))[:-1]
print(chant)

good_chant  = chant[-1] != ' '
print(good_chant)