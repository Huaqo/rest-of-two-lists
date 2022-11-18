# import modules
import numpy as np
import pandas as pd

# load lists
studenten = [5541916,
             5220499,
             5518384,
             5520656,
             5542396,
             5518937,
             5510269,
             5543528,
             4695391,
             5071662,
             5554383,
             5500450,
             5519577,
             5545398,
             5459668,
             5544586,
             5546499,
             5448710,
             5562333,
             5511010,
             5541326,
             5512515,
             5222561,
             4673811,
             5506047,
             5542255,
             5505954,
             5545190,
             5527393,
             5550704,
             5543159,
             5439983,
             5552617,
             5523382,
             5302641,
             5511094,
             5532004,
             5510509,
             4219560,
             5362705,
             5182509,
             5549385,
             5546463,
             5426139,
             5553571,
             5510560,
             5521954,
             5249407,
             5341156,
             5549300,
             5541965,
             5401201,
             5451498,
             5333826,
             5427996,
             5557220,
             5220985,
             5543147,
             5547515,
             5518175,
             5525744,
             5516803,
             5453234,
             5315311,
             5241434,
             5519682,
             5547750,
             5117539,
             5220149,
             5512797,
             5198624,
             5513211,
             5556099,
             5505874,
             5537964,
             5525523,
             5546230,
             5525707,
             5547539,
             5545374,
             5545233,
             5135742,
             5545405,
             5510731,
             5549999,
             5545546,
             5520619,
             5410246,
             5521966,
             5316264,
             5550231,
             5522011,
             5515799,
             5510522,
             5529988,
             5538101,
             5521930,
             5449743,
             5510141,
             5344816,
             5540089,
             5529720,
             4874504,
             5510257,
             5546371,
             5277732,
             5518612,
             5545466,
             5540225,
             5547712,
             5461500,
             5544316,
             5018457,
             5523289,
             5549895,
             5332368,
             5512668,
             5551786,
             5001440,
             5520392,
             5221681,
             5543135,
             5456410,
             5541756,
             5398646,
             4984938,
             5498946,
             5220715,
             5506072,
             5274582,
             5416945,
             5550163]
teilnehmer = [5541916,
              5518384,
              5520656,
              5542396,
              5518937,
              5510269,
              5543528,
              4695391,
              5500450,
              5519577,
              5545398,
              5459668,
              5544586,
              5546499,
              5448710,
              5511010,
              5512515,
              4673811,
              5506047,
              5542255,
              5505954,
              5545190,
              5527393,
              5439983,
              5550704,
              5543159,
              5552617,
              5523382,
              5511094,
              5532004,
              5510509,
              5549385,
              5426139,
              5553571,
              5521954,
              5249407,
              5341156,
              5549300,
              5541965,
              5333826,
              5543147,
              5547515,
              5518175,
              5525744,
              5516803,
              5315311,
              5519682,
              5547750,
              5117539,
              5220149,
              5512797,
              5513211,
              5505874,
              5546230,
              5525523,
              5525707,
              5547539,
              5545374,
              5545233,
              5545405,
              5510731,
              5510522,
              5538101,
              5521930,
              5510141,
              5344816,
              5540089,
              5510257,
              5546371,
              5545466,
              5277732,
              5518612,
              5540225,
              5547712,
              5461500,
              5544316,
              5549895,
              5523289,
              5512668,
              5551786,
              5520392,
              5543135,
              5456410,
              5541756,
              4984938,
              5498946,
              5506072,
              5274582,
              5416945,
              5550163]

# compare lists and make new from missing
nochmal = []
for x in studenten:
    if x not in teilnehmer:
        nochmal.append(x)

# load bigger list
data = np.loadtxt('/Users/huaqo/Desktop/pylist.csv',
                  delimiter=';', dtype='str')

# cleaning
data[0][0] = '5541916'

# compare lists and make new from matches
nochmaldata = []
for i in range(len(data)):
    for j in nochmal:
        if j == int(data[i][0]):
            nochmaldata.append(data[i])

# make dataframe and export
df = pd.DataFrame(nochmaldata)
df.to_csv('/Users/huaqo/Desktop/file.csv', index=False)