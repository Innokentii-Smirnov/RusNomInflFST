import os
from os import path
import sys
import warnings
start_dir = os.getcwd()
sys.path.insert(1, path.join(start_dir, 'python'))
from gen_morph.gramm_systems.gramm_system import GrammaticalSystem
from gen_morph.gramm_forms.linearizer import Linearizer
grammSystem = GrammaticalSystem.from_file(path.join(start_dir, 'grammSystem', 'RusNomInfl.morph'))
linearizer = Linearizer.from_file(path.join(start_dir, 'grammSystem', 'RusNomInfl.lin'))
while (lexeme := input()) != '':
  lemma, gramm_type = lexeme.split('+', 2)[:2];
  if gramm_type in grammSystem:
    for gramm_form in grammSystem.get_gramm_forms(gramm_type):
      linearized = linearizer(gramm_type, gramm_form)
      print(lemma + linearized)
  else:
    warnings.warn(f"Incorrect gramm. type '{gramm_type}' for input '{lexeme}'")
