%{
  open Ast
  let silent = ref false

  let conditionalPrint msg = 
    if !silent then print_endline msg
%}

%token EMPTYSET LTE GTE NEQ UNION INTERSECT PI MOD TIMES DIVIDE DIVIDEFLOOR

%token <Ast.constant> CST 
%token EOF END BEGIN NEWLINE 
%token IF ELSE ELSEIF
%token PRINT RETURN
%token WHILE FOR TO DOWNTO
%token SWAP WITH LENGTH EXCHANGE
%token GT LT MINUS PLUS EQUAL INFINITY
%token LET BE_A_NEW CROSS MATRIX COLUMNS ROWS ARRAY TABLE
%token LBRACKET RBRACKET DOT DOTDOT COMMA LPAREN RPAREN LBRACE RBRACE
%token RANDOM ERROR LOW HIGH
%token MONOTONICALLY_ASCENDING_ORDER_BY_WEIGHT SORT
%token MONOTONICALLY_DECREASING_ORDER_BY_WEIGHT 
%token NIL                                                          (* NULL   *)
%token INSERT INTO ALL ITEMS IN ROOTLIST                             (* INSERT *)
%token AND OR POWER
%token <string> STRING 
%token <string> IDENT
%start file
%type <Ast.file> file
%%


file:
  | NEWLINE? b = nonempty_list(stmt) NEWLINE? EOF
    { Sblock b }
;

(* indentation *)
suite:
  | s = simpleStmt NEWLINE
      { s }
  | NEWLINE BEGIN l = nonempty_list(stmt) END
      { Sblock l }
;

mathOperator:
  | TIMES
  { Bmul }

  | PLUS
  { Badd }
  
  | MINUS
  { Bsub }
  
  | GT
  { Bgt }

  | POWER
  { Bpow }
  
  | LT
  { Blt }

  | MOD
  { Bmod }

  | DIVIDE
  { Bdiv }

  | LTE
  { Blte }

  | GTE
  { Bgte }

  | NEQ
  { Bneq }

  | IN
  { Bin }

  | UNION
  { Bun }

  | INTERSECT
  { Binter }

  | DIVIDEFLOOR
  { Bfloordiv }

;

objectConstant:
  | c = CST
  { Ocst c }

  | i = ident
  { Oident i }

  | pi = PI
  { Ocst Cpi }
;

eDotnotation:
  | i = ident DOT ROWS
  { Erows(i) }

  | i = ident DOT COLUMNS
  { Ecolumns(i) }

  | i = ident DOT LENGTH
  { Elength(i) }

  | i = ident DOT oConst = objectConstant
  { Eobject(i, oConst) }
;


expr:
  | EMPTYSET
  { Memptyset }

  | NIL 
  { Ecst Cnil }

  | INFINITY 
  { Ecst Cinfinity }

  | PI
  { Ecst Cpi }

  | MINUS INFINITY
  { Ecst CminusInfinity }

  | c = CST 
  { Ecst c }

  | dot = eDotnotation 
  { dot }


  | id = ident
	{ Eident id }

  | s = STRING 
	{ Ecst (Cstring s) }

  | e1 = expr m = mathOperator e2 = expr 
	{ Ebinop(m, e1, e2) }

  | LBRACE eList = exprList RBRACE 
  { Eset(eList) }

  | LOW LBRACKET e1 = expr RBRACKET
  { Elow(e1) }

  | HIGH LBRACKET e1 = expr RBRACKET
  { Ehigh(e1) }

  | e1 = expr EQUAL EQUAL e2 = expr 
	{ Ebinop(Beq, e1, e2) }

  | e1 = expr AND e2 = expr
  { Ebinop(Band, e1, e2) }

  | e1 = expr OR e2 = expr
  { Ebinop(Bor, e1, e2) }

  | i = ident LBRACKET e = expr RBRACKET
	{ Earray(i, e) }

  | i = ident LBRACKET e1 = expr COMMA e2 = expr RBRACKET
  { Etable(i, e1, e2) }

  | i = ident LBRACKET e1 = expr RBRACKET LBRACKET e2 = expr RBRACKET
	{ Ematrix(i, e1, e2) }


  | RANDOM LPAREN e1 = expr COMMA e2 = expr RPAREN
  { Erandom(e1, e2) }

  | i = ident LPAREN eList = exprList RPAREN
  { EfunctionCall(i, eList) }


  | e1 = expr DOTDOT e2 = expr
  { Erange(e1, e2) }  
  ;

initArray:
  (* Array *)
  | id = ident LBRACKET expr1 = expr RBRACKET
  { 
    Einitarray(id, expr1) 
  }
  ;

initTable:
  | id = ident LBRACKET expr1 = expr COMMA expr2 = expr RBRACKET
  { 
    conditionalPrint "Einittable -> ";
    Einittable(id, expr1, expr2);
  }
  ;

