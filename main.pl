/* 
   Project: Drug Interaction Checker (AI202)
   Team Members:
   1- Hamsa Mustafa Aboelghit - ID: 202400350 B07
   2- Yasmen Abdelaziz Ramadan Elqady - ID: 202400477 B09
   
*/

/* 
   Project: Drug Interaction Checker (AI202)
   Student: Hamssa - ID: [Your ID]
   File Description: Part 3 - The Interactive System
*/

% Load other files automatically
:- consult('drugs.pl').
:- consult('rules.pl').

% Main entry point
main :-
    format('~n===========================================~n', []),
    format('   Welcome to Al-Shifa Pharmacy System     ~n', []),
    format('===========================================~n', []),
    menu.

menu :-
    format('~n1. Check interaction between two drugs~n', []),
    format('2. Get severity recommendation~n', []),
    format('3. View full interaction profile of a drug~n', []),
    format('4. Run prescription safety check (List)~n', []),
    format('5. View all severe interaction alerts~n', []),
    format('6. Exit the system~n', []),
    format('~nSelect an option (1-6): ', []),
    read(Choice),
    execute_choice(Choice).

% Executing user choices
execute_choice(1) :- 
    format('Enter Drug 1: ', []), read(D1),
    format('Enter Drug 2: ', []), read(D2),
    check_interaction(D1, D2), menu.

execute_choice(2) :- 
    format('Enter Drug 1: ', []), read(D1),
    format('Enter Drug 2: ', []), read(D2),
    recommendation(D1, D2), menu.

execute_choice(3) :- 
    format('Enter Drug Name: ', []), read(D),
    drug_profile(D), menu.

execute_choice(4) :- 
    format('Enter list of drugs (e.g., [aspirin, warfarin].): ', []), read(List),
    check_prescription(List), menu.

execute_choice(5) :- 
    severe_alerts, menu.

execute_choice(6) :- 
    format('~nExiting system... Goodbye!~n', []), !.

execute_choice(_) :- 
    format('Invalid choice. Please try again.~n', []), menu.