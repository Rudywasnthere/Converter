import math;

## customize!!!!!!!
## tries to turn the numbers back into letters
convert_char = True
new_base = int(10)
row_length = 50
numb_length = 8
## coded to be decoded below
coded = "01110010 01100001 00100000 01110010 01100001 00100000 01110010 01100001 01110011 01110000 01110101 01110100 01101001 01101110 00100000 01101100 01101111 01110110 01100101 01110010 00100000 01101111 01100110 00100000 01110100 01101000 01100101 00100000 01110010 01110101 01110011 01110011 01101001 01100001 01101110 00100000 01110001 01110101 01100101 01100101 01101110 00100000 01101111 01101000 00100000 01100110 01110101 01100011 01101011 00100000 01100001 01101110 00100000 01100101 01101110 01100100 01100101 01110010 01101101 01100001 01101110"


to_b_coded = ""

encoded = ""



## dictionaries for changing to different number systems
base_values = {"0":0,"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26, "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

base_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]

c_list = []

print_list = []

## some borrowed code from a different project, does the number shifting
def math_time(base_1, base_2, starting_number):
    final_number = ""
    number = number_to_list(starting_number)
    length = len(number)
    count = 0
    intermediate = 0
    base_1, base_2 = int(base_1), int(base_2)
    ## if base one, the value in base 10 is just the length anyways
    if base_1 == 1:
      intermediate = len(starting_number)
    ## counts through the number turning it into base 10, which is the intermediate
    else:
      while count < length:
        digit = number[count]
        digit_val = base_values[digit]
        intermediate += digit_val * (base_1**(length - count - 1))
        count += 1
        
    x, count = 1,1
    ##checks to see how long the resulting number should be based on base_2
    while x <= intermediate/base_2:
        x*= base_2
        count += 1
    ##Counts down by a process called Weighted Division
    while count >= 1:
      if x <= intermediate:
          new_digit = intermediate/x
          integer_place = math.floor(new_digit)
          ## list comprehension takes the digit value and returns the digit
          integer_pos_place = [str for str, value in base_values.items() if value == integer_place]
          digit_place = integer_pos_place[0]

          ##clean up after each weighted division
          final_number += digit_place
          intermediate -= integer_place*x
      else:
          final_number += "0"
      ## clean up 2
      count -= 1
      x /= base_2
    ##takes out extra 0's infront of the number
    while final_number[0] == 0:
      final_number = final_number[1:]
    return final_number


def number_to_list(number):
  if type(number) != str:
    number = str(number)
  count = 0
  list_1 = [""]
  while count < len(number):
    bit = number[count]
    list_1.insert(-1,bit)
    count += 1
  number = list_1
  useless = number.pop(-1)
  return number

list_pos = []
list_p = ""
correct = False
end = "" 

while end != "q":
  option = input('1 or 2: ')
  correct = False
  while correct == False:
    try:
      option = int(option)
      if option > 0 and option <3:
        correct = True
      else:
        option = input("I need a correct option: ")
    except:
      option = input("I need a correct option: ")

  if option == 1:

    ## decodes entire thing as one number
    """"
    coded_1 = coded.replace(" ", "")
    print(math_time(2,16,coded_1))
    print(len(coded_1), len(math_time(2,16,coded_1)))
    """
    ## decodes as each byte is a seperate number
    if " " not in coded:
      while len(coded) > 0:
        try:
          c_list.append(coded[0:8])
        except:
          c_list.append(coded[0:len(coded)-1])
        coded = coded[8:len(coded)]
    else:
      c_list = coded.split(" ")
    for x in range(0,len(c_list)):
      place = int(math_time(2,new_base,c_list[x]))
      list_pos.append(place)
      ## shifts numbers to letters, can be removed
      if convert_char == True:
        list_p += f"{chr(place)}"
      else:
        list_p += f"{place} "

    while len(list_p) > 0:
        try:
          print_list.append(list_p[0:row_length])
        except:
          print_list.append(list_p[0:len(list_p)-1])
        list_p = list_p[row_length:len(list_p)]

    for x in range(0,len(print_list)):
      print(print_list[x])

  elif option == 2:
    ncoded_l = []
    print_row = ""
    to_b_coded = input("What do you want to say: ")
    base = input("What base to encode into: ")
    correct = False
    while correct == False:
      try:
        base = int(base)
        if base > 0 and base < 36:
          correct = True
        else:
          base = input("I need a base type less than 36: ")
      except:
        base = input("I need a base type less than 36: ")
    for x in range(0, len(to_b_coded)):
      c_place = int(ord(to_b_coded[x]))
      place = int(math_time(10,base,c_place))
      ncoded_l.append(place)
    
    print(len(ncoded_l))

    for x in range(0, len(ncoded_l)):
      char_num = f"{ncoded_l[x]} "
      while len(char_num) < numb_length + 1:
        char_num = f"0{char_num}"
      print_row += char_num
      if len(print_row) > row_length:
        print(print_row)
        print_row = ""
      if x == len(ncoded_l) - 1:
        print(print_row)
  end = input()