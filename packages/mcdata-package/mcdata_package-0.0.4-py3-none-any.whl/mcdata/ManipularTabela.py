import pandas as pd

class TableManipulator:
  def __init__(self, df):
      self.df = df

  def process_table(self, remove_duplicates=False, null_value_replacement=None, column_mapping=None, column_value_mapping=None):
      if remove_duplicates:
          self.df.drop_duplicates(inplace=True)

      if null_value_replacement:
          self.df.fillna(null_value_replacement, inplace=True)

      if column_mapping:
          self.df.rename(columns=column_mapping, inplace=True)

      if column_value_mapping:
          for column, mapping in column_value_mapping.items():
              self.df[column] = self.df[column].map(mapping)

      return self.df
