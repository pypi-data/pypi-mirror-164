with open("../../../Downloads/glycan_sequences_smiles_isomeric.csv", "r") as data_smiles:
    map_smiles = {}
    for line in data_smiles.readlines()[1:]:
        line = line.strip().replace("\"", "").split(",")
        if len(line[0]) < 5 or len(line[1]) < 5:
            continue
        map_smiles[line[0]] = line[2]

with open("../../../Downloads/glycan_sequences_glycam_iupac.csv", "r") as data_iupac:
    map_iupac = {}
    for line in data_iupac.readlines()[1:]:
        line = line.strip().replace("\"", "").split(",")
        if len(line[0]) < 5 or len(line[1]) < 5:
            continue
        if line[1].endswith("-OH"):
            line[1] = line[1][:-3]
        if line[1][-1].isdigit():
            line[1] = line[1][:-1]
        line[1] = line[1].replace("D", "D-").replace("L", "L-")
        line[1] = line[1].replace("KD-N", "Kdn").replace("L-yx", "Lyx").replace("[2S]", "2S").replace("[3S]", "3S")\
            .replace("[4S]", "4S").replace("[5S]", "5S").replace("[6S]", "6S").replace("[2P]", "2P")\
            .replace("[3P]", "3P").replace("[4P]", "4P").replace("[5P]", "5P").replace("[6P]", "6P")\
            .replace("[2A]", "2A").replace("[3A]", "3A").replace("[4A]", "4A").replace("[5A]", "5A")\
            .replace("[6A]", "6A").replace("[7A]", "7A").replace("[8A]", "8A").replace("[9A]", "9A")\
            .replace("[2Me]", "2Me").replace("[3Me]", "3Me").replace("[4Me]", "4Me").replace("[6Me]", "6Me")\
            .replace("[5Me]", "5Me").replace("[7Me]", "7Me").replace("[8Me]", "8Me").replace("[9Me]", "9Me")
        # line[1] = line[1].replace("[", "(").replace("]", ")")
        map_iupac[line[0]] = line[1]

with open("../tests/data/glycam.tsv", "w") as out:
    for key in map_smiles:
        if key in map_iupac:
            print(map_iupac[key], map_smiles[key], sep="\t", file=out)
