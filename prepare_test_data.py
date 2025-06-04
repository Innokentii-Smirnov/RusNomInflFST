import os
from os.path import join, isfile, splitext
from tqdm.auto import tqdm
from udapi.block.read.conllu import Conllu
categories = {
	'ADJ': ['Gender', 'Number', 'Case'],
	'NOUN': ['Number', 'Case'],
	'NOUN': ['Number', 'Case'],
	'DET': ['Case', 'Gender'],
	'PRON': ['Case'],
	'NUM': ['Case'],
}
olddir = os.getcwd()
data = set[tuple[str, str]]()
sources = ['../UD_Russian-SynTagRus', '../UD_Russian-Taiga']
for source in sources:
	print(source)
	os.chdir(source)
	files = [name for name in os.listdir('.')
			if isfile(name) and splitext(name)[1] == '.conllu']
	conllu = Conllu(files=files)
	documents = conllu.read_documents()
	for document in documents:
		for tree in tqdm(document.trees):
			for node in tree.descendants:
				form = node.form
				lemma = node.lemma
				upos = node.upos
				feats = node.feats
				if upos in categories:
					cats = categories[upos]
					if upos == 'NUM' and 'Gender' in feats:
						cats = ['Gender'] + cats
					features = ['+' + node.feats[category]
					for category in cats]
					if (all(feature != '+' for feature in features) and form.isalpha()
					and len(form) > 1 and form.islower()):
						tag = ''.join(features)
						data.add((form, lemma + tag))
result = sorted(data, key=lambda x: x[1])
os.chdir(olddir)
with open('in.txt', 'w', encoding='utf-8') as fout:
	for form, analysis in result:
		fout.write(analysis + '\n')
with open('corr.txt', 'w', encoding='utf-8') as fout:
	for form, analysis in result:
		fout.write(form + '\n')
