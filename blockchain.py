from hashlib import sha256
from datetime import datetime

#Manages blockchain, creating genesis block, adding/printing/validating blocks
class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = ["Genesis Block"]
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        previous_hash = self.chain[-1].hash
        new_block = Block(transactions, previous_hash)

        new_block.generate_hash()
        self.chain.append(new_block)

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.hash != current.generate_hash():
                print("Current hash differs from generated hash")
                return False
            
            if current.previous_hash != previous.hash:
                print("Previous block's hash got changed")
                return False
        
        return True
 
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:difficulty] != "0"*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.hash = proof
        return proof

#Represents the blocks in the blockchain
class Block:
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)      
