string = ("saya dan teman saya makan makan di rumah makan")
huruf = string.split()

jumlah = {}
for kata in huruf:
    if kata in jumlah:
        jumlah[kata] += 1
    else:
        jumlah[kata] = 1

print("Jumlah kata masing-masing:")
for kata, count in jumlah.items():
    print(f"{kata} = {count}")

total_kata = sum(jumlah.values())
kata_unik = len(jumlah)
print(f"Total kata = {total_kata}")
print(f"Kata unik = {kata_unik}")
