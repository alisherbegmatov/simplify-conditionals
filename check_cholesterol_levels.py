# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholostrol = 70
ldl = 30
triglyceride = 120


def print_good_level():
    print('Your cholesterol levels are good.')


def print_High_level():
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')


def print_TLC_diet():
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')


def check_total_cholostrol_ldl(total_cholostrol, ldl):
    if total_cholostrol < 200 and ldl < 100:
        return True
    else:
        return False


def check_cholesterol_levels(total_cholostrol, ldl, triglyceride):
    if check_total_cholostrol_ldl(total_cholostrol, ldl) and triglyceride < 150:
        print_good_level()
    elif check_total_cholostrol_ldl(total_cholostrol, ldl) and triglyceride < 200:
        print_High_level()
    elif check_total_cholostrol_ldl(total_cholostrol, ldl) and triglyceride < 300:
        print_TLC_diet()
    else:
        print('Error: unhandled case.')


check_cholesterol_levels(70, 30, 120)
