{
open Lexing
open Ast
open Parser

exception Lexing_error of string

let silent = ref false

let conditionalPrint str = if not !silent then print_string str

let stringBuff = Buffer.create 256

let isPrintable character = 
  let asciiCode = Char.code character in
  asciiCode >= 32 && asciiCode <= 126  (* Printable ASCII range *)

let charForBackslash = function
  | 'n' -> '\n'
  | 'r' -> '\r'
  | 'b' -> '\b'
  | 't' -> '\t'
  | character -> character

let keywordTable = [
  "for", FOR;
  "to", TO;
  "downto", DOWNTO;
  "swap", SWAP;
  "exchange", EXCHANGE;
  "with", WITH;

  "low", LOW;
  "high", HIGH;

  (*If Statements*)
  "if", IF;
  "else", ELSE;
  "elseif", ELSEIF;

  (*Simple Stmt*)
  "print", PRINT;
  "return", RETURN;
  "error", ERROR;
  "length", LENGTH;
  "RANDOM", RANDOM;
  "random", RANDOM;

  (* While *)
  "while", WHILE;

  (* Matrix & array *)
  "let", LET;
  "matrix", MATRIX;
  "array", ARRAY;
  "arrays", ARRAY;
  "table", TABLE;
  "tables", TABLE;
  "columns", COLUMNS;
  "rows", ROWS;


  (* Sort *)
  "sort", SORT;

  (* Insert *)
  "insert", INSERT;
  "into", INTO;
  "all", ALL;
  "items", ITEMS;
  "in", IN;
  "root-list", ROOTLIST;
]

let idOrKeyword = 
  let hashTable = Hashtbl.create 50 in
  List.iter (fun (keywordString, keywordToken) -> Hashtbl.add hashTable keywordString keywordToken) keywordTable;
  fun searchString ->
    try 
      let found = Hashtbl.find hashTable searchString in
      if not !silent then printStringYellow ("keyword: " ^ searchString ^ " ");
      found
    with Not_found ->
      if not !silent then printStringBlue ("Ident: " ^ searchString ^ " ");
      IDENT searchString


let debugLines = ref 2;;

let indentStack = ref [0]  (* indentation stack *)

let rec unindentTo indentLevel = 
  match !indentStack with
  | stackHead :: _ when stackHead = indentLevel -> [] (* If indentLevel is at head *)
  | stackHead :: iStack when stackHead > indentLevel -> indentStack := iStack; END :: unindentTo indentLevel (* "END" (of block) is prepended to return of the call *)
  | _ -> raise (Lexing_error "bad indentation")

let updateStackTo indentLevel =
  match !indentStack with
  | stackHead :: _ when stackHead < indentLevel ->
    indentStack := indentLevel :: !indentStack;
    [NEWLINE; BEGIN]
  | _ ->
    NEWLINE :: unindentTo indentLevel
}

let letter = ['a'-'z' 'A'-'Z']
let digit = ['0'-'9']
let ident = (letter | '_') (letter | digit | '_')*
let integer = '0' | ['1'-'9'] digit* 
let space = ' ' | '\t'




