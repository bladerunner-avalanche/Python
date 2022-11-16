# Vorlesung 1: Einführung in Python
# Stelle fest ob die Zahl postiv, negativ oder null ist
user_input = int(input("Bro bitte gib eine Zahl ein: "))

if user_input < 0:
    print("Deine Zahl ist negativ")
elif user_input > 0:
    print("Deine Zahl ist positiv")
else:
    print("Deine Zahl ist 0")

# Stelle fest ob die Zahl gerade oder ungerade ist

if user_input % 2 == 0:
    print("Außerdem ist deine Zahl gerade")
else:
    print("Außerdem ist deine Zahl ungerade")

# Stelle fest ob die Zahl durch n teilbar ist
teiler = input("Gib den Teiler ein: ")
int_teiler = int(teiler)

if user_input % int_teiler == 0:
    print("Deine Zahl ist durch " + teiler + " teilbar")
else:
    print("Deine Zahl ist nicht durch " + teiler + " teilbar")


