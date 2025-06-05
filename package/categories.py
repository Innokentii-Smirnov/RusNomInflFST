from .const import CATEGORIES
from udapi.core.feats import Feats

def get_categories(upos: str, feats: Feats):
	if upos == 'ADJ' and feats['Case'] == 'Acc':
		return CATEGORIES['ADJ-Animacy']
	if upos == 'NUM' and 'Gender' in feats:
		return CATEGORIES['NUM-Gender']
	return CATEGORIES[upos]
