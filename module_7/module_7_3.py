class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '') \
                            .replace('?', '').replace(';', '').replace(':', '').replace(' - ', ' ')
                        words.extend(line.split())
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f'Файл "{file_name}" не найден.')
        return all_words

    def find(self, search_word):
        find_word = dict()
        for name, words in self.get_all_words().items():
            if search_word.lower() in words:
                word_position = words.index(search_word.lower()) + 1
                find_word[name] = word_position
            else:
                print(f'Слово "{search_word}" не найдено в файле "{name}"')
        return find_word


    def count(self, search_word):
        count_dict = dict()
        for name, words in self.get_all_words().items():
            count_word = words.count(search_word.lower())
            count_dict[name] = count_word
        return count_dict


if __name__ == '__main__':
    finder1 = WordsFinder('Rudyard Kipling - If.txt', )

    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))