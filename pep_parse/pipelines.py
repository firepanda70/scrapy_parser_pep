import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent
CSV_HEADER = ['Статус', 'Количество']
CSV_FILE_NAME = 'status_summary_{time}.csv'
TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'


class PepParsePipeline:

    def open_spider(self, spider):
        self.total = 0
        self.st_amount = {}

    def process_item(self, item, spider):
        st = item['status']
        if st not in self.st_amount:
            self.st_amount[st] = 1
        else:
            self.st_amount[st] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        summary_dir = BASE_DIR / 'results'
        summary_dir.mkdir(exist_ok=True)
        time = dt.datetime.now().strftime(TIME_FORMAT)
        file_path = summary_dir / CSV_FILE_NAME.format(time=time)
        with open(file_path, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(CSV_HEADER)
            for st in self.st_amount:
                writer.writerow([st, self.st_amount[st]])
            writer.writerow(['Total', self.total])
