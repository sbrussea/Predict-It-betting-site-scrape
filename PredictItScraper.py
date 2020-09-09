import requests
from bs4 import BeautifulSoup
import string
from datetime import date

# 13 13 13 13


def writer(elems):
  today = date.today()
  d1 = today.strftime("%m-%d-%Y")
  newFileName = f"arbitrage {d1}.txt"
  count = 0
  with open(newFileName, 'w') as filehandle:
    for elem in elems:
      count += 1
      filehandle.write(f'{count}) {elem}\n')



def culler(full):
  final = []
  for elem in full:
    if elem == []:
      full.remove(elem)
      continue
    temp = []
    for obj in elem:
      obj = obj.translate({ord("¢"): None})
      temp.append(obj)
    final.append(temp)

  for elem in final:
    if len(elem) >= 2:
      first = int(elem[1])
      second = int(elem[2])
      together = first + second
      elem.append(together)
      elem.append(together - 100)

  final.sort(key = lambda x:x[4])
  writer(final)
  return final


def arbitrageFinder():
  fullList = []
  today = date.today()
  d1 = today.strftime("%m-%d-%Y")

  with open(f'{d1}.html', "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    a = soup.find_all('a')
    counter = 1
    for elem in a:
      temp = []
      objCounter = 0
      h3 = elem.find('h3')
      if h3 != None:
        title = h3.string.strip()
        temp.append(title)
      span = elem.find_all('span')
      if counter >= 13:
        items = []
        for obj in span:
          a = str(obj.string)
          if objCounter == 1 or objCounter == 5:
            items.append(a)
            if objCounter == 5:
              objCounter = -1000
          objCounter += 1
        for price in items:
          temp.append(price)
      counter += 1
      
      fullList.append(temp)
      

      if counter == 1000:
        break
  print(culler(fullList))
      
def main():
  arbitrageFinder()
  print("... Done!")


if __name__ == '__main__':
    main()