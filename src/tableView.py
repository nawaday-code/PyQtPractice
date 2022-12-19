import sys
import calendar

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from dataContainer import *


class TableSettings():
    def __init__(self, rowCount, columnCount):

        self.rowCount = rowCount
        self.columnCount = columnCount


class MainWindow(QMainWindow):
    def __init__(self, members: list[Person], tableSettings: TableSettings):
        super().__init__()
        centralWidget = QWidget()
        self.resize(1500, 800)
        self.setCentralWidget(centralWidget)
        layout = QGridLayout(centralWidget)

        self.tableWidget = self.buildTable(members, tableSettings)

        self.tableWidget.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)

        layout.addWidget(self.tableWidget)

    def buildTable(self, members: list, tableSettings: TableSettings):
        table = QTableWidget()
        table.setRowCount(tableSettings.rowCount)
        table.setColumnCount(tableSettings.columnCount)

        days = [str(day) for day in Person.a_month_days]
        dayOfWeekTemp = ['月', '火', '水', '木', '金', '土', '日']
        dayOfWeek = [dayOfWeekTemp[calendar.weekday(
            Person.date.year, Person.date.month, day)] for day in Person.a_month_days]
        table.setHorizontalHeaderLabels(dayOfWeek)

        for i, person in enumerate(members):
            for day, job in person.jobPerDay.items():
                newItem = QTableWidgetItem(str(job))
                table.setItem(i, day-1, newItem)

        table.resizeColumnsToContents()
        table.resizeRowsToContents()

        return table


ShiftDataReader.readConfigvar('radschedule\勤務表\data\configvar.dat')
members = ShiftDataReader.readStaffInfo('radschedule\勤務表\data\staffinfo.dat')
ShiftDataReader.applyShift2Member('radschedule\勤務表\data\shift.dat', members)

tableSettings = TableSettings(len(members), len(members[0].jobPerDay))

app = QApplication(sys.argv)

testWindow = MainWindow(members, tableSettings)
testWindow.show()

sys.exit(app.exec_())
