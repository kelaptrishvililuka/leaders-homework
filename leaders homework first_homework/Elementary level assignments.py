### **დაწყებითი დონის დავალებები**

# 1. დაბეჭდეთ "გამარჯობა, მსოფლიო!" ტექსტი.
# - გამოიყენეთ ფუნქცია, რომელიც ტექსტს პირდაპირ კონსოლში გამოყოფს.



greet = "hello world"
print(greet)



# 2. შეიყვანეთ სახელი და დაბეჭდეთ მისალმება.
# - ტექსტის შეყვანისთვის გამოიყენეთ შესაბამისი ფუნქცია და ჩასვით სახელი მისალმებაში.



user = input("Enter Your Name: ")
print("hello " + user)



# 3. გამოთვალეთ ორი რიცხვის ჯამი.
# - გადაყვანეთ მომხმარებლის შეყვანილი ტექსტი რიცხვებად და დაამატეთ ერთმანეთს.



num1 = int(input("Enter Your num"))
num2 = int(input("Enter Your Num" ))
num3 = num1 + num2
print(num3)




# 4. შეამოწმეთ, არის თუ არა რიცხვი ლუწი თუ კენტი.
#  - გაარკვიეთ, თუ რიცხვი იყოფა 2-ზე ნაშთის გარეშე.


num = int(input("Enter Your Num"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# 5. დაამატეთ ასაკი და გამოთვალეთ ორმაგი ასაკი.
#  - ასაკი შეინახეთ ცვლადში და გაზარდეთ ორჯერ.

age1 =int(input("Enter Your Age"))
age2 = age1 * 2
print(age2)



# 6. იპოვეთ რიცხვის კვადრატი.
#   - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი კვადრატის მისაღებად.

num = int(input("Enter a Number "))
num_square = num * num 
print(num_square)




# 7. გადააკეთეთ ცელსიუსი ფარენჰაიტად.
#   - გამოიყენეთ მოცემული ფორმულა და შესაბამისი ოპერატორები.


celsius = int(input("Enter a Degree "))
fahrenheit = celsius * (9/5) + 32
print(fahrenheit)


#8. შექმენით სია საყვარელი ფილმებით.

favourite_movies = []
favourite_movies.append("Home alone & Home alone 2")
favourite_movies.append("Violent Night")
favourite_movies.append("Red One")
favourite_movies.append("Home Alone 4")
favourite_movies.append("Christmas & Co")
print(favourite_movies)

# 9. დაბეჭდეთ 1-დან 10-მდე რიცხვები.
# - გამოიყენეთ "for" ან "while" ციკლი რიცხვების ბეჭდვისთვის.

# for loop

for i in range(1,11):
    print(i)


# While loop

number = 1
While number <= 10:
print(number)
number += 1



# 10. გამოთვალეთ რიცხვების ჯამი სიიდან.
#   - გადაუვლეთ სიას ციკლით და მიამატეთ ელემენტები

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)