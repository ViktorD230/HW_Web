from collections import UserDict
from record import Record, RecordIterator


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __iter__(self):
        return RecordIterator(list(self.data.values()))

    def paginate(self, page_size):
        records = list(self.data.values())
        total_records = len(records)
        num_pages = (total_records + page_size - 1) // page_size

        for page in range(num_pages):
            start_index = page * page_size
            end_index = (page + 1) * page_size
            yield [(record.name.value, record) for record in records[start_index:end_index]]
