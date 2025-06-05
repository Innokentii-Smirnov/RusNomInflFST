import os, shutil
from os import path
import sys
start_dir = os.getcwd()
sys.path.insert(1, start_dir)
from package.util import split, join
from package.eval import is_correct
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
n_equal = 0
total = 0
with (open(predfile) as fin,
	  open(corrfile) as ref,
	  open('correct.txt', 'w') as corrf,
	  open('errors.txt', 'w') as errf,
	  open('missing.txt', 'w') as mf,
	  open('incomplete.txt', 'w') as incompf,
	  open('extra.txt', 'w') as extraf):
	for corr_line in ref:
		total += 1
		joined_corr = corr_line.rstrip()
		corr: set[str] = split(joined_corr)
		pred = set[str]()
		while ((line := fin.readline().rstrip()) != ''):
			spl = line.split('\t')
			if len(spl) == 2:
				morpholex, generated = spl
				pred.add(postprocess(generated))
			else:
				morpholex, _, mark = spl
				assert mark == '+?', morpholex
				line = fin.readline().rstrip()
				assert line == ''
				break
		joined_pred = join(pred)
		correctness = is_correct(pred, corr)
		equality = (pred == corr)
		if correctness:
			n_correct += 1
			if equality:
				n_equal += 1
				string = '{0:30} {1}'.format(morpholex, joined_pred)
			else:
				extra = pred - corr
				if len(extra) > 0:
					string = '{0:30} {1:30} {2}'.format(
						morpholex, join(extra), joined_corr)
					extraf.write(string + '\n')
				incomp = corr - pred
				if len(incomp) > 0:
					string = '{0:30} {1:30} {2}'.format(
						morpholex, joined_pred, join(incomp))
					incompf.write(string + '\n')
				else:
					if pred.issubset(corr):
						string = '{0:30} {1}'.format(morpholex, joined_pred)
					else:
						string = '{0:30} {1:30} {2}'.format(
						morpholex, joined_pred, joined_corr)
			corrf.write(string + '\n')
			correct.add(string)
		elif len(pred) > 0:
			string = '{0:30} {1:50} {2}'.format(morpholex, joined_pred, joined_corr)
			errf.write(string + '\n')
			errors.add(string)
		else:
			string = '{0:30} {1}'.format(morpholex, joined_corr)
			mf.write(string + '\n')
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
strict_accuracy = 100 * n_equal / total
print('Equality: {0} % ({1} / {2}).'.format(round(strict_accuracy, 2), n_equal, total))
