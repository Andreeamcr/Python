# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
s_pizza = 0
m_pizza = 0
l_pizza = 0
if size == "S":
  s_pizza = 15
  if add_pepperoni == "Y":
    s_pizza += 2
  if extra_cheese == "Y":
    s_pizza += 1
  print(f"Your final bill is {s_pizza}")
elif size == "M":
  m_pizza = 20
  if add_pepperoni == "Y":
    m_pizza += 3
  if extra_cheese == "Y":
    m_pizza += 1
  print(f"Your final bill is {m_pizza}")
else:
  l_pizza = 25
  if add_pepperoni == "Y":
    l_pizza += 3
  if extra_cheese == "Y":
    l_pizza += 1
  print(f"Your final bill is {l_pizza}")





