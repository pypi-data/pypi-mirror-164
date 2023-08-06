def which_case(circuit):
    
  result=max(answer, key=answer.get)
  for i,e in enumerate(result):
    if i==0:
      first=e
    else:
      if e!=first:
        print("Not Recognized")
        break
  if i==len(result)-1:
    if first==0:
      print("Constant")
    else:
      print("Balanced")

  return result