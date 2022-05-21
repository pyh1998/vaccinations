import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import datetime as dt

# Russia: 50.06% population fully vaccinated, 160 days to 80%
# Falkland Islands: 50.31% population fully vaccinated, 127 days to 80%
# Trinidad and Tobago: 50.6% population fully vaccinated, 97 days to 80%
# Slovakia: 50.72% population fully vaccinated, 135 days to 80%
# Belize: 51.76% population fully vaccinated, 94 days to 80%
# Turkmenistan: 52.41% population fully vaccinated, 95 days to 80%
# Barbados: 52.65% population fully vaccinated, 158 days to 80%
# Tunisia: 53.22% population fully vaccinated, 78 days to 80%
# Pakistan: 53.27% population fully vaccinated, 198 days to 80%
# Botswana: 53.92% population fully vaccinated, 159 days to 80%


def predict(path_to_file):
    print("Analysing data file", path_to_file)
    data = pd.read_csv(path_to_file)
    analyse(data, "Botswana", 80)


def analyse(data, country, rate):
    var = data.loc[data['location'] == country, ['date', 'people_fully_vaccinated_per_hundred']]
    var['date'] = pd.to_datetime(var['date'])
    var['date'] = var['date'].map(dt.datetime.toordinal)
    pds = pd.DataFrame(data=var)
    a = pds.dropna()

    x = a['date'].values.reshape(-1, 1)
    y_ = a['people_fully_vaccinated_per_hundred'].values.reshape(-1, 1)

    reg = LinearRegression()
    reg.fit(x, y_)
    print('a = {:.5}'.format(reg.coef_[0][0]))  # coef_回归系数
    print('b = {:.5}'.format(reg.intercept_[0]))  # intercept_截距
    print("线性模型为: y_ = {:.5}x + {:.5} ".format(reg.coef_[0][0], reg.intercept_[0]))
    predictions = reg.predict(x)

    plt.scatter(a['date'], a['people_fully_vaccinated_per_hundred'], c='black')
    plt.plot(a['date'], predictions, c='blue', linewidth=2)  # 蓝线
    plt.xlabel("date")
    plt.ylabel("vaccinated")
    plt.show()

    # 预测
    # predictions = reg.predict([[8000]])
    # print(predictions)
    # print('8000米高度的温度{:.5}'.format(predictions[0][0]))

    # 初始化预测值为last day，并输出last day的接种比例
    result = x[-1]
    print(reg.predict([result]))

    # 循环直到接种比例大于阈值，输出日期和天数
    while reg.predict([result]) < rate:
        result = result + 1
    print(dt.datetime.fromordinal(result[0]))
    print(result - x[-1])


def date(para):
    delta = pd.Timedelta(str(int(para)) + 'days')
    time = pd.to_datetime('1899-12-30') + delta
    return time


if __name__ == '__main__':
    # test on a CSV file
    predict('./vaccinations2.csv')
