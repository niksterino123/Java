def function(test):
  def wrapper(some_text,string_input,integer_input):
    try:
     textfile = open(some_text, "r")
     print("\n{}".format(textfile.read()))
    except:
      print('\nEs faili ar arsebobs! ')


    try:
      string_input/1
      print('string faili ar arsebobs! ')
    except:
      print(string_input)


    try:
      int(integer_input)/1
      print('arsebobs integeri :{}'.format(integer_input))
    except:
      print('ar arsebobs integeri! ')
    return test(some_text,string_input,integer_input)
  return wrapper





@function
def test_function(some_text,string_input,integer_input):
  return test_function

test_function('some_text.txt',input('sheiyvane stringi: '),input('sheiyvane ricxvi: '))


