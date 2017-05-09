#-*-colding:utf-8-*-

#打开一个文件读取
pokerFile = open("poker-hand-testing.data",'rU')

#创建统计手牌的变量，并初始化
totalCount = 0
nothingCount = 0
pairCount = 0
twoPairCount = 0
threeOfaKindCount = 0
straightCount = 0
flushCount = 0
fullHouseCount = 0
fourOfaKindCount = 0
straightFlushCount = 0
royalFlushCount = 0

#遍历文件的每一行
for line in pokerFile
    totalCount = totalCount + 1
    #获得手牌，用逗号分隔
    handRank = int(line.split(',')[-1])
    #统计每种手牌的数量
    if handRank == 0:
        nothingCount = nothingCount + 1
    if handRank == 1:
        pairCount = pairCount + 1
    if handRank == 2:
        twoPairCount = TwoRairCount + 1
    if handRank == 3:
        threeOfaKindCount = threeOfKindCount + 1
    if handRank == 4:
        straightCount = straightCount + 1
    if handRank == 5:
        flushCount = flushCount + 1
    if handRank == 6:
        fullHouseCount = fullHouseCount + 1
    if handRank == 7:
        fourOfaKindCount == fourOfaKindCount + 1
    if handRank == 8:
        straightFlushCount = straightFlushCount + 1
    if handRank == 9:
        royalFlushCount = royalFlushCount + 1
print "Total hands in file:", totalCount
print "Counts of hands:",nothingCount,pairCount,twoPairCount,\
        threeOfaKindCount,straightCount,flushCount,fullHouseCount,\
        fourOfaKindCount,straightFlushCount,royalFlushCount
totalCountFP = float(totalCount)
print "Probability:"
print "of nothing:  %5.3f %%" % (100* nothingCount/totalCountFP)
print "of one pair:  %5.3f %%" % (100* pairCount/totalCountFP)
print "of two pair:  %5.3f %%" % (100* TwoPairCount/totalCountFP)
print "of three of a kind :  %5.3f %%" % (100* threeOfaKindCount/totalCountFP)
print "of a straight :  %5.3f %%" % (100* straightCount/totalCountFP)
print "of a flush :  %5.3f %%" % (100* flushCount/totalCountFP)
print "of a full house :  %5.3f %%" % (100* fullHouseCount/totalCountFP)
print "of four of a kind :  %5.3f %%" % (100* fourOfaKindCount/totalCountFP)
print "of a straight flush :  %5.3f %%" % (100* straightFlushCount/totalCountFP)
print "of a royal flush :  %5.3f %%" % (100* royalFlushCount/totalCountFP)




