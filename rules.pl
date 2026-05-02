
% 1. Interaction Check: Checks if two drugs interact and prints details.
check_interaction(D1, D2) :-
    interacts_with(D1, D2, Severity),
    effect_of(D1, D2, Effect),
    format('~n--- Interaction Found ---~n', []),
    format('Severity: ~w~nEffect: ~w~n', [Severity, Effect]), !.
check_interaction(_, _) :-
    format('~nNo known interaction between these drugs.~n', []).

% 2. Severity Recommendation: Gives clinical advice based on severity.
recommendation(D1, D2) :-
    interacts_with(D1, D2, severe),
    format('Recommendation: Do NOT administer together. Consult physician immediately!~n', []), !.
recommendation(D1, D2) :-
    interacts_with(D1, D2, moderate),
    format('Recommendation: Use with caution. Monitor patient closely.~n', []), !.
recommendation(D1, D2) :-
    interacts_with(D1, D2, mild),
    format('Recommendation: Interaction possible. Review dosage.~n', []), !.
recommendation(_, _) :-
    format('Recommendation: Safe to administer together.~n', []).

% 3. Drug Interaction Profile: Prints all interactions for a specific drug.
drug_profile(Drug) :-
    format('~n--- Risk Profile for ~w ---~n', [Drug]),
    findall(Other-Sev, interacts_with(Drug, Other, Sev), List),
    print_profile(List).

print_profile([]) :- format('No known interactions for this medication.~n', []).
print_profile([Drug-Sev|T]) :-
    format('- Interacts with: ~w (Severity: ~w)~n', [Drug, Sev]),
    print_profile(T).

% 4. Severe Interactions Alert: Simulates a real-time pharmacy alert.
severe_alerts :-
    format('~n!!! ALERT: SEVERE COMBINATIONS IN DATABASE !!!~n', []),
    forall(interacts(D1, D2, severe), 
           (effect_of(D1, D2, E), format('* [~w + ~w]: ~w~n', [D1, D2, E]))).

% 5. Prescription Safety Check: Scans a list of drugs for any dangerous pairs.
% This uses recursion to check every possible pair in the list.
check_prescription([]).
check_prescription([_]).
check_prescription([H|T]) :-
    check_against_list(H, T),
    check_prescription(T).

check_against_list(_, []).
check_against_list(D, [H|T]) :-
    (interacts_with(D, H, Severity) -> 
        (effect_of(D, H, Effect),
         format('~n[!] WARNING: ~w and ~w interact! (~w)~nEffect: ~w~n', [D, H, Severity, Effect])) 
    ; true),
    check_against_list(D, T).