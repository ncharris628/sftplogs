import sys
import subprocess

def download_log():
    dir = "log_history"
    ##file = file
    # --- add creds to conf file.
    qa_host = "treppftp-qa.ftptoday.com"
    qa_user = "treppprod"
    qa_pw = "@TreppLLC212"

    remote_download = "."
    local_download = "/export/home/nharris/sftpusers/downloads/"
    local_download = local_download + dir
    remote_download = remote_download + "/" + dir

    print ("Download directory specified : " + local_download)
    print("Running Download")
    print("Downloading from " + remote_download)
    print("Downloading to " + local_download)

    exec_cmd = 'lftp -e "open sftp://{}:{{}}@{}; mirror {} {}; bye"'.format(qa_user, qa_host, remote_download, local_download)
    run(exec_cmd, qa_pw)

def run(cmd, passwd):
    #print(cmd.format('********'))
    print(cmd.format(passwd))
    start_time = datetime.now()
    subprocess.call(cmd.format(passwd), shell = True)

def main():
    download_log()
