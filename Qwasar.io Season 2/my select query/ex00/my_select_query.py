class MySelectQuery:
    def __init__(self, csv_content):
        self.csv_content = csv_content
        self.headers = csv_content.split('\n')[0].split(',')
        self.rows = [row.split(',') for row in csv_content.split('\n')[1:]]

    def where(self, column_name, value):
        column_index = self.headers.index(column_name)
        return [','.join(row) for row in self.rows if row[column_index] == value]