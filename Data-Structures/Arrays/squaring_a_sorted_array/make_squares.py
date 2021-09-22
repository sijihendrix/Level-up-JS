def make_squares(arr):
  squares = []
  # TODO: Write your code here
  for element in arr:
      squares.append(element**2)
  return sort_list(squares)


def sort_list(list):
    new_list = []

    while list:
        minimum = list[0]  # arbitrary number in list 
        for x in list: 
            if x < minimum: # all elements less than arbitrary element
                minimum = x
        new_list.append(minimum) #array gets filled with the least valued element till the highest
        list.remove(minimum)    

    return new_list

example_list = [-2, -1, 0, 2, 3]

print(make_squares(example_list))