import sys
import subprocess
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
def unicode_table(sr, er):
    table = []
    for i in range(int(sr), int(er)):
        table.append(chr(i))
    return table
def python_version(encoding=sys.getdefaultencoding()):
    return (subprocess.run([sys.executable, "--version"], capture_output=True).stdout).decode(encoding)
