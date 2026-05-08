/* 
   Project: Expert Drug Interaction System (AI202)
   Team Members:
   1. Hamsa Mustafa Aboelghit      - 202400350
   2. Rewan Mamdouh                - 202403264
   3. Mariem Hassan                - 202403199
   4. Yasmen Abdelaziz Ramadan     - 202400477
   5. Omar saleh el abd            - 202400664
*/

% --- Medical Knowledge Base ---

% Defines drugs and their specific medical classes
drug_class(aspirin, nsaid).
drug_class(ibuprofen, nsaid).
drug_class(warfarin, anticoagulant).
drug_class(heparin, anticoagulant).
drug_class(clopidogrel, antiplatelet).
drug_class(lisinopril, ace_inhibitor).
drug_class(amuric, xanthine_oxidase_inhibitor).
drug_class(zyloric, xanthine_oxidase_inhibitor).
drug_class(colchicine, anti_gout).
drug_class(concor, beta_blocker).

% Interaction rules: (Drug A, Drug B, Severity Level, Medical Explanation)
interaction(aspirin, warfarin, severe, 'Increased risk of major bleeding.').
interaction(ibuprofen, warfarin, severe, 'Potential for serious gastrointestinal bleeding.').
interaction(amuric, warfarin, moderate, 'May enhance the anticoagulant effect.').
interaction(concor, insulin, moderate, 'May mask symptoms of hypoglycemia.').
interaction(aspirin, clopidogrel, moderate, 'Increased risk of bleeding, use with caution.').