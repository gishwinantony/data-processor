import os
import pandas as pd
from datetime import datetime
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import FileMetadata, WellData
import logging
logger = logging.getLogger(__name__)

@receiver(post_migrate)
def import_annual_data(sender, **kwargs):

    """
    Imports annual well data from an Excel file into the WellData model.

    The function performs the following steps:
    1. Extracts the file key (name without extension) and last modified date from the specified Excel file.
    2. Checks if a record with the same file key exists in the FileMetadata model.
    3. If a new record is created:
        - Deletes all existing WellData records.
        - Reads the Excel file and selects relevant columns.
        - Groups data by 'API WELL NUMBER' and sums the production values.
        - Creates and bulk inserts new WellData records based on the grouped data.
    4. logs a success message if the data is imported successfully, or a message indicating the file already exists.

    Handles:
        - File not found errors.
        - Errors related to reading the Excel file.
        - Errors related to database operations.
    """
    file_path = './20210309_2020_1 - 4.xls'
    
    try:
        file_name = os.path.basename(file_path)
        file_key = os.path.splitext(file_name)[0]
        last_modified_timestamp = os.path.getmtime(file_path)
        last_modified = datetime.fromtimestamp(last_modified_timestamp)

        # Check if a record with the same file key exists
        record, created = FileMetadata.objects.update_or_create(
            file_key=file_key,
            defaults={'last_modified': last_modified}
        )
        if created:
            
            logger.info(f"Created new record: {record.file_key}")
            WellData.objects.all().delete()
            
            try:

                df = pd.read_excel(file_path)
            except FileNotFoundError:
                logger.error(f"Error: The file {file_path} was not found.")
                return
            except Exception as e:
                logger.error(f"Error reading the Excel file: {e}")
                return

            try:

                selected_columns = ['API WELL  NUMBER', 'OIL', 'GAS', 'BRINE']
                df_selected = df[selected_columns]
                sum_per_well = df_selected.groupby('API WELL  NUMBER').sum()
                
                well_data_objects = []
                for _, row in sum_per_well.iterrows():
                    well_data_objects.append(
                        WellData(
                            api_well_number=row.name,  
                            oil=row['OIL'],
                            gas=row['GAS'],
                            brine=row['BRINE']
                        )
                    )

                WellData.objects.bulk_create(well_data_objects)
                logger.info('Data imported successfully')

            except KeyError as e:
                logger.error(f"Error: Missing expected column in the Excel file: {e}")
            except Exception as e:
                logger.error(f"Error processing data: {e}")
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")
