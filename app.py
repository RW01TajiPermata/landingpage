from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML Statis
template = '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karang Taruna PERMATA - Persatuan Muda Mudi Taji</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #2563eb;
            --primary-dark: #1e40af;
            --bg-light: #ffffff;
            --bg-secondary-light: #f8fafc;
            --text-light: #1e293b;
            --text-secondary-light: #64748b;
            --border-light: #e2e8f0;
        }

        [data-theme="dark"] {
            --bg-light: #0f172a;
            --bg-secondary-light: #1e293b;
            --text-light: #f1f5f9;
            --text-secondary-light: #94a3b8;
            --border-light: #334155;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg-light);
            color: var(--text-light);
            transition: background 0.3s ease, color 0.3s ease;
            line-height: 1.6;
        }

        nav {
            background: var(--bg-light);
            border-bottom: 1px solid var(--border-light);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary);
        }

        .logo-icon {
            width: 50px;
            height: 50px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
        }

        .logo-icon img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
            align-items: center;
        }

        .nav-links a {
            color: var(--text-light);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--primary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--primary);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .theme-toggle {
            background: var(--bg-secondary-light);
            border: 1px solid var(--border-light);
            border-radius: 50px;
            padding: 0.5rem 1rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
        }

        .theme-toggle:hover {
            transform: scale(1.05);
            border-color: var(--primary);
        }

        .mobile-toggle {
            display: none;
            flex-direction: column;
            gap: 4px;
            cursor: pointer;
        }

        .mobile-toggle span {
            width: 25px;
            height: 3px;
            background: var(--text-light);
            transition: all 0.3s ease;
        }

        .hero {
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
            padding: 6rem 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="2" fill="rgba(255,255,255,0.1)"/></svg>');
            animation: float 20s linear infinite;
        }

        @keyframes float {
            to { transform: translateY(-100px); }
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeInUp 0.8s ease;
        }

        .hero p {
            font-size: 1.25rem;
            margin-bottom: 2rem;
            opacity: 0.95;
            animation: fadeInUp 0.8s ease 0.2s both;
        }

        .btn {
            display: inline-block;
            padding: 0.875rem 2rem;
            background: white;
            color: var(--primary);
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
            animation: fadeInUp 0.8s ease 0.4s both;
        }

        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 4rem 2rem;
        }

        section {
            margin-bottom: 4rem;
        }

        h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--primary);
            text-align: center;
        }

        .section-subtitle {
            text-align: center;
            color: var(--text-secondary-light);
            margin-bottom: 3rem;
            font-size: 1.1rem;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .card {
            background: var(--bg-secondary-light);
            border: 1px solid var(--border-light);
            border-radius: 12px;
            padding: 2rem;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(37, 99, 235, 0.15);
            border-color: var(--primary);
        }

        .card-icon {
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.75rem;
            margin-bottom: 1.5rem;
        }

        .card h3 {
            font-size: 1.5rem;
            margin-bottom: 0.75rem;
            color: var(--text-light);
        }

        .card p {
            color: var(--text-secondary-light);
            line-height: 1.7;
        }

        .program-item {
            background: var(--bg-secondary-light);
            border-left: 4px solid var(--primary);
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .program-item:hover {
            transform: translateX(10px);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.1);
        }

        .program-item h4 {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
            color: var(--primary);
        }

        .struktur-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .struktur-card {
            background: var(--bg-secondary-light);
            border: 2px solid var(--border-light);
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .struktur-card:hover {
            border-color: var(--primary);
            transform: scale(1.05);
        }

        .struktur-avatar {
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            border-radius: 50%;
            margin: 0 auto 1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            position: relative;
        }

        .struktur-avatar img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: relative;
            z-index: 2;
        }

        .struktur-avatar-placeholder {
            font-size: 3rem;
            color: white;
            position: relative;
            z-index: 1;
        }

        .struktur-card h4 {
            font-size: 1.1rem;
            margin-bottom: 0.25rem;
            color: var(--text-light);
        }

        .struktur-card .jabatan {
            color: var(--primary);
            font-weight: 600;
            font-size: 0.9rem;
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .gallery-item {
            height: 250px;
            background: var(--bg-secondary-light);
            border-radius: 12px;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 1px solid var(--border-light);
        }

        .gallery-item:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 16px rgba(37, 99, 235, 0.2);
            border-color: var(--primary);
        }

        .gallery-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.3s ease;
        }

        .gallery-item:hover img {
            transform: scale(1.05);
        }

        .gallery-item video {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }

        .gallery-placeholder {
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            color: white;
        }

        .gallery-caption {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(transparent, rgba(0,0,0,0.8));
            color: white;
            padding: 1rem;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }

        .gallery-item:hover .gallery-caption {
            transform: translateY(0);
        }

        footer {
            background: var(--bg-secondary-light);
            border-top: 1px solid var(--border-light);
            padding: 3rem 2rem 1.5rem;
            margin-top: 4rem;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .footer-section h3 {
            color: var(--primary);
            margin-bottom: 1rem;
        }

        .footer-section ul {
            list-style: none;
        }

        .footer-section ul li {
            margin-bottom: 0.5rem;
        }

        .footer-section a {
            color: var(--text-secondary-light);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        .footer-section a:hover {
            color: var(--primary);
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border-light);
            color: var(--text-secondary-light);
        }

        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 70px;
                left: -100%;
                flex-direction: column;
                background: var(--bg-light);
                width: 100%;
                padding: 2rem;
                border-bottom: 1px solid var(--border-light);
                transition: left 0.3s ease;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            }

            .nav-links.active {
                left: 0;
            }

            .mobile-toggle {
                display: flex;
            }

            .hero h1 {
                font-size: 2rem;
            }

            .hero p {
                font-size: 1rem;
            }

            h2 {
                font-size: 1.75rem;
            }

            .cards-grid {
                grid-template-columns: 1fr;
            }
        }

        .scroll-animate {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease;
        }

        .scroll-animate.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <nav>
        <div class="nav-container">
            <div class="logo">
                <div class="logo-icon">
                    <img src="{{ url_for('static', filename='images/logo-permata.png') }}" alt="Logo PERMATA">
                </div>
                <span>PERMATA</span>
            </div>
            <ul class="nav-links" id="navLinks">
                <li><a href="#beranda">Beranda</a></li>
                <li><a href="#tentang">Tentang</a></li>
                <li><a href="#program">Program</a></li>
                <li><a href="#struktur">Struktur</a></li>
                <li><a href="#galeri">Galeri</a></li>
                <li><a href="#kontak">Kontak</a></li>
            </ul>
            <div style="display: flex; gap: 1rem; align-items: center;">
                <button class="theme-toggle" id="themeToggle">
                    <span id="themeIcon">🌙</span>
                </button>
                <div class="mobile-toggle" id="mobileToggle">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            </div>
        </div>
    </nav>

    <section class="hero" id="beranda">
        <div class="hero-content">
            <h1>PERMATA</h1>
            <p>Persatuan Muda Mudi Taji - Membangun Generasi Berprestasi, Berkarya untuk Negeri</p>
            <a href="#tentang" class="btn">Selengkapnya</a>
        </div>
    </section>

    <div class="container">
        <section id="tentang" class="scroll-animate">
            <h2>Tentang Kami</h2>
            <p class="section-subtitle">Organisasi kepemudaan yang berdedikasi untuk pemberdayaan generasi muda</p>
            
            <div class="cards-grid">
                <div class="card">
                    <div class="card-icon">🎯</div>
                    <h3>Visi</h3>
                    <p>Menjadi organisasi kepemudaan yang unggul dalam mengembangkan potensi generasi muda di Taji, berakhlak mulia, dan berkontribusi aktif dalam pembangunan masyarakat.</p>
                </div>
                <div class="card">
                    <div class="card-icon">🚀</div>
                    <h3>Misi</h3>
                    <p>Memberdayakan pemuda melalui pelatihan, kegiatan sosial, dan program pengembangan diri yang berkelanjutan untuk menciptakan generasi yang mandiri dan produktif.</p>
                </div>
                <div class="card">
                    <div class="card-icon">💎</div>
                    <h3>Nilai</h3>
                    <p>Integritas, Kreativitas, Gotong Royong, Profesionalisme, dan Dedikasi untuk kemajuan bersama dalam membangun masyarakat yang lebih baik.</p>
                </div>
            </div>
        </section>

        <section id="program" class="scroll-animate">
            <h2>Program Kerja</h2>
            <p class="section-subtitle">Berbagai program unggulan untuk pemberdayaan pemuda</p>
            
            <div class="program-item">
                <h4>🏀 Olahraga & Kesehatan</h4>
                <p>Turnamen futsal, voli, badminton, senam sehat, dan kegiatan olahraga rutin setiap minggu untuk menjaga kesehatan dan kebugaran anggota.</p>
            </div>
            <div class="program-item">
                <h4>📚 Pendidikan & Pelatihan</h4>
                <p>Bimbingan belajar gratis, workshop keterampilan, pelatihan leadership, public speaking, dan program beasiswa untuk pelajar berprestasi.</p>
            </div>
            <div class="program-item">
                <h4>🎨 Seni & Budaya</h4>
                <p>Pementasan seni budaya, pelatihan musik, tari tradisional, teater, dan pelestarian budaya lokal Taji yang kaya akan nilai sejarah.</p>
            </div>
            <div class="program-item">
                <h4>🤝 Sosial & Lingkungan</h4>
                <p>Bakti sosial, donor darah, bersih desa, penanaman pohon, bank sampah, dan program peduli lingkungan untuk masyarakat berkelanjutan.</p>
            </div>
            <div class="program-item">
                <h4>💼 Kewirausahaan</h4>
                <p>Pelatihan bisnis, inkubator UMKM pemuda, bazar produk lokal, dan pendampingan usaha untuk meningkatkan ekonomi kreatif.</p>
            </div>
        </section>

        <section id="struktur" class="scroll-animate">
            <h2>Struktur Organisasi</h2>
            <p class="section-subtitle">Pengurus Karang Taruna PERMATA Periode 2025-2030</p>
            
            <div class="struktur-grid">
                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <img src="{{ url_for('static', filename='images/profil_ketua.jpg') }}" alt="Aditya Yuda Pratama">
                        <span class="struktur-avatar-placeholder" style="display: none;">👨‍💼</span>
                    </div>
                    <h4>ADITYA YUDA PRATAMA</h4>
                    <p class="jabatan">Ketua Umum</p>
                </div>

                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <span class="struktur-avatar-placeholder">👨‍💼</span>
                    </div>
                    <h4>RIFKY BALYA SYAIFULLAH</h4>
                    <p class="jabatan">Wakil Ketua</p>
                </div>

                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <span class="struktur-avatar-placeholder">👩‍💼</span>
                    </div>
                    <h4>INTAN SUSILO TRI HANDAYANI</h4>
                    <p class="jabatan">Bendahara 1</p>
                </div>

                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <span class="struktur-avatar-placeholder">👨‍💼</span>
                    </div>
                    <h4>RIJAL HARITS BAKHTIYAR</h4>
                    <p class="jabatan">Bendahara 2</p>
                </div>

                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <span class="struktur-avatar-placeholder">👩‍💼</span>
                    </div>
                    <h4>BELLA NUR UTAMI</h4>
                    <p class="jabatan">Sekretaris 1</p>
                </div>

                <div class="struktur-card">
                    <div class="struktur-avatar">
                        <span class="struktur-avatar-placeholder">👨‍💼</span>
                    </div>
                    <h4>DHESTA KURNIA A</h4>
                    <p class="jabatan">Sekretaris 2</p>
                </div>
            </div>
        </section>

        <section id="galeri" class="scroll-animate">
            <h2>Galeri Kegiatan</h2>
            <p class="section-subtitle">Dokumentasi kegiatan dan program Karang Taruna PERMATA</p>
            
            <div class="gallery">
                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan1.JPG') }}" alt="Kegiatan 1">
                    <div class="gallery-placeholder" style="display: none;">🏆</div>
                    <div class="gallery-caption">Kegiatan 1 - Malam Pentas Seni</div>
                </div>

                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan2.JPG') }}" alt="Kegiatan 2">
                    <div class="gallery-placeholder" style="display: none;">🎭</div>
                    <div class="gallery-caption">Kegiatan 2 - Jalan Sehat RW 01 Taji</div>
                </div>

                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan3.JPG') }}" alt="Kegiatan 3">
                    <div class="gallery-placeholder" style="display: none;">🌳</div>
                    <div class="gallery-caption">Kegiatan 3 - Lomba Voli antar RT</div>
                </div>

                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan4.jpg') }}" alt="Kegiatan 4">
                    <div class="gallery-placeholder" style="display: none;">📖</div>
                    <div class="gallery-caption">Kegiatan 4</div>
                </div>

                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan5.jpg') }}" alt="Kegiatan 5">
                    <div class="gallery-placeholder" style="display: none;">🤝</div>
                    <div class="gallery-caption">Kegiatan 5</div>
                </div>

                <div class="gallery-item">
                    <img src="{{ url_for('static', filename='images/kegiatan6.jpg') }}" alt="Kegiatan 6">
                    <div class="gallery-placeholder" style="display: none;">🎨</div>
                    <div class="gallery-caption">Kegiatan 6</div>
                </div>
            </div>
        </section>

        <section id="kontak" class="scroll-animate">
            <h2>Hubungi Kami</h2>
            <p class="section-subtitle">Bergabunglah bersama kami dalam membangun generasi muda yang lebih baik</p>
            
            <div class="cards-grid">
                <div class="card">
                    <div class="card-icon">📍</div>
                    <h3>Alamat</h3>
                    <p>Jl. Raya Jogja Solo<br>Taji, Prambanan<br>Kabupaten Klaten, Jawa Tengah</p>
                </div>
                <div class="card">
                    <div class="card-icon">📱</div>
                    <h3>Kontak</h3>
                    <p>WhatsApp: 0895422608609(Yuda)<br>Email: permata@gmail.com<br>Instagram: @permata_taji</p>
                </div>
                <div class="card">
                    <div class="card-icon">⏰</div>
                    <h3>Jam Operasional</h3>
                    <p>Kegiatan Sesuai intruksi ketua</p>
                </div>
            </div>
        </section>
    </div>

    <footer>
        <div class="footer-content">
            <div class="footer-section">
                <h3>PERMATA</h3>
                <p>Persatuan Muda Mudi Taji - Organisasi kepemudaan yang berkomitmen membangun generasi muda berprestasi dan berakhlak mulia.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <ul>
                    <li><a href="#beranda">Beranda</a></li>
                    <li><a href="#tentang">Tentang Kami</a></li>
                    <li><a href="#program">Program Kerja</a></li>
                    <li><a href="#struktur">Struktur Organisasi</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h3>Media Sosial</h3>
                <ul>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">Instagram</a></li>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">YouTube</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 Karang Taruna PERMATA. All rights reserved.</p>
        </div>
    </footer>

    <script>
        const themeToggle = document.getElementById('themeToggle');
        const themeIcon = document.getElementById('themeIcon');
        const html = document.documentElement;

        const savedTheme = localStorage.getItem('theme') || 'light';
        html.setAttribute('data-theme', savedTheme);
        themeIcon.textContent = savedTheme === 'dark' ? '☀️' : '🌙';

        themeToggle.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
        });

        const mobileToggle = document.getElementById('mobileToggle');
        const navLinks = document.getElementById('navLinks');

        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });

        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.scroll-animate').forEach(el => {
            observer.observe(el);
        });

        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('img').forEach(img => {
                img.addEventListener('error', function() {
                    const placeholder = this.parentElement.querySelector('.gallery-placeholder, .struktur-avatar-placeholder');
                    if (placeholder) {
                        placeholder.style.display = 'flex';
                        this.style.display = 'none';
                    }
                });
                if (img.complete && img.naturalWidth === 0) {
                    img.dispatchEvent(new Event('error'));
                }
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(template)

app = app






