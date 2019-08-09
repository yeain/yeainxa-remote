scores = [10,20,30,40]

def total(scores):
    score =0
    for score in scores:
            score += score
    return score


def average(scores):
    return total(score)/len(score)


def test_score():
    assert total(scores) ==  100
    assert average(scores) == 25


