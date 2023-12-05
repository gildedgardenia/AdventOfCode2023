import pandas as pd
import regex as re

with open('input.txt') as f:
   lines = f.read().splitlines()

def getGameInfo(str):
   array = re.findall(r'\d+|red|green|blue|;', str)
   return array

df_rows = []
good_ids = []

for i in lines:
   game_object = {"game_id": 0, "red": 0, "green": 0, "blue": 0, "power": 0}
   values = getGameInfo(i)
   game_object["game_id"] = int(values[0])
   for idx in range(len(values)):
      if values[idx] == "red" and game_object["red"] <= int(values[idx-1]):
         game_object["red"] = int(values[idx-1])
      elif values[idx] == "green" and game_object["green"] <= int(values[idx-1]):
         game_object["green"] = int(values[idx-1])
      elif values[idx] == "blue" and game_object["blue"] <= int(values[idx-1]):
         game_object["blue"] = int(values[idx-1])
   # print(game_object)
   game_object["power"] = game_object["red"]*game_object["blue"]*game_object["green"]
   df_rows.append(game_object)

df = pd.DataFrame(df_rows)
# df = df.drop(df[df.red > 12].index)
# df = df.drop(df[df.green > 13].index)
# df = df.drop(df[df.blue > 14].index)

print(df.head())
#  print(df.game_id.sum())
print(df.power.sum())