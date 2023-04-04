


from transformers import  pipeline
# from bs4 import BeautifulSoup
# import requests


class TextSummarizer:

    def __init__(self):
        self.paragraphArray = []

    def summarizeSentence(self,ARTICLE):

        summarizer = pipeline("summarization")

        max_chunk = 400
        ARTICLE = ARTICLE.replace('.', '.<eos>')
        ARTICLE = ARTICLE.replace('?', '?<eos>')
        ARTICLE = ARTICLE.replace('!', '!<eos>')

        sentences = ARTICLE.split('<eos>')
        current_chunk = 0
        chunks = []
        for sentence in sentences:
            if len(chunks) == current_chunk + 1:
                if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                    chunks[current_chunk].extend(sentence.split(' '))
                else:
                    current_chunk += 1
                    chunks.append(sentence.split(' '))
            else:
                print(current_chunk)
                chunks.append(sentence.split(' '))

        for chunk_id in range(len(chunks)):
            chunks[chunk_id] = ' '.join(chunks[chunk_id])


        print(len(chunks))


        res = summarizer(chunks, max_length=100, min_length=30, do_sample=False)

        summ = ' '.join([summ['summary_text'] for summ in res])

        self.paragraphArray.append(summ)

    def returntheSummarizePara(self):
        tempStr = ""
        for sent in self.paragraphArray:
            tempStr+= sent
        return tempStr


# ------------------------------------------------------------------------------------------



# nlp = spacy.load("en_core_web_lg")
# nlp.add_pipe("textrank")
#
# texts = ["Quantum computing is an area of computer science that uses the principles of quantum theory. Quantum theory explains the behavior of energy and material on the atomic and subatomic levels.","Quantum computing uses subatomic particles, such as electrons or photons. Quantum bits, or qubits, allow these particles to exist in more than one state (i.e., 1 and 0) at the same time.","Classical computers today employ a stream of electrical impulses (1 and 0) in a binary manner to encode information in bits. This restricts their processing ability, compared to quantum computing.","Quantum computing has the capability to sift through huge numbers of possibilities and extract potential solutions to complex problems and challenges. Where classical computers store information as bits with either 0s or 1s, quantum computers use qubits. Qubits carry information in a quantum state that engages 0 and 1 in a multidimensional way"]
# # doc = nlp(text)
# #
# # for sent in doc._.textrank.summary(limit_sentences =2):
# #     print(sent)
#
# print("Model Name")
# model_name = "google/pegasus-xsum"
#
# print("pegasus_tokenizer")
# pegasus_tokenizer = PegasusTokenizer.from_pretrained(model_name)
#
# print("Pegasus model")
# pegasus_model = PegasusForConditionalGeneration.from_pretrained(model_name,max_length=5120)
#
#
# for text in texts:
#     print("Tokens")
#     tokens = pegasus_tokenizer(text,truncation=True,padding="longest",return_tensors="pt")
#
#     print("Encoded Sum")
#     encodedSummary = pegasus_model.generate(**tokens,max_length=1024)
#
#     print("Decoded")
#     decodedSummary = pegasus_tokenizer.decode(encodedSummary[0],skip_special_tokens=True)
#
#     print(decodedSummary)