import pandas as pd
from django.core.management.base import BaseCommand
from .models import Dados_Equipamentos  # Ensure the correct model path
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Manually import data from Excel file into the Dados_Equipamentos model'

    def add_arguments(self, parser):
        # Allow user to specify the path of the Excel file
        parser.add_argument('xls_file', type=str, help='Path to the Excel file')

    def handle(self, *args, **options):
        file_path = options['xls_file']
        try:
            # Read the Excel file using pandas
            df = pd.read_excel(file_path)

            # Extract columns from the Excel file
            cidade_column = df['cidade']
            uf_column = df['uf']
            potencia_tx_column = df['potencia_tx']
            modelo_tx_column = df['modelo_tx']
            fabricante_antena_tx_column = df['fabricante_antena_tx']
            modelo_antena_tx_column = df['modelo_antena_tx']
            modelo_rx_column = df['modelo_rx']
            nivel_recepcao_column = df['nivel_recepcao']
            fabricante_antena_rx_column = df['fabricante_antena_rx']
            diametro_antena_rx_column = df['diametro_antena_rx']
            tipo_torre_column = df['tipo_torre']
            altura_torre_column = df['altura_torre']
            modelo_ar_condicionado_column = df['modelo_ar_condicionado']
            comentarios_column = df['comentarios']

            # Loop through each row (row-by-row) and manually insert into the database
            for index in range(len(df)):
                # Check for NaN values and replace them with empty string (" ") or None as needed
                cidade = cidade_column[index] if pd.notna(cidade_column[index]) else ''
                uf = uf_column[index] if pd.notna(uf_column[index]) else ''
                potencia_tx = potencia_tx_column[index] if pd.notna(potencia_tx_column[index]) else ''
                modelo_tx = modelo_tx_column[index] if pd.notna(modelo_tx_column[index]) else ''
                fabricante_antena_tx = fabricante_antena_tx_column[index] if pd.notna(fabricante_antena_tx_column[index]) else ''
                modelo_antena_tx = modelo_antena_tx_column[index] if pd.notna(modelo_antena_tx_column[index]) else ''
                modelo_rx = modelo_rx_column[index] if pd.notna(modelo_rx_column[index]) else ''
                nivel_recepcao = nivel_recepcao_column[index] if pd.notna(nivel_recepcao_column[index]) else ''
                fabricante_antena_rx = fabricante_antena_rx_column[index] if pd.notna(fabricante_antena_rx_column[index]) else ''
                diametro_antena_rx = diametro_antena_rx_column[index] if pd.notna(diametro_antena_rx_column[index]) else None
                tipo_torre = tipo_torre_column[index] if pd.notna(tipo_torre_column[index]) else ''
                altura_torre = altura_torre_column[index] if pd.notna(altura_torre_column[index]) else ''
                modelo_ar_condicionado = modelo_ar_condicionado_column[index] if pd.notna(modelo_ar_condicionado_column[index]) else ''
                comentarios = comentarios_column[index] if pd.notna(comentarios_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - Modelo Tx: {modelo_tx}'))

                # Manually create and save the Dados_Equipamentos object
                try:
                    dados_equipamentos = Dados_Equipamentos(
                        cidade=cidade,
                        uf=uf,
                        potencia_tx=potencia_tx,
                        modelo_tx=modelo_tx,
                        fabricante_antena_tx=fabricante_antena_tx,
                        modelo_antena_tx=modelo_antena_tx,
                        modelo_rx=modelo_rx,
                        nivel_recepcao=nivel_recepcao,
                        fabricante_antena_rx=fabricante_antena_rx,
                        diametro_antena_rx=diametro_antena_rx,
                        tipo_torre=tipo_torre,
                        altura_torre=altura_torre,
                        modelo_ar_condicionado=modelo_ar_condicionado,
                        comentarios=comentarios,
                    )
                    dados_equipamentos.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {cidade}'))
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {cidade} - Error: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while importing {cidade}: {e}'))

            self.stdout.write(self.style.SUCCESS('Data import completed!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
