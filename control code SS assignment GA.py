from Greedy_Algorithm import Greedy_Algorithm

g = Greedy_Algorithm()

with open("spt_corpus_prons.txt") as f:
    lines = f.readlines()

phone_lines = g.get_stripped_tokenized_line_phones(lines)

#print("len(phone_lines) =", len(phone_lines))
#print("phone_lines =", phone_lines)

diphones_lines = g.get_diphoned_lines(phone_lines)

with open("spt_corpus_raw_sentences.txt") as h:
    actual_lines = h.readlines()

n = 5

S = g.master_mover(diphones_lines, actual_lines, n)

for line in S:
    print(line)

output_filename = "combined_GA_test_" + str(n)

data_filename = output_filename + ".data"
file = open(data_filename, "w")
for sentence in list(S):
    sentence_number = str(list(S).index(sentence) + 1)
    file.write("(" + " spt" + "_" + sentence_number + " " + '"' + sentence.strip("\n") + '"' + " )" + "\n")
file.close()

raw_filename = output_filename + "_raw.txt"
file = open(raw_filename, "w")
for sentence in list(S):
    file.write(sentence)
file.close()



