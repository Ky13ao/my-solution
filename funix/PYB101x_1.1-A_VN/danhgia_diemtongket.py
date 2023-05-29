def xeploai_hocsinh(file_name):
    # Đọc file được đưa vào
    detailScore = open(file_name).readlines()

    # Lấy tiêu đề tất cả các cột
    columnNames = [s.strip() for s in detailScore[0].split(",")]

    def rankName(score_dict):
        # Lập dict hệ số
        w = {'Toan': 2, 'Ly': 1, 'Hoa': 1,
             'Sinh': 1, 'Van': 2, 'Anh': 2, 'Su': 1, 'Dia': 1}
        finalAvgScore = sum(
            [w[moduleName]*score for moduleName, score in score_dict.items()])/11
        rankNames = [{"name": "Xuat sac", "require": 9.0, "allge": 8}, {
            "name": "Gioi", "require": 8.0, "allge": 6.5}, {
            "name": "Kha", "require": 6.5, "allge": 5.0}, {
            "name": "TB kha", "require": 6.0, "allge": 4.5}, {
            "name": "TB", "require": 0, "allge": 0}]
        for rank in rankNames:
            if finalAvgScore > rank["require"] and all([_ >= rank["allge"] for _ in score_dict.values()]):
                return rank["name"]

    # Tải dữ liệu theo dạng số float để tính toán
    details = {detail.split(";")[0]: {columnNames[i]: float(s.strip())
               for (i, s) in enumerate(detail.split(";")) if i > 0} for detail in detailScore[1:]}

    # Trả về 1 dict xếp hạng theo Ma HS
    return {studId: rankName(scoreDict) for studId, scoreDict in details.items()}


def xeploai_thidaihoc_hocsinh(file_name):
    # Đọc file được đưa vào
    detailScore = open(file_name).readlines()

    # Lấy tiêu đề tất cả các cột
    columnNames = [s.strip() for s in detailScore[0].split(",")]

    def rankGrade(score_dict):
        # Lập dict khối bao gồm danh sách môn và phân loại
        gradeNames = [{"name": "A", "modules": ["Toan", "Ly", "Hoa"], "kindOfScore": {"1": 24, "2": 18, "3": 12, "4": 0}}, {
            "name": "A1", "modules": ["Toan", "Ly", "Anh"]}, {"name": "B", "modules": ["Toan", "Hoa", "Sinh"]}, {
            "name": "C", "modules": ["Van", "Su", "Dia"], "kindOfScore": {"1": 21, "2": 15, "3": 12, "4": 0}}, {
            "name": "D", "modules": ["Toan", "Van", "Anh", "Anh"], "kindOfScore": {"1": 32, "2": 24, "3": 20, "4": 0}}]
        gradeNames[1]["kindOfScore"] = gradeNames[0]["kindOfScore"]
        gradeNames[2]["kindOfScore"] = gradeNames[0]["kindOfScore"]
        student = {}
        for grade in gradeNames:
            __dtb = sum([score_dict[module]
                        for module in grade["modules"]])
            for kind, score in grade["kindOfScore"].items():
                if __dtb >= score:
                    student["xeploai_"+grade["name"]] = kind
                    break
        return student

    # Tải dữ liệu theo dạng số float để tính toán
    details = {detail.split(";")[0]: {columnNames[i]: float(s.strip())
               for (i, s) in enumerate(detail.split(";")) if i > 0} for detail in detailScore[1:]}

    # Trả về 1 dict xếp loại theo Ma HS
    return {studId: rankGrade(scoreDict) for studId, scoreDict in details.items()}


def main():
    # Khai báo đường dẫn cho input & output file
    inputFile = "diem_trungbinh.txt"
    outputFile = "danhgia_hocsinh.txt"

    # Chạy hàm xeploai_hocsinh()
    calcResult1 = xeploai_hocsinh(inputFile)

    # Chạy hàm xeploai_thidaihoc_hocsinh()
    calcResult2 = xeploai_thidaihoc_hocsinh(inputFile)

    # Xác định tên cột để xuất file
    lines = [", ".join(["Ma HS", "xeploai_TB chuan", 'xeploai_A',
                       'xeploai_A1', 'xeploai_B', 'xeploai_C', 'xeploai_D'])]
    for studId, rankName in calcResult1.items():
        line = [studId, rankName]
        for _ in calcResult2[studId].values():
            line.append(_)
        lines.append("; ".join(line))
    oFile = open(outputFile, mode='w')
    oFile.write("\n".join(lines))
    oFile.close()
    print("File kết quả xếp loại học sinh được lưu với tên '%s'" % outputFile)


if __name__ == "__main__":
    main()
