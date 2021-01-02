#import pandas as pd
from csv import writer
from csv import DictWriter
field_names = ['name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               'name', 'link', 'fan_count', 'checkins','start_date',
               ]
row_contents = {'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020',
                'name': 'Mahitha', 'link': 'https://www.facebook.com/01234567891', 'fan_count': 644931, 'checkins': 679,'start_date':'29-Dec-2020'}
with open('dummydata.csv', 'w', newline='') as f:
    print(type(row_contents))
    dict_writer = DictWriter(f, fieldnames=field_names)
    for i in range(50000000):
        dict_writer.writerow(row_contents)

