def read_book(path):
	with open("books/frankenstein.txt", "r") as file:
		return file.read()

def words_amount(content):
	content = content.split(" ")
	return len(content)


if __name__ == '__main__':
	content = read_book("books/frankenstein.txt")
	amount = words_amount(content)

	print(amount)
	
