import pickle

def main():
	section = "test" # dev / test / training
	corpus = "xinhua" # amr-guidelines / bolt / consensus / cctv / dfa / mt09sdl / proxy / wb / xinhua
	
	try:
		amrs = pickle.load(open("AMR_pickles/{0}/{0}-{1}.pickle".format(section,corpus),"rb"))

		hits,wiki = 0,0 # count hits and total wiki links
		for ID in amrs:
			text = amrs[ID]

			text = text.replace(" :wiki -","") # remove empty wiki links
			stripped = text.split(" ")
			
			previous = ""
			toggle = 0
			for word in stripped:
			 	if previous == ":wiki": # extract every gold wiki link
			 		wiki += 1
			 		gold = word.strip("\n\"")
			 		name = str()
			 		toggle = 1
			 	if toggle == 1 and previous[0:3] == ":op": # extract part of corresponding name
			 		part = word.strip(")\n\"")
			 		if not name: # construct wiki link from words in name
			 			name = part
			 		else:
			 			name += "_" + part
				 	
				 	if word.strip()[-1] ==")": # check for end of name clause
				 		toggle = 0
				 		hit = (name == gold)
				 		print("{0: >65} {1} {2}".format(gold, int(hit), name)) # show local result
				 		if hit:
				 			hits += 1
			 	previous = word

		print("{0}/{1}={2:.2f}".format(hits,wiki,hits/wiki)) # show global result

	except FileNotFoundError:
		print("Corpus does not exist.")
		


if __name__ == '__main__':
	main()