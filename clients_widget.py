from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from models import Session, Client, Passport, Street, City


class ClientsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_data()

    def load_data(self):
        session = Session()
        clients = session.query(Client).all()

        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([
            "Last Name", "First Name", "Middle Name", "Birth Date", "Phone",
            "Arrival", "Departure", "Passport", "Address"
        ])
        self.table.setRowCount(len(clients))

        for row, client in enumerate(clients):
            self.table.setItem(row, 0, QTableWidgetItem(client.last_name))
            self.table.setItem(row, 1, QTableWidgetItem(client.first_name))
            self.table.setItem(row, 2, QTableWidgetItem(client.middle_name or ""))
            self.table.setItem(row, 3, QTableWidgetItem(str(client.birth_date)))
            self.table.setItem(row, 4, QTableWidgetItem(client.phone_number))
            self.table.setItem(row, 5, QTableWidgetItem(str(client.arrival_date)))
            self.table.setItem(row, 6, QTableWidgetItem(str(client.departure_date)))

            passport = client.passport
            if passport:
                self.table.setItem(row, 7, QTableWidgetItem(
                    f"{passport.series} {passport.number}"
                ))
            else:
                self.table.setItem(row, 7, QTableWidgetItem(""))

            address = client.address
            if address and address.city:
                address_str = f"{address.city.name}, {address.name}, {address.house_number}"
                self.table.setItem(row, 8, QTableWidgetItem(address_str))
            else:
                self.table.setItem(row, 8, QTableWidgetItem(""))

        self.table.resizeColumnsToContents()
        session.close()
