#A simple string concatenation where the user input some words (adjetives, verbs, adverbs, etc...) into a template to make a funny word combination.
#Way to accomplish this
#sustantive = input("Sustantive: ")
#adjetive = input("Adjetive: ")
#print("I love to watch" + sustantive)
#print("I love to watch {}".format(sustantive)) #you need a pair of curly braces for each word or variable you enter
#print("I love to watch {}{}".format(sustantive,adjetive)) #you need a pair of curly braces for each word or variable you enter
#print(f"I love to watch {sustantive}")

charac1 = input("Chracter name: ").capitalize()
charac2 = input("Chracter name: ").capitalize()
adj1 = input("Adjetive: ")
sus1 = input("Sustantive: ")
sus2 = input("Sustantive: ")
color1 = input("Color: ")

madlib = f"One afternoon {charac1} and {charac2} were walking down a {adj1} trail, looking for kindling for their campfire. The {sus1} were cryptic and {color1}, and there were colorful wildflowers all around. {charac1} and {charac2} began to pick the {sus1}, and after a while, they restored so far that they had wandered away from the trail."
print(madlib)