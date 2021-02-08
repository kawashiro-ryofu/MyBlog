
import json
import requests


try:

    file = open("bglist.json","r").read()
    lIST = json.loads(file)

except:

    print("ERROR LOADING FILE")

else:
    for a in range(len(lIST["Pix"])):
        r = requests.get(lIST["Pix"][a][1]).status_code
        if(r != 200):
            print("BAD URL OF ID="+lIST["Pix"][a][0] + ", STAT="+ str(r))
        else:
            print("PASS " + lIST["Pix"][a][0] + ", STAT="+ str(r))

    for a in range(len(lIST["mPix"])):
        if(requests.get(lIST["mPix"][a][1]).status_code != 200):
            print("BAD URL OF ID="+lIST["mPix"][a][0] + ",STAT="+ str(r))
        else:
            print("PASS "+lIST["mPix"][a][0] + ", STAT=" + str(r))





