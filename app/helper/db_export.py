__author__ = 'enix.yu.guanyuan'

import pymssql
import xlwt


class Exporter(object):

    def __init__(self, con):
        self.connection = con

    def reconnect(self):
        pass

    def export_to_csv(self, sql):
        pass

    def export_to_xls(self, sql):
        pass

    def export_to_xlsx(self, sql, outfile):
        self.reconnect()
        cursor = self.connection.cursor(as_dict=True)

        wb = xlwt.Workbook()
        sheet = wb.add_sheet('data')
        i, j = 0, 0
        cursor.execute(sql)
        for row in cursor:
            # Write header
            if i == 0:
                #print(cursor.description)
                for meta in cursor.description:  # column name
                    sheet.write(i, j, meta[0])
                    j += 1
                i += 1

            # Write Body
            j = 0
            for meta in cursor.description:  # column name
                sheet.write(i, j, row[meta[0]])
                j += 1
            i += 1
        wb.save(outfile)
        self.close()

    def close(self):
        self.connection.close()
        self.connection = None


class MSSQLExporter(Exporter):

    def __init__(self, con):
        self.server, self.user, self.password, self.database = con.server, con.user, con.password, con.database
        connection = pymssql.connect(con.server, con.user, con.password, con.database)
        super(MSSQLExporter, self).__init__(con=connection)

    def reconnect(self):
        if not self.connection:
            self.connection = pymssql.connect(self.server, self.user, self.password, self.database)

        return self.connection
