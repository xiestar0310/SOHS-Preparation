from flask import Flask, render_template, url_for, request, redirect
import gspread, json, requests
from oauth2client.service_account import ServiceAccountCredentials
import weatherapi as w
from datetime import datetime

SCOPE = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDENTIAL = ServiceAccountCredentials.from_json_keyfile_name('cert.json', SCOPE)
gc = gspread.authorize(CREDENTIAL)

app = Flask(__name__)

WEATHER_SHEET = gc.open('Weather Sheet FINAL')
TEMPERATURE = WEATHER_SHEET.worksheet('Temperature Data')
RAINFALL = WEATHER_SHEET.worksheet('Rainfall Data')
TIME = WEATHER_SHEET.worksheet('Time')
CITYINFO = WEATHER_SHEET.worksheet('City Info')
#WEATHER_SHEET.share('mmmzzz66g@gmail.com', perm_type = 'user', role = 'writer')
#WEATHER = WEATHER_SHEET.add_worksheet(title = "Weather Info", rows = "10", cols = "2")
#WEATHER_SHEET.del_worksheet('Sheet1')
TIME.update('B2', "Success")
now = datetime.now()
DATE = now.strftime("%m/%d/%Y")
if TIME.acell('A1').value != DATE:
    print("Needs updating")
    #update some stuff 

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
monthdict = {"january":0, "february":1, "march":2, "april":3, "may":4, "june":5, "july":6, "august":7, 
"september":8, "october":9, "november":10, "december":11}

def valid(month):
    if month.lower() in months:
        return True
    return False

def check(month, tp):
    num = monthdict[month]
    if tp == 1:
        num += 12
    num += 2
    return chr(num + ord('A'))

def sort_tuple(tup):
    # reverse = None (sorts in ascending order)
    # tuple is sorted by first element using a lambda
    tup.sort(key = lambda x: x[0])
    return tup

@app.route('/', methods=['POST', 'GET'])
def login():
    bcity = ""
    bcountry = ""
    bdesc = ""
    burl = ""
    bwear = ""
    if request.method == 'POST':
        # Check if both form methods are filled in
        if request.form.get('low') and request.form.get('high') and request.form.get('month1') and valid(request.form.get('month1')):
            # values will be filled in
            month = request.form.get('month1').lower()
            lo = request.form.get('low')
            hi = request.form.get('high')
            lo = int(lo)
            hi = int(hi)
            #print(lo, hi, month)
            # do stuff with values
            val = (lo + hi) // 2
            dd = []
            for i in range(2, 22):
                istr = str(i)
                fstr = check(month, 0)
                sstr = check(month, 1)
                city = TEMPERATURE.acell("A{}".format(istr)).value
                temp1 = int(TEMPERATURE.acell("{}{}".format(fstr, istr)).value)
                temp2 = int(TEMPERATURE.acell("{}{}".format(sstr, istr)).value)
                avg = (temp1 + temp2) // 2
                avg2 = abs(avg - val)
                dd.append((avg2, city))
            dd = sort_tuple(dd)
            bcity = dd[0][1]
            for i in range(2, 22):
                istr = str(i)
                if CITYINFO.acell("A{}".format(istr)).value == bcity:
                    bcountry = CITYINFO.acell("B{}".format(istr)).value
                    if bcountry == "":
                        bcountry = bcity
                    bdesc = CITYINFO.acell("C{}".format(istr)).value
                    burl = CITYINFO.acell("D{}".format(istr)).value
                    bwear = CITYINFO.acell("E{}".format(istr)).value
        elif request.form.get('rain') and request.form.get('month2') and valid(request.form.get('month2')):
            month = request.form.get('month2').lower()
            rain = request.form.get('rain')
            rain = float(rain)
            val = rain
            dd = []
            #print(val)
            for i in range(2, 22):
                istr = str(i)
                fstr = check(month, 0)
                city = RAINFALL.acell("A{}".format(istr)).value
                rain1 = float(RAINFALL.acell("{}{}".format(fstr, istr)).value)
                rain2 = abs(rain1 - val)
                #print(city, rain1, rain2)
                dd.append((rain2, city))
            dd = sort_tuple(dd)
            bcity = dd[0][1]
            for i in range(2, 22):
                istr = str(i)
                if CITYINFO.acell("A{}".format(istr)).value == bcity:
                    bcountry = CITYINFO.acell("B{}".format(istr)).value
                    if bcountry == "":
                        bcountry = bcity
                    bdesc = CITYINFO.acell("C{}".format(istr)).value
                    burl = CITYINFO.acell("D{}".format(istr)).value
                    bwear = CITYINFO.acell("E{}".format(istr)).value
                    print(bdesc)
    else: # Not filled in
        print('stuff not filled in') #debug
    return render_template('index.html', bestcity = bcity, bestcountry = bcountry, bestdesc = bdesc, besturl = burl, bestwear = bwear)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

#debug -> heroku ps:scale web=1 