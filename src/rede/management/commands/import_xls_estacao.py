import pandas as pd
from django.core.management.base import BaseCommand
import rede.models as models  # Update this to the correct model path
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Manually import data from Excel file into the Estacao model'

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
            canal_virtual_column = df['canal_virtual']
            potencia_projeto_column = df['potencia_projeto']
            potencia_operacao_column = df['potencia_operacao']
            sfn_column = df['sfn']
            equipe_column = df['equipe']
            operacao_column = df['operacao']
            status_operacao_column = df['status_operacao']
            proprietario_torre_column = df['proprietario_torre']
            pgto_energia_column = df['pgto_energia']
            pgto_aluguel_column = df['pgto_aluguel']
            pgto_agua_column = df['pgto_agua']
            proprietario_terreno_column = df['proprietario_terreno']
            endereco_column = df['endereco']
            comentarios_column = df['comentarios']

            # Loop through each row (row-by-row) and manually insert into the database
            for index in range(len(df)):
                # Check for NaN values and replace them with empty string (" ") or None as needed
                cidade = cidade_column[index] if pd.notna(cidade_column[index]) else ''
                uf = uf_column[index] if pd.notna(uf_column[index]) else ''
                canal_virtual = canal_virtual_column[index] if pd.notna(canal_virtual_column[index]) else ''
                potencia_projeto = potencia_projeto_column[index] if pd.notna(potencia_projeto_column[index]) else ''
                potencia_operacao = potencia_operacao_column[index] if pd.notna(potencia_operacao_column[index]) else ''
                sfn = sfn_column[index] if pd.notna(sfn_column[index]) else ''
                equipe = equipe_column[index] if pd.notna(equipe_column[index]) else ''
                operacao = operacao_column[index] if pd.notna(operacao_column[index]) else ''
                status_operacao = status_operacao_column[index] if pd.notna(status_operacao_column[index]) else ''
                proprietario_torre = proprietario_torre_column[index] if pd.notna(proprietario_torre_column[index]) else ''
                pgto_energia = pgto_energia_column[index] if pd.notna(pgto_energia_column[index]) else ''
                pgto_aluguel = pgto_aluguel_column[index] if pd.notna(pgto_aluguel_column[index]) else ''
                pgto_agua = pgto_agua_column[index] if pd.notna(pgto_agua_column[index]) else ''
                proprietario_terreno = proprietario_terreno_column[index] if pd.notna(proprietario_terreno_column[index]) else ''
                endereco = endereco_column[index] if pd.notna(endereco_column[index]) else ''
                comentarios = comentarios_column[index] if pd.notna(comentarios_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - Canal Virtual: {canal_virtual}'))

                # Manually create and save the Estacao object
                try:
                    estacao = models.Estacao(
                        cidade=cidade,
                        uf=uf,
                        canal_virtual=canal_virtual,
                        potencia_projeto=potencia_projeto,
                        potencia_operacao=potencia_operacao,
                        sfn=sfn,
                        equipe=equipe,
                        operacao=operacao,
                        status_operacao=status_operacao,
                        proprietario_torre=proprietario_torre,
                        pgto_energia=pgto_energia,
                        pgto_aluguel=pgto_aluguel,
                        pgto_agua=pgto_agua,
                        proprietario_terreno=proprietario_terreno,
                        endereco=endereco,
                        comentarios=comentarios
                    )
                    estacao.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported {cidade}'))
                except IntegrityError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to import {cidade} - Error: {e}'))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error while importing {cidade}: {e}'))

            self.stdout.write(self.style.SUCCESS('Data import completed!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
