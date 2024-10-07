class AddressIPv4:
    def __init__(self, address: str):
        self.address = address
        if not self.isValid():
            raise ValueError("Invalid IPv4 address.")

    def isValid(self) -> bool:
        octets = self.address.split('.')
        return len(octets) == 4 and all(0 <= int(octet) <= 255 for octet in octets if octet.isdigit())

    def getAsString(self) -> str:
        return self.address

    def getAsInt(self) -> int:
        return sum(int(octet) << (8 * i) for i, octet in enumerate(reversed(self.address.split('.'))))

    def getAsBinaryString(self) -> str:
        return bin(self.getAsInt())[2:].zfill(32)

    def getOctet(self, number: int) -> int:
        return int(self.address.split('.')[number - 1])

    def getClass(self) -> str:
        first_octet = int(self.address.split('.')[0])
        return 'A' if first_octet < 128 else 'B' if first_octet < 192 else 'C' if first_octet < 224 else 'D' if first_octet < 240 else 'E'

    def isPrivate(self) -> bool:
        first, second = map(int, self.address.split('.')[:2])
        return (first == 10) or (first == 172 and 16 <= second <= 31) or (first == 192 and second == 168)

if __name__ == "__main__":
    address = AddressIPv4("192.168.1.1")
    
    print(f"IP adresa: {address.getAsString()}")
    print(f"Je validní: {address.isValid()}")
    print(f"IP adresa jako celé číslo: {address.getAsInt()}")
    print(f"Binární reprezentace: {address.getAsBinaryString()}")
    print(f"Druhý oktet: {address.getOctet(2)}")
    print(f"Třída IP adresy: {address.getClass()}")
    print(f"Je privátní: {address.isPrivate()}")
