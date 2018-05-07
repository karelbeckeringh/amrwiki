import pickle

def main():
	amrs = pickle.load(open("AMR_pickles/dev/dev-bolt.pickle","rb"))
	for ID in amrs:
		amr = amrs[ID]
		if ":wiki -" in amr:
		#if ":wiki" in amr.replace(":wiki","",4):
			print(ID)
			print(amr)


if __name__ == '__main__':
	main()