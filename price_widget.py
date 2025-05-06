from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from models import Session, Price

class PriceWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_data()

    def load_data(self):
        session = Session()
        prices = session.query(Price).all()

        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Description", "Price"])
        self.table.setRowCount(len(prices))

        for row, item in enumerate(prices):
            self.table.setItem(row, 0, QTableWidgetItem(item.name))
            self.table.setItem(row, 1, QTableWidgetItem(item.description))
            self.table.setItem(row, 2, QTableWidgetItem(str(item.price)))

        self.table.resizeColumnsToContents()
        session.close()
