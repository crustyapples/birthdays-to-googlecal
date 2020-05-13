import re

with open('birthdays.txt', 'r') as T:
    inputBday = T.read()


pattern = r'([@a-zA-Z_.0-9]+) (\d+)\w* (\w{3})'
months = dict(Jan=1,Feb=2,Mar=3,Apr=4,May=5,Jun=6,Jul=7,Aug=8,Sep=9,Oct=10,Nov=11,Dec=12)

bdayreg = re.compile(pattern)
bdaylist = bdayreg.findall(inputBday)

list1 = []
dateslist = []
monthlist = []

for i in range(len(bdaylist)):
    list1.append(bdaylist[i][1])
    dateslist.append(list1[i].zfill(2))
    monthlist.append(str(months[bdaylist[i][2]]).zfill(2))

def output_event_body(i):
    birthdayDict = {
    'summary': f"{bdaylist[i][0]}'s Birthday",
    'start': {
        'date': f'2020-{monthlist[i]}-{dateslist[i]}',
    },
    'end': {
        'date': f'2020-{monthlist[i]}-{dateslist[i]}',
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY;COUNT=10'
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    return birthdayDict
