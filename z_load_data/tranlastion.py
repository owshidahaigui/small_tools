from urllib import parse
input_str = input('请输入')
string = parse.unquote(input_str)
print(string)
