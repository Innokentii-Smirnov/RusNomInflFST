import os
from sys import argv
import warnings
from gen_morph.gramm_systems.gramm_system import GrammaticalSystem
from gen_morph.gramm_forms.linearizer import Linearizer
grammSystemPath = argv[1]
grammSystem = GrammaticalSystem.from_file(grammSystemPath + '.morph')
linearizer = Linearizer.from_file(grammSystemPath + '.lin')
while (lexeme := input()) != '':
  lemma, gramm_type = lexeme.split('+', 2)[:2];
  if gramm_type in grammSystem:
    for gramm_form in grammSystem.get_gramm_forms(gramm_type):
      linearized = linearizer(gramm_type, gramm_form)
      print(lemma + linearized)
  else:
    warnings.warn(f"Incorrect gramm. type '{gramm_type}' for input '{lexeme}'")
