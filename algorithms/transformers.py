from transformers import pipeline , BartConfig , TFBartModel

class Transformers:


    def summarize(self,text):
        self.text =text
        summarizer = pipeline("summarization",model="facebook/bart-large-cnn", max_length=130, min_length=30, do_sample=False,max_time=10,use_cache=True,use_gpu=True)
        sum = summarizer(text)
        return sum