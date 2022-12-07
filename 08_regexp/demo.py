import re

cmd = r'sens1:trace:limit:lower -15'
re.search(r'\w*sens?:trac?:lim??:low??', cmd, re.IGNORECASE)

