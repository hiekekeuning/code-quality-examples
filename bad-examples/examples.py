
# example a
def is_expensive(price):
    if price > 100:
        return True
    else:
        return False


print(is_expensive(1000))
print(is_expensive(10))

# example b


def get_loan():
    print('Getting a loan')


if is_expensive(1000) == True:
    get_loan()
else:
    if not is_expensive(1000):
        print('cheap')

# example c

target = 1000
start = 25
years = 0
reached_target = False
while not reached_target:
    start = start + (start * 0.01)
    if start >= target:
        years += 1
        reached_target = True
    else:
        years += 1

print(years)

# Code duplication example
temp_f1 = 100
temp_f2 = 25
temp_f3 = 34
temp_c1 = (5 / 9) * (temp_f1 - 32)
temp_c2 = (5 / 9) * (temp_f2 - 32)
temp_c3 = (5 / 9) * (temp_f3 - 32)
avg_temp_c = (temp_c1 + temp_c2 + temp_c3) / 3

# Introduced method

def fahrenheit_to_celsius(temp):
    return (5 / 9) * (temp - 32)


temp_c1 = fahrenheit_to_celsius(temp_f1)
temp_c2 = fahrenheit_to_celsius(temp_f2)
temp_c3 = fahrenheit_to_celsius(temp_f3)
avg_temp_c = (temp_c1 + temp_c2 + temp_c3) / 3

# Even shorter with list and map
temps_f = [100, 25, 34]
temps_c = list(map(fahrenheit_to_celsius, temps_f))
avg_temp_c = sum(temps_c) / len(temps_c)


def doIt():
    #...
    # 500 lines of weakly cohesive gibberish
    #...
    print('end')


# PEP-8 violations example

class programmingStudent:
    def __init__(self, name):
        self.name = name

    def printInfo(self):
        print (f"I am {self.name}.")

st1 = programmingStudent('Alex')
st1.printInfo();

