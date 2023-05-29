def lab12_1():
    # Lab12.1: https://docs.google.com/document/d/1qPN_c34jsyXPL04wGZqJlnKUy20AEPB3/view
    class NhanVien():
        def __init__(self, name, base_salary, coefficient):
            self.name = name
            self.baseSalary = base_salary
            self.coefficient = coefficient

        def salaryCalc(self, month_idx, working_days):
            salary = self.baseSalary * working_days * self.coefficient - 1e6
            finalSalary = salary * 0.9 if salary > 9*1e6 else salary
            return finalSalary

        def salaryPrint(self, month_idx, working_days):
            salary = self.salaryCalc(month_idx, working_days)
            print(
                f'Luong cua nhan vien {self.name} nhan duoc trong thang {month_idx:.0f} la: {salary:.0f} VND.')

    class QuanLy(NhanVien):
        def rewardPlusCalc(self, month_idx, working_days, performance):
            salary = self.baseSalary * working_days * self.coefficient - 1e6
            finalSalary = salary * 0.9 if salary > 9*1e6 else salary
            if performance < 1:
                return finalSalary * performance
            else:
                return salary * (performance-1) * 0.85 + finalSalary

        def salaryPrint(self, month_idx, working_days, performance):
            salary = self.rewardPlusCalc(month_idx, working_days, performance)
            print(
                f'Luong cua nhan vien {self.name} nhan duoc trong thang {month_idx:.0f} la: {salary:,.0f} VND.'.replace(",", "."))

    n = input()
    mIdx, baseSalary, workingDays, coefficient, perfomance = list(
        map(float, input().strip().split(' ')))
    mgrObj = QuanLy(n, baseSalary, coefficient)
    mgrObj.salaryPrint(mIdx, workingDays, perfomance)


if __name__ == '__main__':
    from test_proc import multi_testing

    # '''
    multi_testing(lab12_1, [{"input": ["Nguyen Hai Dang", "4 1000000 15 1.7 1.5"]},
                            {"input": ["Nguyen Hai Quang",
                                       "6 1000000 20 1.8 1.9"]},
                            {"input": ["Nguyen Thi Yen", "2 1000000 25 1.5 1.3"]}])
    # '''
