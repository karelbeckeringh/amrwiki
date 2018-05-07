from sys import stdin
import pickle

def main():
	amrs = {}
	amr = 0
	c = 0

	for line in stdin:
		if line[0:5] == "# AMR":
			corpus = line.split()[4][:-1]
			section = line.split()[6][:-1]
		elif line[0:6] == "# ::id":
			ID = line.split()[2]
			amr = str()
		elif line[0:7] == "# ::snt":
			amr += line[8:] + "@@\n"
		elif line.split():
			if line[0] != "#":
				amr += line
		else:
			if amr:
				if ":wiki \"" in amr:
					amrs[ID] = amr
					c += 1

	#print(c)
	pickle.dump(amrs, open("{}-{}.pickle".format(section,corpus), "wb"))

if __name__ == '__main__':
	main()