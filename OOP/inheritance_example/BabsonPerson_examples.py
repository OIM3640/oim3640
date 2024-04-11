from Person import Person
from BabsonPerson import BabsonPerson


def main():
    b3 = BabsonPerson("Mark Zuckerberg")
    b3.set_birthday(5, 14, 84)
    b2 = BabsonPerson("Barack Obama")
    b2.set_birthday(8, 4, 61)
    b1 = BabsonPerson("Bill Gates")
    b1.set_birthday(10, 28, 55)

    babson_person_list = [b1, b2, b3]

    for everyone in babson_person_list:
        print(everyone)
        print(everyone.speak("How are you?"))

    babson_person_list.sort()
    print()
    print("After sorting:")
    print()
    for everyone in babson_person_list:
        print(everyone)
        print(everyone.speak("How are you?"))

    p4 = Person("Donald Trump")
    p5 = Person("Elon Musk")

    person_list = babson_person_list + [p4, p5]

    for everyone in person_list:
        print(everyone)
        print(everyone.speak("How are you?"))


if __name__ == "__main__":
    main()
