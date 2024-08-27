import pandas as pd


def load_lifeExpectancy_data():
    path = 'https://github.com/dongupak/DataML/raw/main/csv/'
    file = path + 'life_expectancy.csv'
    life = pd.read_csv(file)
    return life

if __name__=='__main__':
    life = load_lifeExpectancy_data() 
    print('Life Expectancy: ')
    print(life.describe())