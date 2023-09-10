def is_palindrome(s):
    
    # jadikan huruf kecil semua dan di hilangkan spasinya
    s = s.replace(" ", "").lower()

    # rekursi semisal 1 dan 0 adalah palindrome
    if len(s) <= 1:
        return True
    
    # kalau huruf pertama dan terakhir tidak sama maka bukan palindrom
    if s[0] != s[-1]:
        return False

    # Rekursi Cek palindrom dari substring tengah
    return is_palindrome(s[1:-1])

# Contoh penggunaan
string1 = "race car"
string2 = "gohangasalamiimalasagnahog"
string3 =  "kasur rusak"

if is_palindrome(string1):
    print(f"'{string1}'  palindrom.")
else:
    print(f"'{string1}' bukan palindrom.")

if is_palindrome(string2):
    print(f"'{string2}'  palindrom.")
else:
    print(f"'{string2}' bukan palindrom.")

if is_palindrome(string3):
    print(f"'{string3}'  palindrom.")
else:
    print(f"'{string3}' bukan palindrom.")