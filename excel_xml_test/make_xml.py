from xml.etree.ElementTree import Element, SubElement, ElementTree
import xml.etree.ElementTree as ET
import os

def MakeXmlFile(name, score):
    root = Element("UESRDATA")
    element = Element("Minus")
    root.append(element)
    sub_element1 = SubElement(element, "UserName")
    sub_element1.text = name
    sub_element2 = SubElement(element, "UserScore")
    sub_element2.text = score

    element = Element("Kamui")
    root.append(element)
    sub_element1 = SubElement(element, "UserName")
    sub_element1.text = name
    sub_element2 = SubElement(element, "UserScore")
    sub_element2.text = score

    element = Element("Blue")
    root.append(element)
    sub_element1 = SubElement(element, "UserName")
    sub_element1.text = name
    sub_element2 = SubElement(element, "UserScore")
    sub_element2.text = score

    element = Element("Rfc")
    root.append(element)
    sub_element1 = SubElement(element, "UserName")
    sub_element1.text = name
    sub_element2 = SubElement(element, "UserScore")
    sub_element2.text = score

    element = Element("Kimdoland")
    root.append(element)
    sub_element1 = SubElement(element, "UserName")
    sub_element1.text = name
    sub_element2 = SubElement(element, "UserScore")
    sub_element2.text = score

    tree = ElementTree(root)
    tree.write('C:\Temp\hi.xml')

name = None
score = None
if os.path.isfile("C:\Temp\hi.xml"):
    print("파일이 있습니다.")
else:
    MakeXmlFile(name, score)

tree = ET.parse('C:\Temp\hi.xml')
root = tree.getroot()
for i in root.iter('Minus'):
    i.find('UserName').text = 'as3'
    tree.write('C:\Temp\hi.xml')
    print(i.find('UserName').text)
    print(i.find('UserScore').text)

def MakeDifficultyStar(level, width, Star):
    for i in range(8):
        i = i * width
        DISPLAYSURF.blit(Star, (290 + i, 100))

def WriteBestRank(now_Push, root, Music):
    if now_Push == 1:
        for i in root.iter(Music):
            if i.find('UserScore').text == None:
                nowPage = pygame.font.SysFont('C:\Windows\Fonts\Calibri.ttf', 40).render('None', True, (255,200,0))
                test_width = nowPage.get_rect().size[0]
                DISPLAYSURF.blit(nowPage, (270, 55))
            else:
                nowPage = pygame.font.SysFont('C:\Windows\Fonts\Calibri.ttf', 40).render(i.find('UserName').text +'  ('+i.find('UserRate')+'% / ' + i.find('UserScore')+')', True, (255,200,0))
                test_width = nowPage.get_rect().size[0]
                DISPLAYSURF.blit(nowPage, (270, 55))

def UpdateRank(now_Push, correct_rate, total_score)
    if now_Push == 1:
        for i in root.iter('Minus'):
            if total_score > int(i.find('UserScore').text):
                i.find('UserName').text = LOGIN_ID
                i.find('UserScore').text = format(total_score, ',')
                i.find('UserRate').text = str(correct_rate) + '%'
    elif now_Push == 2:
        for i in root.iter('Kamui'):
            if total_score > int(i.find('UserScore').text):
                i.find('UserName').text = LOGIN_ID
                i.find('UserScore').text = format(total_score, ',')
                i.find('UserRate').text = str(correct_rate) + '%'
    elif now_Push == 3:
        for i in root.iter('Blue'):
            if total_score > int(i.find('UserScore').text):
                i.find('UserName').text = LOGIN_ID
                i.find('UserScore').text = format(total_score, ',')
                i.find('UserRate').text = str(correct_rate) + '%'
    elif now_Push == 4:
        for i in root.iter('Rfc'):
            if total_score > int(i.find('UserScore').text):
                i.find('UserName').text = LOGIN_ID
                i.find('UserScore').text = format(total_score, ',')
                i.find('UserRate').text = str(correct_rate) + '%'
    elif now_Push == 5:
        for i in root.iter('Kimdoland'):
            if total_score > int(i.find('UserScore').text):
                i.find('UserName').text = LOGIN_ID
                i.find('UserScore').text = format(total_score, ',')
                i.find('UserRate').text = str(correct_rate) + '%'
    tree.write('C:\Temp\hi.xml')