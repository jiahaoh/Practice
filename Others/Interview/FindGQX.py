# Import the Packages
import numpy as np
import pandas as pd

# Create the small file on bash shell
# awk '/#CHROM/{y=1;next}y' SQAHuman01_S1.vcf > test.vcf

# Second way to construct the dataframe
# big_file = open("SQAHuman01_S1.vcf", "r")
# found = False
# array = []
# for line in big_file:
#     if line.startswith("#CHROM"):
#         found = True
#     if found:
#         temp = line.replace('\n', '').split('\t')
#         array.append(temp)
#
# 
# df_test = pd.DataFrame.from_records(array)
# df_test.columns = df_test.iloc[0]
# df_test = df_test[1:]

# Get the input file and read it into pandas dataframe
input_file = "test.vcf"
df = pd.read_table(input_file)
df_pass = df[df["FILTER"] == "PASS"]

# Get the sorted scores
GQX_loc = []
score = []
res = []
for entry in df_pass["FORMAT"]:
    temp = entry.split(":")
    loc = temp.index("GQX")
    GQX_loc.append(loc)

for entry in df_pass["Human1"]:
    score.append(entry)

for i in xrange(len(score)):
    temp = score[i].split(":")
    loc = GQX_loc[i]
    res.append(temp[loc])

print sorted(map(int, res))
