import pickle

def main():
	amrs = pickle.load(open("AMR_pickles/dev/dev-bolt.pickle","rb"))

	text = amrs["bolt12_64545_0562.1"]#["bolt12_6454_5051.6"]
	print(text)

	text = text.replace(" :wiki -","")
	stripped = text.split(" ")
	
	previous = ""
	toggle = 0
	for word in stripped:
	 	if previous == ":wiki":
	 		gold = word.strip("\n\"")
	 		name = str()
	 		toggle = 1
	 	if toggle == 1 and previous[0:3] == ":op":
	 		part = word.strip(")\n\"")
	 		if name:
	 			name += "_" + part
	 		else:
	 			name = part
		 	if word.strip()[-1] ==")":
		 		toggle = 0
		 		print(gold)
		 		print(name)
		 		if name == gold:
		 			print(1)
	 	previous = word

	

		


if __name__ == '__main__':
	main()