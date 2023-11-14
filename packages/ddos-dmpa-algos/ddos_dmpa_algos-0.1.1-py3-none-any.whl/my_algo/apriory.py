from itertools import combinations

def get_frequent_itemsets(transactions, min_support):
    unique_items = sorted(list(set(item for sublist in transactions for item in sublist)))
    frequent_itemsets = []
    k = 1
    C = [[item] for item in unique_items]
    max_itemset_length = 0
    
    while C:
        L = {}
        for itemset in C:
            count = sum(all(item in transaction for item in itemset) for transaction in transactions)
            if count >= min_support:
                L[tuple(itemset)] = count
                max_itemset_length = max(max_itemset_length, len(itemset))
        frequent_itemsets.extend(L.keys())
        print(f"Iteration {k}:")
        for itemset, count in L.items():
            print(f"Itemset: {list(itemset)}, Count: {count}")
        
        C = get_next_candidate_sets([list(itemset) for itemset in L.keys()], k)
        k += 1
    
    min_frequent_itemsets = [itemset for itemset in frequent_itemsets if len(itemset) == max_itemset_length]
    print("\nMinimum Frequent Itemset:")
    for itemset in min_frequent_itemsets:
        print(f"Itemset: {list(itemset)}")

    # Example association rule
    antecedent = ['I1', 'I2']
    consequent = ['I4']

    support_antecedent = calculate_support(antecedent, transactions)
    support_rule = calculate_support(antecedent + consequent, transactions)
    confidence_rule = calculate_confidence(antecedent, consequent, transactions)

    print(f"\nSupport for Antecedent: {antecedent} - {support_antecedent}")
    print(f"Support for Rule: {antecedent} -> {consequent} - {support_rule}")
    print(f"Confidence for Rule: {antecedent} -> {consequent} - {confidence_rule}")

def get_next_candidate_sets(L, k):
    C = []
    for i in range(len(L) - 1):
        for j in range(i + 1, len(L)):
            if L[i][:k - 1] == L[j][:k - 1]:
                C.append(L[i] + [L[j][-1]])
    return C


def calculate_support(itemset, transactions):
    return sum(all(item in transaction for item in itemset) for transaction in transactions)

def calculate_confidence(antecedent, consequent, transactions):
    support_antecedent = calculate_support(antecedent, transactions)
    support_rule = calculate_support(antecedent + consequent, transactions)
    if support_antecedent == 0:
        return 0  # Avoid division by zero
    return support_rule / support_antecedent

def main():
    transactions = [['I1', 'I2', 'I5'], ['I2', 'I4'], ['I2', 'I3'], ['I1', 'I2', 'I4'], ['I1', 'I3'], ['I2', 'I3'], ['I1', 'I3'], ['I1', 'I2', 'I3', 'I5'], ['I1', 'I2', 'I3']]
    min_support = 2

    frequent_itemsets = get_frequent_itemsets(transactions, min_support)


main()
