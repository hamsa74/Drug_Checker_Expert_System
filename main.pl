/* 
   Project: Expert Drug Interaction System (AI202)
   Team Members:
   1. Hamsa Mustafa Aboelghit      - 202400350
   2. Rewan Mamdouh                - 202403264
   3. Mariem Hassan                - 202403199
   4. Yasmen Abdelaziz Ramadan     - 202400477
   5. Omar saleh el abd            - 202400664
*/

% --- Main Menu Interface ---

% Starts the system and displays the header
main :-
    shell('cls'), % Clears the terminal screen
    format('-------------------------------------------~n', []),
    format('      AL-SHIFA PHARMACY MANAGEMENT SYSTEM  ~n', []),
    format('-------------------------------------------~n', []),
    menu.

% Displays available options to the user
menu :-
    format('~n1. Check Drug Interaction~n', []),
    format('2. Clinical Recommendation~n', []),
    format('3. Prescription Scan (Batch)~n', []),
    format('4. Exit System~n', []),
    format('~nSelection (1-4) followed by a dot (.): ', []),
    read(Choice),
    execute_choice(Choice).

% Option 1: One-to-one drug check
execute_choice(1) :- 
    format('~nDrug 1: ', []), read(D1),
    format('Drug 2: ', []), read(D2),
    check_interaction(D1, D2), return_to_main.

% Option 2: Get medical advice
execute_choice(2) :- 
    format('~nDrug 1: ', []), read(D1),
    format('Drug 2: ', []), read(D2),
    recommendation(D1, D2), return_to_main.

% Option 3: Check a list of multiple drugs
execute_choice(3) :- 
    format('~nEnter list (e.g. [aspirin, warfarin].): ', []), read(L),
    check_prescription(L), return_to_main.

% Option 4: Close the system
execute_choice(4) :- 
    format('~nExiting system...~n', []), halt.

% Handle invalid inputs
execute_choice(_) :- 
    format('~nInvalid entry.~n', []), menu.

% Utility to pause before returning to main menu
return_to_main :-
    format('~nPress any key followed by a dot (.) to continue: ', []),
    read(_),
    main.