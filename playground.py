import json
import urllib
import urllib.request


sentences = []
labels = []
# YOUR CODE HERE

with open("sarcasm.json", 'r') as f:
    datastore = json.load(f)

for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])

print(sentences[0])