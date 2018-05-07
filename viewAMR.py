import pickle

def main():
	amrs = pickle.load(open("AMR_pickles/dev-bolt.pickle","rb"))
	for ID in amrs:
		sent, amr = amrs[ID].split("@@\n")
		#if ":wiki -" in amr:
		if ":wiki" in amr.replace(":wiki","",4):
			print(ID)
			print(sent)
			print(amr)


if __name__ == '__main__':
	main()