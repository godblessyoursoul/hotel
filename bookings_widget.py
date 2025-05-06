from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from models import Session, Booking


class BookingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.load_data()


    def load_data(self):
        session = Session()
        bookings = session.query(Booking).all()


        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Client", "Room Category", "Departure Date"])
        self.table.setRowCount(len(bookings))


        for row, booking in enumerate(bookings):
            self.table.setItem(row, 0, QTableWidgetItem(str(booking.id)))


            client = booking.client
            full_name = f"{client.last_name} {client.first_name} {client.middle_name or ''}".strip()
            self.table.setItem(row, 1, QTableWidgetItem(full_name))


            self.table.setItem(row, 2, QTableWidgetItem(booking.room_category))
            self.table.setItem(row, 3, QTableWidgetItem(str(booking.departure_date)))


        self.table.resizeColumnsToContents()
        session.close()
