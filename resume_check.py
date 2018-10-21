from docx import Document
import http.client, urllib.parse, json
from auth import AzureAuthInfo
import time
from google.cloud.language import enums
from google.cloud import language
from google.cloud.language import types
import pprint

class AzureSpellChecker:
    def __init__(self):
        self.auth = AzureAuthInfo()

        self.host = 'api.cognitive.microsoft.com'
        self.path = '/bing/v7.0/spellcheck?'
        self.params = 'mkt=en-us&mode=proof'

        self.headers = {'Ocp-Apim-Subscription-Key': self.key,
                        'Content-Type': 'application/x-www-form-urlencoded'}

        print("Connecting to Azure Speck Check API...")
        self.conn = http.client.HTTPSConnection(self.host)

    def check_text(self, text):
        data = {'text':text}
        body = urllib.parse.urlencode(data)
        self.conn.request("POST", self.path + self.params, body, self.headers)
        response =self.conn.getresponse().read().decode('utf-8')
        output = json.loads(response)
        return output['flaggedTokens']


class GooglePOS:
    def __init__(self):
        # Instantiates a client
        self.client = language.LanguageServiceClient()

    def tag(self, text):
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        tokens = self.client.analyze_syntax(document).tokens

        ind = enums.PartOfSpeech
        sent = {}
        #print(tokens[0])
        #print()
        for token in tokens:
            sent[token.text.content] = {"pos":str(ind.Tag(token.part_of_speech.tag))[4:],
                                        "tense":str(ind.Tense(token.part_of_speech.tense))[6:],
                                        "person":str(ind.Person(token.part_of_speech.person))[7:],
                                        "number":str(ind.Number(token.part_of_speech.number))[7:]}

        return sent

class ResumeParse:
    def __init__(self, file_name):
        self.file_name = file_name
        document = Document(self.file_name)
        self.lines = document.paragraphs
        self.line_indexer = {i:self.lines[i] for i in range(len(self.lines))}


    def check_basic(self):
        print("Checking periods and capitalization...")
        incorrect_lines = {"periods":[],
                           "capitalization":[]}
        for i in range(len(self.lines)):
            line = self.line_indexer[i]
            if line.style.name == 'List Paragraph':
                text = line.text
                if text != '':
                    # Check periods
                    if text[-1] == '.' :
                        # Catch acronyms
                        if text.split()[-1].count('.') == 1:
                            incorrect_lines["periods"].append(i)
                    # Check capitalization
                    if text[0].islower():
                        incorrect_lines["capitalization"].append(i)

        print(incorrect_lines)
        print([self.line_indexer[i].text for i in incorrect_lines["periods"]])
        print([self.line_indexer[i].text for i in incorrect_lines["capitalization"]])
        print()
        return incorrect_lines

    def check_spelling(self):
        print('Checking spelling...')
        # List of dictionaries  with sent_index, word_index, suggestion as keys
        incorrect_words = []
        spell_checker = AzureSpellChecker()
        for i in range(len(self.lines)):
            text = self.line_indexer[i].text
            if text != '':
                flagged_tokens = spell_checker.check_text(text)
                if flagged_tokens != []:
                    # For each flagged token
                    for word in flagged_tokens:
                        # For each suggestion
                        max_score = 0
                        best_word = ''
                        #print(word['suggestions'])
                        for suggestion in word['suggestions']:
                            #print(suggestion)
                            if suggestion['score'] > max_score:
                                max_score = suggestion['score']
                                best_word = suggestion['suggestion']
                        #orig_word = text[word['offset']:].split()[0]
                        print(text)
                        split_text = text.split()
                        print(word['token'], ":", best_word)
                        incorrect_words.append((i, split_text.index(word['token'])))
                time.sleep(1)
        print(incorrect_words)
        print()
        return incorrect_words

    def check_tense(self):
        print('Checking tenses and person...')
        # List of dictionaries  with sent_index, word_index, suggestion as keys
        incorrect_words = []
        pos_tagger = GooglePOS()
        tense_errors = []
        count_tenses = {}
        for i in range(len(self.lines)):
            text = self.line_indexer[i].text
            if text != '':
                print(text)
                pos = pos_tagger.tag(text)
                for word in pos:
                    #print(pos[word]['pos'])
                    if pos[word]['pos'] == 'VERB':
                        #print("VERB:", word, ";", "TENSE:", pos[word]['tense'])
                        if pos[word]['tense'] == 'PAST':
                            split_text = text.split()
                            #print(split_text)
                            tense_errors.append({"index":i,
                                          "text":text,
                                          "word_index":split_text.index(word)})
        print(tense_errors)

rp =  ResumeParse("testresume.docx")
#rp.check_basic()
#rp.check_spelling()
#rp.check_tense()
#google = GooglePOS()
#pprint.pprint(google.tag("I went to the store to get food and eat"))
