

def tinhdiem_trungbinh(file_name):
    def averageScore(module_name, score_list):
        '''
        Hàm con này dùng để tính điểm theo param được nêu trong đề
        '''
        if not len(score_list):
            return 0
        rateParams = [{"moduleNames": ["Toan", "Ly", "Hoa", "Sinh"], "rate": [5/100, 10/100, 15/100, 70/100]},
                      {"moduleNames": ["Van", "Anh", "Su", "Dia"], "rate": [5/100, 10/100, 10/100, 15/100, 60/100]}]
        for param in rateParams:
            if module_name in param["moduleNames"]:
                ratio = param["rate"]
                break
        if not len(ratio):
            return 0
        # Kết quả thực tế cuối cùng theo từng môn
        return round(sum([ratio[i]*score for i, score in enumerate(score_list)]), 2)

    # Đọc file được đưa vào
    detailScore = open(file_name).readlines()

    # Lấy tiêu đề tất cả các cột
    columnNames = [s.strip() for s in detailScore[0].split(",")]

    # Áp dụng nhanh công thức tính điểm trung bình bằng chương trình con phía trên
    details = {detail.split(";")[0]: {columnNames[i]: averageScore(columnNames[i], list(map(int, s.strip().split(","))))
               for (i, s) in enumerate(detail.split(";")) if i > 0} for detail in detailScore[1:]}

    details["columnNames"] = columnNames

    return details


def luudiem_trungbinh(scores_dict, file_name):
    lines = [', '.join(scores_dict["columnNames"])]
    del scores_dict["columnNames"]
    for scoresId in scores_dict:
        line = [scoresId]
        for score in scores_dict[scoresId]:
            line.append("%.2f" % scores_dict[scoresId][score])
        lines.append("; ".join(line))
    oFile = open(file_name, mode='w')
    oFile.write("\n".join(lines))
    oFile.close()
    print("File kết quả điểm trung bình được lưu với tên '%s'" % file_name)


def main():
    # Khai báo đường dẫn cho input & output file
    inputFile = "diem_chitiet.txt"
    outputFile = "diem_trungbinh.txt"

    # Chạy hàm tinhdiem_trungbinh()
    calcResult = tinhdiem_trungbinh(inputFile)

    # Chạy hàm luudiem_trungbinh()
    luudiem_trungbinh(calcResult, outputFile)


if __name__ == "__main__":
    main()
