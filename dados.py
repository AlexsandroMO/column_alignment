def alinhamento(var):
  text = var
  lista = text.split()
  result = ''
  for b in lista:
    result = result + b + ', '
  print(result)

  return result

