from udapi.core.node import Node

def is_valid(node: Node):
	form = node.form
	return (
		form.isalpha() and
		len(form) > 1 and
		form.islower() and
		'Typo' not in node.misc and
		'Lang' not in node.misc and
		'Foreign' not in node.misc
	)
