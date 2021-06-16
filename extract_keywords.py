# extracting keywords from an input text using Rapid Automatic Keyword Extraction (RAKE) algorithm in Naltural Language ToolKit Library of Python
# this extracts keywords from text, by identifying runs of non-stopwords and then scoring these phrases across the document
# It requires no training, the only input is a list of stop words for a given language, and a tokenizer that splits the text into sentences and sentences into words
# pip install rake-nltk
from rake_nltk import Rake
rake_nltk_var = Rake()
text = "Data science is a broad field of study pertaining to data systems and processes, aimed at maintaining data sets and deriving meaning out of them. Data scientists use a combination of tools, applications, principles and algorithms to make sense of random data clusters. Since almost all kinds of organizations today are generating exponential amounts of data around the world, it becomes difficult to monitor and store this data. Data science focuses on data modelling and data warehousing to track the ever-growing data set. The information extracted through data science applications are used to guide business processes and reach organisational goals."
rake_nltk_var.extract_keywords_from_text(text)
keywords_extracted = rake_nltk_var.get_ranked_phrases()
print(keywords_extracted)