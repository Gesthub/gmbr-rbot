import subprocess

repo_path = '/content/gmbr-rbot'

codetorun = """
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
!git clone https://github.com/nolanaatama/sd-webui-tunnels /content/gmbr-rbot/extensions/sd-webui-tunnels
!git clone https://github.com/Mikubill/sd-webui-controlnet /content/gmbr-rbot/extensions/sd-webui-controlnet
!git clone https://github.com/hnmr293/posex /content/gmbr-rbot/extensions/posex
!git clone https://github.com/yfszzx/stable-diffusion-webui-images-browser /content/gmbr-rbot/extensions/stable-diffusion-webui-images-browser
"""

codetorun2 = """
!git reset --hard
!git -C /content/gmbr-rbot/repositories/stable-diffusion-stability-ai reset --hard
"""

lines = codetorun.splitlines()

def nylonong(codetoexecute, cwd=''):
    for line in lines:
        line = line.strip()
        if line.startswith('!'):
            line = line[1:]
        if not line == '':
            try:
                if cwd:
                    subprocess.run(line, shell=True, check=True, cwd=repo_path)
                else:
                    subprocess.run(line, shell=True, check=True)
            except Exception as e:
                print("Exception: " + str(e))

nylonong(lines)

lines = codetorun2.splitlines()

nylonong(lines, repo_path)

