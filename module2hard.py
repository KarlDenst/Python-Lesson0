import random
def cell_1():
    cell_1=range(3,21)
    cell_1_num = random.choice(cell_1)
    return cell_1_num

cell_1_num = cell_1()
print(f'Случайное число',cell_1_num)

def cell_2():

    cell_2_num = []
    for i in range(1,cell_1_num-1):
        pair_sum = []
        for j in range(1,cell_1_num):
            if cell_1_num % (i + j) == 0 and i < j:
                pair_sum.append([i,j])
                cell_2_num.append(pair_sum)
                pair_sum = []
    return cell_2_num

cell_2_num = cell_2()
result = (str(cell_2_num).replace('[', '').replace(']', '')
          .replace(',', '').replace(' ', ''))
print(f'result',result)