Stop-Service -Name WinDefend -ErrorAction SilentlyContinue
Set-MpPreference -PUAProtection disabled -DisableBlockAtFirstSeen:$true -DisableCpuThrottleOnIdleScans:$true -MAPSReporting Disabled -SubmitSamplesConsent NeverSend -DisableAutoExclusions:$true -DisablePrivacyMode:$true -RandomizeScheduleTaskTimes:$true -DisableBehaviorMonitoring:$true -DisableRealtimeMonitoring:$true -DisableScriptScanning:$true -DisableArchiveScanning:$true -DisableCatchupFullScan:$true -DisableCatchupQuickScan:$true -DisableEmailScanning:$true -DisableRemovableDriveScanning:$true -DisableScanningMappedNetworkDrivesForFullScan:$true -DisableScanningNetworkFiles:$true -DisableIOAVProtection:$true -DisableDatagramProcessing:$true -DisableIntrusionPreventionSystem:$true -DisableNetworkProtection:$true -EnableControlledFolderAccess Disabled -HighThreatDefaultAction 6 -Force -LowThreatDefaultAction 6 -SevereThreatDefaultAction 6 -ScanScheduleDay 8 
Set-MpPreference -DisableRealtimeMonitoring 1
Set-MpPreference -DisableRealtimeMonitoring $true
Set-MpPreference -DisableRealtimeMonitoring:$true
cmd.exe /c reg delete "HKLM\Software\Policies\Microsoft\Windows Defender" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiSpyware" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender" /v "DisableAntiVirus" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\MpEngine" /v "MpEnablePus" /t cmd.exe /c reg_DWORD /d "0" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableBehaviorMonitoring" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableIOAVProtection" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableOnAccessProtection" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Real-Time Protection" /v "DisableScanOnRealtimeEnable" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\Reporting" /v "DisableEnhancedNotifications" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "DisableBlockAtFirstSeen" /t cmd.exe /c reg_DWORD /d "1" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SpynetReporting" /t cmd.exe /c reg_DWORD /d "0" /f
cmd.exe /c reg add "HKLM\Software\Policies\Microsoft\Windows Defender\SpyNet" /v "SubmitSamplesConsent" /t cmd.exe /c reg_DWORD /d "0" /f