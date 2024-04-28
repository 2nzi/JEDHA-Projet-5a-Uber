import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from sklearn.cluster import DBSCAN
import plotly.express as px
import calendar
import pandas as pd
import numpy as np
import warnings
import sys

# Plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.figure_factory as ff

# Scikit-learn
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.ensemble import (RandomForestClassifier, BaggingClassifier,
                              AdaBoostClassifier, GradientBoostingClassifier,
                              StackingClassifier)
from xgboost import XGBClassifier
# import sys
# sys.path.append(r'C:\Users\antoi\Documents\Work_Learn\JEDHA\M05-Supervised_ML\JEDHA-Projet')
# from function import *

import tkinter as tk
from tkinter import ttk
import pandas as pd
import plotly.express as px
from sklearn.cluster import DBSCAN



df_taxi_zone = pd.read_csv('data/taxi-zone-lookup.csv')
df_raw = pd.read_csv('data/uber-raw-data-apr14.csv')

df = df_raw.sample(10000)

date = 'Date/Time'
df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['year'] = df[date].dt.year
df['month'] = df[date].dt.month
df['dayofweek'] = df[date].dt.dayofweek
df['hour'] = df[date].dt.hour
df['dayofmonth'] = df[date].dt.day
df.head()

categorical_features = ['hour']
numeric_features = ['Lon','Lat']

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop="first")

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

X = preprocessor.fit_transform(df)

class DBSCANInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DBSCAN Interface")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.eps_label = QLabel("Eps:")
        layout.addWidget(self.eps_label)

        self.eps_entry = QLineEdit()
        layout.addWidget(self.eps_entry)
        self.eps_entry.setText("0.2")

        self.min_samples_label = QLabel("Min Samples:")
        layout.addWidget(self.min_samples_label)

        self.min_samples_entry = QLineEdit()
        layout.addWidget(self.min_samples_entry)
        self.min_samples_entry.setText("100")

        self.run_button = QPushButton("Run DBSCAN")
        self.run_button.clicked.connect(self.run_dbscan)
        layout.addWidget(self.run_button)

        self.setLayout(layout)

    def run_dbscan(self):
        Eps = float(self.eps_entry.text())
        Min_samples = int(self.min_samples_entry.text())

        db = DBSCAN(eps=Eps, min_samples=Min_samples, metric="manhattan")
        db.fit(X)
        df['cluster'] = db.labels_
        print(set(db.labels_))

        c = 'dayofweek'
        anim = 'cluster'
        # anim= 'hour'
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        df['dayofweek'] = df['dayofweek'].map(lambda x: day_names[x])

        fig = px.scatter_mapbox(df.sort_values(anim), lat="Lat", lon="Lon",
                                animation_frame=anim, color=c,
                                color_continuous_scale=px.colors.sequential.Viridis,
                                range_color=[min(df[c]), max(df[c])],
                                mapbox_style="carto-positron", zoom=11)
        fig.update_layout(width=1000, height=700, title=f'eps: {Eps}  |  min_sample: {Min_samples}')
        fig.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DBSCANInterface()
    window.show()
    sys.exit(app.exec_())
