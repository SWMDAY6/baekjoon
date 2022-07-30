# 트럭
n, w, l = map(int, input().split())
truck_weight = list(map(int, input().split()))

bridge = [0] * w
time = 0

while bridge:
    time += 1
    bridge.pop(0)
    if truck_weight:
        if sum(bridge) + truck_weight[0] <= l:
            bridge.append(truck_weight.pop(0))
        else:
            bridge.append(0)
print(time)
