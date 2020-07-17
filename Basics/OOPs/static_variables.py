class ExitStatus:
    exit_status=0
    def something_happened(self):
        ExitStatus.exit_status=1
print(ExitStatus.exit_status)
a=ExitStatus()
a.something_happened()        
print(ExitStatus.exit_status)
ExitStatus.exit_status=2
print(ExitStatus.exit_status)
