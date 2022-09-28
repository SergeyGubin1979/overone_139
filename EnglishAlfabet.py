import string

#Алфавит
class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    #Печатаем буквы алфавита
    def print(self):
        print(self.letters)

    #Возвращаем кол-во букв в алфавите
    def letters_num(self):
        return len(self.letters)

#Английский алфавит
class EnAlphabet(Alphabet):

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    __letters_num = 26

    #Проверка, есть ли буква в англ.алфавите
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    #Возвращаем кол-во букв в алфавите
    def letters_num(self):
        return EnAlphabet.__letters_num

    #Печатаем пример текста на англ.языке
    @staticmethod
    def example():
        print("English Example:\nSome words in English")

#Проверка
eng_alphabet = EnAlphabet()
eng_alphabet.print()
print(eng_alphabet.letters_num())
print(eng_alphabet.is_en_letter('D'))
print(eng_alphabet.is_en_letter('Ж'))
EnAlphabet.example()
