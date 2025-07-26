import os
from os import path
from os.path import isfile, splitext
from tqdm.auto import tqdm
from udapi.block.read.conllu import Conllu
from package.const import LANG, CORPORA, CATEGORIES
from package.categories import get_categories
from package.util import join
from package.validate import is_valid
data = dict[str, set[str]]()
lemmata = set[str]()
for corpus in CORPORA:
	source = f'../../UD_{LANG}-{corpus}'
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
				if is_valid(node):
					upos = node.upos
					if upos in CATEGORIES:
						feats = node.feats
						categories = get_categories(upos, feats)
						features = [feats[category] for category in categories]
						if (all(feature != '' for feature in features)):
							tag = ''.join('+'+ feature for feature in features)
							lemma = node.lemma
							morpholex = lemma + tag
							if not morpholex in data:
								data[morpholex] = set[str]()
							data[morpholex].add(form)
							lemmata.add(lemma)
result = [(morpholex, join(forms)) for morpholex, forms in data.items()]
result.sort()
target = '../test_data'
os.makedirs(target, exist_ok=True)
os.chdir(target)
with open('in.txt', 'w', encoding='utf-8') as fout:
	for morhpolex, form in result:
		fout.write(morhpolex + '\n')
with open('corr.txt', 'w', encoding='utf-8') as fout:
	for morpholex, form in result:
		fout.write(form + '\n')
with open('lemmata.txt', 'w', encoding='utf-8') as fout:
	for lemma in sorted(lemmata):
		fout.write(lemma + '\n')
