import pyautogui as py
import time

py.PAUSE = 1
py.press('win')
py.write('opera')
py.press('enter')
time.sleep(1)

#py.hotkey('ctrl','shift','n')
py.write('https://www.trivago.com.br/pt-BR?themeId=143&sem_keyword=hotel%20trivago&sem_creativeid=714750717722&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=&sem_param1=&sem_param2=&sem_campaignid=296067198&sem_adgroupid=21694811118&sem_targetid=kwd-25690702833&sem_location=9101929&cipc=br&cip=5519000005&gad_source=1&gad_campaignid=296067198&gclid=Cj0KCQjw5vLVBhCiARIsAD56SFJNgoDdStQ_bOlpVTIFy4dyMZpJPKM8MrAAwuq3Mk0gjlnd4nUT_rsaAk_-EALw_wcB')
py.press('enter')
time.sleep(1)

#py.click(x=1449, y=353)
#time.sleep(1)

py.click(x=550, y=433)
py.write('japao')
py.click(x=516, y=524)

py.click(x=1379, y=676)

py.click(x=1636, y=426)
time.sleep(4)

py.click(x=577, y=414)
py.scroll(-250)
