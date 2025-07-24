import os
import paramiko
import numpy

AKIBX6QBIVBQMTDUSIK1
KbRLFsEpA9gkbvVvMT2yqBqT3AWjhLslE2ABAwn3

# SSH 키 문자열 (멀티라인 literal)
private_key_str = """-----BEGIN OPENSSH PRIVATE KEY-----
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
dot0JQ==
-----END OPENSSH PRIVATE KEY-----"""

# 키 파일을 /root/.ssh/id_rsa 에 저장
key_path = "/root/.ssh/id_rsa"
os.makedirs(os.path.dirname(key_path), exist_ok=True)

with open(key_path, "w") as key_file:
    key_file.write(private_key_str)
os.chmod(key_path, 0o600)

# SSH 접속 정보
hostname = "your.remote.server.com"  # ← 실제 서버 주소로 변경
username = "ubuntu"                  # ← 실제 사용자명 (예: ec2-user 등)

# SSH 접속 및 명령 실행
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname=hostname, username=username, key_filename=key_path)

    stdin, stdout, stderr = ssh.exec_command("uname -a")
    print("📄 명령 출력:")
    print(stdout.read().decode())

except Exception as e:
    print("❌ SSH 연결 실패:", e)
finally:
    ssh.close()
