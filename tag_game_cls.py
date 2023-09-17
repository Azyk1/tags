from random import shuffle


class TagGame:
    MAX_STEPS = 10 ** 9

    def __init__(self, is_new_game=True, start_config=None, cur_config=None, cur_steps=None, name="", save_time=None):
        if is_new_game:
            self.__steps_number = 0
            self.__name = ""
            self.__save_time = None
            self.__start_configuration, line_configuration = TagGame.generate_configuration()
            self.__cur_configuration = [[self.__start_configuration[i][j] for j in range(4)] for i in range(4)]
            clutter_parameter = self.count_clutter_parametr(line_configuration)
            if self.is_win() or (clutter_parameter % 2 == 0 and clutter_parameter != 0):
                self.__init__()
        else:
            self.__steps_number = cur_steps
            self.__start_configuration = start_config
            self.__cur_configuration = cur_config
            self.__name = name
            self.__save_time = save_time

    def count_clutter_parametr(self, line_configuration):
        clutter_parameter = 0
        for i in range(len(line_configuration) - 1):
            for j in range(i + 1, len(line_configuration)):
                if line_configuration[i] > line_configuration[j] != 0:
                    clutter_parameter += 1
        return clutter_parameter

    @staticmethod
    def generate_configuration():
        random_list = [i for i in range(16)]
        shuffle(random_list)
        k = 0
        config = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                config[i][j] = random_list[k]
                k += 1
        return config, random_list

    def is_win(self):
        matches = 0 if self.__cur_configuration[-1][-1] != 0 else 1
        cur_index = 1
        for i in range(4):
            for j in range(4):
                if self.__cur_configuration[i][j] == cur_index:
                    matches += 1
                cur_index += 1
        return matches == 16

    def is_lost(self):
        return self.__steps_number == self.MAX_STEPS

    @property
    def steps_number(self):
        return self.__steps_number

    @steps_number.setter
    def steps_number(self, steps_number):
        self.__steps_number = steps_number

    @property
    def cur_configuration(self):
        return self.__cur_configuration

    @cur_configuration.setter
    def cur_configuration(self, cur_configuration):
        self.__cur_configuration = cur_configuration

    @property
    def start_configuration(self):
        return self.__start_configuration

    @start_configuration.setter
    def start_configuration(self, start_configuration):
        self.__start_configuration = start_configuration

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def save_time(self):
        return self.__save_time

    @save_time.setter
    def save_time(self, save_time):
        self.__save_time = save_time
