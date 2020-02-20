import numpy as np
import os


METADATA_FOLDER = "../Dataset/metadata_dev"


def read_csv(az, el):
    for file in os.listdir(METADATA_FOLDER):
        file_name = os.path.join(METADATA_FOLDER, file)

        f = open(file_name).readlines()[1:]
        el_list = np.zeros(len(f))  #3
        az_list = np.zeros(len(f))  #4


        for n, riga in enumerate(f):
            el.append(float(riga.split(",")[3]))
            az.append(float(riga.split(",")[4]))

        
    

if __name__ == "__main__":
    #read_csv() 
    az = []
    el = []

    read_csv(az, el)

    print(len(az))
    print(len(el))