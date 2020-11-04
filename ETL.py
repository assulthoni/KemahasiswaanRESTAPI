import csv
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql://root:@localhost/db_prestasi_kmhs?charset=utf8mb4')
df = pd.read_csv("Dir. Kemahasiswaan Tel-U - Kompetisi - KM - Prestasi.csv")
df.to_sql('prestasi', con=engine, index=True)