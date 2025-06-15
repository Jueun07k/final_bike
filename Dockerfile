import subprocess

def install_nanum_font():
    subprocess.run(['apt-get', 'update'], check=True)
    subprocess.run(['apt-get', 'install', '-y', 'fonts-nanum'], check=True)
    subprocess.run(['fc-cache', '-fv'], check=True)
    print("✅ Nanum 폰트 설치 완료")

install_nanum_font()