rule nextTokens = parse
  | '\n'                                { if not !silent then (printStringRed "\nLine: "; print_int !debugLines; print_string "  "); debugLines := !debugLines + 1; new_line lexbuf; updateStackTo (indentation lexbuf) }
  | (space)+                            { nextTokens lexbuf }

  (* Special characters start *)
  | "×"                                 { if not !silent then printStringMagenta " CROSS "; [CROSS] }
  | "cross"                             { if not !silent then printStringMagenta " CROSS "; [CROSS] }
  | "∞"                                 { if not !silent then printStringMagenta " Infinity "; [INFINITY] }
  | "inf"                               { if not !silent then printStringMagenta " Infinity "; [INFINITY] }
  | "⋅"                                 { if not !silent then printStringMagenta " Times "; [TIMES] }
  | "*"                                 { if not !silent then printStringMagenta " Times "; [TIMES] }
  (* Special characters end *)

  (* Math *)
  | '='                                 { if not !silent then printStringMagenta " Equal "; [EQUAL] }
  | '>'                                 { if not !silent then printStringMagenta " GreaterThan "; [GT] }
  | '<'                                 { if not !silent then printStringMagenta " LessThan "; [LT] }
  | '-'                                 { if not !silent then printStringMagenta " Minus "; [MINUS] }
  | '+'                                 { if not !silent then printStringMagenta " Plus "; [PLUS] }
  | '/'                                 { if not !silent then printStringMagenta " Divide "; [DIVIDE] }
  | "//"                                { if not !silent then printStringMagenta " DivideFloor "; [DIVIDEFLOOR] }
  | '%'                                 { if not !silent then printStringMagenta " Mod "; [MOD] }
  | '^'                                 { if not !silent then printStringMagenta " Power "; [POWER] }
  | "∅"                                 { if not !silent then printStringMagenta " Empty_set "; [EMPTYSET] }
  | "≤"                                 { if not !silent then printStringMagenta " LessThanEqual "; [LTE] }
  | "≥"                                 { if not !silent then printStringMagenta " GreaterThanEqual "; [GTE] }
  | "≠"                                 { if not !silent then printStringMagenta " NotEqual "; [NEQ] }
  | "∈"                                 { if not !silent then printStringMagenta " In "; [IN] }
  | "⋃"                                 { if not !silent then printStringMagenta " Union "; [UNION] }
  | "⋂"                                 { if not !silent then printStringMagenta " Intersection "; [INTERSECT] }
  | "π"                                 { if not !silent then printStringMagenta " Pi "; [PI] }



  (* Logical *)
  | "and"                               { if not !silent then printStringMagenta " And "; [AND] }
  | "or"                                { if not !silent then printStringMagenta " Or "; [OR] }

  (* Everything else *)
  | "NIL"                               { if not !silent then printStringMagenta " NIL"; [NIL] }
  | "be" (space)+ "a" (space)+ "new"    { if not !silent then printStringMagenta " BeANew "; [BE_A_NEW] }
  | "be" (space)+ "new"              { if not !silent then printStringMagenta " BeNew "; [BE_A_NEW] }
  | "monotonically" (space)+ "ascending" (space)+ "order" (space)+ "by" (space)+ "weight" { if not !silent then print_string "MONOTONICALLY_ASCENDING_ORDER_BY_WEIGHT "; [MONOTONICALLY_ASCENDING_ORDER_BY_WEIGHT] }
  | "monotonically" (space)+ "decreasing" (space)+ "order" (space)+ "by" (space)+ "weight" { if not !silent then print_string "MONOTONICALLY_DESCENDING_ORDER_BY_WEIGHT "; [MONOTONICALLY_DECREASING_ORDER_BY_WEIGHT] }
  | '['                                 { if not !silent then printStringMagenta " LBracket "; [LBRACKET] }
  | ']'                                 { if not !silent then printStringMagenta " RBracket "; [RBRACKET] }
  | '('                                 { if not !silent then printStringMagenta " LParen "; [LPAREN] }
  | ')'                                 { if not !silent then printStringMagenta " RParen "; [RPAREN] }
  | '{'                                 { if not !silent then printStringMagenta " LBrace "; [LBRACE] }
  | '}'                                 { if not !silent then printStringMagenta " RBrace "; [RBRACE] }
  | '.'                                 { if not !silent then printStringMagenta " Dot "; [DOT] }
  | ".."                                { if not !silent then printStringMagenta " DOTDOT "; [DOTDOT] }
  | ','                                 { if not !silent then printStringMagenta " Comma "; [COMMA] }
  | '"'                                 { Buffer.clear stringBuff; string lexbuf; [STRING (Buffer.contents stringBuff)] }
  | ident as id                         { [idOrKeyword id] }
  | integer as s                        { if not !silent then printIntBlue s;  [CST (Cint(int_of_string s))] }
  | eof                                 { if not !silent then print_endline "eof\n\n"; NEWLINE :: unindentTo 0 @ [EOF] }
  | _ as character
      {
        let position = Lexing.lexeme_start_p lexbuf in
        let charInfo =
          if isPrintable character then
            Printf.sprintf "illegal character: '%c' (ASCII code: %d)" character (Char.code character)
          else
            Printf.sprintf "illegal character with ASCII code: %d" (Char.code character)
        in
        Printf.eprintf "\x1b[31mError on line %d, column %d: %s\x1b[0m\n"
          position.pos_lnum (position.pos_cnum - position.pos_bol + 1) charInfo;
        raise (Lexing_error charInfo)
      }
and indentation = parse
  | (space)* '\n'
      { new_line lexbuf; indentation lexbuf }
  | space* as s
      { String.length s }


and string = parse
  | '"'                     { () }  (* End of string literal *)
  | '\\' (['\\' '\'' '"' 'n' 't' 'b' 'r' ' '] as c)   { Buffer.add_char stringBuff (charForBackslash c); string lexbuf }
  | _ as c                  { Buffer.add_char stringBuff c; string lexbuf }

  {

let nextToken =
    let tokens = Queue.create () in (* next tokens to emit *)
    fun lexerBuffer ->
      if Queue.is_empty tokens then begin
        let lexedTokens = nextTokens lexerBuffer in
        List.iter (fun inputToken -> Queue.add inputToken tokens) lexedTokens
      end;
      Queue.pop tokens
}
