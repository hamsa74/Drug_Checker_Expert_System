/* 
   Project: Expert Drug Interaction System (AI202)
   Team Members:
   1. Hamsa Mustafa Aboelghit      - 202400350
   2. Rewan Mamdouh                - 202403264
   3. Mariem Hassan                - 202403199
   4. Yasmen Abdelaziz Ramadan     - 202400477
   5. Omar saleh el abd            - 202400664
*/

% --- Inference Rules ---

% Checks if an interaction exists between two drugs in any order
check_interaction(D1, D2) :-
    (interaction(D1, D2, Severity, Desc) ; interaction(D2, D1, Severity, Desc)),
    format('~n[!] Warning: ~w and ~w interaction is ~w.~nDetails: ~w~n', [D1, D2, Severity, Desc]), !.
check_interaction(_, _) :-
    format('~n[+] No known interactions found between these drugs.~n', []).

% Provides clinical advice based on the severity level
recommendation(D1, D2) :-
    (interaction(D1, D2, severe, _) ; interaction(D2, D1, severe, _)),
    format('~nRecommendation: DO NOT combine. Consult physician for alternatives.~n', []), !.
recommendation(D1, D2) :-
    (interaction(D1, D2, moderate, _) ; interaction(D2, D1, moderate, _)),
    format('~nRecommendation: Monitor closely for side effects.~n', []), !.
recommendation(_, _) :-
    format('~nRecommendation: Safe to use together under normal conditions.~n', []).

% Scans a list of drugs (Prescription) for any internal conflicts
check_prescription([]).
check_prescription([H|T]) :-
    check_against_list(H, T),
    check_prescription(T).

% Helper: Compares one drug against the rest of the list
check_against_list(_, []).
check_against_list(D, [H|T]) :-
    (   (interaction(D, H, Severity, _) ; interaction(H, D, Severity, _))
    ->  format('~nAlert: Found ~w interaction between ~w and ~w!~n', [Severity, D, H])
    ;   true
    ),
    check_against_list(D, T).