# BEP Calculator

Aplikasi web untuk menghitung Break-Even Point (BEP) - titik impas dalam bisnis.

## Fitur

- Hitung BEP dalam unit
- Hitung BEP dalam Rupiah
- Hitung margin kontribusi
- Interface yang user-friendly

## Hardware Requirements

- Python 3.x
- Flask

## Instalasi


1. Buat virtual environment:
   ```bash
   python -m venv envku
   ```

2. Aktifkan virtual environment:
   - Windows:
   ```bash
   envku\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask
   ```

## Cara Menggunakan

1. Jalankan aplikasi:
   ```bash
   python app.py
   ```

2. Buka browser dan akses `http://127.0.0.1:5000/`

3. Input:
   - **Biaya Tetap (Fixed Cost)**: Biaya yang tidak berubah (sewa, gaji tetap, dll)
   - **Harga Jual per Unit (Price)**: Harga per unit produk
   - **Biaya Variabel per Unit (Variable Cost)**: Biaya bahan baku, dll

4. Output akan menampilkan:
   - BEP dalam Unit
   - BEP dalam Rupiah
   - Margin Kontribusi

## Rumus BEP

- **BEP Unit** = Fixed Cost / (Price - Variable Cost)
- **BEP Rupiah** = BEP Unit × Price
- **Margin Kontribusi** = Price - Variable Cost

## Author

Break-Even Point Calculator
