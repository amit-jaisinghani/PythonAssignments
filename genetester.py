from dnalist import DNAList

def test_init():


    # dna = DNAList(None)
    # print(dna)
    dna = DNAList("")
    print(dna)

    dna = DNAList("AMit")
    print(dna)

    dna = DNAList("A")
    print(dna)

    dna = DNAList("@")
    print(dna)

    dna = DNAList()
    print(dna)

    dna = DNAList("YOUTUBE")
    print(dna)


def test_append():
    dnaAppend = DNAList()
    print(dnaAppend)
    dnaAppend.append("A")
    print(dnaAppend)
    dnaAppend.append("Aditi")
    print(dnaAppend)
    # dnaAppend.append(8)
    # print(dnaAppend)
    dnaAppend.append('@')
    print(dnaAppend)
    # dnaAppend.append(None)
    # print(dnaAppend)


def test_join():
    a = 0



def test():
    test_init()
    test_append()
    test_join()


if __name__ == "__main__":
    test()