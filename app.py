from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# Template HTML/CSS responsivo com Ilustração 2D Canvas sobre Servidores
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidores Web | Infraestrutura e Nuvem</title>
    <!-- Tailwind CSS para estilização rápida -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .hero-bg {
            background: radial-gradient(circle at center, #0f172a 0%, #020617 100%);
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between">

    <!-- Header / Navbar -->
    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <span class="text-2xl font-black bg-gradient-to-r from-cyan-400 to-blue-600 bg-clip-text text-transparent">
                    SERVER-HUB
                </span>
                <span class="bg-blue-950 text-blue-400 text-xs font-semibold px-2.5 py-0.5 rounded border border-blue-800">
                    Infraestrutura
                </span>
            </div>
            <nav class="space-x-6 text-sm font-medium text-slate-400">
                <a href="#conceito" class="hover:text-white transition-colors">Conceito</a>
                <a href="#diagrama" class="hover:text-white transition-colors">Ilustração 2D</a>
                <a href="/api" target="_blank" class="text-cyan-400 hover:text-cyan-300 transition-colors">API JSON</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-bg py-16 px-6 border-b border-slate-800">
        <div class="max-w-5xl mx-auto text-center space-y-6">
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white">
                Como Funcionam os <span class="bg-gradient-to-r from-cyan-400 via-sky-400 to-blue-500 bg-clip-text text-transparent">Servidores Web</span>
            </h1>
            <p class="text-lg md:text-xl text-slate-400 max-w-3xl mx-auto">
                Um servidor é um computador especializado ou programa que processa pedidos de clientes (browsers, apps) e devolve dados através da rede.
            </p>
        </div>
    </section>

    <!-- Interactive 2D Canvas Diagram -->
    <section id="diagrama" class="py-12 px-6 max-w-5xl mx-auto w-full">
        <div class="text-center mb-6">
            <h2 class="text-2xl font-bold text-white">Ilustração 2D: Fluxo Cliente x Servidor</h2>
            <p class="text-sm text-slate-400">Diagrama interativo renderizado via HTML5 Canvas 2D.</p>
        </div>
        
        <div class="relative w-full bg-slate-900 rounded-2xl p-4 border border-slate-800 shadow-2xl flex justify-center items-center">
            <canvas id="serverCanvas" width="800" height="300" class="max-w-full rounded-lg"></canvas>
        </div>
    </section>

    <!-- Features Section -->
    <section id="conceito" class="py-12 px-6 max-w-5xl mx-auto grid md:grid-cols-3 gap-6">
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-cyan-400">1. O Cliente (Browser)</h3>
            <p class="text-sm text-slate-400">
                Envia pedidos HTTP/HTTPS (como <code>GET /</code>) solicitando páginas web, ficheiros ou dados em formato JSON.
            </p>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-sky-400">2. O Servidor Web</h3>
            <p class="text-sm text-slate-400">
                Processa a lógica da aplicação (ex: Flask, Nginx, Node.js), consulta bases de dados e prepara a resposta adequada.
            </p>
        </div>
        <div class="bg-slate-900/60 border border-slate-800 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-blue-400">3. A Resposta</h3>
            <p class="text-sm text-slate-400">
                O servidor devolve o resultado com um código de estado HTTP (ex: <code>200 OK</code>) e os dados ao utilizador.
            </p>
        </div>
    </section>

    <!-- Footer -->
    <footer class="border-t border-slate-800 py-6 text-center text-xs text-slate-500">
        <p>Projeto de demonstração CI/CD & Deploy no Render. Versão 2.0.0</p>
    </footer>

    <!-- Script de Animação e Desenho 2D -->
    <script>
        const canvas = document.getElementById('serverCanvas');
        const ctx = canvas.getContext('2d');
        let packetX = 220;
        let direction = 1;

        function drawDiagram() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Desenhar Cliente 2D (Laptop)
            ctx.fillStyle = '#38bdf8';
            ctx.fillRect(80, 100, 120, 80);
            ctx.fillStyle = '#0284c7';
            ctx.fillRect(60, 180, 160, 12);
            ctx.fillStyle = '#ffffff';
            ctx.font = '14px sans-serif';
            ctx.fillText('Cliente (Browser)', 80, 220);

            // Desenhar Servidor 2D (Rack)
            ctx.fillStyle = '#1e293b';
            ctx.fillRect(600, 70, 120, 140);
            ctx.strokeStyle = '#3b82f6';
            ctx.lineWidth = 2;
            ctx.strokeRect(600, 70, 120, 140);

            // Gavetas do Servidor
            for(let i = 0; i < 4; i++) {
                ctx.fillStyle = '#334155';
                ctx.fillRect(610, 80 + (i * 30), 100, 20);
                // LEDs
                ctx.fillStyle = (Math.floor(Date.now() / 300) % 2 === 0 && i === 0) ? '#22c55e' : '#0ea5e9';
                ctx.beginPath();
                ctx.arc(620, 90 + (i * 30), 3, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.fillStyle = '#ffffff';
            ctx.fillText('Servidor Web', 615, 230);

            // Linha de Conexão de Rede
            ctx.strokeStyle = '#475569';
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.moveTo(220, 140);
            ctx.lineTo(600, 140);
            ctx.stroke();
            ctx.setLineDash([]);

            // Pacote de Dados 2D (Animação)
            ctx.fillStyle = direction === 1 ? '#38bdf8' : '#22c55e';
            ctx.beginPath();
            ctx.arc(packetX, 140, 8, 0, Math.PI * 2);
            ctx.fill();

            // Atualização da Posição do Pacote
            packetX += direction * 3;
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
    """Renderiza a Landing Page sobre Servidores com Ilustração 2D"""
    return render_template_string(HTML_TEMPLATE)


@app.route("/api")
def api():
    """Endpoint que retorna o status da infraestrutura em JSON"""
    return jsonify(
        {
            "status": "sucesso",
            "mensagem": "Servidor operando normalmente!",
            "topico": "Servidores Web e Infraestrutura",
            "versao": "2.0.0",
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
