import pandas as pd
from django.core.management.base import BaseCommand
from ...models import Dados_IBGE
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Manually import data from Excel file into the Dados_IBGE model'

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
            uf_column = df['uf']
            codigo_column = df['codigo']
            prefeito_column = df['prefeito']
            area_territorial_column = df['area_terrritorial']
            populacao_column = df['populacao']
            densidade_demografica_column = df['densidade_demografica']
            escolarizacao_column = df['escolarizacao']
            cobertura_feita_por_column = df['cobertura_feita_por']

            # Loop through each row (row-by-row) and manually insert into the database
            for index in range(len(df)):
                # Check for NaN values and replace them with None (NULL in MySQL)
                cidade = cidade_column[index] if pd.notna(cidade_column[index]) else ''
                uf = uf_column[index] if pd.notna(uf_column[index]) else ''
                codigo = codigo_column[index] if pd.notna(codigo_column[index]) else ''
                prefeito = prefeito_column[index] if pd.notna(prefeito_column[index]) else ''
                area_territorial = area_territorial_column[index] if pd.notna(area_territorial_column[index]) else None
                populacao = populacao_column[index] if pd.notna(populacao_column[index]) else None
                densidade_demografica = densidade_demografica_column[index] if pd.notna(densidade_demografica_column[index]) else None
                escolarizacao = escolarizacao_column[index] if pd.notna(escolarizacao_column[index]) else None
                cobertura_feita_por = cobertura_feita_por_column[index] if pd.notna(cobertura_feita_por_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - UF: {uf}'))

                # Manually create and save the Dados_IBGE object
                try:
                    dados_ibge = Dados_IBGE(
                        cidade=cidade,
                        uf=uf,
                        codigo=codigo,
                        prefeito=prefeito,
                        area_territorial=area_territorial,
                        populacao=populacao,
                        densidade_demografica=densidade_demografica,
                        escolarizacao=escolarizacao,
                        cobertura_feita_por=cobertura_feita_por,
                    )
                    dados_ibge.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {cidade}'))
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {cidade} - Error: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while importing {cidade}: {e}'))

            self.stdout.write(self.style.SUCCESS('Data import completed!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
