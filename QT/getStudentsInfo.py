import os
from openpyxl import load_workbook


class ExcelUtil(object):
    def __init__(self, excelFile):
        self.excelFile = excelFile
        self.myExcel = load_workbook(self.excelFile)
        self.myworkSheet = self.myExcel["Sheet1"]
        self.myworkSheet = self.myExcel.active

    def getStudentNameList(self, columns):
        studentNameList = []
        for cell_object in list(self.myworkSheet.columns)[columns]:
            if not cell_object.value:
                continue
            studentNameList.append(cell_object.value)
        for i in studentNameList:
            print(i)
        return studentNameList

    def getStudentNameList2(self, columnsNum):

        print([cell_object.value for cell_object in list(self.myworkSheet.columns)[columnsNum] if cell_object.value])

    def wirteStudent(self, className, studentsNamesList):
        pass


if __name__ == '__main__':

    excelObj = ExcelUtil(os.path.abspath("./conf/sss.xlsx"))
    # excelObj.getStudentNameList(0)
    excelObj.getStudentNameList2(0)
