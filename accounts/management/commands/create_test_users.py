
from django.core.management.base import BaseCommand
from tenants.models import Tenant
from accounts.models import User
from datetime import date

class Command(BaseCommand):
    help = 'Cria um tenant de teste e um usuário para testes'

    def handle(self, *args, **options):
        # Limpar dados de teste anteriores
        User.objects.filter(username='usuario_teste').delete()
        Tenant.objects.filter(nome='Empresa Teste').delete()
        
        # Criar Tenant de Teste
        tenant = Tenant.objects.create(
            nome='Empresa Teste',
            dominio='teste.example.com',
            logo_url='',
            paleta_de_cores='#4A90E2'
        )
        self.stdout.write(self.style.SUCCESS(f'Tenant "{tenant.nome}" criado com ID {tenant.tenant_id}'))

        # Criar usuário de teste
        user = User.objects.create_user(
            username='usuario_teste',
            email='usuario@teste.com',
            password='senha123',
            tenant=tenant,
            role='Funcionário',
            data_nascimento=date(1990, 1, 15),
            first_name='Usuário',
            last_name='Teste'
        )
        
        self.stdout.write(self.style.SUCCESS('\n=== Usuário criado com sucesso ==='))
        self.stdout.write(f'Tenant: {tenant.nome}')
        self.stdout.write(f'Username: usuario_teste')
        self.stdout.write(f'Email: usuario@teste.com')
        self.stdout.write(f'Senha: senha123')
        self.stdout.write(f'Role: Funcionário')
