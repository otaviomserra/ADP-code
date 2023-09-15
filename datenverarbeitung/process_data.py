import os
from openpyxl import load_workbook
import pandas as pd

class ExcelWriter:
    def __init__(self, process_name):
        self.process_name = process_name
        self.excel_file_path = self.get_excel_file_path()

    def get_excel_file_path(self):
        # Construct the path to the Excel file based on your description
        current_directory = os.path.dirname(__file__)  # Assuming this code is in the same directory as the Excel file
        excel_file_path = os.path.join(current_directory, '..', 'Werk', 'Prozesse', 'KPIS_Prozessen_Matrix.xlsx')
        return excel_file_path

    def write_to_cell(self, value):
        try:
            workbook = load_workbook(self.excel_file_path)
            worksheet = workbook.active

            # Assuming "Work in Process" is in column A (adjust as needed)
            row_index = None
            for row in worksheet.iter_rows(min_col=1, max_col=1, values_only=True):
                if row[0] == "Work in Process":
                    row_index = row[0]
                    break

            if row_index is not None:
                # Find the column with the same name as self.process_name (case-sensitive)
                column_index = None
                for cell in worksheet.iter_cols(min_row=1, max_row=1, values_only=True):
                    if cell[0] == self.process_name:
                        column_index = cell[0]
                        break

                if column_index is not None:
                    # Write the specified value to the cell
                    worksheet[column_index + row_index] = value
                    workbook.save(self.excel_file_path)
                # No need to handle cases where the column or row isn't found, as you requested to ignore errors.
        except Exception:
            pass  # Ignore all exceptions



class ProcessesProcessor:
    def __init__(self, process, log_df):
        self.process = process
        self.log_df = log_df

    def process_logs(self):
        try:
            # Define the directory structure
            base_directory = os.path.join(os.path.dirname(__file__), '..', 'Werk', 'Prozesse')
            process_directory = os.path.join(base_directory, self.process)
            csv_filename = f"{self.process}_logs.csv"
            csv_path = os.path.join(process_directory, csv_filename)

            # Check if the process directory exists, and create it if not
            if not os.path.exists(process_directory):
                os.makedirs(process_directory)

            # Check if the CSV file exists; if not, create it with headers
            if not os.path.exists(csv_path):
                self.log_df.to_csv(csv_path, index=False)
            else:
                # Append the DataFrame to the existing CSV file
                existing_df = pd.read_csv(csv_path)
                combined_df = pd.concat([existing_df, self.log_df], ignore_index=True)
                combined_df.to_csv(csv_path, index=False)
        except Exception as e:
            pass  # Ignore errors

# Example usage:
if __name__ == "__main__":
    # Create a sample DataFrame (replace this with your actual DataFrame)
    log_df = request.log_df
    processor = ProcessesProcessor(process_name, log_df)
    processor.process_logs()
# Example usage:
#if __name__ == "__main__":
#    process_name = "YourProcessName"  # Replace with the actual process name
#
 #   # Create an instance of ExcelWriter
  #  excel_writer = ExcelWriter(process_name)
#
 #   # Write "working" to the cell
  #  excel_writer.write_to_cell("working")
#
 #   # Write "idle" to the same cell
  #  excel_writer.write_to_cell("idle")

