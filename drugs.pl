% --- Part 1: Configuration ---
:- discontiguous drug/1.
:- discontiguous category/2.

% --- Part 2: Knowledge Base (20 Drugs) ---
drug(warfarin).      category(warfarin, anticoagulant).
drug(aspirin).       category(aspirin, antiplatelet).
drug(lisinopril).    category(lisinopril, ace_inhibitor).
drug(digoxin).       category(digoxin, cardiac_glycoside).
drug(amiodarone).    category(amiodarone, antiarrhythmic).
drug(simvastatin).   category(simvastatin, statin).
drug(clopidogrel).   category(clopidogrel, antiplatelet).
drug(ibuprofen).     category(ibuprofen, nsaid).
drug(naproxen).      category(naproxen, nsaid).
drug(celecoxib).     category(celecoxib, nsaid).
drug(metformin).     category(metformin, antidiabetic).
drug(insulin).       category(insulin, antidiabetic).
drug(amoxicillin).   category(amoxicillin, antibiotic).
drug(clarithromycin). category(clarithromycin, antibiotic).
drug(erythromycin).  category(erythromycin, antibiotic).
drug(potassium).     category(potassium, supplement).
drug(contrast_dye).  category(contrast_dye, diagnostic_agent).
drug(grapefruit_juice). category(grapefruit_juice, food_interaction).
drug(spironolactone). category(spironolactone, diuretic).
drug(st_johns_wort). category(st_johns_wort, herbal).

% --- Part 3: Interactions & Effects (10 Pairs) ---
interacts(warfarin, aspirin, severe).
interacts(warfarin, ibuprofen, severe).
interacts(metformin, contrast_dye, severe).
interacts(digoxin, amiodarone, moderate).
interacts(lisinopril, potassium, moderate).
interacts(simvastatin, amiodarone, moderate).
interacts(lisinopril, spironolactone, severe).
interacts(simvastatin, grapefruit_juice, moderate).
interacts(warfarin, st_johns_wort, moderate).
interacts(clarithromycin, digoxin, severe).

interaction_effect(warfarin, aspirin, 'Critical risk of internal bleeding').
interaction_effect(warfarin, ibuprofen, 'High risk of stomach bleeding').
interaction_effect(metformin, contrast_dye, 'Severe risk of lactic acidosis').
interaction_effect(digoxin, amiodarone, 'Increased digoxin blood levels (Toxicity)').
interaction_effect(lisinopril, potassium, 'High potassium levels (Hyperkalemia)').
interaction_effect(simvastatin, amiodarone, 'Muscle breakdown risk (Rhabdomyolysis)').
interaction_effect(lisinopril, spironolactone, 'Life-threatening high potassium levels').
interaction_effect(simvastatin, grapefruit_juice, 'Increased statin concentration in blood').
interaction_effect(warfarin, st_johns_wort, 'Reduced effectiveness of anticoagulant').
interaction_effect(clarithromycin, digoxin, 'Dangerous increase in heart medication levels').



% Symmetry Helper Rules
interacts_with(X, Y, S) :- interacts(X, Y, S).
interacts_with(X, Y, S) :- interacts(Y, X, S).

effect_of(X, Y, E) :- interaction_effect(X, Y, E).
effect_of(X, Y, E) :- interaction_effect(Y, X, E).