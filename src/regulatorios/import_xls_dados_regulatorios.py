import pandas as pd
from django.core.management.base import BaseCommand
from .models import Dados_Regulatorios
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Manually import data from Excel file into the Dados_Regulatorios model'

    def add_arguments(self, parser):
        # Allow user to specify the path of the Excel file
        parser.add_argument('xls_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['xls_file']
        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)

            # Extract columns
            status_anatel_column = df['status_anatel']
            numero_fistel_column = df['numero_fistel']
            carater_column = df['carater']
            finalidade_column = df['finalidade']
            servico_column = df['servico']
            uf_column = df['uf']
            cidade_column = df['cidade']
            canal_fisico_column = df['canal_fisico']
            frequencia_column = df['frequencia']
            classe_column = df['classe']
            categoria_column = df['categoria']
            latitude_column = df['latitude']
            longitude_column = df['longitude']
            erp_column = df['erp']
            hci_column = df['hci']
            fase_column = df['fase']
            comentarios_column = df['comentarios']

            # Loop through each row (row-by-row) and manually insert into the database
            for index in range(len(df)):
                # Check for NaN values and replace them with None (NULL in MySQL)
                status_anatel = status_anatel_column[index] if pd.notna(status_anatel_column[index]) else ''
                numero_fistel = numero_fistel_column[index] if pd.notna(numero_fistel_column[index]) else ''
                carater = carater_column[index] if pd.notna(carater_column[index]) else ''
                finalidade = finalidade_column[index] if pd.notna(finalidade_column[index]) else ''
                servico = servico_column[index] if pd.notna(servico_column[index]) else ''
                uf = uf_column[index] if pd.notna(uf_column[index]) else ''
                cidade = cidade_column[index] if pd.notna(cidade_column[index]) else ''
                canal_fisico = canal_fisico_column[index] if pd.notna(canal_fisico_column[index]) else ''
                frequencia = frequencia_column[index] if pd.notna(frequencia_column[index]) else ''
                classe = classe_column[index] if pd.notna(classe_column[index]) else ''
                categoria = categoria_column[index] if pd.notna(categoria_column[index]) else ''
                latitude = latitude_column[index] if pd.notna(latitude_column[index]) else None
                longitude = longitude_column[index] if pd.notna(longitude_column[index]) else None
                erp = erp_column[index] if pd.notna(erp_column[index]) else ''
                hci = hci_column[index] if pd.notna(hci_column[index]) else ''
                fase = fase_column[index] if pd.notna(fase_column[index]) else ''
                comentarios = comentarios_column[index] if pd.notna(comentarios_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - ERP: {erp}'))

                # Manually create and save the Dados_Regulatorios object
                try:
                    dados_regulatorios = Dados_Regulatorios(
                        status_anatel=status_anatel,
                        numero_fistel=numero_fistel,
                        carater=carater,
                        finalidade=finalidade,
                        servico=servico,
                        uf=uf,
                        cidade=cidade,
                        canal_fisico=canal_fisico,
                        frequencia=frequencia,
                        classe=classe,
                        categoria=categoria,
                        latitude=latitude,
                        longitude=longitude,
                        erp=erp,
                        hci=hci,
                        fase=fase,
                        comentarios=comentarios
                    )
                    dados_regulatorios.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {cidade}'))
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {cidade} - Error: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while importing {cidade}: {e}'))

            self.stdout.write(self.style.SUCCESS('Data import completed!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
