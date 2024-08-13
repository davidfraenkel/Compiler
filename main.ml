open List
open Format
open Lexing
open Parser
open Interp

let usage = "usage: mini-python [options] <file.txt>"

let parseOnly = ref false
let silent = ref false

let spec = [
  "--parse-only", Arg.Set parseOnly, " stop after parsing";
  "-silent", Arg.Unit (fun () -> Lexer.silent := true), "Suppress output";
]

let file = ref None

let setFile filename =
  if not (Filename.check_suffix filename ".txt") then
    raise (Arg.Bad "no .txt extension");
  file := Some filename

let () =
  Arg.parse spec setFile usage; 
    (* (fun x -> raise (Arg.Bad ("Bad argument : " ^ x)))
    "Usage: -silent to suppress output"; *)
  match !file with
  | None ->
    Lexer.conditionalPrint "No file provided\n";
    exit 1
  | Some filename -> 
    let channel = open_in filename in
    let lexbuf = Lexing.from_channel channel in
    try
      let astList = Parser.file Lexer.nextToken lexbuf in
      let interpretedString = interpret astList 0 in
      close_in channel;
      let outChannel = open_out (Filename.remove_extension filename ^ "_result.py") in
      if filename = "for.txt" then
        Printf.fprintf outChannel "from Array import Array"
      else if filename = "fortest.txt" then
        Printf.fprintf outChannel "from Array import Array"
      else 
        Printf.fprintf outChannel "import sys\n";
        Printf.fprintf outChannel "sys.path.append('../../')\n";
        Printf.fprintf outChannel "from Array import Array\n";
        Printf.fprintf outChannel "import random\n\n";
        
        
      Printf.fprintf outChannel "%s\n" interpretedString;
      close_out outChannel;
      printf "Successfully interpreted and wrote the result to %s_result.txt\n" (Filename.remove_extension filename)
    with
    | Sys_error message ->
        printf "Error: %s\n" message
    | Lexer.Lexing_error message ->
        printf "Lexer error: %s\n" message
    | Parser.Error ->
        let (beginError, endError) = (lexeme_start_p lexbuf, lexeme_end_p lexbuf) in
        let line = beginError.pos_lnum in
        let firstChar = beginError.pos_cnum - beginError.pos_bol + 1 in
        let lastChar = endError.pos_cnum - beginError.pos_bol + 1 in
        eprintf "File \"%s\", line %d, characters %d-%d:\n" filename line firstChar lastChar;
        eprintf "(parser) - syntax error@.";
        exit 1
    | End_of_file ->
        printf "End of file\n"
