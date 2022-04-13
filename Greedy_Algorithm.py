# /!/usr/bin/env python

import re
from nltk.tokenize import word_tokenize

class Greedy_Algorithm():

    def get_stripped_tokenized_line_phones(self, lines):

        phone_lines = []

        for line in lines:
            line = re.sub("utt[0-9]{8}", "", line)
            line_no_end_pause = re.sub("_BB|>", "", line)
            line_no_mid_line_pause = re.sub(" _B ", "", line_no_end_pause)
            line_sylls = []
            line_split = line_no_mid_line_pause.split("}")
            for index, word in enumerate(line_split):
                word_number = index
                if word_number == 0:
                    sentence_posi_mark = "_B"
                elif word_number == len(line_split) - 2:
                    sentence_posi_mark = "_E"
                else:
                    sentence_posi_mark = "_M"
                sylls = word.split("(")[1:]
                if sylls:
                    for syll in sylls:
                        syllable = re.sub("\)", "", syll)
                        tokenized_syllable = word_tokenize(syllable)
                        stress_marked_phones_syllable = []
                        for phone in tokenized_syllable:
                            if tokenized_syllable[0] == "0":
                                stress_marked_phone = phone + "_0" + sentence_posi_mark  #### you shouldn't do this twice, have the assignment of the 'stressed mark' to _0 or _1, then have one line to make up the 'stressed marked phone' at the bottom
                                stress_marked_phones_syllable.append(stress_marked_phone)
                            else:
                                stress_marked_phone = phone + "_1" + sentence_posi_mark
                                stress_marked_phones_syllable.append(stress_marked_phone)
                        for syll in stress_marked_phones_syllable:
                            line_sylls.append(syll)
            phone_lines.append(" ".join(line_sylls))

        phone_lines_clean = []
        for line in phone_lines:
            line = re.sub("1_1_[BME]|0_0_[BME]", "", line)
            phone_lines_clean.append(line)

        phone_lines_with_stress = []
        for line in phone_lines_clean:
            phone_line_retokenized = line.split()
            phone_lines_with_stress.append(phone_line_retokenized)

        return phone_lines_with_stress

    def get_triphoned_lines(self, phone_lines):

        triphones_lines = []

        for line in phone_lines:
            line_triphones = []
            for index, phone in enumerate(line):
                if index > 0:
                    preceding_phone_index = index - 1
                    preceding_phone = line[preceding_phone_index]
                else:
                    preceding_phone = "sil"
                if index < (len(line) - 1):
                    following_phone_index = index + 1
                    following_phone = line[following_phone_index]
                else:
                    following_phone = "sil"
                phone_triphone = preceding_phone + "_" + phone + "_" + following_phone
                line_triphones.append(phone_triphone)

            triphones_lines.append(line_triphones)

        return triphones_lines

    def get_diphoned_lines(self, phone_lines):

        diphones_lines = []

        for line in phone_lines:
            line_diphones = []
            line.insert(0, "sil")
            line.append("sil")
            for index, phone in enumerate(line[:-1]):
                following_phone_index = index + 1
                following_phone = line[following_phone_index]
                phone_diphone = phone + "_" + following_phone
                line_diphones.append(phone_diphone)
            diphones_lines.append(line_diphones)

        return diphones_lines

    def get_props(self, corpus):

        freqs = {}
        for sentence in corpus:
            for element in sentence:
                if (element in freqs):
                    freqs[element] += 1
                else:
                    freqs[element] = 1

        return freqs

    def gen_wishlist(self, corpus):

        triphone_dict = self.get_props(corpus)
        for triphone in triphone_dict:
            triphone_dict[triphone] = 0
        wish_list = triphone_dict

        return wish_list

    def update_wishlist(self, wish_list, S):
        S_freqs = self.get_props(S)
        for element in wish_list:
            if element in S_freqs:
                wish_list[element] = S_freqs[element]
            else:
                wish_list[element] = 0

        return wish_list

    def master_score(self, C, wish_list):

        line_scores = []
        C_triphone_freqs = self.get_props(C)
        for line in C:
            line_triphone_score = 0
            for triphone in line:
                triphone_C_score = 1 - (
                        C_triphone_freqs[triphone] / sum(C_triphone_freqs.values()))
                if sum(wish_list.values()) == 0:
                    wish_list_prop = 0
                else:
                    wish_list_prop = (wish_list[triphone] / sum(wish_list.values()))
                wishlist_score = 1 - wish_list_prop
                line_triphone_score += triphone_C_score + wishlist_score  ######### !!!!!!!!!! change this line for weighting of scores !!!!!!!!!!!!!! ###################
                line_score_length_normalised = line_triphone_score / len(line)
            line_scores.append(line_score_length_normalised)

        return line_scores

    def master_mover(self, C, actual_lines, n):
        S = []
        S_prons = []
        C_clone = C[:]
        actual_lines_clone = actual_lines[:]
        wish_list = self.gen_wishlist(C)
        while len(S) < n:
           # print("C_clone =", C_clone)
            scores = self.master_score(C_clone, wish_list)
           # print("scores = ", scores)
            max_value = max(scores)
            winner_index = scores.index(max_value)
            winner = C_clone.pop(winner_index)  # remove this line?
            winner_line = actual_lines_clone.pop(winner_index)
            S.append(winner_line)
            S_prons.append(winner)
            wish_list = self.update_wishlist(wish_list, S_prons)
            print("len(S) =", len(S))

        return S


#################################################

# control code
