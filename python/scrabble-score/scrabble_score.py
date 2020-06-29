scores_list = [
    ("A,E,I,O,U,L,N,R,S,T", 1),
    ("D,G", 2),
    ("B,C,M,P", 3),
    ("F,H,V,W,Y", 4),
    ("K", 5),
    ("J,X", 8),
    ("Q,Z", 10),
]


def score(word):
    scores = {char: score[1] for score in scores_list for char in score[0].split(",")}
    return sum((scores[letter.upper()] for letter in word))