from util.implementation import DbConnection

class Location(DbConnection):

    def _init_(self):
        self.LocationID=''
        self.LocationName=''
        self.Address=''

    def setter(self):
        self.LocationID=int(input('Enter LocationID:'))
        self.LocationName=input('Enter LocationName:')
        self.Address=input('Enter Address:')
        data=[(self.LocationID,self.LocationName,self.Address)]
        insert_str='''INSERT INTO Location(LocationID,LocationName,Address) VALUES (%s,%s,%s)'''
        self.open()
        self.s.executemany(insert_str,data)
        self.conn.commit()
        print('Location record inserted successfully..')


    def getter(self):
        self.open()
        select_str='''SELECT * FROM Location'''
        self.s.execute(select_str)
        records=self.s.fetchall()
        print('')
        print('Records in New Location Table')
        for i in records:
            print(i)


    def update(self):
        self.getter()
        ID=int(input('Enter LocationID to be Updated: '))
        self.LocationName=input('Enter LocationName: ')
        self.Address=input('Enter Address: ')

        update_str='''
            UPDATE Location
            SET LocationName=%s,Address=%s
            WHERE LocationID=%s
        '''

        self.open()
        data=[(self.LocationName,self.Address,ID)]
        self.s.executemany(update_str,data)
        self.conn.commit()
        print('Record updated successfully..')
        return True

    def delete(self):
        LocationID=int(input('Enter the LocationID to be deleted: '))
        delete_str=f'DELETE FROM Location WHERE LocationID={LocationID}'
        self.open()
        self.s.execute(delete_str)
        self.conn.commit()
        print('Record Deleted Successfully..')

        
