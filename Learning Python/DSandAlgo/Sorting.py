
def insertion_sort(input_lst: list):
    for i in range(1, len(input_lst)):
        print(f"accessing index - {i} and value - {input_lst[i]}")
        current_index = i
        while current_index > 0:
            previous_index = current_index - 1
            current_value = input_lst[current_index]
            previous_value = input_lst[previous_index]
            print(f"Current index - {current_index}, current value - {current_value}, "
                  f"previous index - {previous_index}, prev_value - {previous_value}")
            if current_value < previous_value:
                input_lst[previous_index] = current_value
                input_lst[current_index] = previous_value
                current_index = current_index - 1
            else:
                break
    print(input_lst)

input_list = [7, 88, 15, 4, 22, 22, 22, 65, 1, 27, 6, 2, 95, 22]
insertion_sort(input_list)