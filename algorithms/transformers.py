from transformers import pipeline

class Transformers:


    def summarize(self,text):
        self.text =text
        summarizer = pipeline("summarization",model="facebook/bart-large-cnn")
        sum = summarizer(text)
        return sum