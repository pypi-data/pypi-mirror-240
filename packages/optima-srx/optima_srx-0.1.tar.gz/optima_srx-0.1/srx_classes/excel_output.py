import os
import pandas as pd
from datetime import datetime

def extract_excel(sheet_data, file_name):
    # Get the current date and time
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("[%d - %m - %Y]-[%H - %M]")  # Format the date and time as a string

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Go up one level to the "srx" directory
    srx_directory = os.path.dirname(script_directory)

    # Get the path to the "excel_output" folder
    output_directory = os.path.join(srx_directory, 'Excel Outputs')

    # Construct the output file name with date and time
    output_file = os.path.join(output_directory, f'{file_name}-{formatted_datetime}.xlsx')

    # Create an ExcelWriter object with XlsxWriter as the engine
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

    # Get the xlsxwriter workbook object
    workbook = writer.book

    for sheet_data_item in sheet_data:
        sheet_name = sheet_data_item['sheet_name']
        data = sheet_data_item['data']
        columns = sheet_data_item['columns']

        # Create a DataFrame for the current sheet
        df = pd.DataFrame(data, columns=columns)

        # Save the DataFrame in the current sheet
        df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Get the worksheet object for the current sheet
        worksheet = writer.sheets[sheet_name]
        # Apply autofilter for the first row
        worksheet.autofilter(0, 0, 0, len(columns) - 1)
        # Autofit column widths for all columns
  
        # for i, col in enumerate(columns):
            # column_len = max(df[col].astype(str).str.len().max(), len(col))
            # worksheet.set_column(i, i, column_len)


        
        # Apply center alignment, vertical center alignment, and text wrapping to all cells
        center_alignment_wrap = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'text_wrap': True})

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                worksheet.write(row + 1, col, df.iat[row, col], center_alignment_wrap)

        # Freeze the first row
        worksheet.freeze_panes(1, 0)

    # Close the Pandas ExcelWriter, which will save the Excel file
    writer.close()

    print(f'Data saved to {output_file}')


