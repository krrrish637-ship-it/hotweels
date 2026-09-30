from http.server import HTTPServer, BaseHTTPRequestHandler
import os

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cargando tu ramo de Hot Wheels... 🏎️💙</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: #030814;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            overflow: hidden;
            position: relative;
        }

        /* Pantalla de Carga */
        #loading-screen {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            z-index: 100;
            transition: opacity 1s ease, visibility 1s;
        }

        .loading-title {
            font-size: 1.8rem;
            color: #8ed0ff;
            margin-bottom: 25px;
            text-shadow: 0 0 10px rgba(142, 208, 255, 0.5);
        }

        .car-container {
            position: relative;
            width: 280px;
            height: 50px;
            border-bottom: 3px solid #1e3a5f;
            margin-bottom: 20px;
        }

        .car {
            position: absolute;
            left: 0%;
            bottom: 5px;
            font-size: 2.2rem;
            transform: translateX(-50%);
            transition: left 0.1s linear;
        }

        .percentage {
            font-size: 2.5rem;
            font-weight: bold;
            color: #4fc3f7;
            text-shadow: 0 0 15px rgba(79, 195, 247, 0.8);
        }

        /* Contenido Principal (Ramo) */
        #main-content {
            display: none;
            opacity: 0;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            height: 100vh;
            transition: opacity 1.5s ease;
            position: relative;
        }

        .title {
            font-size: 2rem;
            color: #8ed0ff;
            margin-top: 20px;
            text-align: center;
            text-shadow: 0 0 12px rgba(142, 208, 255, 0.7);
            z-index: 10;
        }

        /* SVG del Ramo de Flores */
        .bouquet-container {
            position: relative;
            width: 320px;
            height: 380px;
            display: flex;
            justify-content: center;
            align-items: flex-end;
            margin-top: 10px;
        }

        /* Estrellas / Luces de fondo */
        .bg-glow {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            pointer-events: none;
        }

        .glow-point {
            position: absolute;
            width: 4px;
            height: 4px;
            background: #ffffff;
            border-radius: 50%;
            box-shadow: 0 0 8px #8ed0ff;
            animation: flash 2s infinite ease-in-out alternate;
        }

        @keyframes flash {
            0% { opacity: 0.2; transform: scale(0.8); }
            100% { opacity: 1; transform: scale(1.4); }
        }

        /* Modal/Card de Carritos Hot Wheels */
        .card-modal {
            position: absolute;
            bottom: 30px;
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid #38bdf8;
            border-radius: 16px;
            padding: 15px;
            width: 85%;
            max-width: 320px;
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
            text-align: center;
            z-index: 20;
            animation: slideUp 0.8s ease-out;
        }

        @keyframes slideUp {
            from { transform: translateY(50px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        .hotwheels-badge {
            background: #e11d48;
            color: white;
            font-weight: bold;
            font-style: italic;
            padding: 4px 12px;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 8px;
            font-size: 0.9rem;
            letter-spacing: 1px;
            box-shadow: 0 0 10px rgba(225, 29, 72, 0.6);
        }

        .card-text {
            color: #f1f5f9;
            font-size: 1.1rem;
            line-height: 1.4;
            font-weight: 500;
        }
    </style>
</head>
<body>

    <!-- Pantalla de Carga -->
    <div id="loading-screen">
        <h1 class="loading-title">Cargando tu ramo de<br>Hot Wheels...</h1>
        <div class="car-container">
            <div class="car" id="car-icon">🏎️</div>
        </div>
        <div class="percentage" id="percent-text">0%</div>
    </div>

    <!-- Contenido del Ramo -->
    <div id="main-content">
        <!-- Puntos brillantes de fondo -->
        <div class="bg-glow">
            <div class="glow-point" style="top:20%; left:15%;"></div>
            <div class="glow-point" style="top:15%; right:20%;"></div>
            <div class="glow-point" style="top:40%; left:25%;"></div>
            <div class="glow-point" style="top:35%; right:15%;"></div>
            <div class="glow-point" style="top:60%; left:10%;"></div>
        </div>

        <h1 class="title">Feliz Día de los<br>Carritos de Hot Wheels 💙</h1>

        <div class="bouquet-container">
            <svg width="300" height="350" viewBox="0 0 300 350" fill="none" xmlns="http://www.w3.org/2000/svg">
                <!-- TALLOS Y HOJAS -->
                <path d="M150 330 Q145 250 100 170" stroke="#166534" stroke-width="5" stroke-linecap="round"/>
                <path d="M150 330 Q150 250 150 150" stroke="#15803d" stroke-width="6" stroke-linecap="round"/>
                <path d="M150 330 Q155 250 200 170" stroke="#166534" stroke-width="5" stroke-linecap="round"/>
                <path d="M150 330 Q130 260 70 200" stroke="#16803d" stroke-width="4" stroke-linecap="round"/>
                <path d="M150 330 Q170 260 230 200" stroke="#16803d" stroke-width="4" stroke-linecap="round"/>

                <path d="M110 240 Q70 220 90 260 Z" fill="#15803d"/>
                <path d="M190 240 Q230 220 210 260 Z" fill="#15803d"/>

                <!-- LAZO DE CINTA -->
                <path d="M130 310 C110 300 110 330 145 320 Z" fill="#38bdf8"/>
                <path d="M170 310 C190 300 190 330 155 320 Z" fill="#38bdf8"/>
                <circle cx="150" cy="318" r="7" fill="#0284c7"/>
                <path d="M145 322 L130 345 L145 340 Z" fill="#38bdf8"/>
                <path d="M155 322 L170 345 L155 340 Z" fill="#38bdf8"/>

                <!-- FLOR CENTRO -->
                <g transform="translate(150, 140)">
                    <g fill="#38bdf8">
                        <circle cx="0" cy="-28" r="12"/><circle cx="20" cy="-20" r="12"/><circle cx="28" cy="0" r="12"/><circle cx="20" cy="20" r="12"/><circle cx="0" cy="28" r="12"/><circle cx="-20" cy="20" r="12"/><circle cx="-28" cy="0" r="12"/><circle cx="-20" cy="-20" r="12"/>
                    </g>
                    <circle cx="0" cy="0" r="14" fill="#0f172a"/>
                </g>

                <!-- FLOR IZQUIERDA -->
                <g transform="translate(90, 160)">
                    <g fill="#0284c7">
                        <circle cx="0" cy="-24" r="10"/><circle cx="17" cy="-17" r="10"/><circle cx="24" cy="0" r="10"/><circle cx="17" cy="17" r="10"/><circle cx="0" cy="24" r="10"/><circle cx="-17" cy="17" r="10"/><circle cx="-24" cy="0" r="10"/><circle cx="-17" cy="-17" r="10"/>
                    </g>
                    <circle cx="0" cy="0" r="12" fill="#0f172a"/>
                </g>

                <!-- FLOR DERECHA -->
                <g transform="translate(210, 160)">
                    <g fill="#0284c7">
                        <circle cx="0" cy="-24" r="10"/><circle cx="17" cy="-17" r="10"/><circle cx="24" cy="0" r="10"/><circle cx="17" cy="17" r="10"/><circle cx="0" cy="24" r="10"/><circle cx="-17" cy="17" r="10"/><circle cx="-24" cy="0" r="10"/><circle cx="-17" cy="-17" r="10"/>
                    </g>
                    <circle cx="0" cy="0" r="12" fill="#0f172a"/>
                </g>

                <!-- FLOR ARRIBA IZQ -->
                <g transform="translate(110, 85)">
                    <g fill="#7dd3fc">
                        <circle cx="0" cy="-22" r="9"/><circle cx="15" cy="-15" r="9"/><circle cx="22" cy="0" r="9"/><circle cx="15" cy="15" r="9"/><circle cx="0" cy="22" r="9"/><circle cx="-15" cy="15" r="9"/><circle cx="-22" cy="0" r="9"/><circle cx="-15" cy="-15" r="9"/>
                    </g>
                    <circle cx="0" cy="0" r="10" fill="#0f172a"/>
                </g>

                <!-- FLOR ARRIBA DER -->
                <g transform="translate(190, 85)">
                    <g fill="#7dd3fc">
                        <circle cx="0" cy="-22" r="9"/><circle cx="15" cy="-15" r="9"/><circle cx="22" cy="0" r="9"/><circle cx="15" cy="15" r="9"/><circle cx="0" cy="22" r="9"/><circle cx="-15" cy="15" r="9"/><circle cx="-22" cy="0" r="9"/><circle cx="-15" cy="-15" r="9"/>
                    </g>
                    <circle cx="0" cy="0" r="10" fill="#0f172a"/>
                </g>
            </svg>
        </div>

        <!-- Mensajes tipo Hot Wheels -->
        <div class="card-modal" id="card-modal">
            <div class="hotwheels-badge">HOT WHEELS</div>
            <div class="card-text" id="card-phrase">Aceleraste mi corazón desde el primer día. 🏎️💨</div>
        </div>
    </div>

    <script>
        // Animación de Carga
        const carIcon = document.getElementById('car-icon');
        const percentText = document.getElementById('percent-text');
        const loadingScreen = document.getElementById('loading-screen');
        const mainContent = document.getElementById('main-content');
        const cardPhrase = document.getElementById('card-phrase');

        const frases = [
            "Aceleraste mi corazón desde el primer día. 🏎️💖",
            "Cuanto más tiempo estoy contigo, más te amo. 💙",
            "Haces que cada día sea mejor que el anterior. ✨",
            "Eres el mejor regalo que la vida me dio. 🚗💨"
        ];

        let count = 0;
        const interval = setInterval(() => {
            count += 1;
            percentText.innerText = count + '%';
            carIcon.style.left = count + '%';

            if (count >= 100) {
                clearInterval(interval);
                setTimeout(() => {
                    loadingScreen.style.opacity = '0';
                    setTimeout(() => {
                        loadingScreen.style.display = 'none';
                        mainContent.style.display = 'flex';
                        setTimeout(() => {
                            mainContent.style.opacity = '1';
                        }, 50);
                    }, 1000);
                }, 400);
            }
        }, 35);

        // Cambiar frases periódicamente
        let phraseIndex = 0;
        setInterval(() => {
            phraseIndex = (phraseIndex + 1) % frases.length;
            if (cardPhrase) {
                cardPhrase.innerText = frases[phraseIndex];
            }
        }, 4000);
    </script>
</body>
</html>'''

class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_TEMPLATE.encode('utf-8'))

if __name__ == '__main__':
    # Lee el puerto dinámico de Render
    puerto = int(os.environ.get('PORT', 8000))
    servidor = HTTPServer(('0.0.0.0', puerto), MiServidor)
    print(f"Servidor listo en el puerto {puerto}")
    servidor.serve_forever()
