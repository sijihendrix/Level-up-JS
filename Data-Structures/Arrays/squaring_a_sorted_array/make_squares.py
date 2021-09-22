def make_squares(arr):
  squares = []
  # TODO: Write your code here
  for element in arr:
      squares.append(element**2)
#   squares.sort()
  return sort_list(squares)


def sort_list(list):
    # data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
    new_list = []

    while list:
        minimum = list[0]  # arbitrary number in list 
        for x in list: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        list.remove(minimum)    

    return new_list

example_list = [-2, -1, 0, 2, 3]

print(make_squares(example_list))