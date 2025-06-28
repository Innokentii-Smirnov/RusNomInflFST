from udapi.core.node import Node

def is_valid(node: Node):
	form = node.form
	return (
		form.isalpha() and
		len(form) > 1 and
		form.islower() and
		'Typo' not in node.feats and
		'Abbr' not in node.feats and
		'Foreign' not in node.feats and
		'Lang' not in node.misc
	)
