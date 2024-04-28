import requests
import xml.etree.ElementTree as ET
from geopy.geocoders import Nominatim
from html2image import Html2Image


def get_random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_weather(city):
    geolocator = Nominatim(user_agent='skalutsky')
    loc = geolocator.geocode(city)
    url = f'https://www.7timer.info/bin/astro.php?lon={loc.longitude}&lat={loc.latitude}&ac=0&unit=metric&output=xml&tzshift=0'
    res = requests.get(url)
    tree = ET.ElementTree(ET.fromstring(res.content))
    root = tree.getroot()
    data = root.find('dataseries').findall('data')
    res_text = ''
    for treeEl in data[:8]:
        timepoint = treeEl.attrib['timepoint']
        cloud = treeEl.find('cloudcover').text
        temp = treeEl.find('temp2m').text
        pred = treeEl.find('prec_type').text
        row = f"""<tr>
                <td>{timepoint}</td>
                <td>{cloud}</td>
                <td>{temp}</td>
                <td>{pred}</td>
            </tr>"""
        res_text += row
    css = '''
            table {
                width: 30%;
                border-collapse: collapse;
            }
            table, th, td {
                border: 1px solid black;
            }
            th, td {
                padding: 10px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
        '''
    html = f'''<html>
<body style="background-color: white">
    <div >
        <h1>Погода в {city}</h1>
        <table>
           <thead>
            <tr>
                <th>Время</th>
                <th>Облачность</th>
                <th>Температура</th>
                <th>Осадки</th>
            </tr>
           </thead>
           <tbody style="text-align: center;font-size: larger;">
           {res_text}
           </tbody>
        </table>
    </div>
</body>
</html>
    '''
    hti = Html2Image()
    hti.screenshot(html_str=html, css_str=css, save_as='page.png', size=(400, 500))


