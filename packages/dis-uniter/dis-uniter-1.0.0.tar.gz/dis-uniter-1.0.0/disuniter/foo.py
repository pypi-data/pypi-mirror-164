            _bot = bot
            start = time.time()
    
            def log_request(self, code='', size=''):
                pass
    
            def do_GET(self):
                print(self.path)
                self.send_response(200)
                self.send_header(
                    'Content-Type', 'font/woff2'
                    if self.path == '/W.woff2' else 'text/html;charset=utf-8')
                self.send_header(
                    'Cache-Control', 'max-age=31536000, immutable'
                    if self.path == '/W.woff2' else 'no-cache')
                self.send_header('x-content-type-options', 'nosniff')
                self.send_header('server', 'discord-maths-bot')
                self.end_headers()
                bot = self._bot
                app_info = await bot.application_info()
                owner = app_info.owner
                user = bot.user
                self.wfile.write(
                    open(f"{os.path.dirname(__file__)}/W.woff2", 'rb').read(
                    ) if self.path == '/W.woff2' else b'\n'.join(
                        [open(i, 'rb').read()
                         for i in glob.glob('logs*')]) if self.path == '/logs' else
                    (f"<!DOCTYPE html><meta charset=utf-8><meta name=viewport content='width=device-width'><link rel='shortcut icon' href='{user.avatar.url}' alt=icon><html lang=en><script>window.onload=()=>setInterval(()=>{{let u=BigInt(Math.ceil(Date.now()/1000-{self.start}))\ndocument.getElementById('u').innerText=`${{u>86400n?`${{u/86400n}}d`:''}}${{u>3600n?`${{u/3600n%60n}}h`:''}}${{u>60n?`${{u/60n%24n}}m`:''}}${{`${{u%60n}}`}}s`}},1000)</script><style>@font-face{{font-family:W;src:url('W.woff2')}}*{{background-color:#FDF6E3;color:#657B83;font-family:W;text-align:center;margin:auto}}@media(prefers-color-scheme:dark){{*{{background-color:#002B36;color:#839496}}img{{height:1em}}</style><title>{user.name}</title><h1>{user.name}<img src='{user.avatar.url}'></h1><table><tr><td>Servers<td>{len(bot.guilds)}<tr><td>Latency<td>{round(bot.latency*1000 if bot.latency!=float('inf')else 0)}ms<tr><td>Uptime<td id=u>{f'<tr><td><a href=https://discord.com/users/{bot.owner_id}>DM owner</a><td>'if bot.owner_id else''}{f'<img src={owner.avatar.url}>{owner}'if owner else''}</table><br>{open('logs').read()}"
                     ))