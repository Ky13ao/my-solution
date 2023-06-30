def edashboardplus_export(args):
    import subprocess
    outputPath = "C:\\testing\\sample_request\\"
    funcName = "MESAgingReport"
    cmd = ['cscript.exe', "ChildHelpers\\edashboardplus_export.js",
           '|'.join([funcName, args.customer_id,  outputPath]), "//nologo"]

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    stdout = []
    while True:
        line = p.stdout.readline()
        if not line:
            break
        stdout.append(line.rstrip())
    return stdout
