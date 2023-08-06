from sqlalchemy import create_engine
from sqlalchemy import text


class DBManager(object):
    def __init__(self, connstr):
        self.engine = create_engine(connstr, echo=False, encoding='utf8')

    def insert(self, table, data, fields=None, exist_action='ignore'):
        if type(data) == list:
            if len(data) == 0:
                return None
            keys = list(data[0].keys())
        else:
            keys = list(data.keys())
        if not fields:  # 默认使用data的keys
            fields = ','.join(keys)  # 或者通过参数指定
        pre_values = ','.join([':%s' % k for k in keys])  # 前缀加:
        if exist_action == 'replace':
            pre_sql = 'replace into %s (%s) values(%s)' % (table, fields, pre_values)
        elif exist_action == 'ignore':
            pre_sql = 'insert ignore into %s (%s) values(%s)' % (table, fields, pre_values)
        else:
            pre_sql = 'insert into %s (%s) values(%s)' % (table, fields, pre_values)
        try:
            bind_sql = text(pre_sql)
            if type(data) == list:
                # 对于数组，批量执行，效率非常高
                resproxy = self.engine.connect().execute(bind_sql, *data)
            else:
                resproxy = self.engine.connect().execute(bind_sql, data)
            return resproxy
        except Exception as e:
            raise e

    def execute(self, sql):
        try:
            result = self.engine.connect().execute(sql)
            hasResult = 'select' in sql
            if hasResult:
                rows = result.fetchall()
                return rows
        except Exception as e:
            raise e

    def close(self):
        self.engine.dispose()


if __name__ == '__main__':
    pass
