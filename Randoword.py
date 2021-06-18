import random

class RandomWord:

    def WordGenerator(self):

        textReader = open(r"C:\Users\danny\PycharmProjects\pythonProject2\words.txt","r")
        text = textReader.read()
        contents = text.split("\n")
        randoInt = random.randint(20,len(contents))
        return contents[randoInt]

    def SentenceGenerator(self):
        word = self.WordGenerator()
        randoInt = random.randint(1,20)
        sentence = ""

        for word in range(randoInt):
            sentence += f" {self.WordGenerator()}"

        return sentence




