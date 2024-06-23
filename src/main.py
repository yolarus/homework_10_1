from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_data

if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Счет 35383033474447895560"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Карта"), "\n")
    print(get_data("2018-07-11T02:26:18.671407"), "\n")

    tests_info = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    print(filter_by_state(tests_info), "\n")
    print(filter_by_state(tests_info, "CANCELED"), "\n")

    print(sort_by_date(tests_info), "\n")
    print(sort_by_date(tests_info, True), "\n")
