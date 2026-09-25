from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A-Frame | Realidade Virtual na Web</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://aframe.io/releases/1.4.0/aframe.min.js"></script>
    <style>
        .hero-bg {
            background: radial-gradient(circle at center, #1e1b4b 0%, #0f172a 100%);
        }
    </style>
</head>
<body class="bg-slate-900 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between">

    <header class="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-6 py-4 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <span class="text-2xl font-black bg-gradient-to-r from-pink-500 to-violet-500 bg-clip-text text-transparent">
                    A-FRAME
                </span>
                <span class="bg-violet-900/50 text-violet-300 text-xs font-semibold px-2.5 py-0.5 rounded border border-violet-700">
                    WebXR / VR
                </span>
            </div>
            <nav class="space-x-6 text-sm font-medium text-slate-400">
                <a href="#sobre" class="hover:text-white transition-colors">Sobre</a>
                <a href="#demo" class="hover:text-white transition-colors">Cena 3D</a>
                <a href="/api" target="_blank" class="text-pink-400 hover:text-pink-300 transition-colors">API JSON</a>
            </nav>
        </div>
    </header>

    <section class="hero-bg py-16 px-6 border-b border-slate-800">
        <div class="max-w-5xl mx-auto text-center space-y-6">
            <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight text-white">
                Crie experiências de <span class="bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 bg-clip-text text-transparent">Realidade Virtual</span> na Web
            </h1>
            <p class="text-lg md:text-xl text-slate-400 max-w-3xl mx-auto">
                A-Frame é um framework web open-source para construção de experiências de 3D, VR e AR usando simples tags HTML declarativas.
            </p>
            <div class="flex justify-center gap-4 pt-4">
                <a href="#demo" class="bg-pink-600 hover:bg-pink-500 text-white font-semibold px-6 py-3 rounded-lg shadow-lg transition-all">
                    Ver Exemplo 3D
                </a>
                <a href="https://aframe.io/docs/" target="_blank" class="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold px-6 py-3 rounded-lg transition-all">
                    Documentação Oficial
                </a>
            </div>
        </div>
    </section>

    <section id="demo" class="py-12 px-6 max-w-5xl mx-auto w-full">
        <div class="text-center mb-6">
            <h2 class="text-2xl font-bold text-white">Demonstração Interativa em A-Frame</h2>
            <p class="text-sm text-slate-400">Arraste com o rato para rodar a câmara 3D dentro do container abaixo.</p>
        </div>
        
        <div class="relative w-full h-[400px] rounded-2xl overflow-hidden border border-slate-700 shadow-2xl">
            <a-scene embedded class="w-full h-full">
                <a-box position="-1 0.5 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
                <a-sphere position="0 1.25 -5" radius="1.25" color="#EF2D5E"></a-sphere>
                <a-cylinder position="1 0.75 -3" radius="0.5" height="1.5" color="#FFC65D"></a-cylinder>
                <a-plane position="0 0 -4" rotation="-90 0 0" width="4" height="4" color="#7BC8A4"></a-plane>
                <a-sky color="#0f172a"></a-sky>
            </a-scene>
        </div>
    </section>

    <section id="sobre" class="py-12 px-6 max-w-5xl mx-auto grid md:grid-cols-3 gap-6">
        <div class="bg-slate-800/50 border border-slate-700/60 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-pink-400">HTML Declarativo</h3>
            <p class="text-sm text-slate-400">
                Desenvolva WebVR apenas escrevendo tags como &lt;a-box&gt; e &lt;a-sphere&gt;, sem precisar de configurar do zero retângulos WebGL complexos.
            </p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700/60 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-purple-400">Entity-Component</h3>
            <p class="text-sm text-slate-400">
                Construído sobre Three.js com arquitetura Entity-Component-System (ECS), oferecendo extensibilidade total e alto desempenho.
            </p>
        </div>
        <div class="bg-slate-800/50 border border-slate-700/60 p-6 rounded-xl space-y-2">
            <h3 class="text-xl font-bold text-indigo-400">Multiplataforma</h3>
            <p class="text-sm text-slate-400">
                Funciona em navegadores desktop, dispositivos móveis (iOS/Android) e óculos de RV (Meta Quest, HTC Vive, Apple Vision Pro).
            </p>
        </div>
    </section>

    <footer class="border-t border-slate-800 py-6 text-center text-xs text-slate-500">
        <p>Projeto de demonstração CI/CD & Deploy no Render. Versão 1.2.0</p>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    """Renderiza a Landing Page interativa sobre A-Frame"""
    return render_template_string(HTML_TEMPLATE)

@app.route("/api")
def api():
    """Endpoint que retorna o status em JSON"""
    return jsonify({
        "status": "sucesso",
        "mensagem": "API Python rodando perfeitamente!",
        "tecnologia": "A-Frame / WebXR",
        "versao": "1.2.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
