import builtins
from mock import patch


def perform_lab(lab_proc, input_list):
    '''
    This procedure will conduct the mock input for test cycle
    '''
    for idx, __input in enumerate(input_list):
        print("input[%d]: %s" % (idx, __input))
    inputYields = (_ for _ in input_list)

    def mock_input():
        return next(inputYields)
    with patch.object(builtins, 'input', mock_input):
        print(lab_proc())


def assert_lab(lab_proc, input_list, expected_result):
    '''
    This function will returns the compare result between output and provided expecting result
    '''
    for idx, __input in enumerate(input_list):
        print("input[%d]: %s" % (idx, __input))
    inputYields = (_ for _ in input_list)

    def mock_input():
        return next(inputYields)
    with patch.object(builtins, 'input', mock_input):
        output = lab_proc()
        print("output:", output, " =!= expected:", expected_result)
        return '%s' % output == expected_result


def multi_testing(lab_proc, test_cases):
    results = []
    for case in test_cases:
        if 'output' in case.keys():
            result = assert_lab(lab_proc, case['input'], case['output'])
            print("result:", 'OK' if result else 'FAIL')
            results.append(result)
        else:
            perform_lab(lab_proc, case['input'])
    return results
