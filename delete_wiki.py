import pickle

def main():
	amrs = pickle.load(open("AMR_pickles/dev/dev-bolt.pickle","rb"))

	
	text = amrs["bolt12_6454_5051.6"]
	print(text)

	text = text.replace(" :wiki -","")
	stripped = text.split(" ")
	new_list = []
	previous = ""
	for word in stripped:
	 	if previous == ":wiki":
	 		new_list.append("-\n")
	 	else:
	 		new_list.append(word)
	 	previous = word
	 	#print(word)
	new_amr = " ".join(new_list)
	print(new_amr)

		


if __name__ == '__main__':
	main()