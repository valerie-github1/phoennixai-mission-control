import base64, os, re

logo_path = r'C:\Users\wilco\phoennixai-mission-control\PhoennixAI.jpg'
base = r'C:\Users\wilco\phoennixai-mission-control'

if os.path.exists(logo_path):
    with open(logo_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('utf-8')
    favicon = '<link rel="icon" type="image/jpeg" href="data:image/jpeg;base64,' + b64 + '">'
    print("Logo loaded OK")
else:
    favicon = '<link rel="icon" type="image/jpeg" href="https://phoennixai-mission-control.vercel.app/PhoennixAI.jpg">'
    print("Using URL favicon")

files = ['PhoennixAI_PaymentConfirmation.html','PhoennixAI_NDA_SignHub.html','PhoennixAI_Auth_Login.html','PhoennixAI_BetaWaitlist_Landing.html','PhoennixAI_BetaWaitlist.html','BetaDashboard.html']

for fname in files:
    fpath = os.path.join(base, fname)
    if not os.path.exists(fpath):
        print('SKIP: ' + fname)
        continue
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    if 'rel="icon"' in content:
        content = re.sub(r'<link[^>]*rel="icon"[^>]*>', favicon, content)
        action = 'UPDATED'
    else:
        content = content.replace('<meta charset', favicon + '\n<meta charset', 1)
        action = 'ADDED'
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(action + ': ' + fname)

print('All done.')
