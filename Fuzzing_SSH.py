from datetime import datetime
from pathlib import Path

if __name__ == '__main__':

    Path_logs = Path('/var/log')

    SSH_logs= Path_logs / "auth.log"


    ttl_error=0
    ttl_banner_exchange = 0

    with open(SSH_logs, "r") as F:

        while True:

            for line in F.readlines():

                current_time = datetime.now()
                time_pattern = current_time.strftime("%H:%M:%S")

                if line.find(time_pattern) !=-1:

                    current_line= line
                    if current_line.find("sshd") and current_line.find("error"):
                        ttl_error=ttl_error+1

                        if ttl_error >= 6:
                            print("Fuzzing Detected")
                            exit()


                    if current_line.find("sshd") and current_line.find("banner exchange") and ("invalid format"):
                        ttl_banner_exchange = ttl_banner_exchange + 1

                        if ttl_banner_exchange >=6:
                            print("Fuzzing Detected")
                            exit()

