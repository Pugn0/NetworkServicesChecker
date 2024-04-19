# DNSandMXChecker
## Isenção de Responsabilidade

Este projeto é fornecido "como está", sem garantias de qualquer tipo. Os desenvolvedores deste projeto não se responsabilizam por quaisquer consequências diretas, indiretas, incidentais, especiais, exemplares ou punitivas decorrentes do uso do software ou código fornecido. Este projeto é apenas para fins educacionais e não deve ser usado para atividades ilegais ou maliciosas. O uso deste projeto é inteiramente por sua conta e risco.

## Sobre o Projeto
O DNSandMXChecker é uma ferramenta de linha de comando projetada para verificar registros DNS e MX de domínios específicos. Ele permite que administradores de sistemas e desenvolvedores testem a conectividade com servidores de e-mail e a resolução de registros DNS, fornecendo insights úteis sobre a configuração e saúde do domínio na internet.

## Funcionalidades
- **Verificação de registros MX**: Testa e valida registros de Mail Exchange (MX) de um domínio.
- **Testes de conectividade SMTP**: Verifica a conectividade com servidores de e-mail através de testes SMTP.
- **Ping de servidores**: Realiza testes de ping para endereços IP associados aos registros MX.
- **Resolução de registros DNS**: Resolve registros A e AAAA para domínios.

## Requisitos
- Python 3.6 ou superior
- Bibliotecas: `dnspython`, `pythonping`, `colorama`

## Instalação

Para instalar e executar o DNSandMXChecker, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Pugn0/DNSandMXChecker.git
   
2. Navegue até o diretório do projeto:
   ```bash
   cd DNSandMXChecker

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

4. Execute o script:
   ```bash
   python script.py -ALL yourdomain.com
   
## Agradecimentos
Agradeço a todos que contribuíram para o desenvolvimento desta ferramenta, em especial à comunidade de desenvolvedores Python e aos contribuidores dos pacotes utilizados.

## Contato
- **E-mail**: pugno@x.com
- **Telegram**: [t.me/pugno_fc](https://t.me/pugno_fc)

