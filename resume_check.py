import PyPDF2
import docx2txt
from docx.enum.style import WD_STYLE_TYPE
from docx import Document
import http.client, urllib.parse, json


class AzureSpellChecker:
    def __init__(self):
        text = 'Hollo, wrld!'

        data = {'text': text}

        key = '8e73f9261d9b4b0483c08cf65c2a8d0b'

        host = 'api.cognitive.microsoft.com'
        path = '/bing/v7.0/spellcheck?'
        params = 'mkt=en-us&mode=proof'

        headers = {'Ocp-Apim-Subscription-Key': key,
                   'Content-Type': 'application/x-www-form-urlencoded'}

        conn = http.client.HTTPSConnection(host)
        body = urllib.parse.urlencode(data)
        conn.request("POST", path + params, body, headers)
        response = conn.getresponse().read()
        print(response)


class ResumeParse:
    def __init__(self, file_name):
        self.file_name = file_name
        document = Document(self.file_name)
        self.lines = document.paragraphs
        self.line_indexer = {i:self.lines[i] for i in range(len(self.lines))}


    def check_basic(self):
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
rp =  ResumeParse("testresume.docx")
rp.check_basic()

spellchecker = AzureSpellChecker()