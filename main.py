from colorama import init, Fore
from colorama import Back
from colorama import Style
from os.path import basename


def read_book(path):
	with open("books/frankenstein.txt", "r") as file:
		return file.read()

def words_amount(content):
	content = content.split(" ")
	return len(content)

def characters_amount(content):
	result_dict = {}
	new_content = content.lower()
	for character in content:
		character = character.lower()
		if character not in result_dict:
			result_dict[character] = 1
		else:
			result_dict[character] += 1
	return result_dict


def report_make(path, amount_ch, ch_dict):
	filename = basename(path)
	print(Fore.GREEN + "--- Begin report of " + filename + " ---")
	print(Fore.RED + str(amount_ch) + Style.RESET_ALL + " words was found in the document")
	print()
	ch_dict = dict(sorted(ch_dict.items(), key=lambda x:x[1], reverse=True))

	for key, value in ch_dict.items():
		print("The " + Fore.RED + key + " character was found " + str(value) + " times")

	print(Fore.GREEN + "--- End report ---")



if __name__ == '__main__':
	path = "books/frankenstein.txt"
	content = read_book(path)
	amount = words_amount(content)
	characters = characters_amount(content)

	report_make(path, amount, characters)
