testcases = int(input())

for _ in range(testcases):
    a, b = map(int, input().split())
    xk, yk = map(int, input().split())
    xq, yq = map(int, input().split())

    possible_king = set([(xk + a, yk + b),
    (xk + a, yk - b),
    (xk - a, yk + b),
    (xk - a, yk - b),
    (xk + b, yk + a),
    (xk + b, yk - a),
    (xk - b, yk + a),
    (xk - b, yk - a)])

    possible_queen = set([
    (xq + a, yq + b),
    (xq + a, yq - b),
    (xq - a, yq + b),
    (xq - a, yq - b),
    (xq + b, yq + a),
    (xq + b, yq - a),
    (xq - b, yq + a),
    (xq - b, yq - a)])

    print(len(possible_king.intersection(possible_queen)))
