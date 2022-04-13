# /!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import re
from nltk.tokenize import word_tokenize
import argparse


class Scrape():

    def containsNumber(self, string):   # got this idea from here: https://codefather.tech/blog/check-if-python-string-contains-number/
        for character in string:
            if character.isdigit():
                return True
        return False

    def get_content_list(self, links_list):

        content_list = []
        for link in links_list:
            webpage_response = requests.get(link)
            webpage = webpage_response.content
            soup = BeautifulSoup(webpage, "html.parser")
            for data in soup.findAll('div', {'class': 'content'}):
                content_list.append(data.text)

        self.content_list = content_list
        return content_list


    def get_sentence_list(self, content_list):

        sentence_list = []
        for element in content_list:
            sentences = element.split(".")
            for sentence in sentences:
                if sentence:
                    sentence_list.append(sentence + ".")

        self.sentence_list = sentence_list
        return sentence_list


    def produce_normalized_sentence_list(self, sentence_list):

        sentence_list_normalized = []

        for sentence in sentence_list:
            sentence_normalized = re.sub(r'[!?]', ".", sentence)
            sentence_normalized_2 = re.sub(r'["\']', "", sentence_normalized)
            sentence_normalized_3 = sentence_normalized_2.replace("-", " ")
            if sentence_normalized_3 not in sentence_list_normalized:
                sentence_list_normalized.append(sentence_normalized_3)


        self.normalized_sentence_list = sentence_list_normalized

        return sentence_list_normalized



    def produce_output_files(self, unique_sentences, filename):

        file_raw = open(filename + "_raw_sentences" + ".txt", "a")
        for sentence in unique_sentences:
            file_raw.write(sentence + "\n")
        file_raw.close()

        file_raw_numbered = open(filename + "_numbered.txt", "a")
        for index, sentence in enumerate(list(unique_sentences)):
            number = index + 1
            sentence_number = str(number)
            file_raw_numbered.write(sentence_number + " " + sentence + "\n")
        file_raw_numbered.close()

        data_filename = filename + ".data"
        file = open(data_filename, "a")
        for sentence in list(unique_sentences):
            sentence_number = str(list(unique_sentences).index(sentence) + 1)
            file.write("(" + filename + "_" + sentence_number + " " + '"' + sentence + '"' + " )" + "\n")
        file.close()


    def remove_sentences_with_bad_words(self, sentence_list, bad_words):

        sentence_list_no_bad_words = []
        for sentence in sentence_list:
            sentence = re.sub('“|”', '', sentence)
            sentence_2 = re.sub(":", ". ", sentence)
            sentence_3 = re.sub('\.(?!$)', '',
                                sentence_2)  # got this from here: https://stackoverflow.com/questions/38078862/how-to-remove-periods-from-the-middle-of-sentences
            sentence_4 = re.sub("VisitScotland", "Visit Scotland", sentence_3)
            sentence_5 = re.sub("cybercrime", "cyber crime", sentence_4)
            sentence_6 = re.sub("childrens", "children's", sentence_5)
            sentence_7 = re.sub("cybersecurity", "cyber security", sentence_6)
            sentence_8 = re.sub("[Cc]yberattacks", "Cyber attacks", sentence_7)
            sentence_9 = re.sub("subnational", "national", sentence_8)
            if "—" not in sentence_9 and "(" not in sentence_9 and ")" not in sentence_9 and ";" not in sentence_9 and " ." not in sentence_9 and "’" not in sentence_9:
                if self.containsNumber(sentence_9) == False:
                    if not any(word in sentence_9.split() for word in bad_words):
                        sentence_list_no_bad_words.append(sentence_9)

        self.sentence_list_no_bad_words = sentence_list_no_bad_words

        return sentence_list_no_bad_words




    def remove_sentences_with_numbers(self, length_checked_sentence_list):

        sentence_list_no_numbers = []
        for sentence in length_checked_sentence_list:
            numbers = re.findall('[0-9]{2,}', sentence)
            if not numbers:
                if self.split(sentence)[0] != "[" and self.split(sentence)[1] != "[" and "\n" not in self.split(sentence):
                    sentence_list_no_numbers.append(sentence.strip())

        self.sentence_list_no_numbers = sentence_list_no_numbers

        return sentence_list_no_numbers


    def sentence_length_checker(self, normalized_sentence_list, min_length = 5, max_length = 15):

        len_checked_sentence_list = []
        for sentence in normalized_sentence_list:
        #    print(len(sentence.split()))
            if len(sentence.split()) >= min_length and len(sentence.split()) <= max_length:
                if sentence not in len_checked_sentence_list:
                    len_checked_sentence_list.append(sentence)
        self.len_checked_sentence_list = len_checked_sentence_list

        return len_checked_sentence_list


    def split(self, word):
        return [char for char in word]


    def unique_sentences_checker(self, sentence_list):

        unique_set = set()

        for sentence in sentence_list:
            unique_set.add(sentence)

        unique_sentences = list(unique_set)

        self.unique_sentences = unique_sentences

        return unique_sentences






##########################

#control code:




