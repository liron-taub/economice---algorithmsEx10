import doctest
import statistics as stat
from typing import List

def compute_budget(total_budget:float,citizen_votes:List[List]) -> List[float]:
        """
        >>> compute_budget(100, [[100, 0, 0], [0, 0, 100]])
        [50.0, 0.0, 50.0]
        >>> compute_budget(100, [[100, 0, 0]])
        [100, 0, 0]

        """
        costs_subjs = dict()
        budget = list()

        for s in range(len(citizen_votes[0])):
            costs_subjs[s] = list()
            for vote in citizen_votes:
                costs_subjs[s].append(vote[s])

            # add the median value for each subject
            budget.append(stat.median(costs_subjs[s]))
        return budget


if __name__ == "__main__":
    (failures, tests) = doctest.testmod(report=True)
    print("{} fail test, {} tests passed , ".format(failures, tests))
