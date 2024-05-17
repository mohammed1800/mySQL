#Write a program to solve the weighted interval scheduling problem
class Interval:
    def __init__(self, start, finish, weight):
        self.start = start
        self.finish = finish
        self.weight = weight

def find_previous_non_overlapping(intervals):
    previous = []
    for i in range(len(intervals)):
        for j in range(i - 1, -1, -1):
            if intervals[j].finish <= intervals[i].start:
                previous.append(j)
                break
        else:
            previous.append(None)
    return previous

def weighted_interval_scheduling(intervals):
    intervals.sort(key=lambda x: x.finish)
    previous = find_previous_non_overlapping(intervals)
    dp = [0] * len(intervals)

    # Base case
    dp[0] = intervals[0].weight

    # Fill the dp table
    for i in range(1, len(intervals)):
        weight_with_i = intervals[i].weight
        if previous[i] is not None:
            weight_with_i += dp[previous[i]]
        dp[i] = max(weight_with_i, dp[i-1])

    # Reconstruct the solution
    solution = []
    i = len(intervals) - 1
    while i >= 0:
        if intervals[i].weight + (0 if previous[i] is None else dp[previous[i]]) >= dp[i-1]:
            solution.append(intervals[i])
            i = previous[i] if previous[i] is not None else -1
        else:
            i -= 1

    solution.reverse()
    return dp[-1], solution

# Example usage
if __name__ == "__main__":
    intervals = [
        Interval(1, 3, 5),
        Interval(2, 5, 6),
        Interval(4, 6, 5),
        Interval(7, 8, 7),
        Interval(6, 9, 8)
    ]

    max_weight, selected_intervals = weighted_interval_scheduling(intervals)

    print("Maximum Weight:", max_weight)
    print("Selected Intervals:")
    for interval in selected_intervals:
        print(f"Start: {interval.start}, Finish: {interval.finish}, Weight: {interval.weight}")
