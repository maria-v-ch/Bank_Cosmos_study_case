from main import collect_transactions_for_more_than, generate_list_of_transactions_more_than_threshold


def test_collect_transactions_for_more_than():
    k = {'key': 'value'}
    user_info = {'a': 'b', 'transactions': k}
    for key in k:
        c = collect_transactions_for_more_than(user_info)
        assert next(c) == key


def test_generate_list_of_transactions_more_than_threshold():
    transactions = {'purpose': 15}
    user_info = {'a': 'b', 'transactions': transactions}
    threshold = 10
    list_of_transactions_more_than_threshold = {}
    for key in transactions:
        if transactions[key] >= threshold:
            list_of_transactions_more_than_threshold.update({key: transactions[key]})
            res = list_of_transactions_more_than_threshold
            expected = generate_list_of_transactions_more_than_threshold(user_info, threshold)
            assert res == transactions, list_of_transactions_more_than_threshold == expected
