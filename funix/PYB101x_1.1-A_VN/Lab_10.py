from test_proc import multi_testing


def lab10_1():
    # Lab10.1: https://docs.google.com/document/d/13PugdFDstlfdc5EQ65I4BdOnTnP3PF3k/view
    class Student():
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_diemtk(self):
            score_values = self.score.values()
            diemtk = sum([_ for _ in score_values])/len(score_values)
            print(f'The average mark of {self.name} is {round(diemtk, 2)}')

    n = input()
    s = list(map(float, input().strip().split(' ')))
    studentObj = Student(n, {key: s[idx]
                         for idx, key in enumerate(["Toan", "Ly", "Hoa"])})
    studentObj.print_diemtk()


def lab10_2():
    # Lab10.2: https://docs.google.com/document/d/1-FP7JOb-JxOP_YvhjanJ_CVXd94qqR7F/view
    class NhanVien():
        def __init__(self, name, base_salary):
            self.name = name
            self.baseSalary = base_salary

        def salaryCalc(self, month_idx, working_days, salary_ratio):
            salary = self.baseSalary * working_days * salary_ratio - 1e6
            finalSalary = salary * 0.9 if salary > 9*1e6 else salary
            print(
                f'Luong cua nhan vien {self.name} nhan duoc trong thang {month_idx} la: {finalSalary:.0f} VND.')

    n = input()
    mIdx, baseSalary, workingDays, salaryRatio = list(
        map(float, input().strip().split(' ')))
    empObj = NhanVien(n, baseSalary)
    empObj.salaryCalc(mIdx, workingDays, salaryRatio)


if __name__ == '__main__':
    '''
    multi_testing(lab10_1, [{"input": ["Jelly", " 8.54 9.32 7.32"]},
                            {"input": ["Rose", "8.2 7.1 9.2"]},
                            {"input": ["Bill", "5.2 6.1 7.2"]}])
    # '''

    # '''
    multi_testing(lab10_2, [{"input": ["Nguyen Hai Phong", "3 500000 20 1.5"]},
                            {"input": ["Nguyen Hai Duong",
                                       "4 1000000 15 1.3"]},
                            {"input": ["Nguyen Thi Yen", "5 250000 22 1.2"]}])
    # '''
