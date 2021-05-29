import math
import os

## customize!!!!!!!
## tries to turn the numbers back into letters
convert_char = True
row_length = 50
numb_length = 8

## dictionaries for changing to different number systems
base_values = {"0":0,"1":1, "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,"g":16,"h":17,"i":18,"j":19,"k":20,"l":21,"m":22,"n":23,"o":24,"p":25,"q":26, "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35}

base_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r","s","t","u","v","w","x","y","z"]

def read(case, files):
  if case == 1:
    try:
      file = open(f"{files}", "r")
      message= file.read()
      file.close()
      message = message.replace("\n"," ")
      return message
    except Exception as e: 
      print(f"{e} Error opening file")
      return "1error"
  if case == 2:
    try: 
      file = open(f"{files}", "r")
      message= file.read()
      file.close()
      message = message.replace("\n"," ")
      return message
    except Exception as e: 
      print(f"{e} Error opening file")
      return "1error"

def write(print_out, case, files):
  print_out = str(print_out.replace("", ""))
  if case == 2:
    try:
      file = open(f"{files}", "w")
      file.write(print_out)
      file.close()
      print("Encryption written to \"encrypted.txt\"")
    except Exception as e:
      print(f"{e} Writing to file failed")
  elif case == 1:
    try:
      file = open(f"{files}", "w")
      file.write(print_out)
      file.close()
      print("Decryption written to \"decrypted.txt\"")
    except Exception as e:
      print(f"{e} Writing to file failed")
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


def main():
  direct = os.path.realpath(__file__)
  direct = direct[0:len(direct)-7]
  print(direct)
  list_pos = []
  list_p = ""
  correct = False 
  end = ""
  c_list = []
  print_list = ""
  while end != "q":
    print("1: decrypt text\n2: encrypt text")
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
      print_list = ""
      ## coded to be decoded below
      coded = read(1, f"{direct}encrypted.txt")
      if coded == "1error" or coded == " " or coded == "":
        print("Error opening encrypted.txt")
      else:
        to_b_coded = ""
        encoded = ""
        temp_coded = coded.split(" ")
        while temp_coded[-1] == " ":
          temp_coded.pop()
        old_base = int(temp_coded[-1]) + 1
        coded = coded[0:len(coded) - 2]

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
        place = int(math_time(old_base,10,c_list[x]))
        list_pos.append(place)
        ## shifts numbers to letters, can be removed
        if convert_char == True:
          list_p += f"{chr(place)}"
        else:
          list_p += f"{place} "

      while len(list_p) > 0:
          try:
            print_list += f"{(list_p[0:row_length])}\n"
          except:
            print_list += (list_p[0:len(list_p)-1])
          list_p = list_p[row_length:len(list_p)]
      print(f"\n{print_list}")
      write(print_list, option, f"{direct}decrypted.txt")

    elif option == 2:
      ncoded_l = []
      print_row = ""
      print_out = ""
      to_b_coded = input("Write what you want to say in decrypted.txt")
      to_b_coded = read(option, f"{direct}decrypted.txt")
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
        place = math_time(10,base,c_place)
        ncoded_l.append(place)

      for x in range(0, len(ncoded_l)):
        char_num = f"{ncoded_l[x]} "
        while len(char_num) < numb_length + 1:
          char_num = f"0{char_num}"
        print_row += char_num
        if len(print_row) > row_length:
          print_out += f"{print_row}\n"
          print_row = ""
        if x == len(ncoded_l) - 1:
          print_out += f"{print_row}{base -1}"
      print_out = print_out.replace("00000000 ", "")
      """"
      for x in range(1,math.floor(len(print_out)/7)):
        position_remove = int(x*7 - x + 1)
        print_out = print_out[0:position_remove] + print_out[position_remove +1: len(print_out)]
      """
      write(print_out, option, f"{direct}encrypted.txt")
    end = input()

main()