simpleStmt:
  (* Init array *)
  | LET array = arrayList BE_A_NEW ARRAY {
    conditionalPrint "SinitArrayList -> ";
    SinitArrayList(array)
  }
  | LET table = table_list BE_A_NEW TABLE {
    conditionalPrint "SinitTable -> ";
    SinitTableList(table)
  }

  (* Init statments *)
  | LET i = ident BE_A_NEW e1 = expr CROSS e2 = expr MATRIX {
    conditionalPrint "Sinitmatrix -> ";
	  Sinitmatrix(i, e1, e2)
	}

  | PRINT eList = exprList { 
    conditionalPrint "Sprint -> ";
    Sprint(eList) 
  }

  | SWAP e1 = expr WITH e2 = expr {
    conditionalPrint "Sswap -> ";
	  Sswap(e1, e2)
	}
  | EXCHANGE e1 = expr WITH e2 = expr {
    conditionalPrint "Sexchange -> ";
	  Sexchange(e1, e2)
	}
  | i = ident LBRACKET e1 = expr RBRACKET LBRACKET e2 = expr RBRACKET {
    conditionalPrint "SassignMatrix -> ";
	  Smatrix(i, e1, e2)
	}
  | e1 = expr EQUAL e2 = expr {
    conditionalPrint "Sassign -> ";
    Sassign(e1, e2);
  }

  | RETURN eList = exprList {
    conditionalPrint "Sreturn -> ";
	  Sreturn(eList)
	}

  | RETURN LPAREN eList = exprList RPAREN {
    conditionalPrint "Sreturn -> ";
    Sreturn(eList)
  }

  | ERROR e1 = expr {
    conditionalPrint "Serror -> ";
    Serror(e1)
  }
  | SORT expr1 = expr INTO MONOTONICALLY_ASCENDING_ORDER_BY_WEIGHT expr2 = expr{
    conditionalPrint "SsortA -> ";
    SsortA(expr1, expr2)
  }
  | SORT expr1 = expr INTO MONOTONICALLY_DECREASING_ORDER_BY_WEIGHT expr2 = expr {
    conditionalPrint "SsortD -> ";
    SsortD(expr1, expr2)
  }
  | INSERT expr1 = expr INTO expr2 = expr {
    conditionalPrint "Sinsert -> ";
    Sinsert(expr1, expr2)
  }
  | INSERT ALL ITEMS IN expr1 = expr INTO expr2 = expr {
    conditionalPrint "SinsertAll -> ";
    SinsertAll(expr1, expr2)
  }
  | INSERT expr1 = expr INTO expr2 = expr ROOTLIST {
    conditionalPrint "SinsertRoot -> ";
    SinsertRoot(expr1, expr2)
  }
;

stmt:
  | s = simpleStmt NEWLINE
    { s }
  

  // FUNCTION DEFINITIONS
  | id = ident LPAREN eList = exprList RPAREN NEWLINE {
    SfuncCall (id, eList)
  }
  | id = ident LPAREN eList = exprList RPAREN s = suite {
    Sfunc (id, eList, s)
  }

  
  // FOR LOOPS
  | FOR id = ident EQUAL e1 = expr TO e2 = expr s = suite {
	  Sfor(id, e1, e2, s)
	}
  | FOR id = ident EQUAL e1 = expr DOWNTO e2 = expr s = suite {
	  Sford(id, e1, e2, s)
	}

  // IF STATEMENTS
  | IF e1 = expr s = suite stmt = stmt 
    {Sifnest(e1, s, stmt) }
  | IF e1 = expr s = suite 
    { Sif(e1, s) }
  | ELSEIF e1 = expr s = suite stmt = stmt
    { Selseifnest(e1, s, stmt) }
  | ELSEIF e1 = expr s = suite 
    { Selseif(e1, s) }
  | ELSE s = suite 
    { Selse(s) }

  
  // WHILE LOOPS
  | WHILE e1 = expr s = suite {
	  Swhile(e1, s)
	}
  ;

ident:
  | id = IDENT {
    { loc = ($startpos, $endpos); id } 
  }
;

table_list:
  | e = initTable { [e] }
  | e = initTable AND expr1 = initTable { [e; expr1] }
  | e = initTable COMMA AND expr1 = initTable { [e; expr1] } 
  | e = initTable COMMA es = table_list { e :: es }

arrayList:
  | e = initArray { [e] }
  | e = initArray AND expr1 = initArray { [e; expr1] }
  | e = initArray COMMA AND expr1 = initArray { [e; expr1] } 
  | e = initArray COMMA es = arrayList { e :: es }
;

exprList:
  | id = expr { [id] } 
  | id = expr COMMA ids = exprList { id :: ids } 
  | id = expr ids = exprList { id :: ids } 
;
