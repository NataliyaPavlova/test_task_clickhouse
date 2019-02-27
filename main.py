import datetime
import config
from dbsql import create_conn, create_table

class Data:
    def __init__(self):
        #init connections, create sql table
        self.bulk_size = config.bulk_size
        self.db = create_conn(config.db_file)
        create_table(self.db)
        #create table in clickhouse
        pass

    def get_bulk(self, timestamp_limit, prev, next=None):
        ''' Get a bulk from MySQL; check timestamps'''
        if next:
            sql_stat = 'SELECT * WHERE timestamp < :timestamp_limit LIMIT :prev, :next'
        else:
            sql_stat = 'SELECT * WHERE timestamp < :timestamp_limit LIMIT :prev, '
        return self.db.execute(sql_stat, timestamp_limit=timestamp_limit, prev=prev, next=next)


    def load(self):
        ''' Main functionality: load all data from MySQL to clickhouse'''
        # NB assuming there is no parallel uploading in db
        prev, next = 0, self.bulk_size

        today = int(datetime.datetime.now().timestamp())
        diff = config.days_of_history * 24 * 60 * 60
        timestamp_limit = today-diff

        try:
            bulk = self.get_bulk(timestamp_limit, prev, next)
            print('There are {} read from SQL db'.format(next))
            while bulk:
                self.put_bulk_clickhouse(bulk)
                print('There are {} loaded to Clickhouse')
                prev, next = next, next + config.bulk_size
                bulk = self.get_bulk(timestamp_limit, prev, next)
                print('There are {} read from SQL db'.format(next))
            # check if there is data left and if so put_bulk_clickhouse
            leftovers = self.get_bulk(timestamp_limit, prev=next)
            if leftovers:
                self.put_bulk_clickhouse(leftovers)
        except Exception as e:
            print('Loading failed. {} batches read from SQL dbase, {} loaded to Clickhouse'.format(prev))

    def put_bulk_clickhouse(self, bulk):
        ''' Put a read bulk to clickhouse'''
        # check timestamps and skip if the record exists'''
        pass

def main():
    print('Start loading...')
    data = Data()
    try:
        data.load()
    except Exception as err:
        print('Failed: {}'.format(err))

if __name__=='__main__':
    main()


