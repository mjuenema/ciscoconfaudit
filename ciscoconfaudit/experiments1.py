#!/usr/bin/which python

from __future__ import print_function

import ciscoconfparse as ccp

CONFIG = """
!
! test7 - Parents and Siblings
!
line0
!
parent1a
  parent0a
  parent2a
    parent3a
      sibling1
      sibling2
!
parent1b
  parent2b
    parent3b
      sibling2
      sibling3
!
line1
line2
line3
""".strip().split('\n')


cfg = ccp.CiscoConfParse(CONFIG)

cfgline = cfg.find_objects_w_all_children('parent3', ['sibling1'])[0]

#print(cfgline.linenum, cfgline.text)
print('\n'.join(['%4d    %s' % (l.linenum, l.text) for l in cfgline.geneology]))
#print('\n'.join(cfgline.ioscfg))

#print(cfg.find_objects('parent2'))

print(cfgline.re_search_children('sibling1'))
print(cfgline.re_search_children('sibling3'))



