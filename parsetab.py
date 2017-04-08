
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NAME VAR NUMBER ID PLUS MINUS MULTIPLY DIVIDE COMMA COLON PARANOPEN PARANCLOSE FLOWEROPEN FLOWERCLOSE EQUAL GREATER LESSER GREATEREQ LESSEREQ EQEQ NOTEQ AND OR FOR XRANGE RANGE IN PRINT IFstart : assign start\n            | fLoop start\n            | assign\n            | fLoop stmtstmt : PRINT VARassign : VAR EQUAL expr expr : expr PLUS term\n            | expr MINUS term\n            | term term : term MULTIPLY factor\n            | term DIVIDE factor\n            | factor factor : VAR\n              | NUMBER fLoop : FOR innerinner : PARANOPEN VAR IN rangeSpec PARANCLOSE COLON\n             | VAR IN rangeSpec COLON rangeSpec : RANGE PARANOPEN expr COMMA expr PARANCLOSE\n                 | XRANGE PARANOPEN expr PARANCLOSE '
    
_lr_action_items = {'MULTIPLY':([17,19,20,21,34,35,36,37,],[26,-14,-12,-13,-10,-11,26,26,]),'DIVIDE':([17,19,20,21,34,35,36,37,],[27,-14,-12,-13,-10,-11,27,27,]),'FOR':([0,1,5,10,17,18,19,20,21,33,34,35,36,37,41,],[2,2,2,-15,-9,-6,-14,-12,-13,-17,-10,-11,-7,-8,-16,]),'PARANOPEN':([2,23,24,],[9,31,32,]),'XRANGE':([16,22,],[23,23,]),'EQUAL':([4,],[12,]),'NUMBER':([12,26,27,28,29,31,32,43,],[19,19,19,19,19,19,19,19,]),'PRINT':([1,10,33,41,],[8,-15,-17,-16,]),'RANGE':([16,22,],[24,24,]),'COLON':([25,38,42,45,],[33,41,-19,-18,]),'COMMA':([17,19,20,21,34,35,36,37,40,],[-9,-14,-12,-13,-10,-11,-7,-8,43,]),'IN':([11,15,],[16,22,]),'VAR':([0,1,2,5,8,9,10,12,17,18,19,20,21,26,27,28,29,31,32,33,34,35,36,37,41,43,],[4,4,11,4,14,15,-15,21,-9,-6,-14,-12,-13,21,21,21,21,21,21,-17,-10,-11,-7,-8,-16,21,]),'PLUS':([17,18,19,20,21,34,35,36,37,39,40,44,],[-9,28,-14,-12,-13,-10,-11,-7,-8,28,28,28,]),'MINUS':([17,18,19,20,21,34,35,36,37,39,40,44,],[-9,29,-14,-12,-13,-10,-11,-7,-8,29,29,29,]),'PARANCLOSE':([17,19,20,21,30,34,35,36,37,39,42,44,45,],[-9,-14,-12,-13,38,-10,-11,-7,-8,42,-19,45,-18,]),'$end':([3,5,6,7,13,14,17,18,19,20,21,34,35,36,37,],[0,-3,-4,-2,-1,-5,-9,-6,-14,-12,-13,-10,-11,-7,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([12,28,29,31,32,43,],[17,36,37,17,17,17,]),'fLoop':([0,1,5,],[1,1,1,]),'expr':([12,31,32,43,],[18,39,40,44,]),'stmt':([1,],[6,]),'start':([0,1,5,],[3,7,13,]),'rangeSpec':([16,22,],[25,30,]),'inner':([2,],[10,]),'factor':([12,26,27,28,29,31,32,43,],[20,34,35,20,20,20,20,20,]),'assign':([0,1,5,],[5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> assign start','start',2,'p_start','plyYacc.py',10),
  ('start -> fLoop start','start',2,'p_start','plyYacc.py',11),
  ('start -> assign','start',1,'p_start','plyYacc.py',12),
  ('start -> fLoop stmt','start',2,'p_start','plyYacc.py',13),
  ('stmt -> PRINT VAR','stmt',2,'p_stmt','plyYacc.py',17),
  ('assign -> VAR EQUAL expr','assign',3,'p_assign','plyYacc.py',20),
  ('expr -> expr PLUS term','expr',3,'p_expr','plyYacc.py',23),
  ('expr -> expr MINUS term','expr',3,'p_expr','plyYacc.py',24),
  ('expr -> term','expr',1,'p_expr','plyYacc.py',25),
  ('term -> term MULTIPLY factor','term',3,'p_term','plyYacc.py',28),
  ('term -> term DIVIDE factor','term',3,'p_term','plyYacc.py',29),
  ('term -> factor','term',1,'p_term','plyYacc.py',30),
  ('factor -> VAR','factor',1,'p_factor','plyYacc.py',33),
  ('factor -> NUMBER','factor',1,'p_factor','plyYacc.py',34),
  ('fLoop -> FOR inner','fLoop',2,'p_fLoop','plyYacc.py',37),
  ('inner -> PARANOPEN VAR IN rangeSpec PARANCLOSE COLON','inner',6,'p_inner','plyYacc.py',41),
  ('inner -> VAR IN rangeSpec COLON','inner',4,'p_inner','plyYacc.py',42),
  ('rangeSpec -> RANGE PARANOPEN expr COMMA expr PARANCLOSE','rangeSpec',6,'p_rangeSpec','plyYacc.py',45),
  ('rangeSpec -> XRANGE PARANOPEN expr PARANCLOSE','rangeSpec',4,'p_rangeSpec','plyYacc.py',46),
]