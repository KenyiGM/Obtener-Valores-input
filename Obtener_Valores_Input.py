
def GetValuesInput(input):

  filtro = input.replace(",", "").replace("-", "").replace(";", "").replace("_", "").replace(".","").replace(":", "")

  lista_valores = filtro.split("  ")

  return lista_valores
