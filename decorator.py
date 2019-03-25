def check(func):
  def wrapper(damushaveba):
    if func(damushaveba) != None:
      for i in "aeiouyAEIOUY":
        if func(damushaveba).count(i) >= 1:
          print(i,func(damushaveba).count(i))
  return wrapper


def cencorship(func):
  def wrapper(damushaveba):
    cenzura = ["I Hate Python"]
    for i in cenzura:
       if damushaveba.count(i) >= 1:
         print('msgavsi sityvebis gamoyeneba python-shi akrdzalulia:',i)
       else:
         return damushaveba
  return wrapper



@check
@cencorship
def saxeli(mnishvneloba):
  return mnishvneloba



saxeli("I Hate")
