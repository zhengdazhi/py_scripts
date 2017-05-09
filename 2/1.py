#-*-coding:utf-8-*-

#输入领先的分数
pointsStr = raw_input("Enter the lead in points:")
points = int(pointsStr)
points = points - 3
#领先对是否控球
has_ball = raw_input("Does the lead team have the ball (Yes or No):")
if has_ball == 'Yes':
    points = points + 0.5
else:
    points = points - 0.5
#如果领先分数小于0就设置为0
if points < 0:
    points = 0

points = points ** 2
#输入剩余的比赛时间
seconds = int(raw_input("Enter the number of seconds remaining:"))
if points > seconds:
    print "Lead is safe"
else:
    print "Lead is not safe."

