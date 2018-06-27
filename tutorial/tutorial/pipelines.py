
import sys
import pymysql.cursors
import pymysql
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request





class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class MySQLStorePipeline(object):
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin#123',
                             db='scrap',
                             port=3306)
        #print(self.connection)


    def process_item(self, item, spider):
        #try:
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO handyman(handyman_name, address , contact) VALUES (%s,%s,%s)"
                cursor.execute(sql, (item['handyman_name'],
                                     item['handyman_address'],
                                     item['handyman_contact']))

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            self.connection.commit()
        #finally:
            #self.connection.close()
            return item

'''
if __name__ == '__main__':
    m = MySQLStorePipeline()
'''