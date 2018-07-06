#Sort by length
# def sort_by_length(arr):
#     return sorted(arr, key=len)
#
# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))

#Highest and lowest
def high_and_low(numbers):
    results = [int(i) for i in numbers.split()]
    max_r = str(max(results))
    min_r = str(min(results))
    return ' '.join([max_r, min_r])
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

#Best practice solution:
def high_and_low(numbers):
  n = [int(i) for i in numbers.split()]
  return "{} {}".format(max(n), min(n))

#Predict age
def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    return int(((age_1**2+age_2**2+age_3**2+age_4**2+age_5**2+age_6**2+age_7**2+age_8**2)**.5)/2)

#Best practice solution:
def predict_age(*ages):
    return sum(a*a for a in ages)**.5//2

#Pizza payment
def michael_pays(costs):
    if costs < 5.00:
        return float(round(costs, 2))
    elif costs >= 5.00 and costs <= 30.00:
        return float(round(costs*(2/3), 2))
    else:
        return float(round(costs-10.00))

#Disemvowel
def disemvowel(string):
    new_string = ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in string:
        if i not in vowels:
            new_string += i
    return new_string

#Sum number's digits
def sumDigits(number):
    return sum(int(d) for d in str(abs(number)))
