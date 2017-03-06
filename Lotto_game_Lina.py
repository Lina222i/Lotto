import sys
import random
import copy

# Лотерейные карточки
class bingo_card():
    def __init__(self, type):
        self.type = type
        self.bingo_card = {n: [' ', ' ', ' '] for n in range (0, 9)}
        self.active_cell_count = 15
        all_cells = list(range(1, 90))
        for y in range (0, 3):
            num_list = list(self.bingo_card.keys())
            for x in range (0, 5):
                select_cell = random.choice(num_list)
                num_list.remove(select_cell)
                release_nums = list(range(select_cell * 10, select_cell * 10 + 10))
                for item in release_nums:
                    if not (item in all_cells):
                        release_nums.remove(item)

                self.bingo_card[select_cell][y] = random.choice(release_nums)
                all_cells.remove(self.bingo_card[select_cell][y])

    def __repr__(self):
        if self.type == 0:
            title = 'Your card\n'
        elif self.type == 1:
            title = 'Computer card\n'
        new_card = copy.deepcopy(self.bingo_card)
        for index in range(0, 3):
            if len(str(new_card[0][index])) == 1:
                new_card[0][index] = str('{}'.format(new_card[0][index]))

        line_1 = ' '.join(map(str, [new_card[n][0] for n in range(0, 9)]))
        line_2 = ' '.join(map(str, [new_card[n][1] for n in range(0, 9)]))
        line_3 = ' '.join(map(str, [new_card[n][2] for n in range(0, 9)]))
        return '{0}\n{1}\n{2}\{3}\n{4}\n'.format(title, line_1, line_2, line_3)

    def desired_cell(self, cell):
        column = cell // 10
        if cell in self.bingo_card[column]:
            index = self.bingo_card[column].index(cell)
            self.bingo_card[column][index] = "--"
            self.active_cell_count += -1
            return 1
        else:
            return 0

# Бочонки
class kegs:
    def __init__(self):
        self.set_of_kegs = list(range(1, 90))
        self.active_keg = -1

    def __iter__(self):
        return self

    def __next__(self):
        if len (self.set_of_kegs) > 0:
            self.active_keg = random.choice(self.set_of_kegs)
            self.set_of_kegs.remove(self.active_keg)
            return self.active_keg
        else:
            return -1

    def info(self):
        return '\nNew keg: {0} (expect{1}.'.format(self.active_keg, len(self.set_of_kegs))

# Ход игры
class course_of_the_game():
    def __init__(self):
        self.run_game = -1
        self.kegs = kegs()
        self.your_card = bingo_card(0)
        self.PC_card = bingo_card(1)
        self.game_stage()

    def __repr__(self):
        return  '{0}\n{1}\n{2}'.format(self.kegs.info(), self.your_card, self.PC_card)

    def game_stage(self):
        for keg_item in self.kegs:
            if keg_item != -1:
                print(self)
                self.run_game = -1
                while self.run_game == -1:
                    self.next_stage()
                    if self.your_card.active_cell_count == 0 or self.PC_card.active_cell_count == 0:
                        self.run_game = 0
                if self.run_game == 0:
                    self.game_over()
                continue
            break
        self.game_over()

    def next_stage(self):
        answer = input('Note the cell?\n(Yes/No)')
        your_res = self.your_card.desired_cell(self.kegs.active_keg)
        PC_res = self.PC_card.desired_cell(self.kegs.active_keg)
        if answer == 'Yes':
            if your_res == 0:
                self.run_game = 0
            else:
                self.run_game = 1
        elif answer == 'No':
            if your_res == 1:
                self.run_game = 0
            else:
                self.run_game = 1
        else:
            print('Put the correct answer: only Yes or No')
            self.run_game = -1

# Функция, объявляющая результаты игры
def game_over(self):
    print('Game over')
    if self.your_card.active_cell_count == 0:
        print('Congratulations! You won!')
    elif self.PC_card.active_cell_count == 0:
        print('You lose! The opponent won!')
    elif self.your_card.active_cell_count == 1 and self.PC_card.active_cell_count == 0:
        print('Draw!Friendship won!')

    sys.exit(0)
