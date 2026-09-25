from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidores Web | Infraestrutura e Nuvem</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .hero-bg {
            background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        }
        .glow-cyan {
            box-shadow: 0 0 20px rgba(56, 189, 248, 0.2);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between">

    <header class="border-b border-slate-800/80 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <span class="text-2xl font-black bg-gradient-to-r from-cyan-400 to-blue-600 bg-clip-text text-transparent">
                    SERVER-HUB
                </span>
                <span class="bg-blue-950/80 text-blue-400 text-xs font-semibold px-2.5 py-0.5 rounded-full border border-blue-800">
                    Infraestrutura v2.1
                </span>
            </div>
            <nav class="space-x-6 text-sm font-medium text-slate-400">
                <a href="#conceito" class="hover:text-cyan-400 transition-colors">Conceito</a>
                <a href="#diagrama" class="hover:text-cyan-400 transition-colors">Ilustração 2D</a>
                <a href="/api" target="_blank" class="text-cyan-400 hover:text-cyan-300 font-semibold transition-colors">API JSON ↗</a>
            </nav>
        </div>
    </header>

    <section class="hero-bg py-16 px-6 border-b border-slate-800/60">
        <div class="max-w-5xl mx-auto text-center space-y-6">
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white">
                Como Funcionam os <span class="bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500 bg-clip-text text-transparent">Servidores Web</span>
            </h1>
            <p class="text-lg md:text-xl text-slate-400 max-w-3xl mx-auto">
                Um servidor é o coração da web moderna: recebe requisições, processa a regra de negócio e entrega respostas instantâneas para navegadores e aplicações.
            </p>
            <div class="flex justify-center gap-4 pt-2">
                <a href="#diagrama" class="bg-cyan-600 hover:bg-cyan-500 text-slate-950 font-bold px-6 py-3 rounded-lg shadow-lg transition-all">
                    Ver Fluxo 2D
                </a>
                <a href="/api" target="_blank" class="bg-slate-900 hover:bg-slate-800 text-slate-200 border border-slate-700 font-semibold px-6 py-3 rounded-lg transition-all">
                    Testar Endpoint /api
                </a>
            </div>
        </div>
    </section>

    <section id="diagrama" class="py-12 px-6 max-w-5xl mx-auto w-full">
        <div class="text-center mb-6 space-y-1">
            <h2 class="text-2xl font-bold text-white">Ilustração 2D: Fluxo Cliente x Servidor</h2>
            <p class="text-sm text-slate-400">Simulação em tempo real via HTML5 Canvas 2D.</p>
        </div>
        
        <div class="relative w-full bg-slate-900/90 rounded-2xl p-4 border border-slate-800 glow-cyan shadow-2xl flex justify-center items-center">
            <canvas id="serverCanvas" width="800" height="300" class="max-w-full rounded-lg"></canvas>
        </div>

        <div class="grid grid-cols-3 gap-4 mt-6 text-center">
            <div class="bg-slate-900/40 border border-slate-800/80 p-4 rounded-xl">
                <p class="text-xs text-slate-500 uppercase tracking-wider font-semibold">Uptime da API</p>
                <p class="text-xl font-bold text-emerald-400">99.9%</p>
            </div>
            <div class="bg-slate-900/40 border border-slate-800/80 p-4 rounded-xl">
                <p class="text-xs text-slate-500 uppercase tracking-wider font-semibold">Protocolo</p>
                <p class="text-xl font-bold text-cyan-400">HTTP / 2</p>
            </div>
            <div class="bg-slate-900/40 border border-slate-800/80 p-4 rounded-xl">
                <p class="text-xs text-slate-500 uppercase tracking-wider font-semibold">Latência Estimada</p>
                <p class="text-xl font-bold text-sky-400">&lt; 15ms</p>
            </div>
        </div>
    </section>

    <section id="conceito" class="py-12 px-6 max-w-5xl mx-auto grid md:grid-cols-3 gap-6">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2 hover:border-cyan-500/50 transition-colors">
            <h3 class="text-xl font-bold text-cyan-400">1. O Cliente (Browser)</h3>
            <p class="text-sm text-slate-400">
                Envia pedidos HTTP/HTTPS (como <code>GET /</code>) solicitando páginas web, ficheiros estáticos ou respostas em JSON.
            </p>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2 hover:border-sky-500/50 transition-colors">
            <h3 class="text-xl font-bold text-sky-400">2. O Servidor Web</h3>
            <p class="text-sm text-slate-400">
                Processa a lógica da aplicação (ex: Flask, Python, Nginx), consulta dados e constrói o payload de resposta.
            </p>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2 hover:border-blue-500/50 transition-colors">
            <h3 class="text-xl font-bold text-blue-400">3. A Resposta (Response)</h3>
            <p class="text-sm text-slate-400">
                Retorna o status HTTP (ex: <code>200 OK</code>) acompanhado dos ficheiros HTML/CSS ou dados JSON solicitados.
            </p>
        </div>
    </section>

    <footer class="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500">
        <p>Projeto de demonstração CI/CD & Deploy no Render. Versão 2.1.0</p>
    </footer>

    <script>
        const canvas = document.getElementById('serverCanvas');
        const ctx = canvas.getContext('2d');
        let packetX = 220;
        let direction = 1;

        function drawDiagram() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            ctx.fillStyle = '#38bdf8';
            ctx.fillRect(80, 100, 120, 80);
            ctx.fillStyle = '#0284c7';
            ctx.fillRect(60, 180, 160, 12);
            ctx.fillStyle = '#f8fafc';
            ctx.font = 'bold 13px sans-serif';
            ctx.fillText('Cliente (Browser)', 75, 220);

            ctx.fillStyle = '#0284c7';
            ctx.fillRect(85, 105, 110, 70);

            ctx.fillStyle = '#1e293b';
            ctx.fillRect(600, 70, 120, 140);
            ctx.strokeStyle = '#0284c7';
            ctx.lineWidth = 2;
            ctx.strokeRect(600, 70, 120, 140);

            for(let i = 0; i < 4; i++) {
                ctx.fillStyle = '#334155';
                ctx.fillRect(610, 80 + (i * 30), 100, 20);
                ctx.fillStyle = (Math.floor(Date.now() / 250) % 2 === 0 && i === 0) ? '#22c55e' : '#38bdf8';
                ctx.beginPath();
                ctx.arc(620, 90 + (i * 30), 3, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.fillStyle = '#f8fafc';
            ctx.font = 'bold 13px sans-serif';
            ctx.fillText('Servidor Web', 615, 235);

            ctx.strokeStyle = '#334155';
            ctx.setLineDash([6, 6]);
            ctx.beginPath();
            ctx.moveTo(220, 140);
            ctx.lineTo(600, 140);
            ctx.stroke();
            ctx.setLineDash([]);

            const isRequest = direction === 1;
            const packetColor = isRequest ? '#38bdf8' : '#22c55e';
            
            ctx.shadowColor = packetColor;
            ctx.shadowBlur = 12;
            ctx.fillStyle = packetColor;
            ctx.beginPath();
            ctx.arc(packetX, 140, 9, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0;

            ctx.fillStyle = '#94a3b8';
            ctx.font = '11px monospace';
            const label = isRequest ? 'HTTP GET' : '200 OK';
            ctx.fillText(label, packetX - 20, 120);

            packetX += direction * 3.5;
            if (packetX >= 590) {
                direction = -1;
            } else if (packetX <= 230) {
                direction = 1;
            }

            requestAnimationFrame(drawDiagram);
        }

        drawDiagram();
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)


@app.route("/api")
def api():
    return jsonify(
        {
            "status": "sucesso",
            "topico": "Servidores Web e Infraestrutura",
            "versao": "2.1.0",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
