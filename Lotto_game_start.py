import Lotto_game_Lina as lotto


def main():
    your_answer = True
    while your_answer:
        match = lotto.Course_of_the_game()

        answer = input("\nНачать игру\n(Yes/No): ")
        if answer != "Yes":
            your_answer = False


if __name__ == "__main__":
    main()