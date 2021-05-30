# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# part 1 **Greet Template**
def greet(name, greeting_template = 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    (f'{greeting_template}{name}')
    return greeting

print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))

# part 2 **Force**
def force(mass, body ='earth'):
    planet_gravity = { 
        'sun': 274, 
        'jupiter': round(24.92, 1), 
        'neptune': round(11.15, 1), 
        'saturn': round(10.44, 1), 
        'earth': round(9.798, 1), 
        'uranus': round(8.87, 1), 
        'venus': round(8.87, 1), 
        'mars': round(3.71, 1), 
        'mercuri': 3.7, 
        'moon': round(1.62, 1), 
        'pluto': round(0.58, 1) 
        }

    force = (mass * planet_gravity[body])
    return force

m_aarde = 5.972*(10**24)
print(force(m_aarde))

#part 3 **Gravity**
def pull(m1, m2, d):
    G = 6.674*(10**-11)
    pull = G*((m1*m2)/(d**2))
    return pull

m1 = 0.1 #Gewicht appel in kg
m2 = 5.972*(10**24) #Gewicht aarde in kg
d = 6.371*(10**6) #Afstand tussen appel & aarde

print(pull(m1, m2, d))