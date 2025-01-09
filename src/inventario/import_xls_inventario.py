import pandas as pd
from django.core.management.base import BaseCommand
from .models import Inventario
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Manually import data from Excel file into the Inventario model'

    def add_arguments(self, parser):
        # Allow user to specify the path of the Excel file
        parser.add_argument('xls_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['xls_file']
        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)

            # Extract columns
            cidade_column = df['cidade']
            equipe_column = df['equipe']
            descricao_column = df['descricao']
            serial_number_column = df['serial_number']
            ativo_fixo_column = df['ativo_fixo']
            comentarios_column = df['comentarios']

            # Loop through each row (row-by-row) and manually insert into the database
            for index in range(len(df)):
                # Check for NaN values and replace them with empty strings
                cidade = cidade_column[index] if pd.notna(cidade_column[index]) else ''
                equipe = equipe_column[index] if pd.notna(equipe_column[index]) else ''
                descricao = descricao_column[index] if pd.notna(descricao_column[index]) else ''
                serial_number = serial_number_column[index] if pd.notna(serial_number_column[index]) else ''
                ativo_fixo = ativo_fixo_column[index] if pd.notna(ativo_fixo_column[index]) else ''
                comentarios = comentarios_column[index] if pd.notna(comentarios_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - Descrição: {descricao}'))

                # Manually create and save the Inventario object
                try:
                    inventario = Inventario(
                        cidade=cidade,
                        equipe=equipe,
                        descricao=descricao,
                        serial_number=serial_number,
                        ativo_fixo=ativo_fixo,
                        comentarios=comentarios
                    )
                    inventario.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {cidade}'))
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {cidade} - Error: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while importing {cidade}: {e}'))

            self.stdout.write(self.style.SUCCESS('Data import completed!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
