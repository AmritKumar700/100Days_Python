# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆
w = int(weight) #idhar hamne phle uchit data type me convert kiye hai
h = float(height) #isme value point me aayega isiliye isko float liye hai

bmi = float(w/(h**2))
print(bmi)