import re

occurrences: dict = {}

def p_counter(paragraph: str):
    
    count = re.findall("[a-zA-Z_]+", paragraph.lower())
    
    for i in count:
        
        if i not in occurrences:
            
            occurrences[i] = 1
            
        elif i in occurrences:
            
            occurrences[i] += 1
            
    print(dict(sorted(occurrences.items(), key = lambda item: item[1], reverse= True)))


p_counter("La luce del mattino filtrava tra le tende, tingendo la stanza di un caldo bagliore dorato. Il silenzio era interrotto solo dal cinguettio degli uccelli e dal lieve fruscio delle foglie mosse dal vento. Tutto sembrava sospeso, come se il tempo avesse deciso di rallentare per concedere un momento di quiete prima che la giornata iniziasse davvero.")