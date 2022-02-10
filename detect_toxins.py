# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')


def make_accept_sound():
    print('made acceptance sound')


def detect_toxins(ingredients):
    toxic_ingredients = ['sodium nitrate', 'sodium benzoate', 'sodium oxide']
    for ingredient in toxic_ingredients:
        if ingredient in ingredients:
            return True
    return False


ingredients = ['sodium benzoate']
if detect_toxins(ingredients):
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
