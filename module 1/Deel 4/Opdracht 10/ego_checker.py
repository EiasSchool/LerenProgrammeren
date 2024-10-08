import re
from test_lib import test, report

def extract_text(text:str) -> list:
   marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
   sub_sentences = marked_text.split("|")
   return [s.strip() for s in sub_sentences if s.strip()]

def calculate_ego_score(sub_sentences: list) -> int:
    ego_score = 0
    for sentence in sub_sentences:
        sentence = sentence.lower()
        words = sentence.split(' ')
        if len(words) >= 1 and (words[0] in ('ik', 'mijn') or (len(words) > 1 and words[1] in ('ik', 'mijn'))):
            ego_score += 1
    return ego_score

test_cases = [
    ('Geachte heer/mevrouw, ik ben buitengewoon slim en ik weet dat ik de beste ben.', 3),
    ('Mijn ervaring is indrukwekkend, en ik weet dat ik goed ben.', 2),
    ('De hond is van mij, en ik zorg goed voor hem.', 1),
    ('Het bedrijf is belangrijk omdat het mijn toekomst bepaalt.', 1),
    ('Wij werken samen en we zijn succesvol.', 0),  # No "ik" or "mijn" at start
]

# Run tests
for text, expected_score in test_cases:
    sub_sentences = extract_text(text)
    calculated_score = calculate_ego_score(sub_sentences)
    name = f'test text: "{text[:30]}..."'
    test(name, expected_score, calculated_score)

report()