def hitung_diskon(total_belanja):
    if total_belanja > 500000:
        diskon = 0.1
    elif 300000 <= total_belanja <= 500000:
        diskon = 0.05
    else:
        diskon = 0

    return diskon

def main():
    try:
        total_belanja = float(input("Masukkan total belanjaan pelanggan: "))
        if total_belanja < 0:
            raise ValueError("Total belanjaan tidak boleh negatif.")
        
        diskon = hitung_diskon(total_belanja)
        total_setelah_diskon = total_belanja - (total_belanja * diskon)

        print(f"Total belanjaan: {total_belanja}")
        print(f"Diskon: {diskon * 100}%")
        print(f"Total setelah diskon: {total_setelah_diskon}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
