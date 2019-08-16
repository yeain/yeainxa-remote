# if score >= 50:
#     high_scores.append(score)
#




# 1. Test first
def test_less_number():
    assert less_nember(10, 20) == 10
    assert less_number(20, 10) == 10

# 2. Implement
def less_number(x, y):
    if x < y:
        return x
    return y
