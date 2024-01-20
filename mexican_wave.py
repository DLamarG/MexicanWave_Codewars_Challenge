import re
def wave(people):
   wave_num = 0
   waves = list(people)
   results = []
   while wave_num < len(people):
    alt_wave = list(map(lambda x: x.lower(), waves))
    alt_wave[wave_num] = alt_wave[wave_num].upper()
    results.append(''.join(alt_wave))
    wave_num += 1
   edited_list = list(map(lambda x: x if re.search(r"[A-Z]", x) else '', results))
   return [x for x in edited_list if x]
        
      

print(wave('codewars')) # ['Codewars', 'cOdewars', 'coDewars', 'codEwars', 'codeWars', 'codewArs', 'codewaRs', 'codewarS']
print(wave('hello')) # ['Hello', 'hEllo', 'heLlo', 'helLo', 'hellO']
print(wave('bat man')) # ['Bat man', 'bAt man', 'baT man', 'bat man', 'bat Man', 'bat mAn', 'bat maN']
print(wave('bat')) # ['Bat', 'bAt', 'baT']