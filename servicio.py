<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Feliz Día de los Carritos de Hot Wheels ❤️🏎️</title>
  
  <!-- Fonts & FontAwesome Icons -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Great+Vibes&family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    :root {
      --hw-red: #e51937;
      --hw-orange: #ff5500;
      --hw-yellow: #ffcc00;
      --hw-blue: #0033aa;
      --night-bg: #030712;
    }

    * {
      box-sizing: border-box;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }

    body {
      margin: 0;
      padding: 0;
      font-family: 'Poppins', sans-serif;
      background-color: var(--night-bg);
      color: #ffffff;
      min-height: 100vh;
      overflow-x: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      position: relative;
    }

    /* Floating Stars & Hearts Canvas */
    #bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 0;
      pointer-events: none;
    }

    /* Screen Wrappers */
    .screen-wrapper {
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 500px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      transition: opacity 0.8s ease-in-out, transform 0.8s ease-in-out;
    }

    .hidden-screen {
      opacity: 0;
      pointer-events: none;
      position: absolute;
      transform: scale(0.95);
    }

    /* Loader Styling */
    .loader-box {
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 24px;
      padding: 30px 20px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(229, 25, 55, 0.2);
      width: 100%;
      text-align: center;
    }

    .progress-track {
      width: 100%;
      height: 16px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      position: relative;
      margin: 35px 0 15px 0;
      box-shadow: inset 0 2px 5px rgba(0,0,0,0.5);
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #ff0055, #ffaa00, #00d2ff);
      border-radius: 20px;
      transition: width 0.1s linear;
      box-shadow: 0 0 15px rgba(255, 0, 85, 0.8);
    }

    .car-runner {
      position: absolute;
      top: -26px;
      left: 0%;
      transform: translateX(-50%);
      font-size: 28px;
      filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.5));
      transition: left 0.1s linear;
    }

    /* Glowing Titles */
    .romantic-title {
      font-family: 'Great Vibes', cursive;
      color: #ff99dd;
      text-shadow: 0 0 10px rgba(255, 153, 221, 0.8), 0 0 20px rgba(255, 0, 100, 0.5);
    }

    .hw-title {
      font-family: 'Fredoka', sans-serif;
      font-weight: 700;
      background: linear-gradient(180deg, #fff 0%, #ffe600 40%, #ff0000 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(2px 4px 8px rgba(0, 0, 0, 0.8));
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* Blue Flowers Bouquet */
    .bouquet-wrapper {
      position: relative;
      width: 320px;
      height: 300px;
      margin: 10px 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .stems {
      position: absolute;
      bottom: 20px;
      width: 140px;
      height: 160px;
    }

    .stem {
      position: absolute;
      bottom: 0;
      width: 6px;
      height: 140px;
      background: linear-gradient(to top, #15803d, #4ade80);
      border-radius: 4px;
      box-shadow: 0 0 10px rgba(74, 222, 128, 0.4);
    }

    .stem:nth-child(1) { left: 40%; transform: rotate(-12deg); height: 150px; }
    .stem:nth-child(2) { left: 50%; transform: rotate(0deg); height: 160px; }
    .stem:nth-child(3) { left: 60%; transform: rotate(12deg); height: 150px; }
    .stem:nth-child(4) { left: 30%; transform: rotate(-25deg); height: 130px; }
    .stem:nth-child(5) { left: 70%; transform: rotate(25deg); height: 130px; }

    .ribbon {
      position: absolute;
      bottom: 35px;
      left: 50%;
      transform: translateX(-50%);
      color: #38bdf8;
      font-size: 32px;
      filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.8));
      z-index: 5;
    }

    .flower {
      position: absolute;
      width: 70px;
      height: 70px;
      display: flex;
      justify-content: center;
      align-items: center;
      animation: pulseFlower 3s infinite ease-in-out alternate;
    }

    @keyframes pulseFlower {
      0% { transform: scale(0.95); filter: drop-shadow(0 0 8px rgba(56, 189, 248, 0.6)); }
      100% { transform: scale(1.05); filter: drop-shadow(0 0 18px rgba(56, 189, 248, 1)); }
    }

    /* Blue Flower Petals Layout */
    .flower-center {
      width: 20px;
      height: 20px;
      background: radial-gradient(circle, #fef08a, #ca8a04);
      border-radius: 50%;
      z-index: 2;
      box-shadow: 0 0 10px #fef08a;
    }

    .petal {
      position: absolute;
      width: 26px;
      height: 36px;
      background: linear-gradient(to top, #0284c7, #38bdf8, #bae6fd);
      border-radius: 50% 50% 50% 50% / 80% 80% 20% 20%;
      transform-origin: bottom center;
    }

    .p1 { transform: rotate(0deg) translateY(-14px); }
    .p2 { transform: rotate(60deg) translateY(-14px); }
    .p3 { transform: rotate(120deg) translateY(-14px); }
    .p4 { transform: rotate(180deg) translateY(-14px); }
    .p5 { transform: rotate(240deg) translateY(-14px); }
    .p6 { transform: rotate(300deg) translateY(-14px); }

    .f-pos-1 { top: 30px; left: 125px; }
    .f-pos-2 { top: 60px; left: 60px; }
    .f-pos-3 { top: 60px; right: 60px; }
    .f-pos-4 { top: 120px; left: 90px; }
    .f-pos-5 { top: 120px; right: 90px; }

    /* Hot Wheels Collector Cards Carousel */
    .card-perspective {
      perspective: 1000px;
      width: 290px;
      height: 420px;
      margin: 10px 0;
    }

    .hw-blister-card {
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      cursor: pointer;
    }

    .hw-blister-card.flipped {
      transform: rotateY(180deg);
    }

    .card-face {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.8), 0 0 20px rgba(229, 25, 55, 0.4);
    }

    /* Front of Card (Hot Wheels Packaging) */
    .card-front-face {
      background: linear-gradient(145deg, #cc001b, #990013);
      border: 6px solid #ffffff;
      display: flex;
      flex-direction: column;
      padding: 12px;
      position: relative;
    }

    .card-header-logo {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #000;
      padding: 6px 12px;
      border-radius: 12px;
      border: 2px solid #ffcc00;
    }

    .hw-logo-badge {
      font-family: 'Fredoka', sans-serif;
      font-weight: 800;
      font-size: 20px;
      font-style: italic;
      color: #ffcc00;
      text-shadow: 2px 2px 0px #e51937, -1px -1px 0 #000;
      letter-spacing: -1px;
    }

    .car-number-badge {
      font-size: 11px;
      font-weight: 700;
      color: #fff;
      background: var(--hw-red);
      padding: 2px 6px;
      border-radius: 6px;
    }

    .blister-bubble {
      background: linear-gradient(135deg, rgba(255,255,255,0.4) 0%, rgba(255,255,255,0.05) 50%, rgba(0,0,0,0.3) 100%);
      border: 3px solid rgba(255, 255, 255, 0.7);
      border-radius: 16px;
      margin: 12px 0;
      height: 220px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      position: relative;
      box-shadow: inset 0 0 15px rgba(0,0,0,0.5), 0 8px 15px rgba(0,0,0,0.4);
      overflow: hidden;
    }

    .car-illustration {
      width: 90%;
      height: auto;
      max-height: 140px;
      object-fit: contain;
      filter: drop-shadow(0 10px 8px rgba(0,0,0,0.7));
      transition: transform 0.3s;
    }

    .hw-blister-card:hover .car-illustration {
      transform: scale(1.06) rotate(-2deg);
    }

    .car-name-tag {
      font-family: 'Fredoka', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #ffffff;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
      margin-top: 6px;
      text-align: center;
    }

    .tap-hint {
      font-size: 12px;
      color: #ffe600;
      text-align: center;
      animation: bounce 1.5s infinite;
      font-weight: 600;
    }

    /* Back of Card (Romantic Letter) */
    .card-back-face {
      background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
      border: 4px solid #f43f5e;
      transform: rotateY(180deg);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 25px;
      text-align: center;
      box-shadow: inset 0 0 30px rgba(244, 63, 94, 0.3);
    }

    .romantic-quote {
      font-size: 20px;
      line-height: 1.6;
      font-weight: 600;
      color: #fecdd3;
      text-shadow: 0 2px 10px rgba(244, 63, 94, 0.5);
      margin-bottom: 20px;
    }

    /* Shooting car keyframes across screen */
    @keyframes shootCar {
      0% { transform: translateX(-150px) rotate(-5deg); opacity: 0; }
      20% { opacity: 1; }
      80% { opacity: 1; }
      100% { transform: translateX(calc(100vw + 150px)) rotate(5deg); opacity: 0; }
    }

    .shooting-car {
      position: fixed;
      z-index: 2;
      font-size: 32px;
      pointer-events: none;
      filter: drop-shadow(0 0 12px rgba(255, 204, 0, 0.8));
    }
  </style>
</head>
<body>

  <!-- BACKGROUND CANVAS FOR STARS & NEON PARTICLES -->
  <canvas id="bg-canvas"></canvas>

  <div id="loader-screen" class="screen-wrapper">
    <div class="loader-box">
      <div class="romantic-title text-4xl mb-1">Te amo a mil por hora</div>
      <h2 class="text-xl font-bold text-gray-200 tracking-wide mb-2">Cargando tu ramo de Hot Wheels...</h2>
      
      <div class="progress-track">
        <div id="car-runner" class="car-runner">🏎️</div>
        <div id="progress-fill" class="progress-fill"></div>
      </div>
      
      <div id="progress-text" class="text-2xl font-black text-yellow-400 mt-2 font-mono">0%</div>
      <p class="text-xs text-gray-400 mt-3 animate-pulse">Preparando una sorpresa especial para ti ❤️</p>
    </div>
  </div>

  <div id="main-screen" class="screen-wrapper hidden-screen">
    
    <!-- Title -->
    <div class="text-center mb-2">
      <p class="romantic-title text-3xl">Para la persona más especial</p>
      <h1 class="hw-title text-2xl sm:text-3xl">Feliz Día de los Carritos de Hot Wheels</h1>
    </div>

    <!-- Blue Flower Bouquet -->
    <div class="bouquet-wrapper">
      <div class="stems">
        <div class="stem"></div>
        <div class="stem"></div>
        <div class="stem"></div>
        <div class="stem"></div>
        <div class="stem"></div>
      </div>
      <i class="fa-solid fa-ribbon ribbon"></i>

      <!-- 5 Blue Flowers -->
      <div class="flower f-pos-1">
        <div class="flower-center"></div>
        <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
        <div class="petal p4"></div><div class="petal p5"></div><div class="petal p6"></div>
      </div>
      <div class="flower f-pos-2">
        <div class="flower-center"></div>
        <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
        <div class="petal p4"></div><div class="petal p5"></div><div class="petal p6"></div>
      </div>
      <div class="flower f-pos-3">
        <div class="flower-center"></div>
        <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
        <div class="petal p4"></div><div class="petal p5"></div><div class="petal p6"></div>
      </div>
      <div class="flower f-pos-4">
        <div class="flower-center"></div>
        <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
        <div class="petal p4"></div><div class="petal p5"></div><div class="petal p6"></div>
      </div>
      <div class="flower f-pos-5">
        <div class="flower-center"></div>
        <div class="petal p1"></div><div class="petal p2"></div><div class="petal p3"></div>
        <div class="petal p4"></div><div class="petal p5"></div><div class="petal p6"></div>
      </div>
    </div>

    <!-- Hot Wheels Flip Card Container -->
    <div class="card-perspective">
      <div id="hw-card" class="hw-blister-card">
        
        <!-- Front of Blister Pack -->
        <div class="card-face card-front-face">
          <div class="card-header-logo">
            <span class="hw-logo-badge">🔥 Hot Wheels</span>
            <span id="card-counter" class="car-number-badge">1 / 4</span>
          </div>

          <div class="blister-bubble">
            <img id="car-image" class="car-illustration" src="" alt="Hot Wheels Car" />
            <div id="car-name" class="car-name-tag">Nissan Skyline GT-R</div>
          </div>

          <div class="tap-hint">
            <i class="fa-solid fa-hand-pointer mr-1"></i> ¡Toca la tarjeta para ver mi mensaje!
          </div>
        </div>

        <!-- Back of Blister Pack (Romantic Quote) -->
        <div class="card-face card-back-face">
          <i class="fa-solid fa-heart text-4xl text-rose-500 mb-4 animate-bounce"></i>
          <p id="romantic-quote" class="romantic-quote">"Haces que cada día sea mejor que el anterior."</p>
          <p class="text-xs text-rose-300 font-semibold">(Toca de nuevo para cambiar de carrito 🏎️)</p>
        </div>

      </div>
    </div>

    <!-- Navigation Dots for Cards -->
    <div class="flex items-center gap-2 mt-2">
      <button id="prev-btn" class="w-10 h-10 rounded-full bg-rose-600 hover:bg-rose-500 flex items-center justify-center font-bold text-white shadow-lg active:scale-95 transition">
        <i class="fa-solid fa-chevron-left"></i>
      </button>
      <div id="dots-container" class="flex gap-2 mx-2"></div>
      <button id="next-btn" class="w-10 h-10 rounded-full bg-rose-600 hover:bg-rose-500 flex items-center justify-center font-bold text-white shadow-lg active:scale-95 transition">
        <i class="fa-solid fa-chevron-right"></i>
      </button>
    </div>

  </div>

  <script>
    // Hot Wheels Collectibles Data
    const hotWheelsCollection = [
      {
        name: "Nissan Skyline GT-R R34",
        image: "https://images.unsplash.com/photo-1617814076367-b759c7d7e738?w=600&auto=format&fit=crop&q=80",
        message: "Haces que cada día sea mejor que el anterior. ❤️"
      },
      {
        name: "Datsun Bluebird 510",
        image: "https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=600&auto=format&fit=crop&q=80",
        message: "Cuanto más tiempo estoy contigo, más te amo. 🏎️✨"
      },
      {
        name: "Honda CBR Motorbike 2025",
        image: "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=600&auto=format&fit=crop&q=80",
        message: "Aceleraste mi corazón desde el primer día. 🔥"
      },
      {
        name: "Custom 'Te Amo' Super Classic",
        image: "https://images.unsplash.com/photo-1541348263662-e082662d82da?w=600&auto=format&fit=crop&q=80",
        message: "Eres mi refugio seguro y mi lugar favorito en el mundo. 🌹"
      }
    ];

    let currentIndex = 0;

    // Canvas Background Starfield Animation
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    let particles = [];

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Particle {
      constructor() {
        this.reset();
      }

      reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = Math.random() * 2.5 + 0.5;
        this.speedY = -(Math.random() * 0.5 + 0.2);
        this.alpha = Math.random() * 0.8 + 0.2;
        this.isHeart = Math.random() > 0.85;
      }

      update() {
        this.y += this.speedY;
        if (this.y < 0) {
          this.y = canvas.height;
          this.x = Math.random() * canvas.width;
        }
      }

      draw() {
        ctx.fillStyle = this.isHeart ? `rgba(244, 63, 94, ${this.alpha})` : `rgba(255, 255, 255, ${this.alpha})`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    for (let i = 0; i < 90; i++) {
      particles.push(new Particle());
    }

    function animateCanvas() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      particles.forEach(p => {
        p.update();
        p.draw();
      });
      requestAnimationFrame(animateCanvas);
    }
    animateCanvas();

    // Progress Bar Animation Logic
    let progress = 0;
    const carRunner = document.getElementById('car-runner');
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    const loaderScreen = document.getElementById('loader-screen');
    const mainScreen = document.getElementById('main-screen');

    const progressInterval = setInterval(() => {
      progress += 1;
      progressFill.style.width = `${progress}%`;
      carRunner.style.left = `${progress}%`;
      progressText.innerText = `${progress}%`;

      if (progress >= 100) {
        clearInterval(progressInterval);
        setTimeout(() => {
          loaderScreen.classList.add('hidden-screen');
          mainScreen.classList.remove('hidden-screen');
          triggerShootingCars();
        }, 400);
      }
    }, 35);

    // Hot Wheels Card Logic
    const hwCard = document.getElementById('hw-card');
    const carImage = document.getElementById('car-image');
    const carName = document.getElementById('car-name');
    const romanticQuote = document.getElementById('romantic-quote');
    const cardCounter = document.getElementById('card-counter');
    const dotsContainer = document.getElementById('dots-container');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    function updateCardData(index) {
      const item = hotWheelsCollection[index];
      carImage.src = item.image;
      carName.innerText = item.name;
      romanticQuote.innerText = `"${item.message}"`;
      cardCounter.innerText = `${index + 1} / ${hotWheelsCollection.length}`;
      updateDots();
    }

    function createDots() {
      dotsContainer.innerHTML = '';
      hotWheelsCollection.forEach((_, idx) => {
        const dot = document.createElement('div');
        dot.className = `w-3 h-3 rounded-full transition-all duration-300 ${idx === currentIndex ? 'bg-yellow-400 w-6' : 'bg-gray-600'}`;
        dotsContainer.appendChild(dot);
      });
    }

    function updateDots() {
      Array.from(dotsContainer.children).forEach((dot, idx) => {
        dot.className = `w-3 h-3 rounded-full transition-all duration-300 ${idx === currentIndex ? 'bg-yellow-400 w-6' : 'bg-gray-600'}`;
      });
    }

    hwCard.addEventListener('click', () => {
      hwCard.classList.toggle('flipped');
    });

    prevBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      hwCard.classList.remove('flipped');
      setTimeout(() => {
        currentIndex = (currentIndex - 1 + hotWheelsCollection.length) % hotWheelsCollection.length;
        updateCardData(currentIndex);
      }, 200);
    });

    nextBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      hwCard.classList.remove('flipped');
      setTimeout(() => {
        currentIndex = (currentIndex + 1) % hotWheelsCollection.length;
        updateCardData(currentIndex);
      }, 200);
    });

    // Shooting Cars Background Effect
    function triggerShootingCars() {
      setInterval(() => {
        const car = document.createElement('div');
        car.className = 'shooting-car';
        car.innerText = ['🏎️', '🚗', '🏎️💨'][Math.floor(Math.random() * 3)];
        car.style.top = `${Math.random() * 70 + 10}vh`;
        car.style.animation = `shootCar ${Math.random() * 2 + 3}s linear forwards`;
        document.body.appendChild(car);

        setTimeout(() => car.remove(), 5000);
      }, 3500);
    }

    // Initialize Card Data
    createDots();
    updateCardData(currentIndex);
  </script>
</body>
</html>
