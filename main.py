data = '''19001264
16633737
14572964
13994284
21105829
2951431
29360416
31644638
23902405
18661594
8263449
19204170
10708400
7844183
7590074
5913449
4081707
24082970
15694899
3597721'''

arr = data.splitlines()
sum = 0
count = 1
for i in arr:
  sum += int(i)
  if (count % 10) == 0:
    conv = round(sum / 1000000, 1)
    print(str(conv) + " Mbps")
    sum = 0
    conv = 0
  count += 1
