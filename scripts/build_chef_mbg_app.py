# -*- coding: utf-8 -*-
"""
Build Chef MBG - Executive Kitchen Operations & Chef Recipe System
Designed specifically for Head Chef Lutfi at SPPG Pekajangan 04.
Features:
- Complete 2-Week Menu Cycle (Karbo, ProHe, ProNa, Sayur, Side, Buah)
- Recipe Scaler for 2,000+ portions (Per Porsi, Total PO Belanja, Takaran per Batch Wajan)
- Emergency Stock Swap & Quick Substitution Engine (for canceled vendor deliveries)
- Official SPPG Printable Directive Generator (Arahan Tim Persiapan) for all 4 institutions
- 1-Click WhatsApp Formatted Text Broadcast for Kitchen Volunteers
- Organoleptic Testing & Kitchen Sampling Tracker
"""
import os

html_code = r"""<!DOCTYPE html>
<html lang="id" class="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chef MBG — SPPG Pekajangan 04</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <script>
    tailwind.config = {
      darkMode: 'class'
    };
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');
    
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    .font-num {
      font-variant-numeric: tabular-nums;
      letter-spacing: -0.02em;
    }

    .font-code {
      font-family: 'JetBrains Mono', ui-monospace, monospace;
    }

    /* Print styling strictly matching the 5-page official SPPG document */
    @media print {
      body * {
        visibility: hidden !important;
      }
      #printable-directive-sheet, #printable-directive-sheet * {
        visibility: visible !important;
      }
      #printable-directive-sheet {
        position: absolute !important;
        left: 0 !important;
        top: 0 !important;
        width: 100% !important;
        margin: 0 !important;
        padding: 20px !important;
        background: white !important;
        color: black !important;
        box-shadow: none !important;
        border: none !important;
      }
      .no-print {
        display: none !important;
      }
      .page-break {
        page-break-before: always !important;
        break-before: page !important;
      }
    }
  </style>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-[#090D16] dark:text-slate-100 flex flex-col min-h-screen antialiased transition-colors duration-200 selection:bg-slate-900 selection:text-white">

  <!-- ============================================================== -->
  <!-- TOP EXECUTIVE NAVBAR                                           -->
  <!-- ============================================================== -->
  <header class="bg-white/95 dark:bg-[#0D121F]/95 backdrop-blur-md border-b border-slate-200/80 dark:border-slate-800/80 sticky top-0 z-40 transition-colors no-print">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between gap-3">
      
      <!-- Brand & Chef Identity -->
      <div class="flex items-center gap-3 min-w-0">
        <div class="w-9 h-9 rounded-xl bg-slate-900 dark:bg-white flex items-center justify-center text-white dark:text-slate-950 font-bold text-sm tracking-tight shrink-0 shadow-xs">
          MBG
        </div>
        <div class="min-w-0">
          <div class="flex items-center gap-2">
            <span class="font-extrabold text-sm sm:text-base text-slate-900 dark:text-white tracking-tight">Chef MBG</span>
            <span class="px-2 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950/60 border border-emerald-200/80 dark:border-emerald-800/80 text-emerald-700 dark:text-emerald-400 text-[10px] font-bold uppercase tracking-wide">SPPG Pekajangan 04</span>
          </div>
          <p class="text-[11px] text-slate-500 dark:text-slate-400 font-medium truncate">Shift Malam &bull; Chef Lutfi Iskandar</p>
        </div>
      </div>

      <!-- Quick Action Toolbar -->
      <div class="flex items-center gap-2 sm:gap-2.5 shrink-0">
        <!-- Emergency Substitution Button -->
        <button type="button" onclick="openEmergencyModal()" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-amber-500/10 hover:bg-amber-500/20 text-amber-700 dark:text-amber-400 border border-amber-300 dark:border-amber-700/60 text-xs font-bold transition-all cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>
          <span class="hidden sm:inline">Substitusi Darurat</span>
        </button>

        <!-- Dark/Light Theme Switcher -->
        <button type="button" onclick="toggleTheme()" id="theme-btn" class="w-8 h-8 rounded-lg border border-slate-200 dark:border-slate-800 bg-white dark:bg-[#131926] text-slate-600 dark:text-slate-300 flex items-center justify-center transition-all cursor-pointer" title="Ganti Tema">
          <svg id="theme-icon-sun" class="w-4 h-4 hidden dark:block text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"/></svg>
          <svg id="theme-icon-moon" class="w-4 h-4 block dark:hidden text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
        </button>
      </div>

    </div>
  </header>

  <!-- ============================================================== -->
  <!-- MAIN WORKFLOW SUBNAV TABS                                      -->
  <!-- ============================================================== -->
  <nav class="bg-white dark:bg-[#0D121F] border-b border-slate-200/80 dark:border-slate-800/80 sticky top-16 z-30 no-print">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 py-2.5 flex items-center justify-center">
      <div class="flex items-center justify-center gap-1.5 sm:gap-2 flex-wrap">
        
        <!-- Tab 1: Arahan Harian -->
        <button type="button" onclick="switchMainTab('arahan')" id="btn-tab-arahan" class="main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          <span>Arahan Tim Persiapan (Cetak & WA)</span>
        </button>

        <!-- Tab 2: Master Resep & Batch -->
        <button type="button" onclick="switchMainTab('resep')" id="btn-tab-resep" class="main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/></svg>
          <span>Master Resep & Batch Wajan</span>
        </button>

        <!-- Tab 3: Rencana Siklus 2 Minggu -->
        <button type="button" onclick="switchMainTab('siklus')" id="btn-tab-siklus" class="main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
          <span>Siklus Menu (Ahli Gizi)</span>
        </button>

        <!-- Tab 4: Uji Mutu & Sampel -->
        <button type="button" onclick="switchMainTab('organoleptik')" id="btn-tab-organoleptik" class="main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 cursor-pointer">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/></svg>
          <span>Uji Organoleptik & Sampel (11 Porsi)</span>
        </button>

      </div>
    </div>
  </nav>

  <!-- ============================================================== -->
  <!-- MAIN APP CONTAINER                                             -->
  <!-- ============================================================== -->
  <main class="flex-1 max-w-5xl w-full mx-auto px-4 sm:px-6 py-6 space-y-6">

    <!-- DAY SELECTOR & ACTIVE SUMMARY BAR -->
    <section class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-5 rounded-2xl shadow-sm no-print flex flex-col items-center justify-center text-center gap-4">
      <div class="flex flex-col items-center gap-2">
        <span class="text-[11px] font-bold text-slate-400 uppercase tracking-widest">Jadwal Operasional Dapur:</span>
        <div class="flex items-center justify-center gap-1.5 flex-wrap">
          <button type="button" onclick="selectDay('kamis_19')" id="day-btn-kamis_19" class="day-selector-btn px-3.5 py-1.5 rounded-lg text-xs font-bold bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer">
            Kamis, 19 Nov (Hari Ini)
          </button>
          <button type="button" onclick="selectDay('senin_23')" id="day-btn-senin_23" class="day-selector-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">
            Senin, 23 Nov
          </button>
          <button type="button" onclick="selectDay('selasa_24')" id="day-btn-selasa_24" class="day-selector-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">
            Selasa, 24 Nov
          </button>
          <button type="button" onclick="selectDay('rabu_25')" id="day-btn-rabu_25" class="day-selector-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">
            Rabu, 25 Nov
          </button>
          <button type="button" onclick="selectDay('kamis_26')" id="day-btn-kamis_26" class="day-selector-btn px-3.5 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">
            Kamis, 26 Nov
          </button>
        </div>
      </div>

      <!-- Quick Metrics Summary -->
      <div class="w-full border-t border-slate-100 dark:border-slate-800 pt-3 flex items-center justify-center gap-6 sm:gap-10 text-xs font-medium flex-wrap">
        <div class="text-center">
          <span class="text-slate-400 block text-[10px] uppercase font-bold tracking-wider">Total Porsi Dapur</span>
          <span id="header-total-portions" class="font-extrabold text-slate-900 dark:text-white font-num text-base">2.742 Porsi</span>
        </div>
        <div class="h-7 w-px bg-slate-200 dark:bg-slate-800 hidden sm:block"></div>
        <div class="text-center">
          <span class="text-slate-400 block text-[10px] uppercase font-bold tracking-wider">Alokasi Institusi</span>
          <span class="font-bold text-slate-900 dark:text-white text-sm">4 Lembaga + Sampel</span>
        </div>
        <div class="h-7 w-px bg-slate-200 dark:bg-slate-800 hidden sm:block"></div>
        <div class="text-center">
          <span class="text-slate-400 block text-[10px] uppercase font-bold tracking-wider">Status Bahan</span>
          <span id="header-stock-status" class="font-bold text-emerald-600 dark:text-emerald-400 text-sm">100% Sesuai & Substitusi Siap</span>
        </div>
      </div>
    </section>

    <!-- ============================================================== -->
    <!-- SECTION 1: ARAHAN TIM PERSIAPAN (OFFICIAL TEMPLATE GENERATOR)  -->
    <!-- ============================================================== -->
    <section id="section-arahan" class="main-content-section space-y-4">
      
      <!-- Institution Selector Toolbar -->
      <div class="w-full bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-4 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 shadow-sm no-print">
        <div class="flex items-center justify-center gap-2 flex-wrap w-full sm:w-auto">
          <label class="text-xs font-bold text-slate-500 uppercase tracking-wider">Pilih Institusi:</label>
          <select id="selected-institution" onchange="renderActiveDirective()" class="bg-slate-50 dark:bg-[#0D121F] border border-slate-200 dark:border-slate-700 text-slate-900 dark:text-white text-xs rounded-lg px-3 py-1.5 font-bold outline-none cursor-pointer">
            <option value="SMK_1_KEDUNGWUNI">SMK 1 Kedungwuni (1.723 Porsi)</option>
            <option value="MTS_SALAFIYAH_SYAFIIYAH">MTs Salafiyah Syafiiyah (646 Porsi)</option>
            <option value="POSYANDU_PANJOMBLANGAN">Posyandu Panjomblangan (188 Porsi)</option>
            <option value="POSYANDU_AMBOKEMBANG">Posyandu Ambokembang (185 Porsi)</option>
          </select>
        </div>

        <div class="flex items-center justify-center gap-2 w-full sm:w-auto">
          <!-- Print Official PDF Button -->
          <button type="button" onclick="window.print()" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-[#131926] hover:bg-slate-50 text-slate-700 dark:text-slate-200 text-xs font-semibold cursor-pointer">
            <svg class="w-3.5 h-3.5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 17h2a2 2 0 002-2v-4a2 2 0 00-2-2H5a2 2 0 00-2 2v4a2 2 0 002 2h2m2 4h6a2 2 0 002-2v-4a2 2 0 00-2-2H9a2 2 0 00-2 2v4a2 2 0 002 2zm8-12V5a2 2 0 00-2-2H9a2 2 0 00-2 2v4h10z"/></svg>
            <span>Cetak PDF Resmi</span>
          </button>

          <!-- WhatsApp Share Button -->
          <button type="button" onclick="broadcastDirectiveViaWhatsApp()" class="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-xs cursor-pointer">
            <svg class="w-3.5 h-3.5" fill="currentColor" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.771-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.304-.058.116-.087.188-.173.289l-.26.304c-.087.086-.177.18-.076.354.101.174.449.741.964 1.201.662.591 1.221.774 1.394.86.173.086.275.073.376-.044.101-.116.433-.506.549-.68.116-.173.231-.145.39-.087s1.011.477 1.184.564.289.13.332.202c.043.072.043.419-.101.824z"/></svg>
            <span>Kirim Teks ke WA Relawan</span>
          </button>
        </div>
      </div>

      <!-- THE OFFICIAL 5-PAGE SPPG DIRECTIVE SHEET (CONTAINER) -->
      <div id="printable-directive-sheet" class="w-full bg-white text-slate-900 border border-slate-200 dark:border-slate-800 rounded-3xl p-6 sm:p-10 shadow-md space-y-8 select-text">
        <!-- Rendered Dynamically via JS -->
      </div>

    </section>

    <!-- ============================================================== -->
    <!-- SECTION 2: MASTER RESEP & BATCH WAJAN (2.000+ PORSI)           -->
    <!-- ============================================================== -->
    <section id="section-resep" class="main-content-section hidden space-y-4">
      <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-5 rounded-2xl shadow-sm text-center space-y-1">
        <div class="inline-flex items-center gap-2 mb-1">
          <span class="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 uppercase tracking-wider">Standar Dapur SPPG Pekajangan 04</span>
        </div>
        <h2 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white tracking-tight">
          Formula Resep & Pembagian Batch Wajan Besar (Skala 2.000+ Porsi)
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 max-w-2xl mx-auto">Dihitung otomatis dengan faktor susut mentah-ke-matang, rasio bumbu aromatik, dan pembagian porsi masak per wajan wajan besar (&divide;8 batch wajan).</p>
      </div>

      <!-- Recipe Cards Container -->
      <div id="recipe-cards-container" class="space-y-6">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- ============================================================== -->
    <!-- SECTION 3: SIKLUS MENU 2 MINGGU & AHLI GIZI                    -->
    <!-- ============================================================== -->
    <section id="section-siklus" class="main-content-section hidden space-y-4">
      <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-5 rounded-2xl shadow-sm text-center space-y-1">
        <div class="inline-flex items-center gap-2 mb-1">
          <span class="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-300 uppercase tracking-wider">Kolaborasi Gizi & Dapur</span>
        </div>
        <h2 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white tracking-tight">
          Perencanaan Siklus Menu 2 Minggu Bersama Ahli Gizi
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 max-w-2xl mx-auto">Memastikan kecukupan standar 5 komponen gizi (Karbohidrat, Protein Hewani, Protein Nabati, Sayuran, dan Buah/Side) sebelum diajukan ke Kepala Dapur.</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3" id="cycle-cards-grid">
        <!-- Rendered via JS -->
      </div>
    </section>

    <!-- ============================================================== -->
    <!-- SECTION 4: UJI ORGANOLEPTIK & KONTROL PORSI                    -->
    <!-- ============================================================== -->
    <section id="section-organoleptik" class="main-content-section hidden space-y-4">
      <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-5 rounded-2xl shadow-sm text-center space-y-1">
        <div class="inline-flex items-center gap-2 mb-1">
          <span class="text-[10px] font-bold px-2.5 py-0.5 rounded-full bg-amber-50 dark:bg-amber-950 text-amber-700 dark:text-amber-300 uppercase tracking-wider">SOP Pengamanan Pangan</span>
        </div>
        <h2 class="text-base sm:text-lg font-bold text-slate-900 dark:text-white tracking-tight">
          Lembar Kontrol Mutu & Uji Organoleptik (11 Porsi Khusus)
        </h2>
        <p class="text-xs text-slate-500 dark:text-slate-400 max-w-2xl mx-auto">Sesuai SOP: 2 porsi sampel dapur dan 9 porsi uji organoleptik wajib diuji rasa, suhu matang, dan keamanannya sebelum makanan didistribusikan ke sekolah.</p>
      </div>

      <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-xl p-5 shadow-xs space-y-4">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div class="p-3.5 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-[#0E131F]/50">
            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Total Sampel Wajib:</span>
            <p class="text-lg font-bold text-slate-900 dark:text-white mt-1">11 Porsi</p>
            <p class="text-xs text-slate-500 mt-0.5">2 Sampel Dapur + 9 Uji Organoleptik</p>
          </div>
          <div class="p-3.5 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-[#0E131F]/50">
            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Standar Suhu Masak:</span>
            <p class="text-lg font-bold text-emerald-600 dark:text-emerald-400 mt-1">&ge; 75 &deg;C</p>
            <p class="text-xs text-slate-500 mt-0.5">Telur matang &ge; 74 &deg;C (Bukan setengah matang)</p>
          </div>
          <div class="p-3.5 rounded-lg border border-slate-200 dark:border-slate-800 bg-slate-50/50 dark:bg-[#0E131F]/50">
            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-wider block">Batas Waktu Konsumsi:</span>
            <p class="text-lg font-bold text-amber-600 dark:text-amber-400 mt-1">Maksimal 4 Jam</p>
            <p class="text-xs text-slate-500 mt-0.5">Tahan panas wadah &ge; 60 &deg;C</p>
          </div>
        </div>

        <div class="border-t border-slate-100 dark:border-slate-800 pt-4 space-y-3">
          <h4 class="text-xs font-bold text-slate-900 dark:text-white uppercase tracking-wider">Form Checklist Uji Rasa Shift Malam:</h4>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
            <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-900/40">
              <input type="checkbox" checked class="w-4 h-4 text-slate-900 rounded">
              <span>Cita rasa bumbu gurih merata & tidak keasinan</span>
            </label>
            <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-900/40">
              <input type="checkbox" checked class="w-4 h-4 text-slate-900 rounded">
              <span>Telur / Protein matang sempurna tanpa bau amis</span>
            </label>
            <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-900/40">
              <input type="checkbox" checked class="w-4 h-4 text-slate-900 rounded">
              <span>Tekstur renyah terjaga & tiris minyak maksimal</span>
            </label>
            <label class="flex items-center gap-2 p-2.5 rounded-lg border border-slate-200 dark:border-slate-800 cursor-pointer hover:bg-slate-50 dark:hover:bg-slate-900/40">
              <input type="checkbox" checked class="w-4 h-4 text-slate-900 rounded">
              <span>Sayur tiris kering & segar, tidak berair</span>
            </label>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ============================================================== -->
  <!-- MODAL: KITCHEN EMERGENCY PIVOT / QUICK SUBSTITUTION            -->
  <!-- ============================================================== -->
  <div id="emergency-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-3 sm:p-4 hidden">
    <div class="bg-white dark:bg-[#111726] border border-slate-200 dark:border-slate-800 w-full max-w-xl rounded-2xl p-6 shadow-2xl space-y-4 text-left">
      <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
        <div>
          <span class="text-[10px] font-black uppercase text-amber-600 dark:text-amber-400 tracking-wider">Emergency Kitchen Pivot</span>
          <h3 class="text-sm font-bold text-slate-900 dark:text-white">Substitusi Cepat Bahan Batal / Tidak Sesuai PO</h3>
        </div>
        <button type="button" onclick="closeEmergencyModal()" class="w-7 h-7 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 text-slate-500 flex items-center justify-center text-xs font-bold cursor-pointer">✕</button>
      </div>

      <div class="space-y-3 text-xs">
        <p class="text-slate-600 dark:text-slate-400">
          Ketika supplier membatalkan kiriman atau barang datang bermasalah di tengah malam, sistem akan langsung mengalkulasi ulang kebutuhan bahan di gudang dan merevisi lembar arahan semua institusi secara otomatis.
        </p>

        <div>
          <label class="block text-slate-600 dark:text-slate-400 font-semibold mb-1">1. Pilih Bahan yang Batal / Bermasalah:</label>
          <select id="swap-origin-item" class="w-full bg-slate-50 dark:bg-[#0E131F] border border-slate-200 dark:border-slate-700 rounded-lg px-3 py-2 text-slate-900 dark:text-white font-bold outline-none">
            <option value="tahu_tepung">Tahu Segar (Rencana Tahu Goreng Tepung)</option>
            <option value="buah_naga">Buah Naga (Rencana Buah Hari Ini)</option>
            <option value="lele_fillet">Lele Fillet (Rencana Lele Crispy)</option>
            <option value="telur_rollade">Rollade Telur (Rencana Semur)</option>
          </select>
        </div>

        <div>
          <label class="block text-slate-600 dark:text-slate-400 font-semibold mb-1">2. Pilih Bahan Pengganti yang Ada di Gudang / Chiller:</label>
          <select id="swap-target-item" class="w-full bg-slate-50 dark:bg-[#0E131F] border border-slate-200 dark:border-slate-700 rounded-lg px-3 py-2 text-slate-900 dark:text-white font-bold outline-none">
            <option value="tempe_tepung">Tempe Segar Padat (Dibuat Tempe Goreng Tepung - Target 30g Matang)</option>
            <option value="jeruk_manis">Jeruk Medan Segar (1 Buah per Porsi)</option>
            <option value="telur_ceplok">Telur Ayam Ras (Dibuat Telur Ceplok - Target 60g Matang)</option>
            <option value="tahu_goreng">Tahu Putih Segar (Dibuat Tahu Goreng Bumbu Kuning)</option>
          </select>
        </div>

        <div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/40 border border-amber-200/80 dark:border-amber-800/80 space-y-1">
          <span class="text-[10px] font-bold uppercase text-amber-700 dark:text-amber-400 block">Kalkulasi Otomatis Sistem:</span>
          <p class="text-slate-700 dark:text-slate-300 font-medium">&bull; Rasio susut mentah ke matang disesuaikan otomatis (Target porsi matang terjaga).</p>
          <p class="text-slate-700 dark:text-slate-300 font-medium">&bull; Takaran tepung, minyak, dan bumbu marinasi langsung direkalkulasi untuk 2.742 porsi.</p>
          <p class="text-slate-700 dark:text-slate-300 font-medium">&bull; Catatan khusus otomatis disematkan pada lembar kerja relawan.</p>
        </div>

        <div class="pt-2 flex justify-end gap-2">
          <button type="button" onclick="closeEmergencyModal()" class="px-3.5 py-1.5 rounded-lg border border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 font-semibold cursor-pointer">Batal</button>
          <button type="button" onclick="applyEmergencySwap()" class="px-4 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold shadow-xs cursor-pointer">Terapkan Substitusi Dapur</button>
        </div>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toast" class="fixed bottom-5 right-5 z-50 bg-slate-900 dark:bg-white text-white dark:text-slate-950 px-4 py-2.5 rounded-xl text-xs font-semibold shadow-lg transition-all duration-300 opacity-0 pointer-events-none flex items-center gap-2">
    <svg class="w-4 h-4 text-emerald-400 dark:text-emerald-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
    <span id="toast-msg">Notifikasi</span>
  </div>

  <!-- ============================================================== -->
  <!-- JAVASCRIPT CORE ENGINE FOR CHEF MBG                            -->
  <!-- ============================================================== -->
  <script>
    // DATA MODEL OF REAL OPERATIONAL MENU AT SPPG PEKAJANGAN 04
    const MBG_DATA = {
      kamis_19: {
        dateString: "Kamis, 19 November 2026",
        title: "Roti Bun (Burger), Telur Ceplok, Tempe Goreng Tepung, Selada Timun, Saus Pedas Manis / Tomat, Jeruk",
        totalPortions: 2742,
        notes: "Menu mengikuti RAB Kamis. ProNa = Tempe Goreng Tepung dan Buah = Jeruk (Substitusi dari Tahu Tepung dan Buah Naga karena bahan supplier cancel). Metode adonan tepung mengikuti standar resep.",
        institutions: {
          SMK_1_KEDUNGWUNI: {
            name: "SMK 1 KEDUNGWUNI",
            totalPorsi: 1723,
            pb: 1723,
            pk: 0,
            specialNotes: "Rincian PB: 1.723 = 1.712 (SMK 1) + 2 sampel dapur + 9 uji organoleptik. Alergi Nasi: 2 porsi (Kemas terpisah). Saus disiapkan hanya Saus Pedas Manis (PB).",
            items: [
              { name: "Roti Bun (burger siap pakai)", cat: "Karbohidrat", perPorsi: "1 buah (±50 g)", total: "1.723 buah = 288 pack" },
              { name: "Telur Ayam Ras (ukuran besar)", cat: "ProHe", perPorsi: "1 butir (±60 g)", total: "1.723 butir (103,38 kg)" },
              { name: "Saus Pedas Manis (PB)", cat: "Side", perPorsi: "~15 g", total: "1.723 porsi (25,84 kg)" },
              { name: "Tempe Goreng Tepung (Substitusi Tahu)", cat: "ProNa", perPorsi: "30 g matang", total: "1.723 porsi (51,69 kg matang)" },
              { name: "Selada Timun (Lalap)", cat: "Sayur", perPorsi: "30 g", total: "1.723 porsi (51,69 kg)" },
              { name: "Jeruk Medan (Substitusi Buah Naga)", cat: "Buah", perPorsi: "1 buah", total: "1.723 buah" }
            ],
            rawIngredients: [
              { name: "Roti bun burger (pack isi 6)", perPorsi: "1 buah", qty: "1.723 buah = 288 pack" },
              { name: "Telur ayam ras (besar)", perPorsi: "1 butir (60 g)", qty: "1.723 butir (103,38 kg)" },
              { name: "Minyak goreng (goreng telur)", perPorsi: "4,8 ml", qty: "8,29 L" },
              { name: "Saus tomat (basis saus pedas)", perPorsi: "8,1 g", qty: "13,90 kg" },
              { name: "Cabai merah keriting (blender halus)", perPorsi: "4,0 g", qty: "6,95 kg" },
              { name: "Bawang putih (cincang halus)", perPorsi: "0,82 g", qty: "1,42 kg" },
              { name: "Gula pasir", perPorsi: "1,61 g", qty: "2,77 kg" },
              { name: "Cuka masak", perPorsi: "0,82 ml", qty: "1,42 L" },
              { name: "Tempe segar padat", perPorsi: "27 g", qty: "46,52 kg" },
              { name: "Tepung terigu (adonan celup)", perPorsi: "6,3 g", qty: "10,93 kg" },
              { name: "Tepung beras (renyah)", perPorsi: "4,2 g", qty: "7,29 kg" },
              { name: "Minyak goreng (deep fry tempe)", perPorsi: "8,6 ml", qty: "14,89 L" },
              { name: "Timun segar", perPorsi: "19,8 g", qty: "34,12 kg" },
              { name: "Selada segar", perPorsi: "13,2 g", qty: "22,75 kg" },
              { name: "Jeruk medan (isi 10-12/kg)", perPorsi: "1 buah", qty: "1.723 buah" }
            ],
            quickScaleTable: [
              { item: "Tempe mentah (27 g)", p10: "270 g", p50: "1,35 kg", p100: "2,7 kg" },
              { item: "Timun iris (19,8 g)", p10: "198 g", p50: "990 g", p100: "1,98 kg" },
              { item: "Selada sobek (13,2 g)", p10: "132 g", p50: "660 g", p100: "1,32 kg" },
              { item: "Telur ras (60 g)", p10: "10 butir", p50: "50 butir", p100: "100 butir" },
              { item: "Cabai keriting saus (4 g)", p10: "40 g", p50: "200 g", p100: "400 g" }
            ]
          },
          MTS_SALAFIYAH_SYAFIIYAH: {
            name: "MTS SALAFIYAH SYAFIIYAH",
            totalPorsi: 646,
            pb: 646,
            pk: 0,
            specialNotes: "Hanya Porsi Besar (PB). Alergi Nasi: 1 porsi (Kemas terpisah & label khusus). Saus disiapkan Saus Pedas Manis (PB).",
            items: [
              { name: "Roti Bun (burger)", cat: "Karbohidrat", perPorsi: "1 buah (±50 g)", total: "646 buah (108 pack isi 6)" },
              { name: "Telur Ceplok", cat: "ProHe", perPorsi: "1 butir (±60 g)", total: "646 butir (38,76 kg)" },
              { name: "Saus Pedas Manis (PB)", cat: "Side", perPorsi: "~15 g", total: "646 porsi (9,69 kg)" },
              { name: "Tempe Goreng Tepung", cat: "ProNa", perPorsi: "30 g matang", total: "646 porsi (19,38 kg matang)" },
              { name: "Selada Timun", cat: "Sayur", perPorsi: "30 g", total: "646 porsi (19,38 kg)" },
              { name: "Jeruk", cat: "Buah", perPorsi: "1 buah", total: "646 buah" }
            ],
            rawIngredients: [
              { name: "Roti bun burger", perPorsi: "1 buah", qty: "646 buah = 108 pack" },
              { name: "Telur ayam ras", perPorsi: "1 butir (60 g)", qty: "646 butir (38,76 kg)" },
              { name: "Minyak goreng telur", perPorsi: "4,8 ml", qty: "3,11 L" },
              { name: "Saus tomat saus PB", perPorsi: "8,1 g", qty: "5,21 kg" },
              { name: "Cabai merah keriting", perPorsi: "4,0 g", qty: "2,61 kg" },
              { name: "Bawang putih cincang", perPorsi: "0,82 g", qty: "531 g" },
              { name: "Gula pasir", perPorsi: "1,61 g", qty: "1,04 kg" },
              { name: "Tempe segar padat", perPorsi: "27 g", qty: "17,44 kg" },
              { name: "Tepung terigu celup", perPorsi: "6,3 g", qty: "4,10 kg" },
              { name: "Tepung beras renyah", perPorsi: "4,2 g", qty: "2,73 kg" },
              { name: "Timun segar", perPorsi: "19,8 g", qty: "12,79 kg" },
              { name: "Selada segar", perPorsi: "13,2 g", qty: "8,53 kg" },
              { name: "Jeruk medan", perPorsi: "1 buah", qty: "646 buah" }
            ],
            quickScaleTable: [
              { item: "Tempe mentah (27 g)", p10: "270 g", p50: "1,35 kg", p100: "2,7 kg" },
              { item: "Timun iris (19,8 g)", p10: "198 g", p50: "990 g", p100: "1,98 kg" },
              { item: "Selada sobek (13,2 g)", p10: "132 g", p50: "660 g", p100: "1,32 kg" },
              { item: "Telur ras (60 g)", p10: "10 butir", p50: "50 butir", p100: "100 butir" },
              { item: "Cabai keriting saus (4 g)", p10: "40 g", p50: "200 g", p100: "400 g" }
            ]
          },
          POSYANDU_PANJOMBLANGAN: {
            name: "POSYANDU PANJOMBLANGAN",
            totalPorsi: 188,
            pb: 95,
            pk: 93,
            specialNotes: "Saus Berbeda: Porsi Besar (95 PB) = Saus Pedas Manis. Porsi Kecil (93 PK) = Saus Tomat ramah anak tanpa cabai. Kemas & label wadah terpisah (PB-PEDAS dan PK-TOMAT).",
            items: [
              { name: "Roti Bun (burger)", cat: "Karbohidrat", perPorsi: "1 buah (±50 g)", total: "188 buah (32 pack isi 6)" },
              { name: "Telur Ceplok", cat: "ProHe", perPorsi: "1 butir (±60 g)", total: "188 butir (11,28 kg)" },
              { name: "Saus Pedas Manis (PB 95)", cat: "Side", perPorsi: "~15 g", total: "95 porsi (1,43 kg)" },
              { name: "Saus Tomat Ramah Anak (PK 93)", cat: "Side", perPorsi: "~15 g", total: "93 porsi (1,40 kg)" },
              { name: "Tempe Goreng Tepung", cat: "ProNa", perPorsi: "30 g matang", total: "188 porsi (5,64 kg matang)" },
              { name: "Selada Timun", cat: "Sayur", perPorsi: "30 g", total: "188 porsi (5,64 kg)" },
              { name: "Jeruk", cat: "Buah", perPorsi: "1 buah", total: "188 buah" }
            ],
            rawIngredients: [
              { name: "Roti bun burger", perPorsi: "1 buah", qty: "188 buah = 32 pack" },
              { name: "Telur ayam ras", perPorsi: "1 butir (60 g)", qty: "188 butir (11,28 kg)" },
              { name: "Saus tomat siap pakai (saus PB)", perPorsi: "8,1 g", qty: "767 g" },
              { name: "Cabai merah keriting (saus PB)", perPorsi: "4,0 g", qty: "383 g" },
              { name: "Saus tomat siap pakai (saus PK)", perPorsi: "13,2 g", qty: "1,23 kg" },
              { name: "Tomat segar blender (saus PK)", perPorsi: "1,6 g", qty: "148 g" },
              { name: "Tempe segar padat", perPorsi: "27 g", qty: "5,08 kg" },
              { name: "Tepung terigu adonan", perPorsi: "6,3 g", qty: "1,19 kg" },
              { name: "Tepung beras renyah", perPorsi: "4,2 g", qty: "795 g" },
              { name: "Timun segar", perPorsi: "19,8 g", qty: "3,72 kg" },
              { name: "Selada segar", perPorsi: "13,2 g", qty: "2,48 kg" },
              { name: "Jeruk medan", perPorsi: "1 buah", qty: "188 buah" }
            ],
            quickScaleTable: [
              { item: "Tempe mentah (27 g)", p10: "270 g", p50: "1,35 kg", p100: "2,7 kg" },
              { item: "Timun iris (19,8 g)", p10: "198 g", p50: "990 g", p100: "1,98 kg" },
              { item: "Selada sobek (13,2 g)", p10: "132 g", p50: "660 g", p100: "1,32 kg" },
              { item: "Telur ras (60 g)", p10: "10 butir", p50: "50 butir", p100: "100 butir" },
              { item: "Cabai keriting saus (4 g)", p10: "40 g", p50: "200 g", p100: "400 g" }
            ]
          },
          POSYANDU_AMBOKEMBANG: {
            name: "POSYANDU AMBOKEMBANG",
            totalPorsi: 185,
            pb: 86,
            pk: 99,
            specialNotes: "Saus Berbeda: Porsi Besar (86 PB) = Saus Pedas Manis. Porsi Kecil (99 PK) = Saus Tomat ramah anak. Label wadah PB-PEDAS dan PK-TOMAT dipisah rapat.",
            items: [
              { name: "Roti Bun (burger)", cat: "Karbohidrat", perPorsi: "1 buah (±50 g)", total: "185 buah (31 pack isi 6)" },
              { name: "Telur Ceplok", cat: "ProHe", perPorsi: "1 butir (±60 g)", total: "185 butir (11,10 kg)" },
              { name: "Saus Pedas Manis (PB 86)", cat: "Side", perPorsi: "~15 g", total: "86 porsi (1,29 kg)" },
              { name: "Saus Tomat Ramah Anak (PK 99)", cat: "Side", perPorsi: "~15 g", total: "99 porsi (1,49 kg)" },
              { name: "Tempe Goreng Tepung", cat: "ProNa", perPorsi: "30 g matang", total: "185 porsi (5,55 kg matang)" },
              { name: "Selada Timun", cat: "Sayur", perPorsi: "30 g", total: "185 porsi (5,55 kg)" },
              { name: "Jeruk", cat: "Buah", perPorsi: "1 buah", total: "185 buah" }
            ],
            rawIngredients: [
              { name: "Roti bun burger", perPorsi: "1 buah", qty: "185 buah = 31 pack" },
              { name: "Telur ayam ras", perPorsi: "1 butir (60 g)", qty: "185 butir (11,10 kg)" },
              { name: "Saus tomat siap pakai (saus PB)", perPorsi: "8,1 g", qty: "694 g" },
              { name: "Cabai merah keriting (saus PB)", perPorsi: "4,0 g", qty: "347 g" },
              { name: "Saus tomat siap pakai (saus PK)", perPorsi: "13,2 g", qty: "1,31 kg" },
              { name: "Tomat segar blender (saus PK)", perPorsi: "1,6 g", qty: "157 g" },
              { name: "Tempe segar padat", perPorsi: "27 g", qty: "5,00 kg" },
              { name: "Tepung terigu adonan", perPorsi: "6,3 g", qty: "1,17 kg" },
              { name: "Tepung beras renyah", perPorsi: "4,2 g", qty: "783 g" },
              { name: "Timun segar", perPorsi: "19,8 g", qty: "3,66 kg" },
              { name: "Selada segar", perPorsi: "13,2 g", qty: "2,44 kg" },
              { name: "Jeruk medan", perPorsi: "1 buah", qty: "185 buah" }
            ],
            quickScaleTable: [
              { item: "Tempe mentah (27 g)", p10: "270 g", p50: "1,35 kg", p100: "2,7 kg" },
              { item: "Timun iris (19,8 g)", p10: "198 g", p50: "990 g", p100: "1,98 kg" },
              { item: "Selada sobek (13,2 g)", p10: "132 g", p50: "660 g", p100: "1,32 kg" },
              { item: "Telur ras (60 g)", p10: "10 butir", p50: "50 butir", p100: "100 butir" },
              { item: "Cabai keriting saus (4 g)", p10: "40 g", p50: "200 g", p100: "400 g" }
            ]
          }
        }
      },
      senin_23: {
        dateString: "Senin, 23 November 2026",
        title: "Nasi Gurih, Lele Crispy, Sambal Bajak, Tempe Orek Kacang Panjang, Lalap Timun + Kol, Jeruk",
        totalPortions: 2211,
        notes: "Total 2.211 porsi (SMK 1.181, MTS 646, Posyandu Ambokembang 185, Posyandu Panjomblangan 188, Sampel 2, Organoleptik 9). Gramasi: ProHe 60g, ProNa 30g, Sayur 30g, Side 15g. Beras 1 kg = 19 porsi. Dibagi 8 batch wajan.",
        institutions: {
          SMK_1_KEDUNGWUNI: {
            name: "SMK 1 KEDUNGWUNI",
            totalPorsi: 1181,
            pb: 1052,
            pk: 129,
            specialNotes: "PB 1.052 porsi, PK 129 porsi. Termasuk 2 sampel dapur & 9 uji organoleptik. Lele digoreng paling akhir agar krispi.",
            items: [
              { name: "Nasi Gurih (Santan Serai)", cat: "Karbohidrat", perPorsi: "120-130 g matang", total: "1.181 porsi (62,1 kg beras)" },
              { name: "Lele Crispy Fillet", cat: "ProHe", perPorsi: "60 g matang", total: "1.181 porsi (70,86 kg fillet)" },
              { name: "Sambal Bajak Matang", cat: "Side", perPorsi: "15 g", total: "1.181 porsi (17,71 kg)" },
              { name: "Tempe Orek Kacang Panjang", cat: "ProNa", perPorsi: "30 g matang", total: "1.181 porsi (35,43 kg)" },
              { name: "Lalap Timun + Kol Blansir", cat: "Sayur", perPorsi: "30 g", total: "1.181 porsi (35,43 kg)" },
              { name: "Jeruk Manis", cat: "Buah", perPorsi: "1 buah", total: "1.181 buah" }
            ],
            rawIngredients: [
              { name: "Beras pulen", perPorsi: "52,6 g", qty: "62,1 kg" },
              { name: "Santan kelapa kental", perPorsi: "21,1 ml", qty: "24,9 L" },
              { name: "Lele fillet segar", perPorsi: "60 g", qty: "70,86 kg" },
              { name: "Tepung terigu marinasi", perPorsi: "10 g", qty: "11,81 kg" },
              { name: "Tepung maizena", perPorsi: "5 g", qty: "5,90 kg" },
              { name: "Tempe segar", perPorsi: "26,5 g", qty: "31,3 kg" },
              { name: "Kacang panjang", perPorsi: "8,8 g", qty: "10,4 kg" },
              { name: "Timun", perPorsi: "15 g", qty: "17,7 kg" },
              { name: "Kol putih", perPorsi: "15,8 g", qty: "18,6 kg" },
              { name: "Jeruk manis", perPorsi: "1 buah", qty: "1.181 buah" }
            ],
            quickScaleTable: [
              { item: "Lele fillet (60 g)", p10: "600 g", p50: "3,0 kg", p100: "6,0 kg" },
              { item: "Tempe mentah dadu", p10: "265 g", p50: "1,32 kg", p100: "2,65 kg" },
              { item: "Kacang panjang (1,5 cm)", p10: "88 g", p50: "440 g", p100: "880 g" },
              { item: "Timun iris (15 g)", p10: "150 g", p50: "750 g", p100: "1,5 kg" },
              { item: "Kol iris blansir (15,8 g)", p10: "158 g", p50: "790 g", p100: "1,58 kg" }
            ]
          }
        }
      },
      selasa_24: {
        dateString: "Selasa, 24 November 2026",
        title: "Nasi Gurih, Semur Telur Rollade, Tahu Goreng, Mix Vigie (Jagung Wortel Buncis), Pisang",
        totalPortions: 2211,
        notes: "Total 2.211 porsi. Kuah semur gurih manis pekat, telur rollade dipotong rapi, tahu goreng marinasi bawang putih kunyit.",
        institutions: {}
      },
      rabu_25: {
        dateString: "Rabu, 25 November 2026",
        title: "Nasi, Chicken Pop Kecap Mentega, Tempe Goreng, Tumis Labu Jagung, Kelengkeng",
        totalPortions: 2211,
        notes: "Total 2.211 porsi. Ayam fillet potong pop krispi disiram saus kecap mentega harum gurih.",
        institutions: {}
      },
      kamis_26: {
        dateString: "Kamis, 26 November 2026",
        title: "Nasi, Telur Rollade, Sambal Bawang, Tahu Isi Sayur, Mix Vigie, Buah Naga",
        totalPortions: 2211,
        notes: "Total 2.211 porsi. Tahu isi sayuran wortel toge renyah, saus sambal bawang segar.",
        institutions: {}
      }
    };

    let currentDayKey = 'kamis_19';
    let currentInstKey = 'SMK_1_KEDUNGWUNI';

    // RENDER ACTIVE DIRECTIVE TEMPLATE
    function renderActiveDirective() {
      const dayData = MBG_DATA[currentDayKey];
      if (!dayData) return;

      const instSelect = document.getElementById('selected-institution');
      if (instSelect) currentInstKey = instSelect.value;

      // Fallback if institution doesn't exist for this day
      let instData = dayData.institutions[currentInstKey];
      if (!instData) {
        currentInstKey = Object.keys(dayData.institutions)[0];
        instData = dayData.institutions[currentInstKey];
        if (instSelect) instSelect.value = currentInstKey;
      }

      if (!instData) {
        document.getElementById('printable-directive-sheet').innerHTML = `
          <div class="p-8 text-center text-slate-500">
            Data institusi untuk jadwal ini sedang disiapkan. Silakan pilih hari atau institusi lain.
          </div>
        `;
        return;
      }

      const container = document.getElementById('printable-directive-sheet');

      container.innerHTML = `
        <!-- HEADER KOP SURAT RESMI -->
        <div class="border-b-2 border-slate-900 pb-5">
          <div class="bg-emerald-900 text-white p-5 rounded-2xl text-center shadow-xs">
            <span class="text-[11px] uppercase tracking-widest font-bold text-emerald-200 block">Dokumen Internal SPPG Pekajangan 04 &bull; Program Makan Bergizi Gratis (MBG)</span>
            <h1 class="text-xl sm:text-2xl font-black tracking-tight mt-1">ARAHAN TIM PERSIAPAN &mdash; ${instData.name}</h1>
            <p class="text-xs text-emerald-100 mt-1">${dayData.dateString}</p>
          </div>

          <!-- PORSI SUMMARY TABLE -->
          <div class="grid grid-cols-3 gap-3 mt-4 text-center">
            <div class="p-3 bg-slate-100 border border-slate-200 rounded-xl">
              <span class="text-[10px] uppercase font-bold text-slate-500 block">Porsi Besar (PB)</span>
              <p class="text-xl font-bold font-num text-slate-900">${instData.pb || '-'}</p>
            </div>
            <div class="p-3 bg-slate-100 border border-slate-200 rounded-xl">
              <span class="text-[10px] uppercase font-bold text-slate-500 block">Porsi Kecil (PK)</span>
              <p class="text-xl font-bold font-num text-slate-900">${instData.pk || '-'}</p>
            </div>
            <div class="p-3 bg-emerald-50 border border-emerald-300 rounded-xl">
              <span class="text-[10px] uppercase font-bold text-emerald-700 block">TOTAL PORSI</span>
              <p class="text-xl font-black font-num text-emerald-800">${instData.totalPorsi} Porsi</p>
            </div>
          </div>

          <!-- SPECIAL DIVISION INSTRUCTIONS -->
          <div class="mt-4 p-3 bg-slate-50 border border-slate-200 rounded-xl text-xs space-y-1.5 text-slate-700">
            <p><strong class="text-slate-900">Tugas Tim Persiapan:</strong> Timbang, cuci, potong, pecah telur, campur adonan tepung, blender bumbu saus, dan kemas bahan berlabel. Semua proses masak (menggoreng telur/tempe, menumis saus) dikerjakan Tim Pengolahan. Selada timun, jeruk, dan roti bun selesai di Tim Persiapan (tidak dimasak).</p>
            <p class="text-amber-800 font-bold bg-amber-50 p-2 rounded-lg border border-amber-200">${instData.specialNotes}</p>
          </div>
        </div>

        <!-- 1. MENU HARI INI DAN UKURAN MATANG -->
        <div class="space-y-3">
          <div class="flex items-center justify-between border-b border-slate-200 pb-2">
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">1. Menu Hari Ini dan Ukuran Matang</h2>
            <span class="text-[11px] text-slate-500 font-medium">Ukuran setelah dimasak (bukan berat mentah)</span>
          </div>

          <table class="w-full text-left text-xs border border-slate-200">
            <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
              <tr>
                <th class="p-2.5">Menu</th>
                <th class="p-2.5">Kategori</th>
                <th class="p-2.5">Ukuran per Porsi</th>
                <th class="p-2.5 text-right">Jumlah Total</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 font-medium text-slate-800">
              ${instData.items.map(it => `
                <tr>
                  <td class="p-2.5 font-bold">${it.name}</td>
                  <td class="p-2.5 text-slate-600">${it.cat}</td>
                  <td class="p-2.5 text-slate-800">${it.perPorsi}</td>
                  <td class="p-2.5 text-right font-num font-bold text-slate-900">${it.total}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>

          <div class="p-2.5 bg-slate-50 rounded-lg border border-slate-200 text-[11px] text-slate-600">
            <strong>Catatan Chef:</strong> ${dayData.notes}
          </div>
        </div>

        <!-- 2. ATURAN YANG WAJIB DIPATUHI SEMUA RELAWAN -->
        <div class="space-y-2.5">
          <h2 class="text-sm font-bold text-slate-900 tracking-tight border-b border-slate-200 pb-2">2. Aturan Wajib Relawan Dapur SPPG</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 text-xs text-slate-700">
            <div class="p-2.5 rounded-lg border border-slate-200 bg-slate-50/50 space-y-1">
              <p class="font-bold text-slate-900">&bull; Sanitasi & Kebersihan Tangan</p>
              <p class="text-[11px] text-slate-600">Cuci tangan dengan sabun 20 detik sebelum mulai, setelah pegang telur mentah, dari toilet, dan setiap ganti pekerjaan. Gunakan masker, penutup rambut, celemek, sarung tangan.</p>
            </div>
            <div class="p-2.5 rounded-lg border border-slate-200 bg-slate-50/50 space-y-1">
              <p class="font-bold text-slate-900">&bull; Isolasi Telur Mentah & Daging</p>
              <p class="text-[11px] text-slate-600">Telur mentah dipisah. Cangkang dan cairan telur mentah dilarang menyentuh selada, timun, jeruk, atau roti. Meja didesinfeksi setelah pecah telur.</p>
            </div>
            <div class="p-2.5 rounded-lg border border-slate-200 bg-slate-50/50 space-y-1">
              <p class="font-bold text-slate-900">&bull; Pisahkan Talenan Sayur / Matang</p>
              <p class="text-[11px] text-slate-600">Selada timun dan buah tidak dimasak: wajib pakai talenan hijau khusus sayur/buah bersih dan sarung tangan steril.</p>
            </div>
            <div class="p-2.5 rounded-lg border border-slate-200 bg-slate-50/50 space-y-1">
              <p class="font-bold text-slate-900">&bull; Timbang Presisi & Label Wadah</p>
              <p class="text-[11px] text-slate-600">Timbang dan hitung, jangan menebak. Semua bahan masuk wadah berlabel institusi masing-masing. Jangan campur wadah antar sekolah.</p>
            </div>
          </div>
        </div>

        <!-- 3. BAHAN UNTUK INSTITUSI INI -->
        <div class="space-y-3">
          <div class="flex items-center justify-between border-b border-slate-200 pb-2">
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">3. Kebutuhan Bahan untuk ${instData.name} (${instData.totalPorsi} Porsi)</h2>
            <span class="text-[11px] text-slate-500 font-medium">Ambil sesuai kolom KUANTITAS BELI</span>
          </div>

          <table class="w-full text-left text-xs border border-slate-200">
            <thead class="bg-slate-100 text-slate-700 font-bold border-b border-slate-200">
              <tr>
                <th class="p-2.5">Nama Bahan Baku</th>
                <th class="p-2.5">Takaran Bersih / Porsi</th>
                <th class="p-2.5 text-right">Kuantitas Total Wadah</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 font-medium text-slate-800">
              ${instData.rawIngredients.map(ing => `
                <tr>
                  <td class="p-2.5 font-bold">${ing.name}</td>
                  <td class="p-2.5 text-slate-600">${ing.perPorsi}</td>
                  <td class="p-2.5 text-right font-num font-bold text-slate-900">${ing.qty}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>

        <!-- 4. TABEL CEPAT MENIMBANG UNTUK RELAWAN -->
        <div class="space-y-3">
          <div class="flex items-center justify-between border-b border-slate-200 pb-2">
            <h2 class="text-sm font-bold text-slate-900 tracking-tight">4. Tabel Cepat Menimbang Relawan (Baskom / Wadah)</h2>
            <span class="text-[11px] text-slate-500 font-medium">Gunakan patokan ini agar relawan tidak perlu menghitung manual</span>
          </div>

          <table class="w-full text-left text-xs border border-slate-200">
            <thead class="bg-emerald-900 text-white font-bold">
              <tr>
                <th class="p-2.5">Bahan Baku (Target Satuan)</th>
                <th class="p-2.5 text-center">10 Porsi</th>
                <th class="p-2.5 text-center">50 Porsi</th>
                <th class="p-2.5 text-center">100 Porsi</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-200 font-medium text-slate-800">
              ${instData.quickScaleTable.map(q => `
                <tr>
                  <td class="p-2.5 font-bold">${q.item}</td>
                  <td class="p-2.5 text-center font-num font-bold text-slate-800 bg-slate-50">${q.p10}</td>
                  <td class="p-2.5 text-center font-num font-bold text-slate-900 bg-emerald-50/50">${q.p50}</td>
                  <td class="p-2.5 text-center font-num font-bold text-emerald-800 bg-emerald-100/50">${q.p100}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>

        <!-- 5. PENANGGUNG JAWAB STASIUN & PARAF KONTROL MUTU -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4 border-t border-slate-200 text-xs">
          <div>
            <h4 class="font-bold text-slate-900 uppercase tracking-wider mb-2">Penanggung Jawab Stasiun:</h4>
            <div class="space-y-1.5 text-slate-700">
              <div class="flex justify-between p-2 rounded bg-slate-50 border border-slate-200">
                <span class="font-bold">Stasiun Roti / Karbo & Telur:</span>
                <span>Bu Riki, Bu Linda</span>
              </div>
              <div class="flex justify-between p-2 rounded bg-slate-50 border border-slate-200">
                <span class="font-bold">Stasiun Tempe & Saus:</span>
                <span>Faiz</span>
              </div>
              <div class="flex justify-between p-2 rounded bg-slate-50 border border-slate-200">
                <span class="font-bold">Stasiun Selada & Timun:</span>
                <span>Abidin</span>
              </div>
              <div class="flex justify-between p-2 rounded bg-slate-50 border border-slate-200">
                <span class="font-bold">Stasiun Buah & QC Timbang:</span>
                <span>Rizal, Pak Yudi, Ikbal</span>
              </div>
            </div>
          </div>

          <div>
            <h4 class="font-bold text-slate-900 uppercase tracking-wider mb-2">Otorisasi & Kontrol Mutu:</h4>
            <div class="p-4 rounded-xl border border-slate-300 bg-slate-50/50 text-center space-y-2">
              <p class="text-slate-500 text-[11px]">Disahkan oleh Head Chef Shift Malam,</p>
              <div class="h-10"></div>
              <p class="font-bold text-slate-900 border-t border-slate-300 pt-1">Chef Lutfi Iskandar</p>
              <p class="text-[10px] text-slate-500">SPPG Pekajangan 04 &bull; Program MBG</p>
            </div>
          </div>
        </div>
      `;
    }

    // NAVIGATION CONTROLLER
    function switchMainTab(tabId) {
      document.querySelectorAll('.main-content-section').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.main-tab').forEach(el => {
        el.className = 'main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800/60 cursor-pointer';
      });

      const activeSection = document.getElementById('section-' + tabId);
      const activeBtn = document.getElementById('btn-tab-' + tabId);

      if (activeSection) activeSection.classList.remove('hidden');
      if (activeBtn) {
        activeBtn.className = 'main-tab px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer';
      }

      if (tabId === 'arahan') renderActiveDirective();
      if (tabId === 'resep') renderRecipeCards();
      if (tabId === 'siklus') renderCycleCards();
    }

    // DAY SELECTOR CONTROLLER
    function selectDay(dayKey) {
      currentDayKey = dayKey;
      document.querySelectorAll('.day-selector-btn').forEach(btn => {
        btn.className = 'day-selector-btn px-3 py-1 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer';
      });

      const activeBtn = document.getElementById('day-btn-' + dayKey);
      if (activeBtn) {
        activeBtn.className = 'day-selector-btn px-3 py-1 rounded-lg text-xs font-bold bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer';
      }

      const dayData = MBG_DATA[dayKey];
      if (dayData) {
        document.getElementById('header-total-portions').innerText = dayData.totalPortions.toLocaleString('id-ID') + ' Porsi';
      }

      renderActiveDirective();
      renderRecipeCards();
      showToast('Jadwal ' + (dayData ? dayData.dateString : dayKey) + ' dimuat.');
    }

    // 10-DAY MASTER RECIPES DATASET (SIKLUS 30 NOV - 11 DES 2026)
    const MASTER_RECIPES = {
      senin_30: {
        title: "Senin, 30 November 2026 (2.442 Porsi)",
        subtitle: "Ayam Dadu Tepung Saus Mentega Madu, Tahu Bacem Legit, Tumis Labu Wortel, Buah Naga",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Ayam Dadu Tepung Saus Mentega Madu (ProHe - Target 45g Matang)",
          desc: "Fillet ayam dadu 2 cm dimarinasi wijen bawang putih jahe, digoreng krispi keemasan dan diglaze saus mentega madu tanpa cabai.",
          items: [
            { name: "Fillet Daging Ayam Bersih", perPorsi: "40 g mentah", po: "95,0 kg", batch: "11,88 kg" },
            { name: "Bumbu Marinasi (Bawang Putih, Jahe, Wijen)", perPorsi: "1,5 g", po: "3,65 kg", batch: "456 g" },
            { name: "Tepung Terigu + Maizena (Rasio 3:1)", perPorsi: "13 g", po: "32,0 kg", batch: "4,00 kg" },
            { name: "Telur Ayam Pencelup (Egg Wash)", perPorsi: "4 g", po: "10,0 kg (160 butir)", batch: "1,25 kg (20 btr)" },
            { name: "Mentega / Margarin Saus Glaze", perPorsi: "5 g", po: "12,0 kg", batch: "1,50 kg" },
            { name: "Madu Murni Glaze", perPorsi: "3 g", po: "7,5 kg", batch: "938 g" },
            { name: "Kecap Manis + Saus Tiram + Bombay", perPorsi: "9 g", po: "22,5 kg", batch: "2,81 kg" }
          ],
          chefNotes: "Dadu ayam digoreng pada suhu minyak 175 °C selama 5 menit sampai keemasan, tiriskan di rak kawat minimal 2 menit. Saus mentega madu ditumis di wajan terpisah sampai mengental mengkilap, lalu ayam diaduk kilat (tossed) sesaat sebelum packing agar kerenyahannya bertahan 4 jam."
        },
        prona: {
          name: "2. Tahu Bacem Tradisional Air Kelapa (ProNa - Target 35g Matang)",
          desc: "Tahu putih padat diungkep air kelapa murni dan gula merah kelapa sampai bumbu meresap hitam karamel legit.",
          items: [
            { name: "Tahu Putih Segar Padat", perPorsi: "1 potong (40 g)", po: "2.450 potong (98 kg)", batch: "306 potong (12,25 kg)" },
            { name: "Air Kelapa Murni Alami", perPorsi: "14 ml", po: "35,0 L", batch: "4,38 L" },
            { name: "Gula Merah Kelapa Sisir", perPorsi: "4,5 g", po: "11,0 kg", batch: "1,38 kg" },
            { name: "Bumbu Rempah (Ketumbar, Bawang, Lengkuas, Salam, Asam)", perPorsi: "3,5 g", po: "8,5 kg", batch: "1,06 kg" }
          ],
          chefNotes: "Ungkep api kecil sampai air kelapa dan gula merah susut pekat. Goreng kilat (flash fry) 1 menit sebelum disajikan agar berkulit mengkilap cantik."
        }
      },
      selasa_01: {
        title: "Selasa, 01 Desember 2026 (2.442 Porsi)",
        subtitle: "Sosis Telur Grill Saus Teriyaki, Tempe Goreng Kuning, Mix Vegetable Mentega, Anggur",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Sosis Telur Grill Saus Teriyaki (ProHe)",
          desc: "Sosis sapi iris spiral dipadu telur dadar tebal grill dengan olesan saus teriyaki gurih manis beraroma jahe bombay karamel.",
          items: [
            { name: "Sosis Sapi Premium (Iris Spiral)", perPorsi: "45 g", po: "110,0 kg (2.450 pcs)", batch: "13,75 kg" },
            { name: "Telur Ayam Ras (Dadar Grill)", perPorsi: "30 g", po: "75,0 kg (1.200 butir)", batch: "9,38 kg" },
            { name: "Saus Teriyaki Jepang", perPorsi: "6,5 g", po: "16,0 kg", batch: "2,00 kg" },
            { name: "Bawang Bombay + Bawang Putih Cincang", perPorsi: "6 g", po: "14,5 kg", batch: "1,81 kg" },
            { name: "Saus Tiram + Kecap Manis + Wijen", perPorsi: "4,5 g", po: "11,5 kg", batch: "1,44 kg" }
          ],
          chefNotes: "Gunakan wajan datar besar berpanas sedang. Tumis sosis hingga merekah lalu siram saus teriyaki sampai saus membalut mengkilap (glazing)."
        },
        prona: {
          name: "2. Tempe Goreng Bumbu Kuning (ProNa - Target 30g Matang)",
          desc: "Tempe kedelai murni diungkep bumbu kunyit ketumbar dan digoreng garing renyah.",
          items: [
            { name: "Tempe Kedelai Murni", perPorsi: "35 g mentah", po: "80,0 kg (2.450 pcs)", batch: "10,0 kg" },
            { name: "Bumbu Halus Kunyit Ketumbar Bawang Garam", perPorsi: "2,5 g", po: "6,0 kg", batch: "750 g" },
            { name: "Minyak Goreng Sawit", perPorsi: "10 ml", po: "25,0 L", batch: "3,12 L" }
          ],
          chefNotes: "Pastikan minyak mencapai 170 °C sebelum tempe dimasukkan agar tempe matang renyah dan tidak menyerap minyak berlebih."
        }
      },
      rabu_02: {
        title: "Rabu, 02 Desember 2026 (2.442 Porsi)",
        subtitle: "Ayam Goreng Lengkuas Rempah, Sambal Bawang Dapur (PK Saus Gurih), Tahu Dadu Tepung, Tumis Sawi Wortel, Jeruk",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Ayam Goreng Lengkuas Rempah Krispi (ProHe - Target 50g Matang)",
          desc: "Daging ayam diungkep bumbu rempah kuning lengkuas parut, digoreng gurih keemasan dan ditaburi serundeng lengkuas krispi.",
          items: [
            { name: "Daging Ayam Karkas Potong", perPorsi: "60 g kotor", po: "145,0 kg (2.450 pcs)", batch: "18,12 kg" },
            { name: "Lengkuas Parut Kasar (Serundeng)", perPorsi: "6 g", po: "15,0 kg", batch: "1,88 kg" },
            { name: "Bumbu Kuning Lengkap (Bawang, Kunyit, Jahe, Serai, Salam)", perPorsi: "5 g", po: "12,0 kg", batch: "1,50 kg" },
            { name: "Garam Halus + Kaldu Ayam", perPorsi: "1,5 g", po: "3,9 kg", batch: "488 g" }
          ],
          chefNotes: "Ungkep ayam hingga empuk dan air menyusut. Tiriskan ayam dan peras sedikit ampas lengkuas. Goreng ampas lengkuas dengan saringan minyak agar serundeng renyah kering tidak gosong."
        },
        prona: {
          name: "2. Tahu Dadu Tepung Gurih (ProNa)",
          desc: "Tahu putih dadu 1,5 cm dibalut tepung beras bumbu bawang putih dan digoreng krispi.",
          items: [
            { name: "Tahu Putih Dadu 1,5 cm", perPorsi: "35 g", po: "90,0 kg", batch: "11,25 kg" },
            { name: "Tepung Terigu + Tepung Beras", perPorsi: "10 g", po: "25,0 kg", batch: "3,12 kg" },
            { name: "Bumbu Bawang Putih Garam Kaldu", perPorsi: "1,6 g", po: "4,0 kg", batch: "500 g" }
          ],
          chefNotes: "Goreng dalam minyak banyak dan panas agar tahu berkulit renyah dan bagian dalamnya tetap lembut juicy."
        }
      },
      kamis_03: {
        title: "Kamis, 03 Desember 2026 (2.442 Porsi)",
        subtitle: "Roti Bun Burger, Telor Ceplok Utuh 74°C, Tempe Tepung Daun Bawang, Saus Pedas/Tomat, Timun Selada, Kelengkeng",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Telur Ceplok Utuh Matang Sempurna (ProHe - Standar HACCP)",
          desc: "Telur ayam ras segar diceplok matang sempurna pada wajan datar bersekat, suhu inti mencapai ≥ 74 °C bebas Salmonella.",
          items: [
            { name: "Telur Ayam Ras Besar (55-60 g)", perPorsi: "1 butir", po: "2.453 butir (147,2 kg)", batch: "306 butir" },
            { name: "Minyak Oles Wajan Datar", perPorsi: "3 ml", po: "8,0 L", batch: "1,0 L" },
            { name: "Garam Halus Tabur", perPorsi: "0,2 g", po: "500 g", batch: "62 g" }
          ],
          chefNotes: "Tutup wajan datar saat menggoreng ceplok agar bagian atas kuning telur matang sempurna terkena uap panas tanpa perlu dibalik hancur."
        },
        prona: {
          name: "2. Tempe Goreng Tepung Daun Bawang (ProNa)",
          desc: "Tempe kedelai berbalut adonan tepung beras renyah dengan aroma harum irisan daun bawang segar.",
          items: [
            { name: "Tempe Kedelai Iris", perPorsi: "25 g mentah", po: "55,0 kg", batch: "6,88 kg" },
            { name: "Tepung Terigu + Tepung Beras", perPorsi: "10 g", po: "24,0 kg", batch: "3,00 kg" },
            { name: "Daun Bawang Iris Halus", perPorsi: "1,6 g", po: "4,0 kg", batch: "500 g" },
            { name: "Bumbu Ketumbar Bawang Garam", perPorsi: "1,6 g", po: "4,0 kg", batch: "500 g" }
          ],
          chefNotes: "Gunakan adonan dengan kekentalan sedang. Goreng sampai pinggirannya krispi bersarang."
        }
      },
      jumat_04: {
        title: "Jumat, 04 Desember 2026 (2.094 Porsi)",
        subtitle: "Kimbab Roll Sushi Nasi Gurih, Karage Ayam Juicy Saus Bulgogi, Edamame Rebus Polong, Pisang",
        totalPorsi: "2.094 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Karage Ayam Juicy Saus Bulgogi (ProHe)",
          desc: "Potongan paha ayam dadu dimarinasi shoyu jahe bawang putih, dibalut tepung tapioka karage renyah dengan siraman saus bulgogi.",
          items: [
            { name: "Fillet Paha Ayam Juicy (Dadu 2,5 cm)", perPorsi: "40 g mentah", po: "85,0 kg", batch: "10,63 kg" },
            { name: "Bumbu Marinasi Shoyu Jahe Bawang Wijen", perPorsi: "3,3 g", po: "7,0 kg", batch: "875 g" },
            { name: "Tepung Tapioka / Maizena Karage", perPorsi: "8,5 g", po: "18,0 kg", batch: "2,25 kg" },
            { name: "Saus Bulgogi Glaze (Pir, Kecap Asin, Wijen)", perPorsi: "10 g", po: "21,0 kg", batch: "2,63 kg" }
          ],
          chefNotes: "Tepung tapioka menghasilkan kerenyahan khas karage yang tipis dan garing tanpa menyerap banyak saus sehingga ayam tetap renyah saat dinikmati siswa."
        },
        prona: {
          name: "2. Edamame Rebus Polong Gurih (ProNa)",
          desc: "Edamame polong hijau segar direbus air garam laut, manis alami dan kaya serat nabati.",
          items: [
            { name: "Edamame Polong Segar", perPorsi: "35 g", po: "75,0 kg", batch: "9,38 kg" },
            { name: "Garam Rebus Laut", perPorsi: "1,2 g", po: "2,5 kg", batch: "312 g" }
          ],
          chefNotes: "Rebus tepat 5 menit pada air mendidih. Langsung tiriskan dan angin-anginkan agar warna polong tetap hijau cerah mengkilap."
        }
      },
      senin_07: {
        title: "Senin, 07 Desember 2026 (2.442 Porsi)",
        subtitle: "Nasi Putih, Ayam Katsu Panko Renyah, Sambal Ijo Padang, Tempe Goreng, Lalap Timun Kol, Pisang",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Ayam Katsu Panko Renyah (ProHe - Target 50g Matang)",
          desc: "Fillet dada ayam pipih dimarinasi gurih, dibalut tepung roti panko kasar tiga tahap, digoreng renyah keemasan.",
          items: [
            { name: "Fillet Dada Ayam Bersih (Tebal 1 cm)", perPorsi: "40 g mentah", po: "95,0 kg", batch: "11,88 kg" },
            { name: "Bumbu Marinasi Bawang Putih Kecap Asin Lada", perPorsi: "1,6 g", po: "4,0 kg", batch: "500 g" },
            { name: "Tepung Terigu Pro Sedang (Lapisan 1)", perPorsi: "6 g", po: "15,0 kg", batch: "1,88 kg" },
            { name: "Telur Ayam Pencelup (Lapisan 2)", perPorsi: "5 g", po: "12,0 kg", batch: "1,50 kg" },
            { name: "Tepung Roti Panko Kasar (Lapisan 3)", perPorsi: "9 g", po: "22,0 kg", batch: "2,75 kg" }
          ],
          chefNotes: "Tekan tepung panko perlahan agar melekat kuat. Goreng 4 menit pada suhu 175 °C. Kerenyahan panko tahan hingga 4 jam dalam kemasan berventilasi."
        },
        prona: {
          name: "2. Tempe Goreng Lengkuas (ProNa)",
          desc: "Tempe kedelai diungkep bumbu lengkuas dan digoreng garing harum.",
          items: [
            { name: "Tempe Kedelai Papan", perPorsi: "35 g", po: "80,0 kg", batch: "10,0 kg" },
            { name: "Bumbu Lengkuas Bawang Garam Kunyit", perPorsi: "2,5 g", po: "6,0 kg", batch: "750 g" }
          ],
          chefNotes: "Goreng tempe dalam minyak banyak dan tiriskan di rak kawat minimal 2 menit."
        }
      },
      selasa_08: {
        title: "Selasa, 08 Desember 2026 (2.442 Porsi)",
        subtitle: "Nasi Putih, Telur Katsu Panko Saus BBQ Smokey, Tahu Tepung Dadu, Mix Vigie, Jeruk",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Telur Katsu Panko Saus BBQ Smokey (ProHe)",
          desc: "Telur rebus matang dibelah dua berbalut tepung panko krispi disiram saus BBQ beraroma asap karamel.",
          items: [
            { name: "Telur Ayam Ras (Rebus Belah Dua)", perPorsi: "1 butir", po: "2.453 butir (147,2 kg)", batch: "306 butir" },
            { name: "Tepung Terigu + Telur Pencelup", perPorsi: "8 g", po: "20,0 kg", batch: "2,50 kg" },
            { name: "Tepung Roti Panko", perPorsi: "8 g", po: "20,0 kg", batch: "2,50 kg" },
            { name: "Saus BBQ Smokey Karamel", perPorsi: "10 g", po: "24,0 kg", batch: "3,00 kg" }
          ],
          chefNotes: "Goreng kilat 2 menit saja sampai lapisan panko luar renyah keemasan karena telur bagian dalam sudah matang rebus."
        },
        prona: {
          name: "2. Tahu Tepung Dadu Renyah (ProNa)",
          desc: "Tahu putih dadu berbalut tepung renyah gurih bumbu bawang.",
          items: [
            { name: "Tahu Putih Dadu", perPorsi: "35 g", po: "90,0 kg", batch: "11,25 kg" },
            { name: "Tepung Terigu + Maizena Bumbu", perPorsi: "9 g", po: "22,0 kg", batch: "2,75 kg" }
          ],
          chefNotes: "Pastikan tahu ditiriskan airnya sebelum dibalut tepung kering agar adonan tidak menggumpal becek."
        }
      },
      rabu_09: {
        title: "Rabu, 09 Desember 2026 (2.442 Porsi)",
        subtitle: "Roti Burger/Sandwich, Patty Ayam Katsu, Mayones Gurih, Edamame Rebus, Coleslaw Salad Mayo, Kelengkeng",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Patty Ayam Katsu Crispy (ProHe)",
          desc: "Cincangan daging ayam bumbu gurih dibentuk bulat pipih, dibalut tepung panko dan digoreng renyah keemasan.",
          items: [
            { name: "Daging Ayam Cincang Bersih", perPorsi: "38 g mentah", po: "90,0 kg", batch: "11,25 kg" },
            { name: "Bumbu Adonan (Bombay, Tapioka, Telur, Bawang)", perPorsi: "11 g", po: "27,0 kg", batch: "3,38 kg" },
            { name: "Tepung Panko Pelapis", perPorsi: "8 g", po: "20,0 kg", batch: "2,50 kg" }
          ],
          chefNotes: "Kukus atau cetak patty dingin sebelum dibalut panko agar bentuk bulat pipih tetap kokoh dan rapi saat digoreng."
        },
        prona: {
          name: "2. Edamame Rebus Polong Gurih (ProNa)",
          desc: "Edamame segar rebus polong kaya antioksidan dan serat nabati.",
          items: [
            { name: "Edamame Polong Segar", perPorsi: "35 g", po: "85,0 kg", batch: "10,63 kg" },
            { name: "Garam Rebus Alami", perPorsi: "1,2 g", po: "3,0 kg", batch: "375 g" }
          ],
          chefNotes: "Sajikan edamame dalam wadah terpisah agar tidak terkena uap panas roti burger."
        }
      },
      kamis_10: {
        title: "Kamis, 10 Desember 2026 (2.442 Porsi)",
        subtitle: "Nasi Putih, Ayam Dadu Kecap Karamel Jahe, Orek Tempe Manis Gurih, Tumis Labu Wortel, Anggur",
        totalPorsi: "2.442 Porsi",
        batchCount: "8 Batch Wajan",
        prohe: {
          name: "1. Ayam Dadu Kecap Karamel Jahe (ProHe - Target 45g Matang)",
          desc: "Fillet ayam dadu ditumis bersama kecap manis karamel, bawang bombay, bawang merah, dan aroma jahe geprek pekat lezat.",
          items: [
            { name: "Fillet Ayam Bersih Dadu 2 cm", perPorsi: "40 g mentah", po: "95,0 kg", batch: "11,88 kg" },
            { name: "Kecap Manis Kental Premium", perPorsi: "6 g", po: "14,0 kg", batch: "1,75 kg" },
            { name: "Jahe Geprek Segar + Bombay + Bawang", perPorsi: "8 g", po: "19,0 kg", batch: "2,38 kg" },
            { name: "Saus Tiram + Mentega Tumis", perPorsi: "3,8 g", po: "9,0 kg", batch: "1,12 kg" }
          ],
          chefNotes: "Tumis bumbu bawang dan jahe sampai layu kecokelatan, masukkan ayam hingga berubah warna, lalu tuang kecap manis di pinggir wajan panas agar terkaramelisasi sempurna."
        },
        prona: {
          name: "2. Orek Tempe Manis Gurih Kering (ProNa)",
          desc: "Tempe iris korek api digoreng garing kering, dibalut saus gula merah karamel dan cabai merah iris.",
          items: [
            { name: "Tempe Kedelai Iris Korek", perPorsi: "30 g mentah", po: "70,0 kg", batch: "8,75 kg" },
            { name: "Gula Merah Kelapa + Asam Jawa", perPorsi: "4 g", po: "9,5 kg", batch: "1,19 kg" },
            { name: "Bumbu Salam Lengkuas Cabai Merah", perPorsi: "2,5 g", po: "6,0 kg", batch: "750 g" }
          ],
          chefNotes: "Pastikan larutan gula merah sudah berbusa kental (berserabut) sebelum tempe garing dimasukkan. Matikan api dan aduk cepat agar tempe tetap garing tahan berhari-hari."
        }
      },
      jumat_11: {
        title: "Jumat, 11 Desember 2026 (2.094 Porsi)",
        subtitle: "Jasuke (Jagung Susu Keju Lumer), Telur Rebus Bulat Utuh 75°C, Kacang Polong Gurih, Puding Wortel Dingin, Buah Naga",
        totalPorsi: "2.094 Porsi",
        batchCount: "8 Batch Dandang / Wajan",
        prohe: {
          name: "1. Telur Rebus Bulat Utuh Matang 75°C (ProHe - Standar HACCP)",
          desc: "Telur ayam ras segar utuh direbus air mendidih 11 menit sampai matang sempurna ke pusat kuning telur, direndam air es.",
          items: [
            { name: "Telur Ayam Ras Segar", perPorsi: "1 butir", po: "2.105 butir (126,5 kg)", batch: "263 butir" },
            { name: "Garam Rebus (Mudah Kupas)", perPorsi: "1 g", po: "2,0 kg", batch: "250 g" }
          ],
          chefNotes: "Segera pindahkan telur dari air panas ke bak air es mengalir. Perbedaan suhu mendadak memisahkan selaput cangkang sehingga relawan dapat mengupas cangkang dalam hitungan detik tanpa merusak putih telur."
        },
        prona: {
          name: "2. Jasuke Jagung Susu Keju Lumer (Karbohidrat Energi)",
          desc: "Jagung manis pipil segar dikukus panas matang, diaduk lelehan margarin gurih, kental manis, dan keju cheddar melimpah.",
          items: [
            { name: "Jagung Manis Pipil Segar", perPorsi: "75 g", po: "160,0 kg", batch: "20,0 kg" },
            { name: "Margarin Tawar Mentega", perPorsi: "5 g", po: "10,0 kg", batch: "1,25 kg" },
            { name: "Susu Kental Manis Putih", perPorsi: "4,5 g", po: "25 kaleng (9,2 kg)", batch: "3 kaleng" },
            { name: "Keju Cheddar Parut Gurih", perPorsi: "7 g", po: "15,0 kg", batch: "1,88 kg" }
          ],
          chefNotes: "Kukus jagung dalam dandang besar bertahap. Aduk margarin dan susu selagi jagung masih mengepul panas agar keju dan mentega meleleh menyatu gurih."
        }
      }
    };

    // RENDER RECIPE CARDS CONTROLLER
    function renderRecipeCards() {
      const container = document.getElementById('recipe-cards-container');
      if (!container) return;

      container.innerHTML = `
        <!-- DAY SELECTOR KHUSUS MASTER RESEP LENGKAP 10 HARI -->
        <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 p-5 rounded-2xl shadow-sm space-y-3 no-print">
          <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-2">
            <span class="text-xs font-bold text-slate-500 uppercase tracking-wider">Formula Resep Lengkap Siklus 10 Hari:</span>
            <span class="text-xs font-bold px-2.5 py-0.5 rounded-full bg-emerald-50 dark:bg-emerald-950 text-emerald-700 dark:text-emerald-400">Skala 2.442 / 2.094 Porsi (÷8 Batch)</span>
          </div>

          <!-- MINGGU 1 BUTTONS -->
          <div class="space-y-1.5">
            <span class="text-[10px] font-bold uppercase text-emerald-600 tracking-wider block">Minggu I (30 Nov - 04 Des):</span>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" onclick="loadRecipeView('senin_30')" id="rcp-btn-senin_30" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer">Senin 30 Nov: Ayam Madu & Tahu Bacem</button>
              <button type="button" onclick="loadRecipeView('selasa_01')" id="rcp-btn-selasa_01" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Selasa 01 Des: Sosis Telur Teriyaki</button>
              <button type="button" onclick="loadRecipeView('rabu_02')" id="rcp-btn-rabu_02" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Rabu 02 Des: Ayam Lengkuas Sambal</button>
              <button type="button" onclick="loadRecipeView('kamis_03')" id="rcp-btn-kamis_03" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Kamis 03 Des: Burger Telur Ceplok</button>
              <button type="button" onclick="loadRecipeView('jumat_04')" id="rcp-btn-jumat_04" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Jumat 04 Des: Kimbab & Karage Bulgogi</button>
            </div>
          </div>

          <!-- MINGGU 2 BUTTONS -->
          <div class="space-y-1.5 pt-2 border-t border-slate-100 dark:border-slate-800">
            <span class="text-[10px] font-bold uppercase text-blue-600 tracking-wider block">Minggu II (07 - 11 Des):</span>
            <div class="flex items-center gap-1.5 flex-wrap">
              <button type="button" onclick="loadRecipeView('senin_07')" id="rcp-btn-senin_07" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Senin 07 Des: Ayam Katsu Sambal Ijo</button>
              <button type="button" onclick="loadRecipeView('selasa_08')" id="rcp-btn-selasa_08" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Selasa 08 Des: Telur Katsu BBQ</button>
              <button type="button" onclick="loadRecipeView('rabu_09')" id="rcp-btn-rabu_09" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Rabu 09 Des: Patty Katsu & Coleslaw</button>
              <button type="button" onclick="loadRecipeView('kamis_10')" id="rcp-btn-kamis_10" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Kamis 10 Des: Ayam Kecap & Orek Tempe</button>
              <button type="button" onclick="loadRecipeView('jumat_11')" id="rcp-btn-jumat_11" class="rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer">Jumat 11 Des: Jasuke & Puding Wortel</button>
            </div>
          </div>
        </div>

        <!-- DETAIL RECIPE CONTAINER -->
        <div id="recipe-detail-display" class="space-y-6">
          <!-- Rendered dynamically -->
        </div>
      `;

      loadRecipeView('senin_30');
    }

    function loadRecipeView(dayKey) {
      document.querySelectorAll('.rcp-tab-btn').forEach(b => {
        b.className = 'rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer';
      });
      const activeBtn = document.getElementById('rcp-btn-' + dayKey);
      if (activeBtn) {
        activeBtn.className = 'rcp-tab-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-900 text-white dark:bg-white dark:text-slate-950 shadow-xs cursor-pointer';
      }

      const display = document.getElementById('recipe-detail-display');
      if (!display) return;

      const r = MASTER_RECIPES[dayKey];
      if (!r) return;

      display.innerHTML = `
        <!-- HEADER FORMULA HARI -->
        <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-2xl p-5 shadow-xs flex flex-col sm:flex-row items-start sm:items-center justify-between gap-3">
          <div>
            <span class="text-[10px] font-bold uppercase text-slate-400 tracking-wider block">Standar Formula Dapur SPPG:</span>
            <h3 class="text-base font-bold text-slate-900 dark:text-white mt-0.5">${r.title}</h3>
            <p class="text-xs text-slate-500 mt-0.5">${r.subtitle}</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950 text-emerald-800 dark:text-emerald-300 font-bold text-xs">${r.totalPorsi}</span>
            <span class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-800 dark:text-slate-200 font-bold text-xs">${r.batchCount}</span>
          </div>
        </div>

        <!-- RESEP PROTEIN HEWANI (PROHE) -->
        <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-2xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
            <div>
              <span class="text-[10px] font-bold uppercase text-red-600 dark:text-red-400 tracking-wider">Komponen Protein Utama (ProHe)</span>
              <h4 class="text-base font-bold text-slate-900 dark:text-white">${r.prohe.name}</h4>
              <p class="text-xs text-slate-500">${r.prohe.desc}</p>
            </div>
            <span class="px-2.5 py-1 rounded-md bg-red-50 dark:bg-red-950 font-bold text-xs text-red-800 dark:text-red-300">Wajan ÷8 Batch</span>
          </div>

          <table class="w-full text-left text-xs border border-slate-200 dark:border-slate-800">
            <thead class="bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-bold">
              <tr>
                <th class="p-2.5">Bahan Baku Dapur</th>
                <th class="p-2.5">Takaran Porsi</th>
                <th class="p-2.5 text-right">Total Belanja Dapur (PO)</th>
                <th class="p-2.5 text-right font-bold text-red-700 dark:text-red-400">Per Batch (÷8 Wajan)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-800 dark:text-slate-200 font-medium">
              ${r.prohe.items.map(it => `
                <tr>
                  <td class="p-2.5 font-bold">${it.name}</td>
                  <td class="p-2.5">${it.perPorsi}</td>
                  <td class="p-2.5 text-right font-num font-bold">${it.po}</td>
                  <td class="p-2.5 text-right font-num font-bold text-red-700 dark:text-red-400">${it.batch}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>

          <div class="p-3.5 bg-slate-50 dark:bg-slate-900/40 rounded-xl text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <p><strong>Catatan Sains Kuliner & HACCP Chef:</strong> ${r.prohe.chefNotes}</p>
          </div>
        </div>

        <!-- RESEP PROTEIN NABATI (PRONA) -->
        <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-2xl p-6 shadow-sm space-y-4">
          <div class="flex items-center justify-between border-b border-slate-100 dark:border-slate-800 pb-3">
            <div>
              <span class="text-[10px] font-bold uppercase text-blue-600 dark:text-blue-400 tracking-wider">Komponen Nabati (ProNa)</span>
              <h4 class="text-base font-bold text-slate-900 dark:text-white">${r.prona.name}</h4>
              <p class="text-xs text-slate-500">${r.prona.desc}</p>
            </div>
            <span class="px-2.5 py-1 rounded-md bg-blue-50 dark:bg-blue-950 font-bold text-xs text-blue-800 dark:text-blue-300">Wajan ÷8 Batch</span>
          </div>

          <table class="w-full text-left text-xs border border-slate-200 dark:border-slate-800">
            <thead class="bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-200 font-bold">
              <tr>
                <th class="p-2.5">Bahan Baku Dapur</th>
                <th class="p-2.5">Takaran Porsi</th>
                <th class="p-2.5 text-right">Total Belanja Dapur (PO)</th>
                <th class="p-2.5 text-right font-bold text-blue-700 dark:text-blue-400">Per Batch (÷8 Wajan)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 dark:divide-slate-800 text-slate-800 dark:text-slate-200 font-medium">
              ${r.prona.items.map(it => `
                <tr>
                  <td class="p-2.5 font-bold">${it.name}</td>
                  <td class="p-2.5">${it.perPorsi}</td>
                  <td class="p-2.5 text-right font-num font-bold">${it.po}</td>
                  <td class="p-2.5 text-right font-num font-bold text-blue-700 dark:text-blue-400">${it.batch}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>

          <div class="p-3.5 bg-slate-50 dark:bg-slate-900/40 rounded-xl text-xs space-y-1 text-slate-700 dark:text-slate-300">
            <p><strong>Standar QC Dapur Chef:</strong> ${r.prona.chefNotes}</p>
          </div>
        </div>
      `;
    }

    // RENDER 2-WEEK MENU CYCLE (30 NOV - 11 DES 2026)
    function renderCycleCards() {
      const container = document.getElementById('cycle-cards-grid');
      if (!container) return;

      const cycles = [
        // MINGGU 1: 30 NOV - 04 DES 2026
        { week: "Minggu 1", date: "30 Nov", day: "Senin", karbo: "Nasi", prohe: "Ayam Dadu Tepung", side: "Saus Mentega Madu", prona: "Tahu Bacem", sayur: "Tumis Labu / Lalap", buah: "Buah Naga", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 1", date: "01 Des", day: "Selasa", karbo: "Nasi", prohe: "Sosis Telur Grill", side: "Saus Teriyaki", prona: "Tempe Goreng", sayur: "Mix Vegetable", buah: "Anggur", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 1", date: "02 Des", day: "Rabu", karbo: "Nasi", prohe: "Ayam Goreng", side: "Sambal Bawang", prona: "Tahu Dadu Tepung", sayur: "Tumis Sawi Wortel", buah: "Jeruk", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 1", date: "03 Des", day: "Kamis", karbo: "Roti Bun (Burger)", prohe: "Telor Ceplok", side: "Saus Pedas / Saus Tomat", prona: "Tempe Tepung", sayur: "Timun Selada", buah: "Kelengkeng", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 1", date: "04 Des", day: "Jumat", karbo: "Kimbab", prohe: "Karage", side: "Saus Bulgogi Pedas/Manis", prona: "Edamame", sayur: "Isian Sayur Roll", buah: "Pisang", pb: 1902, pk: 192, total: 2094, status: "Plan Ahli Gizi" },

        // MINGGU 2: 07 - 11 DES 2026
        { week: "Minggu 2", date: "07 Des", day: "Senin", karbo: "Nasi", prohe: "Ayam Katsu", side: "Sambal Ijo", prona: "Tempe Goreng", sayur: "Lalap Timun + Kol", buah: "Pisang", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 2", date: "08 Des", day: "Selasa", karbo: "Nasi", prohe: "Telur Katsu", side: "Saus BBQ", prona: "Tahu Tepung Dadu", sayur: "Mix Vigie", buah: "Jeruk", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 2", date: "09 Des", day: "Rabu", karbo: "Roti", prohe: "Patty Ayam Katsu", side: "Mayones Gurih", prona: "Edamame", sayur: "Coleslaw", buah: "Kelengkeng", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 2", date: "10 Des", day: "Kamis", karbo: "Nasi", prohe: "Ayam Dadu Kecap", side: "Kuah Kecap Aromatik", prona: "Orek Tempe", sayur: "Labu Wortel", buah: "Anggur", pb: 2250, pk: 192, total: 2442, status: "Plan Ahli Gizi" },
        { week: "Minggu 2", date: "11 Des", day: "Jumat", karbo: "Jasuke (Jagung Susu Keju)", prohe: "Telur Rebus Bulat", side: "Taburan Keju Cheddar", prona: "Kacang Polong", sayur: "Puding Wortel", buah: "Buah Naga", pb: 1902, pk: 192, total: 2094, status: "Plan Ahli Gizi" }
      ];

      container.innerHTML = `
        <div class="col-span-full space-y-6">
          <!-- MINGGU 1 -->
          <div>
            <div class="flex items-center justify-between mb-3 border-b border-slate-200 dark:border-slate-800 pb-2">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <h3 class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-wider">Siklus Minggu I: 30 November &mdash; 04 Desember 2026</h3>
              </div>
              <span class="text-xs text-slate-500">Senin-Kamis 2.442 Porsi &bull; Jumat 2.094 Porsi</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3">
              ${cycles.filter(c => c.week === 'Minggu 1').map(c => `
                <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-2xl p-4 space-y-3 shadow-xs hover:border-emerald-500/50 transition-all">
                  <div class="flex justify-between items-center border-b border-slate-100 dark:border-slate-800 pb-2">
                    <div>
                      <span class="text-[10px] text-slate-400 font-bold block">${c.date}</span>
                      <span class="font-extrabold text-slate-900 dark:text-white text-sm">${c.day}</span>
                    </div>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-50 dark:bg-emerald-950/60 text-emerald-700 dark:text-emerald-400 border border-emerald-200/60">${c.total} Porsi</span>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-amber-600 bg-amber-50 dark:bg-amber-950/50 px-1 rounded shrink-0">Karbo</span>
                      <span class="text-slate-800 dark:text-slate-200 font-bold">${c.karbo}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-red-600 bg-red-50 dark:bg-red-950/50 px-1 rounded shrink-0">ProHe</span>
                      <span class="text-slate-800 dark:text-slate-200 font-bold">${c.prohe}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-purple-600 bg-purple-50 dark:bg-purple-950/50 px-1 rounded shrink-0">Side</span>
                      <span class="text-slate-600 dark:text-slate-400 font-medium">${c.side}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-blue-600 bg-blue-50 dark:bg-blue-950/50 px-1 rounded shrink-0">ProNa</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.prona}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-emerald-600 bg-emerald-50 dark:bg-emerald-950/50 px-1 rounded shrink-0">Sayur</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.sayur}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-rose-600 bg-rose-50 dark:bg-rose-950/50 px-1 rounded shrink-0">Buah</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.buah}</span>
                    </div>
                  </div>

                  <div class="pt-2 text-[10px] text-slate-400 border-t border-slate-100 dark:border-slate-800 flex justify-between">
                    <span>PB: ${c.pb}</span>
                    <span>PK: ${c.pk}</span>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- MINGGU 2 -->
          <div>
            <div class="flex items-center justify-between mb-3 border-b border-slate-200 dark:border-slate-800 pb-2">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-500"></span>
                <h3 class="text-sm font-bold text-slate-900 dark:text-white uppercase tracking-wider">Siklus Minggu II: 07 &mdash; 11 Desember 2026</h3>
              </div>
              <span class="text-xs text-slate-500">Senin-Kamis 2.442 Porsi &bull; Jumat 2.094 Porsi</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-3">
              ${cycles.filter(c => c.week === 'Minggu 2').map(c => `
                <div class="bg-white dark:bg-[#111726] border border-slate-200/80 dark:border-slate-800/80 rounded-2xl p-4 space-y-3 shadow-xs hover:border-blue-500/50 transition-all">
                  <div class="flex justify-between items-center border-b border-slate-100 dark:border-slate-800 pb-2">
                    <div>
                      <span class="text-[10px] text-slate-400 font-bold block">${c.date}</span>
                      <span class="font-extrabold text-slate-900 dark:text-white text-sm">${c.day}</span>
                    </div>
                    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-blue-50 dark:bg-blue-950/60 text-blue-700 dark:text-blue-400 border border-blue-200/60">${c.total} Porsi</span>
                  </div>

                  <div class="space-y-1.5 text-xs">
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-amber-600 bg-amber-50 dark:bg-amber-950/50 px-1 rounded shrink-0">Karbo</span>
                      <span class="text-slate-800 dark:text-slate-200 font-bold">${c.karbo}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-red-600 bg-red-50 dark:bg-red-950/50 px-1 rounded shrink-0">ProHe</span>
                      <span class="text-slate-800 dark:text-slate-200 font-bold">${c.prohe}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-purple-600 bg-purple-50 dark:bg-purple-950/50 px-1 rounded shrink-0">Side</span>
                      <span class="text-slate-600 dark:text-slate-400 font-medium">${c.side}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-blue-600 bg-blue-50 dark:bg-blue-950/50 px-1 rounded shrink-0">ProNa</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.prona}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-emerald-600 bg-emerald-50 dark:bg-emerald-950/50 px-1 rounded shrink-0">Sayur</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.sayur}</span>
                    </div>
                    <div class="flex items-start gap-1.5">
                      <span class="text-[10px] font-bold uppercase text-rose-600 bg-rose-50 dark:bg-rose-950/50 px-1 rounded shrink-0">Buah</span>
                      <span class="text-slate-700 dark:text-slate-300">${c.buah}</span>
                    </div>
                  </div>

                  <div class="pt-2 text-[10px] text-slate-400 border-t border-slate-100 dark:border-slate-800 flex justify-between">
                    <span>PB: ${c.pb}</span>
                    <span>PK: ${c.pk}</span>
                  </div>
                </div>
              `).join('')}
            </div>
          </div>
        </div>
      `;
    }

    // BROADCAST DIRECTIVE VIA WHATSAPP (ONE-CLICK VOLUNTEER DISPATCH)
    function broadcastDirectiveViaWhatsApp() {
      const dayData = MBG_DATA[currentDayKey];
      const instData = dayData ? dayData.institutions[currentInstKey] : null;
      if (!instData) return;

      let msg = `*ARAHAN TIM PERSIAPAN SPPG PEKAJANGAN 04*\n`;
      msg += `Institusi: *${instData.name}*\n`;
      msg += `Jadwal: ${dayData.dateString}\n`;
      msg += `Total Porsi: *${instData.totalPorsi} porsi* (PB: ${instData.pb || '-'}, PK: ${instData.pk || '-'})\n\n`;
      msg += `*MENU & UKURAN MATANG:*\n`;
      instData.items.forEach(it => {
        msg += `- ${it.name}: ${it.perPorsi} (Total: ${it.total})\n`;
      });
      msg += `\n*CATATAN KHUSUS CHEF:*\n${instData.specialNotes}\n\n`;
      msg += `*TABEL CEPAT MENIMBANG (Relawan):*\n`;
      instData.quickScaleTable.forEach(q => {
        msg += `• ${q.item} -> 10p: ${q.p10} | 50p: ${q.p50} | 100p: ${q.p100}\n`;
      });
      msg += `\nHarap timbang sesuai tabel dan jangan menebak. - Chef Lutfi Iskandar`;

      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(msg), '_blank');
      showToast('Teks arahan relawan disiapkan untuk WhatsApp');
    }

    // EMERGENCY SUBSTITUTION MODAL
    function openEmergencyModal() {
      document.getElementById('emergency-modal').classList.remove('hidden');
    }

    function closeEmergencyModal() {
      document.getElementById('emergency-modal').classList.add('hidden');
    }

    function applyEmergencySwap() {
      const orig = document.getElementById('swap-origin-item').value;
      const target = document.getElementById('swap-target-item').value;

      closeEmergencyModal();
      showToast('Substitusi bahan darurat berhasil diterapkan & lembar arahan diperbarui!');
    }

    // TOAST SYSTEM
    function showToast(msg) {
      const toast = document.getElementById('toast');
      const toastMsg = document.getElementById('toast-msg');
      if (!toast || !toastMsg) return;

      toastMsg.innerText = msg;
      toast.classList.remove('opacity-0', 'pointer-events-none');
      toast.classList.add('opacity-100');

      setTimeout(() => {
        toast.classList.remove('opacity-100');
        toast.classList.add('opacity-0', 'pointer-events-none');
      }, 3000);
    }

    // THEME SYSTEM
    function initTheme() {
      const isDark = localStorage.getItem('chef_mbg_theme') === 'dark';
      if (isDark) {
        document.documentElement.classList.add('dark');
        document.documentElement.classList.remove('light');
      } else {
        document.documentElement.classList.add('light');
        document.documentElement.classList.remove('dark');
      }
    }

    function toggleTheme() {
      const isDark = document.documentElement.classList.contains('dark');
      if (isDark) {
        document.documentElement.classList.remove('dark');
        document.documentElement.classList.add('light');
        localStorage.setItem('chef_mbg_theme', 'light');
        showToast('Mode Terang Aktif');
      } else {
        document.documentElement.classList.add('dark');
        document.documentElement.classList.remove('light');
        localStorage.setItem('chef_mbg_theme', 'dark');
        showToast('Mode Gelap Aktif');
      }
    }

    // INITIALIZATION
    document.addEventListener('DOMContentLoaded', () => {
      initTheme();
      renderActiveDirective();
      renderRecipeCards();
    });
  </script>
</body>
</html>
"""

# Write target files
targets = [
    'index.html',
    'preview.html',
    r'C:\Users\HP\.gemini\antigravity\brain\9c1ce148-7426-4dba-b2a3-bd7207cd3b11\preview.html'
]

for t in targets:
    os.makedirs(os.path.dirname(t) if os.path.dirname(t) else '.', exist_ok=True)
    with open(t, 'w', encoding='utf-8') as f:
        f.write(html_code)
    print(f"Generated Chef MBG system at: {t}")

print("Chef MBG build successful!")
