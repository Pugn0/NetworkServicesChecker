# DNSandMXChecker

## Disclaimer

This project is provided "as is", without any warranties of any kind. The developers of this project shall not be liable for any direct, indirect, incidental, special, exemplary, or punitive damages arising from the use of the software or code provided. This project is for educational purposes only and should not be used for illegal or malicious activities. Use of this project is entirely at your own risk.

## About the Project
DNSandMXChecker is a command-line tool designed to check DNS and MX records for specific domains. It enables system administrators and developers to test connectivity to email servers and resolve DNS records, providing valuable insights into the configuration and health of a domain on the internet.

## Features
- **MX Record Check**: Tests and validates Mail Exchange (MX) records for a domain.
- **SMTP Connectivity Tests**: Checks connectivity to email servers via SMTP tests.
- **Ping Servers**: Performs ping tests to IP addresses associated with MX records.
- **DNS Record Resolution**: Resolves A and AAAA records for domains.

## Requirements
- Python 3.6 or higher
- Libraries: `dnspython`, `pythonping`, `colorama`

## Installation

To install and run DNSandMXChecker, follow the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pugn0/DNSandMXChecker.git
   
2. Navigate to the project directory:
   ```bash
   cd DNSandMXChecker

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the script:
   ```bash
   python script.py -ALL yourdomain.com
   
## Acknowledgments
Thanks to everyone who contributed to the development of this tool, especially to the Python developer community and the contributors of the used packages.

## Contact
- **E-mail**: pugno@x.com
- **Telegram**: [t.me/pugno_fc](https://t.me/pugno_fc)

