
(* The type of tokens. *)

type token = 
  | WITH
  | WHILE
  | UNION
  | TO
  | TIMES
  | TABLE
  | SWAP
  | STRING of (string)
  | SORT
  | RPAREN
  | ROWS
  | ROOTLIST
  | RETURN
  | RBRACKET
  | RBRACE
  | RANDOM
  | PRINT
  | POWER
  | PLUS
  | PI
  | OR
  | NIL
  | NEWLINE
  | NEQ
  | MONOTONICALLY_DECREASING_ORDER_BY_WEIGHT
  | MONOTONICALLY_ASCENDING_ORDER_BY_WEIGHT
  | MOD
  | MINUS
  | MATRIX
  | LTE
  | LT
  | LPAREN
  | LOW
  | LET
  | LENGTH
  | LBRACKET
  | LBRACE
  | ITEMS
  | INTO
  | INTERSECT
  | INSERT
  | INFINITY
  | IN
  | IF
  | IDENT of (string)
  | HIGH
  | GTE
  | GT
  | FOR
  | EXCHANGE
  | ERROR
  | EQUAL
  | EOF
  | END
  | EMPTYSET
  | ELSEIF
  | ELSE
  | DOWNTO
  | DOTDOT
  | DOT
  | DIVIDEFLOOR
  | DIVIDE
  | CST of (Ast.constant)
  | CROSS
  | COMMA
  | COLUMNS
  | BE_A_NEW
  | BEGIN
  | ARRAY
  | AND
  | ALL

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val file: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.stmt)
