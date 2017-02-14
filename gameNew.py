from pyspark import SparkContext, SparkConf
import functions

conf = SparkConf().setAppName('ProcessGame').setMaster('spark://10.169.9.142:7077')
sc = SparkContext(conf=conf)
path = 'hdfs://10.169.9.142:9000/user/make/gameData/vgsales.csv'
rawData = sc.textFile(path).setName('game_data').cache()
header = rawData.map(lambda line: line.split(',')).filter(lambda line: line[0] == 'Rank').collect()
sales = rawData.map(functions.splitCols).filter(lambda line :line[0] != 'Rank').cache()#all sales data without header
platforms = sales.map(lambda line: line[2]).collect()
platforms = list(set(platforms))
genre = sales.map(lambda line: line[4]).collect()
genre = list(set(genre))
publishers = sales.map(lambda line: line[5]).collect()
publishers = list(set(publishers))
print(publishers)
sc.stop()
