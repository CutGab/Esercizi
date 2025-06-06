tpl: list[tuple] = [('a', 2), ('b', 2), ('c', 3), ('a', 6)]

def convert (tpl: list) -> dict:

     dct: dict = {}

     for key, value in tpl:
 
          if key in dct: #(Io facevo dct[key] in dct)
             dct[key] += value

          else:
             dct[key] = value

     return dct

print(convert(tpl))

####################SOLUZIONE#########################

# tpl: list = [('a', 2), ('b', 2), ('c', 3), ('a', 6)]

# def convert2(tpl: list) -> dict:

#     dct: dict = {}

#     for element in tpl:

#         key, value = element[0], element[1]

#         if key in dct:

#             dct[key] += value

#         else:
#             dct[key] = value

#     return dct


# print(convert2(tpl))

    