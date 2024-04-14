import requests
import xml.etree.ElementTree as ET

def get_random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json() 
    return data['url']


def get_weather(lon, lat):
    url = f'https://www.7timer.info/bin/astro.php?lon={lon}&lat={lat}&ac=0&unit=metric&output=xml&tzshift=0'
    res = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(res.content))
    root = tree.getroot()
    data = root.find('dataseries').findall('data')
    res_text = ''
    for treeEl in data:
        timepoint = treeEl.attrib['timepoint']
        cloud = treeEl.find('cloudcover').text
        temp = treeEl.find('temp2m').text
        pred = treeEl.find('prec_type').text
        res_text += f'{timepoint} | {cloud} | {temp} | {pred}\n'
    return res_text
