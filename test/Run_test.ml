(* Define test functions here *)
let insertion_sort () = (* ... *)
let optimal_bst () = (* ... *)
(* Define all other test functions similarly *)

(* List all test functions in the order they need to be executed *)
let tests = [
  ("Insertion-sort", insertion_sort);
  ("Optimal-BST", optimal_bst);
  (* Add all other test functions in similar tuples *)
]

(* Function to run all tests *)
let run_tests test_list =
  List.iter (fun (name, test_func) ->
    Printf.printf "Running %s...\n" name;
    test_func ();
    Printf.printf "Test %s completed.\n" name
  ) test_list

(* Call run_tests with the list of tests *)
let () = run_tests tests
