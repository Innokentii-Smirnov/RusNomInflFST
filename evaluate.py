import os, shutil
from os import path
def postprocess(morpholex: str) -> str:
	return morpholex.replace('\u0301', '').replace('|', '').replace('ё', 'е')
predfile = '../Morphonology/ConvToOrth/out.txt'
corrfile = '../corr.txt'
target = 'test_result'
os.makedirs(target, exist_ok=True)
os.chdir(target)
if path.exists('correct.txt'):
	with open('correct.txt') as fin:
		old_correct = set(map(str.rstrip, fin))
else:
	old_correct = set()
if path.exists('errors.txt'):
	with open('errors.txt') as fin:
		old_errors = set(map(str.rstrip, fin))
else:
	old_errors = set()
correct = set()
errors = set()
n_correct = 0
total = 0
with open(predfile) as fin, open(corrfile) as ref, open('correct.txt', 'w') as corrf, open('errors.txt', 'w') as errf, open('missing.txt', 'w') as mf:
	it = iter(ref)
	new_morpholex = True
	for line in fin:
		if new_morpholex:
			corr = next(it).rstrip()
			new_morpholex = False
		line = line.rstrip()
		if line != '':
			total += 1
			spl = line.split('\t')
			if len(spl) == 2:
				morpholex, generated = spl
				if postprocess(generated) == corr:
					string = '{0:30} {1}'.format(morpholex, generated)
					corrf.write(string + '\n')
					correct.add(string)
					n_correct += 1
				elif generated != '+?':
					string = '{0:30} {1:50} {2}'.format(morpholex, generated, corr)
					errf.write(string + '\n')
					errors.add(string)
			else:
				morpholex, _, mark = spl
				assert mark == '+?', morpholex
				string = '{0:30} {1}'.format(morpholex, corr)
				mf.write(string + '\n')
		else:
			new_morpholex = True
new_correct = sorted(correct - old_correct)
print('New correct: {0}.'.format(len(new_correct)))
new_errors = sorted(errors - old_errors)
if len(new_errors) == 0:
	print('No new errors.')
else:
	print('New errors: {0}.'.format(len(new_errors)))
with open('new_correct.txt', 'w') as fout:
	for string in new_correct:
		fout.write(string + '\n')
with open('new_errors.txt', 'w') as fout:
	for string in new_errors:
		fout.write(string + '\n')
accuracy = 100 * n_correct / total
print('Accuracy: {0} % ({1} / {2}).'.format(round(accuracy, 2), n_correct, total))
