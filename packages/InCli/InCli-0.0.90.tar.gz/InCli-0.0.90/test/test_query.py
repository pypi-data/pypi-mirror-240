import unittest,sys,simplejson
from InCli.SFAPI import restClient,query,utils,file_csv


class Test_Query(unittest.TestCase):
    def test_query1(self):
        restClient.init('DEVNOSCAT2')
        res = query.query("SELECT Id,Name FROM vlocity_cmt__DRBUNDLE__C ")

        output = []

        for rec in res['records']:
            res2 = query.query(f"SELECT count(Id) FROM vlocity_cmt__DRMapItem__c where name = '{rec['Name']}' ")
            out = {
                'Name':rec['Name'],
                'size:':res2['records'][0]['expr0']
            }
            output.append(out)
            print(".")
            
        utils.printFormated(output)

        print()

    def test_query2(self):
        restClient.init('DEVNOSCAT2')
        res = query.query("SELECT Id,name FROM vlocity_cmt__DRMapItem__c ")

        output = {}

        for rec in res['records']:
            name = rec['Name']

            if rec['Name'] in output:
                output[rec['Name']] = output[rec['Name']] + 1
            else:
                output[rec['Name']] = 1
        
        oo = []
        for key in output.keys():
            o = {
                'name':key,
                'size':output[key]
            }
            oo.append(o)

        oo.sort(key=lambda x: x["size"])

        file_csv.write('DR_size',oo)

        utils.printFormated(oo)


