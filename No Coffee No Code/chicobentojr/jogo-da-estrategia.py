if __name__ == '__main__':
    players, rounds = [int(x) for x in input().split(' ')]
    points = [int(x) for x in input().split(' ')]
    results = []
    for player in range(players):
        results.append((player, sum(points[player::players])))
    final_results = sorted(results, key=lambda element: (element[1], element[0]), reverse=True)
    winner = final_results[0]
    print(winner[0] + 1)
