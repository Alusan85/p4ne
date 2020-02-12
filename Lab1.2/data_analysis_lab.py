from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')  # Загрузить таблицу Excel из файла в переменную wb
sheet = wb['Data']  # Загрузить лист с именем "Data" в переменную sheet


def getvalue(x):
    return x.value


list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['C'][1:]))
list_z = list(map(getvalue, sheet['D'][1:]))
# Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)

pyplot.plot(list_x, list_y, label='Годы и температура')
pyplot.plot(list_x, list_z, label='Годы и активность солнца')
pyplot.legend()

# Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y 
pyplot.show()  # показать график
