import hashlib
import datetime
import json

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
         # Convert the datetime object to an ISO formatted string
        block_dict = self.__dict__.copy()
        block_dict['timestamp'] = self.timestamp.isoformat()
        return json.dumps(block_dict, indent=4)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(datetime.datetime.now(), data, previous_block.hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(block)
            print("---")


def main():
    blockchain = Blockchain()

    blockchain.add_block("Transaction 1: Alice sent 10 coins to Bob")
    blockchain.add_block("Transaction 2: Bob sent 5 coins to Charlie")
    blockchain.add_block("Transaction 3: Charlie mined 2 coins")


    print("Blockchain Ledger:")
    blockchain.display_chain()

if __name__ == "__main__":
    main()