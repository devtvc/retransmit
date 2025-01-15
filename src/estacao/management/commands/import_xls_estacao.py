import pandas as pd
from django.core.management.base import BaseCommand
from ...models import Estacao
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
            sfn_id_column = df['sfn_id']
            equipe_column = df['equipe']
            responsabilidade_operacao_column = df['responsabilidade_operacao']
            status_operacao_column = df['status_operacao']
            modelo_tx_column = df['modelo_tx']
            fabricante_antena_tx_column = df['fabricante_antena_tx']
            modelo_antena_tx_column = df['modelo_antena_tx']
            modelo_rx_column = df['modelo_rx']
            fabricante_antena_rx_column = df['fabricante_antena_rx']
            diametro_antena_rx_column = df['diametro_antena_rx']
            tipo_torre_column = df['tipo_torre']
            altura_torre_column = df['altura_torre']
            modelo_ar_condicionado_column = df['modelo_ar_condicionado']
            status_telemetria_column = df['status_telemetria']
            proprietario_torre_column = df['proprietario_torre']
            energia_paga_por_column = df['energia_paga_por']
            aluguel_pago_por_column = df['aluguel_pago_por']
            agua_paga_por_column = df['agua_paga_por']
            iptu_pago_por_column = df['iptu_pago_por']
            proprietario_terreno_column = df['proprietario_terreno']
            tipo_abrigo_column = df['tipo_abrigo']
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
                sfn_id = sfn_id_column[index] if pd.notna(sfn_id_column[index]) else ''
                equipe = equipe_column[index] if pd.notna(equipe_column[index]) else ''
                responsabilidade_operacao = responsabilidade_operacao_column[index] if pd.notna(responsabilidade_operacao_column[index]) else ''
                status_operacao = status_operacao_column[index] if pd.notna(status_operacao_column[index]) else ''
                modelo_tx = modelo_tx_column[index] if pd.notna(modelo_tx_column[index]) else ''
                fabricante_antena_tx = fabricante_antena_tx_column[index] if pd.notna(fabricante_antena_tx_column[index]) else ''
                modelo_antena_tx = modelo_antena_tx_column[index] if pd.notna(modelo_antena_tx_column[index]) else ''
                modelo_rx = modelo_rx_column[index] if pd.notna(modelo_rx_column[index]) else ''
                fabricante_antena_rx = fabricante_antena_rx_column[index] if pd.notna(fabricante_antena_rx_column[index]) else ''
                diametro_antena_rx = diametro_antena_rx_column[index] if pd.notna(diametro_antena_rx_column[index]) else None
                tipo_torre = tipo_torre_column[index] if pd.notna(tipo_torre_column[index]) else ''
                altura_torre = altura_torre_column[index] if pd.notna(altura_torre_column[index]) else ''
                modelo_ar_condicionado = modelo_ar_condicionado_column[index] if pd.notna(modelo_ar_condicionado_column[index]) else ''
                proprietario_torre = proprietario_torre_column[index] if pd.notna(proprietario_torre_column[index]) else ''
                status_telemetria = status_telemetria_column[index] if pd.notna(status_telemetria_column[index]) else ''
                energia_paga_por = energia_paga_por_column[index] if pd.notna(energia_paga_por_column[index]) else ''
                aluguel_pago_por = aluguel_pago_por_column[index] if pd.notna(aluguel_pago_por_column[index]) else ''
                agua_paga_por = agua_paga_por_column[index] if pd.notna(agua_paga_por_column[index]) else ''
                iptu_pago_por = iptu_pago_por_column[index] if pd.notna(iptu_pago_por_column[index]) else ''
                proprietario_terreno = proprietario_terreno_column[index] if pd.notna(proprietario_terreno_column[index]) else ''
                tipo_abrigo = tipo_abrigo_column[index] if pd.notna(tipo_abrigo_column[index]) else ''
                endereco = endereco_column[index] if pd.notna(endereco_column[index]) else ''
                comentarios = comentarios_column[index] if pd.notna(comentarios_column[index]) else ''

                # Debugging: Log the data being processed
                self.stdout.write(self.style.SUCCESS(f'Importing: {cidade} - Canal Virtual: {canal_virtual}'))

                # Manually create and save the Estacao object
                try:
                    estacao = Estacao(
                        cidade=cidade,
                        uf=uf,
                        canal_virtual=canal_virtual,
                        potencia_projeto=potencia_projeto,
                        potencia_operacao=potencia_operacao,
                        sfn=sfn,
                        sfn_id=sfn_id,
                        equipe=equipe,
                        responsabilidade_operacao=responsabilidade_operacao,
                        status_operacao=status_operacao,
                        modelo_tx=modelo_tx,
                        fabricante_antena_tx=fabricante_antena_tx,
                        modelo_antena_tx=modelo_antena_tx,
                        modelo_rx=modelo_rx,
                        fabricante_antena_rx=fabricante_antena_rx,
                        diametro_antena_rx=diametro_antena_rx,
                        tipo_torre=tipo_torre,
                        altura_torre=altura_torre,
                        modelo_ar_condicionado=modelo_ar_condicionado,
                        proprietario_torre=proprietario_torre,
                        status_telemetria=status_telemetria,
                        energia_paga_por=energia_paga_por,
                        aluguel_pago_por=aluguel_pago_por,
                        agua_paga_por=agua_paga_por,
                        iptu_pago_por=iptu_pago_por,
                        proprietario_terreno=proprietario_terreno,
                        tipo_abrigo=tipo_abrigo,
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
