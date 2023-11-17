def hitung_diskon(total_belanja, status_anggota):
    if status_anggota.lower() == "premium":
        if total_belanja > 500000:
            diskon = 0.15
        else:
            diskon = 0.10
    elif status_anggota.lower() == "biasa":
        if total_belanja > 300000:
            diskon = 0.07
        else:
            diskon = 0
    else:
        raise ValueError("Status anggota tidak valid.")

    return diskon

def main():
    try:
        total_belanja = float(input("Masukkan total belanjaan pelanggan: "))
        status_anggota = input("Masukkan status anggota (biasa/premium): ")

        diskon = hitung_diskon(total_belanja, status_anggota)
        total_setelah_diskon = total_belanja - (total_belanja * diskon)

        print(f"Total belanjaan: {total_belanja}")
        print(f"Diskon: {diskon * 100}%")
        print(f"Total setelah diskon: {total_setelah_diskon}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
