import json
import argparse


def fill_values(tests):
    for test in tests:
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_values(test['values'])


def main(values_path, tests_path):
    with open('tests.json', 'r') as f:
        tests_data = json.load(f)
    with open('report.json', 'w') as f:
        json.dump(tests_data, f, indent=2)
    with open(tests_path, 'r') as f:
        tests_data = json.load(f)

    with open(values_path, 'r') as f:
        values_data = json.load(f)

    global values_dict
    values_dict = {item['id']: item['value'] for item in values_data['values']}

    fill_values(tests_data['tests'])
    with open('report.json', 'w') as f:
        json.dump(tests_data, f, indent=2)


if __name__ == "__main__":
    print('to use write in console: python task3.py path/to/values.json path/to/tests.json')
    parser = argparse.ArgumentParser(description='Process some JSON files.')
    parser.add_argument('values_path', type=str)
    parser.add_argument('tests_path', type=str)

    args = parser.parse_args()

    main(args.values_path, args.tests_path)



