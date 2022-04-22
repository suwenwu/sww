lucky = int(input("请输入幸运瓶盖的数量"))

encourage = int(input("请输入鼓励瓶盖的数量"))

if lucky >= 10 or encourage >= 20:
    print("恭喜你，可以兑换大奖")
else:
    print("抱歉，暂时不能兑换大奖")
