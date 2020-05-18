def file_read(filePath):
    file_object = open(filePath, "r")
    fileString = file_object.readlines()
    marker = 0
    for i in range(len(fileString)):
        if fileString[i].startswith("#"):
            continue
        if marker == 0:
            prob_sameDice = float(fileString[i].strip())
            marker += 1
            continue
        if marker == 1:
            fileString[i] = fileString[i].strip()
            emissionProb_d1 = fileString[i].split(" ")
            marker += 1
            continue
        if marker == 2:
            fileString[i] = fileString[i].strip()
            emissionProb_d2 = fileString[i].split(" ")
            marker += 1
            continue
        if marker == 3:
            fileString[i] = fileString[i].strip()
            emissionProb_d3 = fileString[i].split(" ")
            marker += 1
            continue
        else:
            fileString[i] = fileString[i].strip()
            emissions = fileString[i].split(",")
            break
    return prob_sameDice, emissionProb_d1, emissionProb_d2, emissionProb_d3, emissions
