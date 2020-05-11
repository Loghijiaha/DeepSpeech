# -*- coding: utf-8 -*-
import kenlm
model = kenlm.LanguageModel('lm.binary')
print model.score(u'ஓத')
